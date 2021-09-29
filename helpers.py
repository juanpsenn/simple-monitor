import requests
import os
from dotenv import load_dotenv

load_dotenv()


def telegram_send_message(message):
    send_text = (
        "https://api.telegram.org/bot"
        + os.getenv("BOTTOKEN")
        + "/sendMessage?chat_id="
        + os.getenv("CHATID")
        + "&parse_mode=Markdown&text="
        + message
    )

    response = requests.get(send_text)

    return response.json()
