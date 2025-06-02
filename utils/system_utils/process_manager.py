# utils/system_utils/process_manager.py
import asyncio
import os
import signal
import subprocess
from typing import Tuple, List, Optional, Any

# 尝试导入 psutil，如果失败则将其设为 None，并在需要时处理
try:
    import psutil
except ImportError:
    psutil = None

class ProcessManager:
    """
    封装进程管理相关的功能。
    """

    @staticmethod
    def is_process_running(pid: int) -> bool:
        """
        检查具有给定 PID 的进程是否正在运行。

        Args:
            pid: 要检查的进程 ID。

        Returns:
            如果进程正在运行则返回 True，否则返回 False。
        """
        if psutil:
            return psutil.pid_exists(pid)
        else:
            # psutil 不可用时的备用方法 (可能因平台而异且不太可靠)
            try:
                os.kill(pid, 0)
            except OSError:
                return False
            else:
                return True

    @staticmethod
    def kill_process(pid: int) -> bool:
        """
        终止具有给定 PID 的进程。

        Args:
            pid: 要终止的进程 ID。

        Returns:
            如果进程成功终止则返回 True，否则返回 False。
        """
        if psutil:
            try:
                process = psutil.Process(pid)
                process.terminate()  # 或者 process.kill()
                process.wait(timeout=3) # 等待进程终止
                return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired):
                return False
        else:
            # psutil 不可用时的备用方法
            try:
                os.kill(pid, signal.SIGTERM)  # 或者 signal.SIGKILL
                return True
            except OSError:
                return False

    @staticmethod
    async def run_command(command: str, shell: bool = True, cwd: Optional[str] = None) -> Tuple[str, str, int]:
        """
        异步运行 shell 命令并返回输出和返回码。

        Args:
            command: 要执行的命令字符串。
            shell: 是否通过 shell 执行命令。如果为 True，则通过 shell 执行。
                   注意: Pylance 可能会对此参数的类型提示发出警告，但 asyncio.create_subprocess_shell 期望 shell=True。
                   如果需要 shell=False 的行为，应考虑使用 asyncio.create_subprocess_exec。
            cwd: 执行命令的工作目录。

        Returns:
            一个元组 (stdout, stderr, return_code)。
        """
        if not shell:
            # 如果调用者明确设置 shell=False，但我们这里只用 create_subprocess_shell，
            # 这可能不是预期的行为。但为了骨架代码的简单性，我们暂时只处理 shell=True 的情况。
            # 在实际应用中，这里可能需要根据 shell 的值选择不同的 asyncio.create_subprocess_xxx 函数。
            # 或者，如果此函数设计为总是通过 shell 执行，则可以移除 shell 参数或固定其值为 True。
            # 为了消除 Pylance 警告，并且因为函数签名默认为 True，我们将在此处硬编码为 True。
            # 如果需要 shell=False 的功能，应创建另一个函数或修改此函数以使用 create_subprocess_exec。
            pass # 保持 shell = True 的行为

        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            shell=True, # 硬编码为 True 以满足 create_subprocess_shell 的期望并消除 Pylance 警告
            cwd=cwd
        )
        stdout_bytes, stderr_bytes = await process.communicate()
        
        return_code = process.returncode if process.returncode is not None else -1 
        
        return stdout_bytes.decode(errors='ignore'), stderr_bytes.decode(errors='ignore'), return_code

# 也可以定义一组独立的函数
# def is_process_running_func(pid: int) -> bool:
#     """检查具有给定 PID 的进程是否正在运行。"""
#     if psutil:
#         return psutil.pid_exists(pid)
#     raise NotImplementedError("psutil is required for is_process_running_func if not using the class method.")

# def kill_process_func(pid: int) -> bool:
#     """终止具有给定 PID 的进程。"""
#     if psutil:
#         try:
#             process = psutil.Process(pid)
#             process.terminate()
#             return True
#         except psutil.NoSuchProcess:
#             return False
#     raise NotImplementedError("psutil is required for kill_process_func if not using the class method.")

# async def run_command_func(command: str) -> Tuple[str, str, int]:
#     """异步运行 shell 命令并返回输出和返回码。"""
#     process = await asyncio.create_subprocess_shell(
#         command,
#         stdout=asyncio.subprocess.PIPE,
#         stderr=asyncio.subprocess.PIPE,
#         shell=True # 确保 shell=True
#     )
#     stdout, stderr = await process.communicate()
#     rc = process.returncode if process.returncode is not None else -1
#     return stdout.decode(errors='ignore'), stderr.decode(errors='ignore'), rc