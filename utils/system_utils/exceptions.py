# utils/system_utils/exceptions.py

class SystemUtilError(Exception):
    """
    system_utils 模块中所有自定义异常的基类。
    """
    pass

class ProcessManagerError(SystemUtilError):
    """
    与进程管理相关的操作失败时引发的异常。
    """
    pass

class ProcessExecutionError(ProcessManagerError):
    """
    执行外部命令失败时引发的异常。
    """
    def __init__(self, command: str, return_code: int, stdout: str, stderr: str):
        self.command = command
        self.return_code = return_code
        self.stdout = stdout
        self.stderr = stderr
        super().__init__(
            f"命令 '{command}' 执行失败，返回码: {return_code}\n"
            f"STDOUT: {stdout}\n"
            f"STDERR: {stderr}"
        )

class ProcessNotFoundError(ProcessManagerError):
    """
    当尝试操作一个不存在的进程时引发的异常。
    """
    def __init__(self, pid: int):
        self.pid = pid
        super().__init__(f"未找到 PID 为 {pid} 的进程。")

class SystemInfoError(SystemUtilError):
    """
    获取系统信息失败时引发的异常。
    """
    pass

class PsutilNotAvailableError(SystemUtilError):
    """
    当 psutil 库不可用但又是必需的时引发的异常。
    """
    def __init__(self, feature_name: str):
        self.feature_name = feature_name
        super().__init__(f"psutil 库未安装或不可用，无法使用 '{feature_name}' 功能。")

# 可以在这里根据需要添加更多特定的异常类
# 例如:
# class InsufficientPermissionsError(ProcessManagerError):
#     """当操作因权限不足而失败时引发。"""
#     pass