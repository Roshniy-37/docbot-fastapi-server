from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Your Medical Assistant"}


@app.get("/msg/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}



@app.get("/api/chat/{msg}")
async def send_message(msg):
    print(msg)
    # Handle the received message (you can replace this logic with your own)
    # user_message = message.message
    # response = process_user_message(user_message)

    return {"response": "Hii I am working"}



def process_user_message(user_message):
    # Here, you can implement your logic to process the user's message
    # and generate a response. For this example, we'll just echo the message.
    return f"You said: {user_message}"
