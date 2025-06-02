from pydantic import BaseModel
from typing import Optional, Dict, Any

class ServiceStatus(BaseModel):
    """
    服务状态模型。
    """
    gui_running: bool
    proxy_port: Optional[int] = None
    # 可以根据需要添加更多状态字段
    # 例如: llm_service_status: str = "unknown"
    #       auth_service_status: str = "unknown"

class ProcessInfo(BaseModel):
    """
    进程信息模型。
    """
    name: str
    status: str # 例如："running", "stopped", "error"
    pid: Optional[int] = None

# 可以根据需要添加更多与 GUI 服务相关的 Pydantic 模型