from fastapi import FastAPI, HTTPException
from app.data import cases, suspects, clues
from app.models import AskRequest

app = FastAPI(
    title="CaseZero API",
    description="Backend API for the CaseZero AI Mystery Game",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to CaseZero API!",
        "status": "running"
    }


@app.get("/case")
def get_case():
    return cases[0]


@app.get("/suspects")
def get_suspects():
    return suspects


@app.get("/suspects/{suspect_id}")
def get_suspect(suspect_id: int):
    for suspect in suspects:
        if suspect.suspect_id == suspect_id:
            return suspect

    raise HTTPException(
        status_code=404,
        detail="Suspect not found"
    )


@app.get("/clues")
def get_clues():
    return clues


@app.get("/clues/{clue_id}")
def get_clue(clue_id: int):
    for clue in clues:
        if clue.clue_id == clue_id:
            return clue

    raise HTTPException(
        status_code=404,
        detail="Clue not found"
    )


@app.post("/ask")
def ask_suspect(request: AskRequest):

    # Find the selected suspect
    suspect = None

    for s in suspects:
        if s.suspect_id == request.suspect_id:
            suspect = s
            break

    # Check whether the suspect exists
    if suspect is None:
        raise HTTPException(
            status_code=404,
            detail="Suspect not found"
        )

    # Predefined answers for each suspect
    answers = {
        1: "I was attending a business meeting that night. I had nothing to do with the murder.",
        2: "I left the office at 9 PM. I don't know what happened after that.",
        3: "I was watching the security cameras. I didn't see anything unusual.",
        4: "I was at home that night. I had no reason to visit the office."
    }

    return {
        "suspect_id": suspect.suspect_id,
        "suspect_name": suspect.name,
        "question": request.question,
        "answer": answers[suspect.suspect_id]
    }
