import asyncio
from typing import AsyncGenerator, List, Dict, Any

# 依赖说明：
# 本模块依赖于 utils/playwright_automation 和 utils/text_processing
# (当前阶段仅作注释说明，未来通过依赖注入实现)

class LLMService:
    """
    LLM 服务类，封装与 LLM 服务的交互逻辑。
    """

    async def query_llm(self, prompt: str, model_id: str, params: Dict[str, Any]) -> AsyncGenerator[str, None]:
        """
        异步流式查询 LLM (占位符实现)。

        Args:
            prompt: 用户输入的提示。
            model_id: 要查询的模型 ID。
            params: 传递给模型的额外参数。

        Yields:
            str: LLM 生成的文本块。
        """
        # 模拟 LLM 思考时间
        await asyncio.sleep(0.1)
        yield "这是从模拟 LLM 返回的第一个文本块。"
        await asyncio.sleep(0.1)
        yield f"您查询的模型是: {model_id}。"
        await asyncio.sleep(0.1)
        yield f"您的提示是: '{prompt[:20]}...'。" # 显示部分提示
        await asyncio.sleep(0.1)
        yield "这是最后一个模拟文本块。"
        # pragma: no cover (因为这是占位符，实际实现会不同)

    async def get_available_models(self) -> List[str]:
        """
        获取 LLM 服务支持的模型列表。

        此方法目前返回一个硬编码的列表，用于初期开发和测试。
        未来将替换为从实际 LLM 服务动态获取模型列表的逻辑。

        Returns:
            List[str]: 可用模型 ID 的列表。
        """
        return ["gemini-pro", "gemini-pro-vision", "text-embedding-004"]