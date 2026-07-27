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


def execute_config(commands: list[str]) -> bool:
    """
    Execute a list of Cisco IOS configuration commands.

    Args:
        commands (list[str]): Cisco IOS configuration commands.

    Returns:
        bool: True if the commands were executed successfully,
              False otherwise.
    """

    connection = None

    try:
        connection = ConnectHandler(**router)

        output = connection.send_config_set(commands)

        print(output)

        return True

    except NetmikoTimeoutException:
        print("Erreur : impossible de joindre le routeur Cisco.")
        return False

    except NetmikoAuthenticationException:
        print("Erreur : échec de l'authentification Cisco.")
        return False

    except Exception as error:
        print(f"Erreur inattendue : {error}")
        return False

    finally:
        if connection:
            connection.disconnect()


def block_ip(ip_address: str) -> bool:
    """
    Create an ACL entry to block a source IP address.

    Args:
        ip_address (str): Attacker IP address.

    Returns:
        bool: True if the ACL was created successfully,
              False otherwise.
    """

    commands = [
        "ip access-list extended ANSDS-BLOCK",
        f"deny ip host {ip_address} any",
    ]

    return execute_config(commands)


def remove_acl() -> bool:
    """
    Remove the ANSDS ACL.

    Returns:
        bool: True if the ACL was removed successfully,
              False otherwise.
    """

    commands = [
        "no ip access-list extended ANSDS-BLOCK"
    ]

    return execute_config(commands)