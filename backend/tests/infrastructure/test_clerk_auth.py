import logging
from unittest.mock import patch

import pytest
from fastapi import HTTPException
from starlette.requests import Request

from infrastructure.clerk_auth import (
    _auth_failures_by_ip,
    _clear_auth_failures,
    _enforce_domain_authorization,
    _extract_email_from_payload,
    _is_auth_rate_limited,
    _record_auth_failure,
    verify_clerk_token,
)


def test_extract_email_prefers_primary_email_address_id():
    payload = {
        "sub": "user_123",
        "primary_email_address_id": "id_primary",
        "email_addresses": [
            {"id": "id_secondary", "email_address": "secondary@other.com"},
            {"id": "id_primary", "email_address": "primary@students.iaac.net"},
        ],
    }

    assert _extract_email_from_payload(payload) == "primary@students.iaac.net"


def test_enforce_domain_authorization_allows_matching_domain(monkeypatch):
    monkeypatch.setenv("ALLOWED_EMAIL_DOMAIN", "students.iaac.net,iaac.net")
    payload = {"sub": "user_abc", "email": "person@students.iaac.net"}

    authorized_payload = _enforce_domain_authorization(payload)

    assert authorized_payload == payload


def test_enforce_domain_authorization_denies_non_matching_domain_and_logs(monkeypatch, caplog):
    monkeypatch.setenv("ALLOWED_EMAIL_DOMAIN", "students.iaac.net")
    payload = {"sub": "user_xyz", "email": "person@example.com"}

    with caplog.at_level(logging.WARNING):
        with pytest.raises(HTTPException) as exc_info:
            _enforce_domain_authorization(payload)

    assert exc_info.value.status_code == 403
    assert exc_info.value.detail == "IAAC email required"
    assert "Email domain not allowed" in caplog.text
    assert "user_id=user_xyz" in caplog.text
    assert "email=person@example.com" in caplog.text


def test_enforce_domain_authorization_missing_email_logs_and_raises(monkeypatch, caplog):
    monkeypatch.setenv("ALLOWED_EMAIL_DOMAIN", "students.iaac.net")
    payload = {"sub": "user_no_email"}

    with caplog.at_level(logging.WARNING):
        with pytest.raises(HTTPException) as exc_info:
            _enforce_domain_authorization(payload)

    assert exc_info.value.status_code == 403
    assert exc_info.value.detail == "Email claim missing"
    assert "Email claim missing" in caplog.text
    assert "user_id=user_no_email" in caplog.text


def test_auth_rate_limit_triggers_and_resets(monkeypatch):
    monkeypatch.setenv("AUTH_FAILURE_WINDOW_SECONDS", "60")
    monkeypatch.setenv("AUTH_FAILURE_MAX_ATTEMPTS", "3")
    ip_address = "127.0.0.1"

    _clear_auth_failures(ip_address)

    _record_auth_failure(ip_address, now=100.0)
    _record_auth_failure(ip_address, now=110.0)
    assert _is_auth_rate_limited(ip_address, now=120.0) is False

    _record_auth_failure(ip_address, now=125.0)
    assert _is_auth_rate_limited(ip_address, now=126.0) is True

    assert _is_auth_rate_limited(ip_address, now=200.0) is False
    _clear_auth_failures(ip_address)


@pytest.mark.asyncio
async def test_verify_clerk_token_returns_generic_invalid_token_error(monkeypatch):
    monkeypatch.setenv("CLERK_DOMAIN", "test.clerk.accounts.dev")
    monkeypatch.setenv("CLERK_ISSUER", "https://test.clerk.accounts.dev")
    monkeypatch.setenv("ALLOWED_EMAIL_DOMAIN", "students.iaac.net")
    monkeypatch.setenv("AUTH_FAILURE_MAX_ATTEMPTS", "20")
    monkeypatch.delenv("SKIP_AUTH", raising=False)

    _auth_failures_by_ip.clear()

    scope = {
        "type": "http",
        "method": "GET",
        "path": "/api/metrics",
        "headers": [(b"authorization", b"Bearer test-token")],
        "client": ("127.0.0.1", 12345),
    }
    request = Request(scope)

    with patch("infrastructure.clerk_auth.get_clerk_jwks", return_value={"keys": []}):
        with patch("infrastructure.clerk_auth.jwt.get_unverified_header", return_value={"kid": "test-kid"}):
            with pytest.raises(HTTPException) as exc_info:
                await verify_clerk_token(request)

    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Invalid token"


@pytest.mark.asyncio
async def test_verify_clerk_token_allows_missing_header_in_local_by_default(monkeypatch):
    monkeypatch.delenv("SKIP_AUTH", raising=False)
    monkeypatch.delenv("LOCAL_AUTH_OPTIONAL", raising=False)
    monkeypatch.delenv("RENDER", raising=False)

    scope = {
        "type": "http",
        "method": "GET",
        "path": "/api/metrics",
        "headers": [],
        "client": ("127.0.0.1", 12345),
    }
    request = Request(scope)

    payload = await verify_clerk_token(request)

    assert payload.get("sub") == "local-dev"
    assert payload.get("email") == "dev@iaac.net"


@pytest.mark.asyncio
async def test_verify_clerk_token_requires_header_in_production(monkeypatch):
    monkeypatch.delenv("SKIP_AUTH", raising=False)
    monkeypatch.setenv("RENDER", "true")
    monkeypatch.delenv("LOCAL_AUTH_OPTIONAL", raising=False)

    scope = {
        "type": "http",
        "method": "GET",
        "path": "/api/metrics",
        "headers": [],
        "client": ("127.0.0.1", 12345),
    }
    request = Request(scope)

    with pytest.raises(HTTPException) as exc_info:
        await verify_clerk_token(request)

    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Missing authorization header"
