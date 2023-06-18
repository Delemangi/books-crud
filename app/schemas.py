from pydantic import BaseModel


class VariableSchema(BaseModel):
    value: str = ""
