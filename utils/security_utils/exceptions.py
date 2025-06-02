# utils/security_utils/exceptions.py
"""
此模块定义了 security_utils 模块特定的自定义异常。
"""

class SecurityUtilError(Exception):
    """
    security_utils 模块中所有自定义异常的基类。
    """
    pass

class EncryptionError(SecurityUtilError):
    """
    表示在加密或解密过程中发生的错误。
    """
    pass

class DecryptionError(EncryptionError): # 通常解密错误也是一种加密错误
    """
    表示在解密过程中发生的特定错误。
    例如，无效的token或密钥。
    """
    pass

class HashingError(SecurityUtilError):
    """
    表示在密码哈希或验证过程中发生的错误。
    """
    pass

class KeyGenerationError(SecurityUtilError):
    """
    表示在生成密钥过程中发生的错误。
    """
    pass

# 可以根据需要添加更多特定的异常类
# 例如：
# class InvalidKeyError(SecurityUtilError):
#     """密钥无效或格式不正确时抛出。"""
#     pass
#
# class WeakPasswordError(HashingError):
#     """密码不符合强度要求时抛出。"""
#     pass