from datetime import datetime

from marshmallow import Schema

from flask_app.db.models import CountType


class MaterialBaseSchema(Schema):
    title: str
    model_name: str
    count_type: CountType
    amount: float
    color: str


class MaterialReadSchema(MaterialBaseSchema):
    id: int
    created_at: datetime
    last_updated_at: datetime


class MaterialPatchSchema(Schema):
    title: str | None
    model_name: str | None
    count_type: CountType | None
    amount: float | None
    color: str | None


class MaterialCreateSchema(MaterialBaseSchema):
    pass


class MaterialPutSchema(MaterialBaseSchema):
    pass
