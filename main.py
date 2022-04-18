from _datetime import datetime
import uvicorn
from fastapi import FastAPI
import requests
from requests.structures import CaseInsensitiveDict

# Initialising the api

api = FastAPI()

# Getting 10 Chuck Norris jokes

url = "http://api.icndb.com/jokes/random/"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
jokes = []


def get_jokes_from_api(number_of_jokes, website):
    jokes.clear()
    for i in range(number_of_jokes):
        resp = requests.get(website, headers=headers)
        status = resp.status_code
        if status == 200:
            resp_dict = resp.json()
            jokes.append(resp_dict['value']['joke'])

    return jokes


# API Health Checkpoint

@api.get("/health")
def check_health():
    """API health checkpoint. Used as a probe to know if the API is alive and ready to handle requests."""
    return {"status": "OK",
            "date time": str(datetime.now())}


# API Jokes Checkpoint


@api.get("/getJokes")
def get_jokes():
    """API getJokes checkpoint. Used as an endpoint to get the jokes from the api."""
    return get_jokes_from_api(10, url)


if __name__ == "__main__":
    uvicorn.run("main:api", reload=True, log_level="debug", debug=True)
