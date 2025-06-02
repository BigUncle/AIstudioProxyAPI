from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

# --------------------
# /v1/models 模式定义
# --------------------

class ModelCard(BaseModel):
    """
    代表一个可用模型的详细信息，用于 `/v1/models` 端点。
    """
    id: str = Field(..., description="模型的唯一标识符。例如：'gemini-pro'")
    object: str = Field("model", description="对象类型，固定为 'model'。")
    # created: int = Field(..., description="模型创建的时间戳 (Unix epoch)。为了简化，此版本暂不强制要求。") # 暂时注释掉，根据需求，此字段非必需
    owned_by: str = Field("system", description="拥有该模型的组织或实体。例如：'system' 或 'user'")
    # permission: List[Dict] # 更复杂的权限结构，暂时简化

class ModelList(BaseModel):
    """
    代表可用模型列表的响应体，用于 `/v1/models` 端点。
    """
    object: str = Field("list", description="对象类型，固定为 'list'。")
    data: List[ModelCard] = Field(..., description="包含模型卡片对象（ModelCard）的列表。")

# --------------------
# /v1/chat/completions 模式定义 (初步)
# --------------------

class ChatMessage(BaseModel):
    """
    聊天消息对象。
    """
    role: str = Field(..., description="消息发送者的角色 (e.g., 'user', 'assistant', 'system')。")
    content: str = Field(..., description="消息内容。")
    # name: Optional[str] = None # 可选的发送者名称

class ChatCompletionRequest(BaseModel):
    """
    聊天补全请求体。
    这是一个简化的版本，后续可以根据 OpenAI API 规范扩展更多参数。
    """
    model: str = Field(..., description="要使用的模型 ID。")
    messages: List[ChatMessage] = Field(..., description="描述对话的消息列表。")
    # temperature: Optional[float] = 1.0
    # top_p: Optional[float] = 1.0
    # n: Optional[int] = 1
    # stream: Optional[bool] = False
    # max_tokens: Optional[int] = None
    # presence_penalty: Optional[float] = 0
    # frequency_penalty: Optional[float] = 0
    # user: Optional[str] = None

class ChatCompletionChoice(BaseModel):
    """
    聊天补全响应中的一个选项。
    """
    index: int = Field(..., description="选项的索引。")
    message: ChatMessage = Field(..., description="模型生成的消息。")
    finish_reason: Optional[str] = Field(None, description="模型停止生成令牌的原因。")
    # logprobs: Optional[Dict] = None # 如果请求了 logprobs

class Usage(BaseModel):
    """
    API 使用情况统计。
    """
    prompt_tokens: int = Field(0, description="提示中的令牌数。")
    completion_tokens: int = Field(0, description="生成补全中的令牌数。")
    total_tokens: int = Field(0, description="总令牌数。")

class ChatCompletionResponse(BaseModel):
    """
    聊天补全响应体。
    这是一个简化的版本。
    """
    id: str = Field(..., description="补全的唯一标识符。")
    object: str = Field("chat.completion", description="对象类型，通常是 'chat.completion'。")
    created: int = Field(..., description="补全创建的时间戳 (Unix epoch)。")
    model: str = Field(..., description="用于补全的模型。")
    choices: List[ChatCompletionChoice] = Field(..., description="补全选项列表。")
    usage: Optional[Usage] = Field(None, description="API 使用情况统计。")
    # system_fingerprint: Optional[str] = None # 系统指纹

# --------------------
# /health 模式定义
# --------------------

class HealthStatus(BaseModel):
    """
    健康检查响应体。
    """
    status: str = Field(..., description="服务健康状态。")