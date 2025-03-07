from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

def test_env_loading():
    env_path = BASE_DIR / '.env'
    print(f"Looking for .env at: {env_path}")
    
    if not env_path.exists():
        print("❌ .env file not found!")
        return
    
    load_dotenv(env_path)
    print("✅ .env file loaded")
    print(f"SECRET_KEY exists: {'DJANGO_SECRET_KEY' in os.environ}")

if __name__ == "__main__":
    test_env_loading()