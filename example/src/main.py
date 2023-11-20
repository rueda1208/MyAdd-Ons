# import yaml
import uvicorn
# from typing import Dict
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

# # Get configuration
# configFile = yaml.load(open("./config/config.yaml"),Loader=yaml.Loader)
# InsightHomeConfig = configFile.get('InsightHome')

# # Create eGauge client
# InsightHomeClient = InsightHome(config=InsightHomeConfig)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/datetime")
async def root():
    return {'datetime': datetime.now()}

def main() -> None:
    uvicorn.run("main:app", port=8000, reload=True)

if __name__ == "__main__":
    main()
