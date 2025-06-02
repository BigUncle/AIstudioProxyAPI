# from pydantic import BaseModel

# 此文件用于定义 `llm_service` 模块内部使用的 Pydantic 模型。
# 例如，用于表示 LLM 请求或响应的特定内部数据结构。
# 如果暂时不需要特定的内部模型，此文件可以为空或包含基本注释。

# 示例:
# class LLMInternalRequest(BaseModel):
#     processed_prompt: str
#     internal_model_id: str
#     custom_params: dict

# class LLMInternalResponseChunk(BaseModel):
#     text_chunk: str
#     is_final: bool