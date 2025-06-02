"""
文本格式化工具函数。
"""
from typing import Any, Optional
import json # to_json_string 需要用到

def to_json_string(data: Any, indent: Optional[int] = None) -> str:
    """
    将数据结构格式化为 JSON 字符串。

    :param data: 要格式化的数据结构。
    :param indent: 缩进级别，如果为 None 则不进行美化打印。
    :return: JSON 格式的字符串。
    """
    # TODO: 实现更健壮的 JSON 序列化，处理可能的异常
    # raise NotImplementedError("功能尚未实现")
    try:
        return json.dumps(data, indent=indent, ensure_ascii=False)
    except TypeError:
        # 可以选择记录错误或返回一个默认值
        return "{}"

def wrap_text(text: str, width: int) -> str:
    """
    按指定宽度包装文本。

    :param text: 原始文本。
    :param width: 每行的最大宽度。
    :return: 包装后的文本。
    """
    # TODO: 实现文本包装逻辑
    # raise NotImplementedError("功能尚未实现")
    if width <= 0:
        return text # 或者抛出异常

    lines = []
    current_line = ""
    for word in text.split():
        if not current_line:
            current_line = word
        elif len(current_line) + 1 + len(word) <= width:
            current_line += " " + word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return "\n".join(lines)