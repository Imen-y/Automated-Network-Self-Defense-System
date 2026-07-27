import os

from dotenv import load_dotenv
from netmiko import ConnectHandler
from netmiko.exceptions import (
    NetmikoAuthenticationException,
    NetmikoTimeoutException,
)

load_dotenv()

router = {
    "device_type": "cisco_ios",
    "host": os.getenv("ROUTER_HOST"),
    "username": os.getenv("ROUTER_USERNAME"),
    "password": os.getenv("ROUTER_PASSWORD"),
}

connection = None

try:

    connection = ConnectHandler(**router)

    print("=" * 60)
    print("Hostname")
    print("=" * 60)
    print(connection.send_command(
        "show running-config | include hostname"
    ))

    print("\n" + "=" * 60)
    print("IOS Version")
    print("=" * 60)
    print(connection.send_command(
        "show version | include Cisco IOS"
    ))

    print("\n" + "=" * 60)
    print("Interfaces")
    print("=" * 60)
    print(connection.send_command(
        "show ip interface brief"
    ))

except NetmikoTimeoutException:
    print("Erreur : impossible de joindre le routeur Cisco.")

except NetmikoAuthenticationException:
    print("Erreur : échec de l'authentification Cisco.")

except Exception as error:
    print(f"Erreur inattendue : {error}")

finally:
    if connection:
        connection.disconnect()