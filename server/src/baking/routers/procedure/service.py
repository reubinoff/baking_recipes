from typing import Optional, List

from .models import ProcedureRead, ProcedureCreate, Procedure, ProcedureUpdate

from baking.routers.ingredients.service import create as create_ingredient


def get(*, db_session, procedure_id: int) -> Optional[Procedure]:
    """Returns a item based on the given Procedure id."""
    return (
        db_session.query(Procedure).filter(Procedure.id == procedure_id).one_or_none()
    )


def get_all(*, db_session) -> List[Optional[Procedure]]:
    """Returns all Procedures."""
    return db_session.query(Procedure)


def create(*, db_session, procedure_in: ProcedureCreate) -> Procedure:
    """Creates a new Procedure."""

    ingredients = [
        create_ingredient(db_session=db_session, ingredient_in=ingredient_in)
        for ingredient_in in procedure_in.ingredients
    ]

    procedure = Procedure(
        **procedure_in.dict(exclude={"ingredients"}), ingredients=ingredients
    )

    db_session.add(procedure)
    db_session.commit()
    return procedure


def update(
    *, db_session, procedure: Procedure, procedure_in: ProcedureUpdate
) -> Procedure:
    """Updates a procedure."""
    recipe_data = procedure.dict()

    update_data = procedure_in.dict(exclude_unset=True, exclude={})

    for field in recipe_data:
        if field in update_data:
            setattr(procedure, field, update_data[field])

    db_session.commit()
    return procedure


def delete(*, db_session, procedure_id: int):
    """Deletes a recipe."""
    project = db_session.query(Procedure).filter(Procedure.id == procedure_id).first()
    db_session.delete(project)
    db_session.commit()
