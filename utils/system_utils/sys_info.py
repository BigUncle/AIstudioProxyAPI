# utils/system_utils/sys_info.py
import platform
from typing import Dict, Any, Optional

# 尝试导入 psutil，如果失败则将其设为 None，并在需要时处理
try:
    import psutil
except ImportError:
    psutil = None

def get_os_version() -> str:
    """
    获取操作系统版本信息。

    Returns:
        操作系统版本字符串。
    """
    return platform.platform()

def get_cpu_usage() -> float:
    """
    获取当前 CPU 使用率。

    Returns:
        CPU 使用率 (百分比)。
        如果 psutil 不可用，则返回 -1.0 并打印警告。
    """
    if psutil:
        return psutil.cpu_percent(interval=1)
    else:
        print("警告: psutil 未安装，无法获取 CPU 使用率。返回 -1.0。")
        return -1.0

def get_memory_info() -> Dict[str, Any]:
    """
    获取内存使用信息。

    Returns:
        一个包含内存信息的字典，例如：
        {
            'total': '总内存 (GB)',
            'available': '可用内存 (GB)',
            'percent': '内存使用率 (%)',
            'used': '已用内存 (GB)',
            'free': '空闲内存 (GB)'
        }
        如果 psutil 不可用，则返回一个包含错误信息的字典。
    """
    if psutil:
        mem = psutil.virtual_memory()
        return {
            "total": f"{mem.total / (1024**3):.2f} GB",
            "available": f"{mem.available / (1024**3):.2f} GB",
            "percent": mem.percent,
            "used": f"{mem.used / (1024**3):.2f} GB",
            "free": f"{mem.free / (1024**3):.2f} GB",
        }
    else:
        print("警告: psutil 未安装，无法获取内存信息。")
        return {"error": "psutil not available"}

def get_disk_usage(path: str = '/') -> Optional[Dict[str, Any]]:
    """
    获取指定路径的磁盘使用情况。

    Args:
        path: 要检查的磁盘路径，默认为根目录。

    Returns:
        一个包含磁盘使用信息的字典，例如：
        {
            'total': '总空间 (GB)',
            'used': '已用空间 (GB)',
            'free': '可用空间 (GB)',
            'percent': '使用率 (%)'
        }
        如果 psutil 不可用或路径无效，则返回 None。
    """
    if psutil:
        try:
            disk = psutil.disk_usage(path)
            return {
                "total": f"{disk.total / (1024**3):.2f} GB",
                "used": f"{disk.used / (1024**3):.2f} GB",
                "free": f"{disk.free / (1024**3):.2f} GB",
                "percent": disk.percent,
            }
        except FileNotFoundError:
            print(f"警告: 路径 '{path}' 未找到，无法获取磁盘使用情况。")
            return None
        except Exception as e:
            print(f"警告: 获取路径 '{path}' 的磁盘使用情况时发生错误: {e}")
            return None
    else:
        print("警告: psutil 未安装，无法获取磁盘使用情况。")
        return None

if __name__ == '__main__':
    print(f"操作系统版本: {get_os_version()}")
    print(f"CPU 使用率: {get_cpu_usage()}%")
    mem_info = get_memory_info()
    if "error" not in mem_info:
        print(f"内存信息: 总共 {mem_info['total']}, 可用 {mem_info['available']}, 使用率 {mem_info['percent']}%")
    else:
        print(f"内存信息: {mem_info['error']}")

    disk_info_root = get_disk_usage('/')
    if disk_info_root:
        print(f"根目录磁盘使用: 总共 {disk_info_root['total']}, 已用 {disk_info_root['used']}, 使用率 {disk_info_root['percent']}%")

    # 示例：检查当前目录所在磁盘 (Windows 上可能需要指定驱动器号如 'C:/')
    current_dir_disk_info = get_disk_usage('.')
    if current_dir_disk_info:
        print(f"当前目录磁盘使用: 总共 {current_dir_disk_info['total']}, 已用 {current_dir_disk_info['used']}, 使用率 {current_dir_disk_info['percent']}%")