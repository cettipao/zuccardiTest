from typing import Optional, List
from pydantic import BaseModel
import datetime

class Estacion30300(BaseModel):
    id: Optional[str]
    date: datetime.datetime
    humedad: float
    temperatura: float