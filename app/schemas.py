from pydantic import BaseModel

class ConfResponse(BaseModel):
    status: str
    mode: str

class MeasureResponse(BaseModel):
    value: float
    timestamp: float

