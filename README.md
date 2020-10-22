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
