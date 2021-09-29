import os
from dotenv import load_dotenv

load_dotenv()


def ram(resource_value):
    return (
        "\t- Se detecta un uso elevado de RAM. "
        "El porcentaje de utilziacion ({}%) esta por encima del {}%\n".format(
            resource_value, os.getenv("MAX_RAM")
        )
    )


def storage(resource_value):
    return (
        "\t- Se detecta un uso elevado de alamcenamiento. "
        "El porcentaje total disponible ({}%) esta encima de del {}%\n".format(
            resource_value, os.getenv("MAX_STORAGE")
        )
    )


def service(name):
    return "\t- {} esta inactivo.\n".format(name)


messages = {"ram": ram, "storage": storage, "service": service}
