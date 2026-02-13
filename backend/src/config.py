import os

WORKSPACE_ID = os.getenv("WORKSPACE_ID", "a1cd06bae2")
PROJECT_ID = os.getenv("PROJECT_ID", "128262a20c")
SOURCE_MODEL_ID = os.getenv("SOURCE_MODEL_ID", "a1014e4b32")
TARGET_MODEL_ID = os.getenv("TARGET_MODEL_ID", "39d99ae41a")
OFFSET_Z = float(os.getenv("OFFSET_Z", "16000"))
OBJECT_ID = os.getenv("OBJECT_ID", "a10ba28aeafaf089fe5f46ea1d730b8ed2014e4b32")
OBJECT_DATA_FILE = os.getenv("OBJECT_DATA_FILE", "object_data.json")