"""
文本处理模块自定义异常。
"""

class TextProcessingError(Exception):
    """文本处理模块的基础异常类。"""
    pass

class SanitizationError(TextProcessingError):
    """文本清洗过程中发生的错误。"""
    pass

class FormattingError(TextProcessingError):
    """文本格式化过程中发生的错误。"""
    pass

class ParsingError(TextProcessingError):
    """文本解析过程中发生的错误。"""
    pass