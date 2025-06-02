class LLMServiceError(Exception):
    """
    LLM 服务模块的基础异常类。
    """
    pass

class ModelNotFoundError(LLMServiceError):
    """
    当请求的模型未找到或不可用时引发的异常。
    """
    pass

class LLMAPIError(LLMServiceError):
    """
    当与 LLM 服务 API 交互发生错误时引发的异常。
    """
    pass

# 可以根据需要添加更多特定的异常类
# 例如:
# class RateLimitError(LLMServiceError):
#     """当达到 API 调用频率限制时引发。"""
#     pass

# class AuthenticationError(LLMServiceError):
#     """当 LLM 服务认证失败时引发。"""
#     pass