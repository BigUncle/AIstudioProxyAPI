# utils/network_utils/exceptions.py

class NetworkUtilError(Exception):
    """
    网络工具模块的基础异常类。
    """
    pass

class HttpRequestError(NetworkUtilError):
    """
    当 HTTP 请求失败时抛出。
    """
    pass

class PortScanError(NetworkUtilError):
    """
    当端口扫描操作失败时抛出。
    """
    pass