import logging
from pathlib import Path


# ---------------------------------
# ANSDS log file
# ---------------------------------

BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "ansds.log"

LOG_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------
# Logger configuration
# ---------------------------------

logger = logging.getLogger("ANSDS")
logger.setLevel(logging.INFO)

if not logger.handlers:

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


# ---------------------------------
# Security event logger
# ---------------------------------

def log_event(event: str, **details) -> None:
    """
    Write a structured ANSDS security event to ansds.log.
    """

    if details:
        detail_text = " | ".join(
            f"{key}={value}"
            for key, value in details.items()
        )

        logger.info(
            f"EVENT={event} | {detail_text}"
        )

    else:
        logger.info(
            f"EVENT={event}"
        )
