from app.agent import ask_ollama
from app.config import AGENT_NAME, OLLAMA_MODEL, ENABLE_THINKING


def main():
    print(f"{AGENT_NAME} is starting...")
    print(f"Using local model: {OLLAMA_MODEL}")
    print(f"Thinking enabled: {ENABLE_THINKING}")

    user_prompt = "Return only this exact text: Local model connected."

    response = ask_ollama(user_prompt)

    print("\nAgent response:")
    print(response)


if __name__ == "__main__":
    main()