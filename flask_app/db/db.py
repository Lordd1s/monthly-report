from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.testing.schema import mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"


DB = SQLAlchemy(model_class=Base)
