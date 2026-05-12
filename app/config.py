import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3:4b")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
AGENT_NAME = os.getenv("AGENT_NAME", "Local Work Agent")

ENABLE_THINKING = os.getenv("ENABLE_THINKING", "false").lower() == "true"