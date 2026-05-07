from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class BaseSchema(BaseModel):
    create_ts: Optional[datetime] = Field(default=None, example="2024-04-22T10:30:00")
    update_ts: Optional[datetime] = Field(default=None, example="2024-04-22T10:30:00")
    delete_ts: Optional[datetime] = Field(default=None, example=None)
