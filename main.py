from datetime import datetime

from helpers import telegram_send_message
import os

from dotenv import load_dotenv

from resources import check_resources
from services import check_services

load_dotenv()


def show_me_something():
    with open("temp.txt", "w") as message:
        message.write(f"Reporte de estado {os.getenv('SERVER_NAME')} - {str(datetime.now())}\n")
    fail_r = check_resources()
    fail_s = check_services()
    if fail_r or fail_s:
        with open("temp.txt", "r") as message:
            data = message.read()
            telegram_send_message(data)


show_me_something()
