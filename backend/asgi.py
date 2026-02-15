"""ASGI entry point for Render.com deployment"""
import sys
from pathlib import Path

# Add src directory to Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Now import main (which is in src/ directory)
import main

app = main.app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
