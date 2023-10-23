from fastapi import FastAPI
from TelegramBot import *

app = FastAPI()

@app.get("/SendMessageToTelegram/{typeMessage}&{message}")
def SendMessageToTelegram(typeMessage, message):
    SendMessageToGroupTelegram(typeMessage, message)
    return "Message send with sucess to group in telegram."