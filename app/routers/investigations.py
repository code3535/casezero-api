
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, status

from app.data import investigations
from app.auth import get_current_user
from app.models import (
    Investigation,
    InvestigationCreate,
    InvestigationUpdate
)

router = APIRouter(
    prefix="/api/v1/investigations",
    tags=["Investigations"]
)


# CHECK USER PERMISSIONS
def check_access(investigation, user):

    if user["role"] == "admin":
        return

    if investigation.ownerId != user["user_id"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to access this investigation"
        )


# GET ALL INVESTIGATIONS
@router.get("/")
def get_investigations(user=Depends(get_current_user)):

    if user["role"] == "admin":
        user_investigations = investigations
    else:
        user_investigations = [
            inv for inv in investigations
            if inv.ownerId == user["user_id"]
        ]

    return {
        "success": True,
        "data": user_investigations
    }


# GET INVESTIGATION BY ID
@router.get("/{investigation_id}")
def get_investigation(
    investigation_id: str,
    user=Depends(get_current_user)
):

    for investigation in investigations:

        if investigation.id == investigation_id:

            check_access(investigation, user)

            return {
                "success": True,
                "data": investigation
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Investigation not found"
    )


# CREATE INVESTIGATION
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_investigation(
    request: InvestigationCreate,
    user=Depends(get_current_user)
):

    new_investigation = Investigation(
        id=f"investigation_{uuid4().hex[:8]}",
        title=request.title,
        description=request.description,
        status="active",
        ownerId=user["user_id"]
    )

    investigations.append(new_investigation)

    return {
        "success": True,
        "message": "Investigation created successfully",
        "data": new_investigation
    }


# UPDATE INVESTIGATION
@router.put("/{investigation_id}")
def update_investigation(
    investigation_id: str,
    request: InvestigationUpdate,
    user=Depends(get_current_user)
):

    for investigation in investigations:

        if investigation.id == investigation_id:

            check_access(investigation, user)

            investigation.title = request.title
            investigation.description = request.description
            investigation.status = request.status

            return {
                "success": True,
                "message": "Investigation updated successfully",
                "data": investigation
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Investigation not found"
    )


# DELETE INVESTIGATION
@router.delete("/{investigation_id}")
def delete_investigation(
    investigation_id: str,
    user=Depends(get_current_user)
):

    for investigation in investigations:

        if investigation.id == investigation_id:

            check_access(investigation, user)

            investigations.remove(investigation)

            return {
                "success": True,
                "message": "Investigation deleted successfully"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Investigation not found"
    )
