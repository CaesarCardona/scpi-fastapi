# app/models.py
from pydantic import BaseModel
from typing import Optional
import time

class SCPIRequest(BaseModel):
    command: str
    channel: Optional[int] = None
    client_id: Optional[str] = None
    timestamp: float = time.time()

class SCPIResponse(BaseModel):
    status: str
    data: Optional[str]
    error: Optional[str] = None

