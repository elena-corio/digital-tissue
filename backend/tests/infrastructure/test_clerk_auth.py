import logging

import pytest
from fastapi import HTTPException

from infrastructure.clerk_auth import _enforce_domain_authorization, _extract_email_from_payload


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
