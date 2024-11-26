from marshmallow import ValidationError
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from flask_app.db import Material
from flask_app.schemas import (
    MaterialReadSchema,
    MaterialCreateSchema,
    MaterialPutSchema,
    MaterialPatchSchema,
)


def create_material(db: Session, data: dict) -> Material:
    schema = MaterialCreateSchema()
    try:
        validated_data = schema.load(data)
        new_material = Material(**validated_data)
        db.add(new_material)
        db.commit()
        db.refresh(new_material)
        return new_material
    except ValidationError as ve:
        raise ValueError(f"Validation error: {ve.messages}")
    except SQLAlchemyError as se:
        db.rollback()
        raise RuntimeError(f"Database error: {str(se)}")
    except Exception as e:
        db.rollback()
        raise RuntimeError(f"Unexpected error: {str(e)}")


def get_materials(db: Session) -> list[Material]:
    stmt = select(Material).order_by(Material.created_at)
    result: Result = db.execute(stmt)
    materials = result.scalars().all()
    return list(materials)


def get_material(db: Session, material_id: int) -> Material | None:
    return db.get(Material, material_id)


def update_material(
    db: Session, data: dict, material: Material, partial: bool = False
) -> Material:
    schema = MaterialPatchSchema() if partial else MaterialPutSchema()
    try:
        validated_data = schema.load(data)
        for name, value in validated_data.items():
            setattr(material, name, value)

        db.commit()
        return material
    except ValidationError as ve:
        raise ValueError(f"Validation error: {ve.messages}")
    except SQLAlchemyError as se:
        db.rollback()
        raise RuntimeError(f"Database error: {str(se)}")
    except Exception as e:
        db.rollback()
        raise RuntimeError(f"Unexpected error: {str(e)}")


def delete_material(db: Session, material: Material) -> None:
    db.delete(material)
    db.commit()
