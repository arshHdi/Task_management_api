from typing import Optional
from pydantic import BaseModel
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from models.base_model import BaseModel

class Comment(BaseModel):
    __tablename__ = "comments"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    task_id: Mapped[int] = mapped_column(ForeignKey("tasks.id"))
    content: Mapped[str] = mapped_column(String(255))