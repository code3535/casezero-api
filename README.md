# CaseZero – AI Mystery Game

## Project Description

CaseZero is an interactive AI Mystery Game prototype developed as part of the Software Engineering course at ADA University.

The system allows users to investigate a fictional murder case, examine crime scenes, discover clues, interrogate suspects, and make accusations to identify the culprit.

The project consists of a FastAPI backend and an HTML, CSS, and JavaScript frontend.

## Team Members

- **Orkhan Ahmadov** – Backend API development, authentication, authorization, investigation CRUD operations, and API design.
- **Mahsun Alkhasov** – Frontend development, user interface, and frontend/backend integration.

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for details.

## Technologies Used

### Backend
- Python
- FastAPI
- Pydantic
- Uvicorn

### Frontend
- HTML5
- CSS3
- JavaScript

### Development Tools
- Visual Studio Code
- Git and GitHub
- FastAPI Swagger UI

## Project Structure

```text
casezero-api/
│
├── app/
│   ├── main.py
│   ├── auth.py
│   ├── models.py
│   ├── data.py
│   └── routers/
│       ├── __init__.py
│       └── investigations.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── docs/
│   ├── API_DOCUMENTATION.md
│   └── EXAMPLES.md
│
├── CONTRIBUTORS.md
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/code3535/casezero-api.git
cd casezero-api
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

macOS / Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Backend

```bash
uvicorn app.main:app --reload
```

The backend will run at:

`http://127.0.0.1:8000`

## API Documentation

FastAPI provides interactive API documentation through Swagger UI.

Open:

`http://127.0.0.1:8000/docs`

The API documentation describes available endpoints, request parameters, authentication, and responses.

Additional documentation:

- [API Documentation](docs/API_DOCUMENTATION.md)
- [API Examples](docs/EXAMPLES.md)

## Mock Authentication

The project uses predefined mock Bearer tokens.

| User | Token | Role |
|---|---|---|
| User A | `user-a-token` | Regular user |
| User B | `user-b-token` | Regular user |
| Administrator | `admin-token` | Admin |

Include the token in the Authorization header:

```http
Authorization: Bearer user-a-token
```

Regular users can manage only their own investigations, while administrators can manage all investigations.

## Mock Data

The project uses in-memory mock data rather than a real database.

This allows the team to demonstrate API functionality, CRUD operations, authentication, and authorization without implementing database integration.

**Important:** Data changes are not permanently stored. Newly created investigations and discovered clues may reset when the backend server restarts.

## Main Features

- Retrieve the main mystery case.
- View suspects and clues.
- Interrogate suspects.
- Investigate locations and discover clues.
- View discovered clues.
- Make final accusations.
- Create, retrieve, update, and delete investigations.
- Token-based authentication.
- Role-based authorization and ownership checks.

## Git Contribution Summary

Output of `git shortlog -sn --all`:

```text
6  Orkhan Ahmadov
2  Mahsun
```

### Contribution Overview

**Orkhan Ahmadov**
- Backend API implementation.
- Authentication and authorization.
- Investigation CRUD operations.
- Mock data and API integration.

**Mahsun**
- Frontend implementation.
- HTML, CSS, and JavaScript.
- Frontend/backend communication.

## Academic Context

Developed for Assignment 2 – API Prototype with Mocked Backend and Frontend, as part of the Software Engineering course at ADA University.