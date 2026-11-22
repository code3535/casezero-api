# CaseZero API Documentation

**Version:** 1.0.0  
**Project:** CaseZero – AI Mystery Game  
**Backend:** FastAPI  
**Data Storage:** In-memory mock data

## 1. Project Overview

CaseZero is an AI Mystery Game prototype that allows users to investigate a fictional murder case, examine clues, interrogate suspects, and make a final accusation.

The API provides case information, suspect information, clue discovery, suspect interrogation, final accusations, and investigation management.

## 2. Base URL

Local development:

`http://127.0.0.1:8000`

API documentation:

`http://127.0.0.1:8000/docs`

## 3. Authentication

The investigation management endpoints require Bearer Token authentication.

Include the following header:

`Authorization: Bearer YOUR_TOKEN`

### Predefined Mock Users

| User | Token | Role |
|---|---|---|
| User A | `user-a-token` | Regular user |
| User B | `user-b-token` | Regular user |
| Administrator | `admin-token` | Admin |

### Permissions

- Regular users can manage their own investigations.
- Regular users cannot access or modify another user's investigations.
- Administrators can access and manage all investigations.

Missing or invalid tokens return HTTP 401.

Unauthorized access to another user's investigation returns HTTP 403.

## 4. Investigation Resource Endpoints

All investigation endpoints use:

`/api/v1/investigations`

### 4.1 Get All Investigations

**Method:** GET  
**Endpoint:** `/api/v1/investigations/`  
**Authentication:** Required

Returns investigations belonging to the authenticated user. Administrators can view all investigations.

Example request:

```http
GET /api/v1/investigations/
Authorization: Bearer user-a-token
```

Example success response:

```json
{
  "success": true,
  "data": [
    {
      "id": "investigation_101",
      "title": "Office Murder Case",
      "description": "Investigate the office murder.",
      "status": "active",
      "ownerId": "user-a"
    }
  ]
}
```

### 4.2 Get Investigation by ID

**Method:** GET  
**Endpoint:** `/api/v1/investigations/{investigation_id}`  
**Authentication:** Required

Returns a specific investigation if it exists and the user has permission to access it.

Example:

```http
GET /api/v1/investigations/investigation_101
Authorization: Bearer user-a-token
```

Possible responses:

- 200 – Investigation retrieved successfully.
- 401 – Missing or invalid authentication token.
- 403 – User does not own the investigation.
- 404 – Investigation does not exist.

### 4.3 Create Investigation

**Method:** POST  
**Endpoint:** `/api/v1/investigations/`  
**Authentication:** Required

Creates a new investigation owned by the authenticated user.

Example request:

```http
POST /api/v1/investigations/
Authorization: Bearer user-a-token
Content-Type: application/json
```

Request body:

```json
{
  "title": "New Mystery Case",
  "description": "Investigate a suspicious incident."
}
```

Example success response:

```json
{
  "success": true,
  "message": "Investigation created successfully",
  "data": {
    "id": "investigation_generated_id",
    "title": "New Mystery Case",
    "description": "Investigate a suspicious incident.",
    "status": "active",
    "ownerId": "user-a"
  }
}
```

HTTP status: 201 Created.

### 4.4 Update Investigation

**Method:** PUT  
**Endpoint:** `/api/v1/investigations/{investigation_id}`  
**Authentication:** Required

Updates an existing investigation owned by the authenticated user.

Example request:

```http
PUT /api/v1/investigations/investigation_101
Authorization: Bearer user-a-token
Content-Type: application/json
```

Request body:

```json
{
  "title": "Updated Mystery Case",
  "description": "Updated investigation description.",
  "status": "completed"
}
```

Possible responses:

- 200 – Investigation updated.
- 401 – Missing or invalid token.
- 403 – Insufficient permissions.
- 404 – Investigation not found.
- 422 – Invalid request data.

### 4.5 Delete Investigation

**Method:** DELETE  
**Endpoint:** `/api/v1/investigations/{investigation_id}`  
**Authentication:** Required

Deletes an existing investigation if the user has permission.

Example:

```http
DELETE /api/v1/investigations/investigation_101
Authorization: Bearer user-a-token
```

Example success response:

```json
{
  "success": true,
  "message": "Investigation deleted successfully"
}
```

## 5. Main Game Endpoints

The following game endpoints are implemented in the main application.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API welcome message and status |
| GET | `/case` | Retrieve the main case |
| GET | `/suspects` | Retrieve all suspects |
| GET | `/suspects/{suspect_id}` | Retrieve a specific suspect |
| GET | `/clues` | Retrieve all clues |
| GET | `/clues/{clue_id}` | Retrieve a specific clue |
| POST | `/ask` | Interrogate a suspect |
| POST | `/investigate` | Search a location for clues |
| GET | `/discovered-clues` | Retrieve discovered clues |
| POST | `/accuse` | Make a final accusation |

### Interrogate a Suspect

Example request:

```json
{
  "suspect_id": 1,
  "question": "Where were you on the night of the murder?"
}
```

### Investigate a Location

Example request:

```json
{
  "location": "office"
}
```

### Make a Final Accusation

Example request:

```json
{
  "suspect_id": 3
}
```

The accusation endpoint returns whether the selected suspect is the actual culprit.

## 6. Validation and Error Handling

The API uses Pydantic request models for request validation.

Common HTTP status codes:

| Status | Meaning |
|---|---|
| 200 | Successful request |
| 201 | Resource created |
| 401 | Authentication required or invalid token |
| 403 | Access forbidden |
| 404 | Resource or suspect not found |
| 422 | Request validation failed |

Example validation error from FastAPI:

```json
{
  "detail": [
    {
      "loc": ["body", "title"],
      "msg": "Field required",
      "type": "missing"
    }
  ]
}
```

Example not-found error:

```json
{
  "detail": "Investigation not found"
}
```

## 7. Mock Data

The prototype uses in-memory Python data structures instead of a real database.

Investigation information, suspects, clues, and case information are stored as mock data.

Changes to in-memory data may be lost when the backend server restarts.

## 8. Interactive API Documentation

FastAPI automatically generates interactive Swagger documentation.

Open:

`http://127.0.0.1:8000/docs`

Users can inspect endpoints, provide authentication tokens, send requests, and examine API responses.