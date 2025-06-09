from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://chatdoctor.onrender.com"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

generator = pipeline("text-generation", model="linkanjarad/Doctor-OPT-350M")

@app.post("/api/chat")
async def chat(request: Request):
    data = await request.json()
    prompt = f"Patient: {data['message']}\nDoctor: <start>"
    output = generator(
        prompt,
        do_sample=True,
        min_length=10,
        max_length=500,
        temperature=0.5
    )
    return {"response": output[0]["generated_text"]}
