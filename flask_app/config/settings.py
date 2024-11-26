import os
from dotenv import load_dotenv
from marshmallow import Schema, fields, ValidationError

load_dotenv()


class SettingsSchema(Schema):
    DATABASE_URL: str = fields.String(required=True)

    def get_db_url(self, data: dict) -> str:
        validated_data = self.load(data)
        return validated_data.get("DATABASE_URL")


schema = SettingsSchema()

DATABASE = schema.get_db_url({"DATABASE_URL": os.getenv("DATABASE_URL")})
