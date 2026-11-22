
from pydantic import BaseModel


# EXISTING CASEZERO MODELS

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


class AskRequest(BaseModel):
    suspect_id: int
    question: str


class InvestigateRequest(BaseModel):
    location: str


class AccusationRequest(BaseModel):
    suspect_id: int


# ASSIGNMENT 2 - INVESTIGATION MODELS

class Investigation(BaseModel):
    id: str
    title: str
    description: str
    status: str
    ownerId: str


class InvestigationCreate(BaseModel):
    title: str
    description: str


class InvestigationUpdate(BaseModel):
    title: str
    description: str
    status: str
