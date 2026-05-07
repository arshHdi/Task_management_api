from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from datetime import datetime
from typing import Optional

class BaseModel(Base):
    __abstract__ = True
    
    create_ts: Mapped[Optional[datetime]] = mapped_column(DateTime, default=datetime.utcnow)
    update_ts: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True, onupdate=datetime.utcnow)
    delete_ts: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
