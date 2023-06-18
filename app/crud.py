from sqlalchemy.orm import Session
from . import models


def create(db: Session, name: str, value: str):
    """
    Create a variable.

    Args:
        db (Session): The session object.
        name (str): The name of the variable.
        value (str): The value of the variable.

    Returns:
        Variable | None: The created variable, unless it already exists.
    """

    if read(db, name) is not None:
        return None

    var = models.Variable(name=name, value=value)
    db.add(var)
    db.commit()
    db.refresh(var)

    return var


def read(db: Session, name: str):
    """
    Read a variable.

    Args:
        db (Session): The session object.
        name (str): The name of the variable.

    Returns:
        Optional[Variable]: The variable, if it exists.
    """

    return db.query(models.Variable).filter(models.Variable.name == name).first()


def update(db: Session, name: str, value: str):
    """
    Update a variable.

    Args:
        db (Session): The session object.
        name (str): The name of the variable.
        value (str): The value of the variable.

    Returns:
        Optional[Variable]: The variable, if it exists.
    """

    var = read(db, name)
    if var is None:
        return None

    var.value = value
    db.commit()
    db.refresh(var)

    return var


def delete(db: Session, name: str):
    """
    Delete a variable.

    Args:
        db (Session): The session object.
        name (str): The name of the variable.

    Returns:
        Optional[Variable]: The variable, if it exists.
    """

    var = read(db, name)
    if var is None:
        return None

    db.delete(var)
    db.commit()

    return var


def get_all(db: Session):
    """
    Get all variables.

    Args:
        db (Session): The session object.

    Returns:
        List[Variable]: The list of variables.
    """

    return db.query(models.Variable).all()
