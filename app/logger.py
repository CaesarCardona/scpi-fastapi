# app/logger.py
import json
import time
from pathlib import Path

LOG_FILE = Path("scpi_log.jsonl")

async def log_event(command: str, response: str | None):
    entry = {
        "ts": time.time(),
        "command": command,
        "response": response,
    }
    with LOG_FILE.open("a") as f:
        f.write(json.dumps(entry) + "\n")

