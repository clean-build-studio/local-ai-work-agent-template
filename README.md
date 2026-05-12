# Setup

## 1. Install Ollama

This project uses Ollama to run a local AI model on your computer.

Install Ollama from:

```text
https://ollama.com
```

On Linux, you can install Ollama with:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Check that Ollama installed:

```bash
ollama --version
```

If Ollama is not running, start it with:

```bash
sudo systemctl start ollama
```

Optional status check:

```bash
sudo systemctl status ollama
```

---

## 2. Pull the local model

This template uses Qwen3 4B by default:

```bash
ollama pull qwen3:4b
```

You can test the model directly with:

```bash
ollama run qwen3:4b
```

Then try a simple prompt:

```text
Say hello in one sentence and confirm the local model is working.
```

To exit the Ollama chat, type:

```text
/bye
```

---

## 3. Clone this repo

Clone the project from GitHub:

```bash
git clone https://github.com/YOUR-USERNAME/local-ai-work-agent-template.git
```

Move into the project folder:

```bash
cd local-ai-work-agent-template
```

Replace `YOUR-USERNAME` with your actual GitHub username or organization name.

---

## 4. Create a Python virtual environment

Create the virtual environment:

```bash
python3 -m venv .venv
```

Activate it on Linux or macOS:

```bash
source .venv/bin/activate
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

When the virtual environment is active, you should see something like this at the beginning of your terminal line:

```text
(.venv)
```

---

## 5. Install Python packages

Install the required packages:

```bash
pip install -r requirements.txt
```

For this first version, the project uses:

```text
requests
python-dotenv
```

`requests` lets Python send a request to Ollama.

`python-dotenv` lets Python read local settings from the `.env` file.

---

## 6. Create your local `.env` file

Copy the example environment file:

```bash
cp .env.example .env
```

Your `.env` file should include:

```bash
OLLAMA_MODEL=qwen3:4b
OLLAMA_BASE_URL=http://localhost:11434
AGENT_NAME=Local Work Agent

ENABLE_THINKING=false
ENABLE_FILE_ACCESS=true
ENABLE_CALENDAR_ACCESS=false
ENABLE_WEATHER_ACCESS=false

DATA_INBOX_PATH=data/inbox
DATA_PROCESSED_PATH=data/processed
DATA_OUTPUTS_PATH=data/outputs

ALLOW_FULL_COMPUTER_ACCESS=false
SAVE_OUTPUTS=true
```

The `.env.example` file is safe to commit to GitHub.

The real `.env` file should stay on your computer and should not be pushed to GitHub.

---

## 7. Run the first agent test

From the project root, with your virtual environment activated, run:

```bash
python3 -m app.main
```

Expected output:

```text
Local Work Agent is starting...
Using local model: qwen3:4b
Thinking enabled: False

Agent response:
Local model connected.
```

This proves the basic local path is working:

```text
Python project
→ Ollama running locally
→ Qwen model
→ response back to Python
```

---

# Troubleshooting

## `python` command not found

On some Linux systems, use `python3` instead of `python`.

```bash
python3 -m venv .venv
```

---

## Missing `venv`

If you see an error about `venv` not being available, install it:

```bash
sudo apt-get update
sudo apt-get install python3-venv
```

Then try again:

```bash
python3 -m venv .venv
```

---

## Missing `requests`

If you see:

```text
ModuleNotFoundError: No module named 'requests'
```

Make sure your virtual environment is activated:

```bash
source .venv/bin/activate
```

Then install dependencies:

```bash
pip install -r requirements.txt
```

---

## Ollama install error: `zstd`

If you see:

```text
ERROR: This version requires zstd for extraction.
```

Install `zstd` first:

```bash
sudo apt-get update
sudo apt-get install zstd
```

Then rerun the Ollama install command:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

## Qwen overthinking a simple prompt

Qwen3 can sometimes generate reasoning text even for simple prompts.

For this first connection test, the template uses several guardrails:

- `ENABLE_THINKING=false`
- `/no_think`
- a strict system prompt
- low randomness settings
- a response length limit
- cleanup logic for leaked thinking text

The goal of the first test is not deep reasoning.

The goal is to confirm that Python can talk to Ollama and return a clean local response.

---

# Required files

Make sure your `requirements.txt` has:

```txt
requests
python-dotenv
```

Make sure your `.gitignore` includes:

```gitignore
.env
.venv/

data/inbox/*
data/processed/*
data/outputs/*

!data/inbox/.gitkeep
!data/processed/.gitkeep
!data/outputs/.gitkeep
```