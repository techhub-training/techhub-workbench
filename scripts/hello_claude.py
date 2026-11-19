"""Your first Claude API call (TechHub challenge 416): read your key from .env and ask Claude one question.

python scripts/hello_claude.py
"""
import os

import requests
from dotenv import load_dotenv

load_dotenv()
key = os.environ.get("ANTHROPIC_API_KEY", "")
if not key.startswith("sk-ant-"):
    raise SystemExit("Put your Anthropic key in .env first: ANTHROPIC_API_KEY=sk-ant-...")

r = requests.post(
    "https://api.anthropic.com/v1/messages",
    headers={"x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json"},
    json={
        "model": "claude-haiku-5-5",
        "max_tokens": 200,
        "messages": [{"role": "user", "content": "In two sentences, what is a three-way match in accounts payable?"}],
    },
    timeout=60,
)
print("Status:", r.status_code)              # 200 is success; 401 means the key is wrong
reply = r.json()
print(next(b["text"] for b in reply["content"] if b["type"] == "text"))
print("Usage:", reply["usage"])              # tokens in and out: what you are billed for
