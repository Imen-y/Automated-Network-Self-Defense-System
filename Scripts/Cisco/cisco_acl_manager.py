import os
import threading

from dotenv import load_dotenv
from netmiko import ConnectHandler
from netmiko.exceptions import (
    NetmikoAuthenticationException,
    NetmikoTimeoutException,
)
from Scripts.Logging.ansds_logger import log_event


# ---------------------------------
# Configuration
# ---------------------------------

BLOCK_DURATION = 60  # seconds


# ---------------------------------
# Environment configuration
# ---------------------------------

load_dotenv()

router = {
    "device_type": "cisco_ios",
    "host": os.getenv("ROUTER_HOST"),
    "username": os.getenv("ROUTER_USERNAME"),
    "password": os.getenv("ROUTER_PASSWORD"),
}


# ---------------------------------
# Execute Cisco configuration
# ---------------------------------

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


# ---------------------------------
# Unblock IP
# ---------------------------------

def unblock_ip(ip_address: str) -> bool:
    """
    Remove the temporary Cisco ACL block for a source IP.

    Args:
        ip_address (str): Source IP address to unblock.

    Returns:
        bool: True if the IP was successfully unblocked,
              False otherwise.
    """

    print(
        f"[+] Temporary block expired for {ip_address}. "
        f"Removing Cisco ACL..."
    )

    log_event(
       "TEMPORARY_BLOCK_EXPIRED",
       source_ip=ip_address,
       acl="ANSDS-BLOCK"
    )

    commands = [
        "interface FastEthernet1/1",
        "no ip access-group ANSDS-BLOCK in",
        "exit",
        "no ip access-list extended ANSDS-BLOCK",
    ]

    success = execute_config(commands)

    if success:
        print(
            f"[+] IP {ip_address} unblocked successfully on Cisco."
        )

        log_event(
           "IP_UNBLOCKED",
           source_ip=ip_address,
           acl="ANSDS-BLOCK",
           interface="FastEthernet1/1"
        )

    else:
        print(
            f"[-] Failed to unblock IP {ip_address} on Cisco."
        )

    return success


# ---------------------------------
# Block IP
# ---------------------------------

def block_ip(ip_address: str) -> bool:
    """
    Create and apply a temporary ACL entry
    to block a source IP address.

    The block is automatically removed after
    BLOCK_DURATION seconds.

    Args:
        ip_address (str): Source IP address to block.

    Returns:
        bool: True if the IP was successfully blocked,
              False otherwise.
    """

    print(
        f"[+] Blocking IP {ip_address} on Cisco "
        f"for {BLOCK_DURATION} seconds..."
    )

    commands = [
        "ip access-list extended ANSDS-BLOCK",
        f"deny ip host {ip_address} any",
        "exit",
        "interface FastEthernet1/1",
        "ip access-group ANSDS-BLOCK in",
    ]

    success = execute_config(commands)

    if not success:
        print(
            f"[-] Failed to block IP {ip_address} on Cisco."
        )
        return False

    print(
        f"[+] IP {ip_address} blocked successfully on Cisco."
    )

    log_event(
       "IP_BLOCKED",
       source_ip=ip_address,
       duration=f"{BLOCK_DURATION}s",
       acl="ANSDS-BLOCK",
       interface="FastEthernet1/1"
    )

    print(
        f"[+] Automatic unblock scheduled in "
        f"{BLOCK_DURATION} seconds."
    )

    log_event(
       "TEMPORARY_BLOCK_SCHEDULED",
       source_ip=ip_address,
       duration=f"{BLOCK_DURATION}s"
    )

    # Schedule automatic unblock
    timer = threading.Timer(
        BLOCK_DURATION,
        unblock_ip,
        args=(ip_address,)
    )

    timer.start()

    return True


# ---------------------------------
# Manual ACL removal
# ---------------------------------

def remove_acl() -> bool:
    """
    Remove the ANSDS ACL from the Cisco router.

    Returns:
        bool: True if the ACL was removed successfully,
              False otherwise.
    """

    commands = [
        "interface FastEthernet1/1",
        "no ip access-group ANSDS-BLOCK in",
        "exit",
        "no ip access-list extended ANSDS-BLOCK",
    ]

    return execute_config(commands)
