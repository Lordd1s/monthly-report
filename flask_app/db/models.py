from datetime import datetime
from enum import Enum

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column
from flask_app.db.db import DB


class CountType(Enum):
    KILOGRAM = "kg."
    METER = "m."
    PIECE = "p."
    BOBINE = "bob."


class Material(DB.Model):
    title: Mapped[str] = mapped_column(String(32))
    model_name: Mapped[str] = mapped_column(String(50))
    count_type: Mapped[CountType] = mapped_column()
    amount: Mapped[float] = mapped_column()
    color: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    last_updated_at: Mapped[datetime] = mapped_column(
        default=func.now(), onupdate=func.now()
    )
