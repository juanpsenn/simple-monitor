import os
from dotenv import load_dotenv

import alert_builder

load_dotenv()


def check_services() -> bool:
    fail = False
    with open("temp.txt", "a") as message:
        message.write("\n SERVICIOS: \n")
        if os.getenv("SERVICES"):
            for service in os.getenv("SERVICES").split(" "):
                active = check_service(service)
                if active != 0:
                    message.write(alert_builder.messages["service"](service))
                    fail = True
    return fail


def check_service(name):
    return os.system(f"systemctl is-active --quiet {name}")
