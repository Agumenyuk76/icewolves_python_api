from pydantic import BaseModel


def validator(schema: type[BaseModel], response: dict):
    return schema(**response)