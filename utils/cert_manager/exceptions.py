"""
此模块定义了 `cert_manager` 模块特定的异常。
"""

class CertManagerError(Exception):
    """
    证书管理模块的基础异常类。
    所有特定于此模块的自定义异常都应从此类继承。
    """
    pass

class CertificateGenerationError(CertManagerError):
    """
    当证书生成失败时引发此异常。
    """
    pass

class CertificateLoadError(CertManagerError):
    """
    当从文件加载证书或私钥失败时引发此异常。
    """
    pass

class PrivateKeyLoadError(CertManagerError):
    """
    当从文件加载私钥失败时引发此异常。
    """
    pass