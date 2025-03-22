from typing import Annotated

from fastapi import Security
from fastapi.security import APIKeyHeader

from core.security.globals import HEADER_TOKEN_KEY

HeaderTokenSec = Annotated[
    str,
    Security(APIKeyHeader(name=HEADER_TOKEN_KEY, auto_error=False)),
]
