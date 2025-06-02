"""
文本解析工具函数。
"""
import re
from typing import List, Dict, Any

def extract_emails(text: str) -> List[str]:
    """
    从文本中提取电子邮件地址。

    :param text: 包含电子邮件地址的文本。
    :return: 提取到的电子邮件地址列表。
    """
    # TODO: 实现更完善的邮件提取逻辑，考虑各种邮件格式
    # raise NotImplementedError("功能尚未实现")
    # 一个简单的正则表达式示例
    email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(email_regex, text)

def parse_key_value_pairs(text: str, delimiter: str = ':') -> Dict[str, str]:
    """
    解析键值对文本。
    例如 "name: John Doe\nage: 30"

    :param text: 包含键值对的文本，每行一个键值对。
    :param delimiter: 键和值之间的分隔符。
    :return: 解析后的键值对字典。
    """
    # TODO: 实现更健壮的键值对解析，处理空格、多行值等情况
    # raise NotImplementedError("功能尚未实现")
    pairs = {}
    for line in text.splitlines():
        line = line.strip()
        if delimiter in line:
            key, value = line.split(delimiter, 1)
            pairs[key.strip()] = value.strip()
    return pairs