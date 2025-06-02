# core/auth_service/exceptions.py

"""
本模块定义了 `auth_service` 模块特定的异常类。
"""

class AuthServiceError(Exception):
    """
    认证服务模块的基础异常类。
    所有 `auth_service` 模块抛出的特定异常都应继承此类。
    """
    pass

class AuthenticationFailed(AuthServiceError):
    """
    表示用户认证失败的错误。
    """
    pass

class AuthorizationFailed(AuthServiceError):
    """
    表示请求授权失败的错误。
    """
    pass

class SessionManagementError(AuthServiceError):
    """
    表示会话管理过程中发生的错误。
    例如，无法加载或保存会话状态。
    """
    pass

# 可以根据需要添加更多特定的异常类