# core/gui_service/exceptions.py

"""
本模块定义了 `gui_service` 模块特定的异常类。
"""

class GuiServiceError(Exception):
    """
    GUI 服务模块的基础异常类。
    所有 `gui_service` 模块抛出的特定异常都应继承此类。
    """
    pass

class ProcessManagementError(GuiServiceError):
    """
    表示进程管理过程中发生的错误。
    例如，无法启动或停止指定的进程。
    """
    pass

class PortInUseError(GuiServiceError):
    """
    表示尝试使用的端口已被占用的错误。
    """
    pass

# 可以根据需要添加更多特定的异常类