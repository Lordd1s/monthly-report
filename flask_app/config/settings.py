import os
from marshmallow import Schema, fields


class SettingsSchema(Schema):
    DATABASE_URL = fields.String(required=True)


config_data = {"DATABASE_URL": os.getenv("DATABASE_URL")}

schema = SettingsSchema()
schema.load(config_data)
