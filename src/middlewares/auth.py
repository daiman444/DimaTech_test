from fastapi import Request, HTTPException

from starlette.middleware.base import(
    BaseHTTPMiddleware,
    DispatchFunction,
)

from core.oauth import oauth


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self,
        request: Request,
        call_next: DispatchFunction,
    ):
        public_path = {
            "/docs",
            "/openapi.json",
            "/api/auth/signin",
            "/api/auth/signup",
        }
        if request.url.path in  public_path:
            return await call_next(request)
        
        authorization: str = request.headers.get("Authorization")
        
        if not authorization or not authorization.startswith("Bearer "):
            raise HTTPException(
                status_code=401,
                detail="Missing token",
            )
        
        token = authorization.split(" ")[1]
        payload = await oauth.decode_token(token=token)
        request.state.user = payload
        return await call_next(request)




