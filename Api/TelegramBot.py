import requests
from datetime import datetime
from Configuration.Configuration import GetConfiguration
from Enum.EnumTypeMessage import EnumTypeMessage

configuration = GetConfiguration()
tokenApiTelegram = configuration["TokenApiTelegram"]

def GetJsonTelegram():
    try:
        url = f"https://api.telegram.org/bot{tokenApiTelegram}/getUpdates"

        response = requests.get(url)

        if (response.status_code == 200):
            json_msg = response.json()
            return json_msg
        else:
            print(f'Error to send message to telegram: : {response.status_code}')
            return ""
    except Exception as e:
        print("Error connect in API Telegram: ", e)



def SendMessageToGroupTelegram(typeMessage : EnumTypeMessage, message):
    try:
        dateTimeCurrent = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        message = f"{typeMessage} {dateTimeCurrent}:{message}"

        groupId = GetGroupIdTelegram()
        data = {"chat_id": groupId, "text": message}
        url = f"https://api.telegram.org/bot{tokenApiTelegram}/sendMessage"

        requests.post(url, data)
    except Exception as e:
        print("Error to send message to group in telegram: ", e)

def GetGroupIdTelegram():
    try:
        json_msg = GetJsonTelegram()
        for json_result in reversed(json_msg['result']):
            return json_result['message']['chat']['id']
    except Exception as e:
        print("Error to get groupId in telegram:", e)