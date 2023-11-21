import os
import uvicorn
import logging
from requests import get
from fastapi import FastAPI
from datetime import datetime
# import yaml
# from typing import Dict

logger = logging.getLogger(__name__)
app = FastAPI()

# # Get configuration
# configFile = yaml.load(open("./config/config.yaml"),Loader=yaml.Loader)
# serviceNameConfig = configFile.get('serviceName')

URL_BASE = "http://supervisor/core"
SUPERVISOR_TOKEN = os.getenv('SUPERVISOR_TOKEN')
HEADERS = {"Authorization": f"Bearer {SUPERVISOR_TOKEN}", "content-type": "application/json"}

@app.get("/")
async def root():
    payload = get(URL_BASE + '/api', headers=HEADERS)
    return payload.jscon()

@app.get("/states")
async def root():
    payload = get(URL_BASE + '/api/states', headers=HEADERS)
    return payload.json()

def main() -> None:
    uvicorn.run("main:app", port=8000, reload=True)

if __name__ == "__main__":
    main()
