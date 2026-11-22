from app.routers.investigations import router as investigations_router
from fastapi import FastAPI, HTTPException
from app.data import cases, suspects, clues, solutions
from app.models import AskRequest, InvestigateRequest, AccusationRequest

# Shared investigation progress
discovered_clues = []

app = FastAPI(
    title="CaseZero API",
    description="Backend API for the CaseZero AI Mystery Game",
    version="1.0.0"
)
app.include_router(investigations_router)

# HOME
@app.get("/")
def home():
    return {
        "message": "Welcome to CaseZero API!",
        "status": "running"
    }


# CASE
@app.get("/case")
def get_case():
    return cases[0]


# SUSPECTS
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


# CLUES
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


# SUSPECT INTERROGATION
@app.post("/ask")
def ask_suspect(request: AskRequest):

    suspect = None

    for s in suspects:
        if s.suspect_id == request.suspect_id:
            suspect = s
            break

    if suspect is None:
        raise HTTPException(
            status_code=404,
            detail="Suspect not found"
        )

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


# CLUE DISCOVERY
@app.post("/investigate")
def investigate(request: InvestigateRequest):

    location = request.location.strip().lower()

    for clue in clues:

        if clue.found_at.strip().lower() == location:

            if clue.clue_id in discovered_clues:
                continue

            discovered_clues.append(clue.clue_id)

            return {
                "message": "New clue discovered!",
                "clue": clue
            }

    return {
        "message": "No new clues found at this location."
    }


# DISCOVERED CLUES
@app.get("/discovered-clues")
def get_discovered_clues():

    return [
        clue for clue in clues
        if clue.clue_id in discovered_clues
    ]
# FINAL ACCUSATION
@app.post("/accuse")
def accuse(request: AccusationRequest):

    # Check whether the suspect exists
    suspect = None

    for s in suspects:
        if s.suspect_id == request.suspect_id:
            suspect = s
            break

    if suspect is None:
        raise HTTPException(
            status_code=404,
            detail="Suspect not found"
        )

    # Get the secret solution
    solution = solutions[cases[0].case_id]

    # Check the accusation
    if request.suspect_id == solution["culprit_id"]:

        return {
            "correct": True,
            "message": "Congratulations! You solved the case!",
            "suspect": suspect.name,
            "motive": solution["motive"],
            "explanation": solution["explanation"]
        }

    return {
        "correct": False,
        "message": "Incorrect accusation! The real culprit is still out there. Continue investigating."
    }