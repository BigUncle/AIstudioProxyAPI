# utils/interceptors/base.py
from typing import Any, Protocol

class Interceptor(Protocol):
    """
    拦截器协议，定义了拦截和处理数据流的接口。
    """

    async def intercept(self, data: bytes, **kwargs: Any) -> bytes:
        """
        拦截并处理数据。

        Args:
            data: 原始数据字节流。
            **kwargs: 其他可能的参数。

        Returns:
            处理后的数据字节流。
        """
        raise NotImplementedError