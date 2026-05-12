import re
import requests

from app.config import OLLAMA_BASE_URL, OLLAMA_MODEL, ENABLE_THINKING


EXPECTED_TEST_RESPONSE = "Local model connected."


def load_system_prompt():
    with open("app/prompts/system_prompt.md", "r", encoding="utf-8") as file:
        return file.read()


def clean_response(text):
    """
    Clean common Qwen thinking/reasoning output.
    """

    if EXPECTED_TEST_RESPONSE in text:
        return EXPECTED_TEST_RESPONSE

    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)

    if "</think>" in text:
        text = text.split("</think>")[-1]

  
    reasoning_starters = [
        "Hmm,",
        "The user wants",
        "Okay,",
        "Let me think",
        "I need to",
        "First,",
    ]

    cleaned = text.strip()

    for starter in reasoning_starters:
        if cleaned.startswith(starter):
            return "The model responded, but did not follow the exact output format."

    return cleaned


def ask_ollama(user_prompt):
    system_prompt = load_system_prompt()

    if not ENABLE_THINKING:
        user_prompt = f"/no_think {user_prompt}"

    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "think": ENABLE_THINKING,
        "stream": False,
        "options": {
            "num_predict": 80,
            "temperature": 0,
            "top_p": 0.1,
            "num_ctx": 1024,
        },
    }

    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/chat",
        json=payload,
        timeout=180,
    )

    response.raise_for_status()

    raw_response = response.json()["message"]["content"]
    return clean_response(raw_response)