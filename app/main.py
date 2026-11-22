from fastapi import FastAPI, HTTPException
from app.data import cases, suspects, clues

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
