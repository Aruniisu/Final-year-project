from fastapi import FastAPI
from pydantic import BaseModel
from agent import process_command

app = FastAPI()

class RequestData(BaseModel):
    command: str

@app.post("/run")
def run_command(data: RequestData):
    result = process_command(data.command)
    return {"response": result}