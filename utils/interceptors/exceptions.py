# utils/interceptors/exceptions.py

class InterceptorError(Exception):
    """
    拦截器模块的基础异常类。
    """
    pass

class InterceptorConfigError(InterceptorError):
    """
    当拦截器配置错误时抛出。
    """
    pass

class DataTransformationError(InterceptorError):
    """
    当数据转换失败时抛出。
    """
    pass