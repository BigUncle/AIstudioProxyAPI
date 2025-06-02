# utils/network_utils/http_client.py
from typing import Any, Dict, Optional
import httpx

class AsyncHttpClient:
    """
    一个简单的异步 HTTP 客户端封装。
    """
    def __init__(self, timeout: float = 10.0):
        self.timeout = timeout

    async def get(self, url: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None, **kwargs: Any) -> httpx.Response:
        """
        执行异步 GET 请求。

        Args:
            url: 请求的 URL。
            params: URL 查询参数。
            headers: 请求头部。
            **kwargs: 其他传递给 httpx.AsyncClient.get 的参数。

        Returns:
            httpx.Response 对象。

        Raises:
            httpx.HTTPStatusError: 如果发生 HTTP 错误 (4xx 或 5xx 状态码)。
            httpx.RequestError: 如果发生网络请求相关的错误。
        """
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                response = await client.get(url, params=params, headers=headers, **kwargs)
                response.raise_for_status()  # 如果是 4xx 或 5xx 状态码则抛出异常
                return response
            except httpx.HTTPStatusError as e:
                # 可以选择在这里记录错误或进行特定处理
                print(f"HTTP error occurred: {e}")
                raise
            except httpx.RequestError as e:
                print(f"An error occurred while requesting {e.request.url!r}: {e}")
                raise

    async def post(self, url: str, data: Any = None, json: Any = None, headers: Optional[Dict[str, str]] = None, **kwargs: Any) -> httpx.Response:
        """
        执行异步 POST 请求。

        Args:
            url: 请求的 URL。
            data: 表单数据。
            json: JSON 数据。
            headers: 请求头部。
            **kwargs: 其他传递给 httpx.AsyncClient.post 的参数。

        Returns:
            httpx.Response 对象。

        Raises:
            httpx.HTTPStatusError: 如果发生 HTTP 错误 (4xx 或 5xx 状态码)。
            httpx.RequestError: 如果发生网络请求相关的错误。
        """
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                response = await client.post(url, data=data, json=json, headers=headers, **kwargs)
                response.raise_for_status()
                return response
            except httpx.HTTPStatusError as e:
                print(f"HTTP error occurred: {e}")
                raise
            except httpx.RequestError as e:
                print(f"An error occurred while requesting {e.request.url!r}: {e}")
                raise

# 也可以定义一组独立的异步函数，如果不需要类封装
# async def get(url: str, **kwargs: Any) -> Any:
#     """执行 GET 请求。"""
#     # 示例：使用 httpx
#     # async with httpx.AsyncClient() as client:
#     #     response = await client.get(url, **kwargs)
#     #     return response.json() # 或者 response.text, response.content
#     print(f"GET request to {url} with kwargs: {kwargs}")
#     raise NotImplementedError("GET request not implemented yet.")

# async def post(url: str, data: Any = None, json: Any = None, **kwargs: Any) -> Any:
#     """执行 POST 请求。"""
#     # 示例：使用 httpx
#     # async with httpx.AsyncClient() as client:
#     #     response = await client.post(url, data=data, json=json, **kwargs)
#     #     return response.json()
#     print(f"POST request to {url} with data: {data}, json: {json}, kwargs: {kwargs}")
#     raise NotImplementedError("POST request not implemented yet.")