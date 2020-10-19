# Insurance Recommender

This application receives the user profile through the API and transforms it into a risk profile by calculating a risk score for each line of insurance (life, disability, home & auto) based on the information.

## Run locally

It is recommended to use virtualenv or pyenv.

Requirements:

- Python 3.8

```
pip install -r requirements-dev.txt
```

```
PYTHONPATH=app uvicorn main:app --reload
```

## Documentation

Interactive documentation will be available on:

http://127.0.0.1:8000/docs
