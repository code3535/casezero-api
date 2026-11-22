
from pydantic import BaseModel


class Case(BaseModel):
    case_id: int
    title: str
    description: str
    location: str
    status: str


class Suspect(BaseModel):
    suspect_id: int
    case_id: int
    name: str
    occupation: str
    description: str
    alibi: str


class Clue(BaseModel):
    clue_id: int
    case_id: int
    title: str
    description: str
    found_at: str
