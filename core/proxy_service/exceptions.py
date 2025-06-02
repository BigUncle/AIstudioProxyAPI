# core/proxy_service/exceptions.py

"""
本模块定义了 `proxy_service` 模块特定的异常类。
"""

class ProxyServiceError(Exception):
    """
    代理服务模块的基础异常类。
    所有 `proxy_service` 模块抛出的特定异常都应继承此类。
    """
    pass

class ProxyConnectionError(ProxyServiceError):
    """
    表示代理连接过程中发生的错误。
    例如，无法连接到目标服务器，或连接意外断开等。
    """
    pass

class ProxyConfigurationError(ProxyServiceError):
    """
    表示代理服务配置相关的错误。
    例如，无效的端口号，或缺失必要的配置项。
    """
    pass

class DataTransformationError(ProxyServiceError):
    """
    表示在拦截和转换数据流过程中发生的错误。
    """
    pass

# 可以根据需要添加更多特定的异常类