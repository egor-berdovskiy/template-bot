from . import logging, payments
from typing import Dict, Any


def utils_setup(data: Dict[str, Any]):
    logging.init()


async def close(data: Dict[str, Any]):
    pass