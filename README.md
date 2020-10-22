# Insurance Recommender Engine (IRE)

This application receives the user profile through the API and transforms it into a risk profile by calculating a risk score for each line of insurance (life, disability, home & auto) based on the information.

## Run locally

**Requirements:**

- Python ^3.7
- [Poetry](https://python-poetry.org/)
- Optional: [pre-commit](https://pre-commit.com/)

**Required steps:**

Then:

```
poetry install
```

```
poetry shell
```

```
uvicorn main:app --reload --app-dir ire
```

## Documentation

Interactive documentation will be available on:

http://127.0.0.1:8000/docs

## Endpoints

POST /api/v1/risk

Example call:

```
curl -X POST "http://localhost:8000/api/v1/risk/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"age\":35,\"dependents\":2,\"house\":{\"ownership_status\":\"owned\"},\"income\":0,\"marital_status\":\"married\",\"risk_questions\":[0,1,0],\"vehicle\":{\"year\":2018}}"
```
