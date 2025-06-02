from typing import AsyncGenerator, List

# 依赖说明：
# 本模块依赖于 utils/playwright_automation 和 utils/text_processing
# (当前阶段仅作注释说明，未来通过依赖注入实现)

class LLMService:
    """
    LLM 服务类，封装与 LLM 服务的交互逻辑。
    """

    async def query_llm(self, prompt: str, model_id: str, params: dict) -> AsyncGenerator[str, None]:
        """
        异步流式查询 LLM。

        Args:
            prompt (str): 输入的提示。
            model_id (str): 使用的模型 ID。
            params (dict): 传递给模型的额外参数。

        Yields:
            AsyncGenerator[str, None]: LLM 生成的文本流。
        """
        # TODO: 实现与 LLM 服务的实际交互逻辑
        yield ""
        return
        # 或者 raise NotImplementedError("query_llm 方法尚未实现")

    async def get_available_models(self) -> List[str]:
        """
        获取 LLM 服务支持的模型列表。

        Returns:
            List[str]: 可用模型 ID 的列表。
        """
        # TODO: 实现获取可用模型列表的逻辑
        return []
        # 或者 raise NotImplementedError("get_available_models 方法尚未实现")