import os


def _require_env(name: str) -> str:
	value = os.getenv(name, "").strip()
	if not value:
		raise RuntimeError(f"Missing required environment variable: {name}")
	return value


WORKSPACE_ID = _require_env("WORKSPACE_ID")
PROJECT_ID = _require_env("PROJECT_ID")
SOURCE_MODEL_ID = _require_env("SOURCE_MODEL_ID")
# TARGET_MODEL_ID = _require_env("TARGET_MODEL_ID")