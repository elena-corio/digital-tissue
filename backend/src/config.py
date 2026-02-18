import os

WORKSPACE_ID = os.getenv("WORKSPACE_ID", "a1cd06bae2")
PROJECT_ID = os.getenv("PROJECT_ID", "dcca94731b")
SOURCE_MODEL_ID = os.getenv("SOURCE_MODEL_ID", "827526cd48")

# CORS allowed origins: read from env, fallback to default list
def get_cors_allowed_origins():
	env_val = os.getenv("CORS_ALLOWED_ORIGINS")
	if env_val:
		# Split comma-separated origins, strip whitespace
		return [origin.strip() for origin in env_val.split(",") if origin.strip()]
	# Default: local dev and production domain
	return [
		"http://localhost:5173",
		"https://digitaltissue.org"
	]