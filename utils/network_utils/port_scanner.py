# utils/network_utils/port_scanner.py
import asyncio
import socket
from typing import Optional

async def check_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """
    异步检查指定主机的端口是否开放。

    Args:
        host: 主机名或 IP 地址。
        port: 要检查的端口号。
        timeout: 连接超时时间（秒）。

    Returns:
        如果端口开放则返回 True，否则返回 False。
    """
    try:
        conn = asyncio.open_connection(host, port)
        _, writer = await asyncio.wait_for(conn, timeout=timeout)
        writer.close()
        await writer.wait_closed()
        return True
    except (socket.error, asyncio.TimeoutError, ConnectionRefusedError, OSError):
        return False

async def find_available_port(start_port: int, end_port: int, host: str = "127.0.0.1") -> Optional[int]:
    """
    异步查找指定范围内的可用端口。

    Args:
        start_port: 开始搜索的端口号。
        end_port: 结束搜索的端口号。
        host: 要检查的主机，默认为 "127.0.0.1"。

    Returns:
        如果找到可用端口则返回端口号，否则返回 None。
    """
    for port in range(start_port, end_port + 1):
        if not await check_port(host, port, timeout=0.1):  # 使用较短的超时进行快速扫描
            # 进一步确认端口是否真的可用，避免快速扫描的误判
            # (在某些系统上，即使端口未被监听，check_port 也可能因防火墙等原因快速失败)
            # 这里可以尝试绑定一下端口来确认
            try:
                # 尝试创建一个临时服务器套接字来绑定端口
                temp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                temp_socket.bind((host, port))
                temp_socket.close()
                return port
            except socket.error:
                continue  # 端口已被占用
    return None