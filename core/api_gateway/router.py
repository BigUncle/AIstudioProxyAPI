from fastapi import APIRouter, FastAPI

# 创建一个 API 路由实例
router = APIRouter()

# --------------------
# API 路由定义
# --------------------

@router.post("/v1/chat/completions", summary="处理聊天补全请求")
async def chat_completions():
    """
    处理聊天补全请求。
    这是 OpenAI API 兼容的端点。
    """
    # TODO: 实现聊天补全逻辑，调用 llm_service
    return {"message": "Chat completions endpoint not implemented yet."}

@router.get("/v1/models", summary="获取可用模型列表")
async def get_models():
    """
    获取当前系统可用的 AI 模型列表。
    这是 OpenAI API 兼容的端点。
    """
    # TODO: 实现获取模型列表的逻辑，调用 llm_service
    return {"models": ["model1", "model2"], "message": "Models endpoint not implemented yet."}

@router.get("/health", summary="健康检查")
async def health_check():
    """
    执行健康检查，返回系统状态。
    """
    return {"status": "healthy"}

# 可以创建一个 FastAPI 应用实例，用于在本地测试 router (可选)
# app = FastAPI()
# app.include_router(router, prefix="/api_gateway")