# main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

class InputText(BaseModel):
    message: str

@app.post("/process")
async def process_text(data: InputText):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": data.message}]
    )
    return {"response": response.choices[0].message["content"]}
