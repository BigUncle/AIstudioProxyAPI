from fastapi import APIRouter, FastAPI
from typing import List, Dict # 添加 List 和 Dict 的导入
from .services import APIGatewayService  # 导入服务
from .schemas import HealthStatus, ModelList, ModelCard  # 导入响应模型 ModelList 和 ModelCard

# 创建一个 API 路由实例
router = APIRouter()

# --------------------
# API 路由定义
# --------------------

@router.post("/v1/chat/completions", summary="处理聊天补全请求")
async def chat_completions(): # pragma: no cover
    """
    处理聊天补全请求。
    这是 OpenAI API 兼容的端点。
    """
    # TODO: 实现聊天补全逻辑，调用 llm_service
    return {"message": "Chat completions endpoint not implemented yet."}

@router.get("/v1/models", summary="获取可用模型列表", response_model=ModelList)
async def get_models() -> ModelList:
    """
    获取当前系统可用的 AI 模型列表。

    此端点遵循 OpenAI API `/v1/models` 的规范，返回一个包含模型信息的列表。
    数据由 `APIGatewayService` 提供。

    Returns:
        ModelList: 一个包含模型列表的 Pydantic 模型。
    """
    service = APIGatewayService()
    # APIGatewayService.get_models_list() 返回 List[Dict[str, str]]
    raw_models_data: List[Dict[str, str]] = await service.get_models_list()
    
    # 将 List[Dict[str, str]] 显式转换为 List[ModelCard]
    # Pydantic 会根据 ModelCard 的字段从字典中提取数据
    # 注意：在 ModelCard 中，我之前注释掉了 'created' 字段。如果 LLMService 返回的字典中
    # 包含 'created'，而 ModelCard 中没有此字段或其非可选，Pydantic 会报错。
    # 当前 ModelCard 定义中 'id' 和 'owned_by' 是必须的，'object' 有默认值。
    # LLMService 返回的字典包含 'id', 'object', 'owned_by'。
    model_cards: List[ModelCard] = [ModelCard(**data) for data in raw_models_data]
    
    return ModelList(data=model_cards, object="list")

@router.get("/health", summary="健康检查", response_model=HealthStatus)
async def health_check() -> HealthStatus:
    """
    执行健康检查，返回系统状态。

    Returns:
        HealthStatus: 包含服务健康状态的对象。
    """
    service = APIGatewayService()
    health_status = await service.perform_health_check()
    return health_status

# 可以创建一个 FastAPI 应用实例，用于在本地测试 router (可选)
# app = FastAPI()
# app.include_router(router, prefix="/api_gateway")