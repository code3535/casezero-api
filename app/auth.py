
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


# MOCK USERS AND TOKENS
fake_users_db = {
    "user-a-token": {
        "user_id": "user-a",
        "role": "user"
    },
    "user-b-token": {
        "user_id": "user-b",
        "role": "user"
    },
    "admin-token": {
        "user_id": "admin",
        "role": "admin"
    }
}


# BEARER TOKEN SECURITY
security = HTTPBearer(auto_error=False)


# GET CURRENT AUTHENTICATED USER
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    # Check if token was provided
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required"
        )

    # Extract token
    token = credentials.credentials

    # Validate token
    user = fake_users_db.get(token)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token"
        )

    return user
