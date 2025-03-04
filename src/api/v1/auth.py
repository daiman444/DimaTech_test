from fastapi import APIRouter, Depends

from db.session import async_session
from schemas.auth import AuthRequest, AuthResponse

auth_router = APIRouter()


@auth_router.post(
    path="/register",
    response_model=UserRegister,
)
async def register_user(
    user_data: AuthRequest,
    session: Depends(async_session),
) -> AuthResponse:
    ...
