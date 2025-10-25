# config.py (context-engineering/config.py)
import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env file from project root
BASE_DIR = Path(__file__).parent  # This will be context-engineering/
load_dotenv(BASE_DIR / '.env')

# API Keys - loaded from .env
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
COHERE_API_KEY = os.getenv('COHERE_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY')

# Other config
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

def setup_environment():
    """Set all environment variables for API libraries"""
    env_vars = {
        'GROQ_API_KEY': GROQ_API_KEY,
        'COHERE_API_KEY': COHERE_API_KEY,
        'OPENAI_API_KEY': OPENAI_API_KEY,
        'LANGCHAIN_API_KEY': LANGCHAIN_API_KEY,
    }
    
    for key, value in env_vars.items():
        if value and not os.getenv(key):
            os.environ[key] = value
            print(f"Set environment variable: {key}")
        elif not os.getenv(key):
            print(f"{key} not set (empty in .env file)")
    
    print("Environment setup complete!")

def check_keys():
    """Check if API keys are loaded"""
    print("=== API Keys from config.py ===")
    print(f"  GROQ_API_KEY: {'Loaded' if GROQ_API_KEY else 'Missing'}")
    print(f"  COHERE_API_KEY: {'Loaded' if COHERE_API_KEY else 'Missing'}")
    print(f"  OPENAI_API_KEY: {'Loaded' if OPENAI_API_KEY else 'Missing'}")
    print(f"  LANGCHAIN_API_KEY: {'Loaded' if LANGCHAIN_API_KEY else 'Missing'}")
    
    print("\n=== Environment Variables ===")
    print(f"  os.environ['GROQ_API_KEY']: {'Set' if os.getenv('GROQ_API_KEY') else 'Not set'}")
    print(f"  os.environ['COHERE_API_KEY']: {'Set' if os.getenv('COHERE_API_KEY') else 'Not set'}")
    
    all_good = all([GROQ_API_KEY, COHERE_API_KEY])
    print(f"\n{'All essential keys loaded!' if all_good else 'Some keys are missing!'}")
    return all_good

# Optional: Auto-setup when imported (uncomment if desired)
# setup_environment()

if __name__ == "__main__":
    # Test when running config.py directly
    check_keys()
    setup_environment()