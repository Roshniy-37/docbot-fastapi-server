from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://chatdoctor.onrender.com/"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

generator = pipeline("text-generation", model="linkanjarad/Doctor-OPT-350M")

@app.post("/api/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get("message", "")
    print(f"Received message: {message}")
    if not message:
        return {"response": "Please provide a message."}
    
    try:
        response = generator(message, max_length=100, do_sample=True)[0]["generated_text"]
        print(f"Generated response: {response}")
    except Exception as e:
        print(f"Error generating response: {e}")
        return {"response": "Error generating response."}
    
    return {"response": response}
