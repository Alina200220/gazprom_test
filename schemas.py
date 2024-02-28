from pydantic import BaseModel
from datetime import datetime

class Info(BaseModel):
    device: str
    date: datetime
    x: float
    y: float
    z: float