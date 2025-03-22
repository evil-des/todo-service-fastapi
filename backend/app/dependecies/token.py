from typing import Annotated

from fastapi import Depends

from core.security.token import get_user_token
from schemas.token import TokenSchema

TokenDependency = Annotated[TokenSchema, Depends(get_user_token)]
