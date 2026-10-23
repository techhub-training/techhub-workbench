"""Check your workbench: read your key from .env and ask the TechHub API sandbox who you are."""
import os

import requests
from dotenv import load_dotenv

load_dotenv()
key = os.environ.get("TECHHUB_API_KEY", "")
if not key.startswith("thk_") or key == "thk_your_key_here":
    raise SystemExit("Put your sandbox key in .env first (cp .env.example .env, then edit .env).")
# The User-Agent names your program: the server refuses Python's default one (406).
r = requests.get("https://techhub.byuaccounting.net/api/v1/me", headers={"X-API-Key": key, "User-Agent": "TechHub-student/1.0"}, timeout=30)
print(r.status_code, r.json())
