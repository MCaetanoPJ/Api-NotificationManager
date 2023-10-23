from fastapi import FastAPI

from Api.TelegramBot import SendMessageToGroupTelegram
from Enum.EnumTypeMessage import EnumTypeMessage

app = FastAPI()

@app.get("/SendMessageToTelegram/{typeMessage}&{message}")
def IndicatorCurrency(typeMessage : EnumTypeMessage, message):
    SendMessageToGroupTelegram(typeMessage, message)
    return "Message send with sucess to group in telegram."