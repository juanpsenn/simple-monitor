import os
from operator import gt
from typing import Optional

import psutil
from dotenv import load_dotenv

import alert_builder

load_dotenv()

resources = [
    {
        "name": "ram",
        "get_resource_value": lambda: psutil.virtual_memory()[2],
        "comparator": gt,
        "var_name": "MAX_RAM",
    },
    {
        "name": "storage",
        "get_resource_value": lambda: psutil.disk_usage("/")[3],
        "comparator": gt,
        "var_name": "MAX_STORAGE",
    },
]


def check_resources() -> bool:
    fail = False
    with open("temp.txt", "a") as message:
        message.write("\n RECURSOS:\n")
        for resource in resources:
            alert = check_resource(**resource)
            if alert:
                fail = True
                message.write(alert)
    return fail


def check_resource(
    name: str, get_resource_value, comparator, var_name: str
) -> Optional[str]:
    value = get_resource_value()
    if comparator(value, float(os.getenv(var_name))):
        return alert_builder.messages[name](value)
    return None
