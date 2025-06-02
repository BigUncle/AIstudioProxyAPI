from pydantic import BaseModel
from typing import Dict, Any

class UserCredentials(BaseModel):
    """
    用户凭据模型。
    """
    username: str
    password: str

class AuthToken(BaseModel):
    """
    认证令牌模型。
    """
    access_token: str
    token_type: str

class SessionState(BaseModel):
    """
    会话状态模型。
    """
    profile_name: str
    state_data: Dict[str, Any]

# 可以根据需要添加更多与认证和会话相关的 Pydantic 模型