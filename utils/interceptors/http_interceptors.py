# utils/interceptors/http_interceptors.py
from typing import Any
from .base import Interceptor

class ModifyHeadersInterceptor(Interceptor):
    """
    一个示例拦截器，用于修改 HTTP 头部。
    """
    async def intercept(self, data: bytes, **kwargs: Any) -> bytes:
        """
        拦截并修改 HTTP 头部。

        Args:
            data: 原始数据字节流 (例如 HTTP 请求或响应)。
            **kwargs: 可能包含头部信息等。

        Returns:
            处理后的数据字节流。
        """
        # 示例：此处可以添加修改头部的逻辑
        # http_headers = kwargs.get("headers", {})
        # http_headers["X-Custom-Header"] = "MyValue"
        # # 根据实际情况重新构建 data
        print(f"ModifyHeadersInterceptor: Intercepted data (first 100 bytes): {data[:100]}")
        print(f"ModifyHeadersInterceptor: kwargs: {kwargs}")
        return data

class ContentBlockInterceptor(Interceptor):
    """
    一个示例拦截器，用于阻止特定内容的传输。
    """
    def __init__(self, blocked_patterns: list[bytes]):
        self.blocked_patterns = blocked_patterns

    async def intercept(self, data: bytes, **kwargs: Any) -> bytes:
        """
        拦截并检查是否包含被阻止的内容。

        Args:
            data: 原始数据字节流。
            **kwargs: 其他可能的参数。

        Returns:
            如果包含被阻止的内容，则可能返回空字节流或抛出异常；
            否则返回原始数据。
        """
        for pattern in self.blocked_patterns:
            if pattern in data:
                # 示例：阻止包含特定模式的数据
                print(f"ContentBlockInterceptor: Blocked pattern '{pattern.decode(errors='ignore')}' found.")
                return b""  # 返回空字节表示阻止
        return data