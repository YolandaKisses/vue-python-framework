"""Authentication endpoints."""

from datetime import timedelta
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel

from core.config import settings
from core.deps import TokenData
from schemas import Token, User
from utils.crypto import decrypt

router = APIRouter()


# 硬编码的测试用户（生产环境请使用数据库）
TEST_USERS: dict[str, dict[str, str]] = {
    "admin": {
        "password": "123456",
        "username": "admin",
        "email": "admin@example.com",
    },
}


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """Create JWT access token."""
    from jose import jwt

    to_encode = data.copy()
    expire = timedelta(minutes=settings.access_token_expire_minutes)
    if expires_delta:
        expire = expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        settings.secret_key,
        algorithm=settings.algorithm,
    )
    return encoded_jwt


class LoginRequest(BaseModel):
    """登录请求模型 - 支持加密密码"""
    username: str
    password: str  # 前端加密后的密码


class LoginResponse(BaseModel):
    """登录响应模型"""
    access_token: str
    token_type: str = "bearer"


@router.post("/login", response_model=LoginResponse)
async def login(login_data: LoginRequest) -> LoginResponse:
    """
    用户登录接口

    接收前端加密的密码，解密后验证
    """
    try:
        # 解密密码
        decrypted_password = decrypt(login_data.password)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="密码解密失败",
        )

    # 验证用户名和密码
    user_info = TEST_USERS.get(login_data.username)

    if not user_info or user_info["password"] != decrypted_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
        )

    # 生成 token
    access_token = create_access_token(
        data={
            "sub": login_data.username,
            "username": user_info["username"],
            "email": user_info["email"],
        }
    )

    return LoginResponse(
        access_token=access_token,
        token_type="bearer",
    )


@router.get("/me", response_model=User)
async def get_current_user(
    current_user: Annotated[TokenData, Depends()]
) -> User:
    """获取当前登录用户信息"""
    user_info = TEST_USERS.get(current_user.user_id or "")
    if not user_info:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="用户不存在",
        )

    return User(
        id=1,
        username=user_info["username"],
        email=user_info["email"],
        is_active=True,
    )


@router.post("/refresh", response_model=Token)
async def refresh_token(current_user: Annotated[TokenData, Depends()]) -> Token:
    """刷新访问令牌"""
    user_info = TEST_USERS.get(current_user.user_id or "")
    if not user_info:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="用户不存在",
        )

    access_token = create_access_token(
        data={
            "sub": current_user.user_id,
            "username": user_info["username"],
            "email": user_info["email"],
        }
    )

    return Token(
        access_token=access_token,
        token_type="bearer",
    )


@router.post("/logout")
async def logout() -> dict[str, str]:
    """用户登出"""
    return {"message": "Successfully logged out"}