# utils/security_utils/hashing.py
"""
此模块提供密码哈希和验证相关的工具函数。
"""
import hashlib
import bcrypt # 示例库，也可以选择 argon2 或其他
from typing import Union

def hash_password(password: str) -> str:
    """
    哈希给定的明文密码。

    参数:
        password (str): 需要哈希的明文密码。

    返回:
        str: 哈希后的密码字符串。
    """
    # TODO: 实现密码哈希逻辑
    # 示例使用 bcrypt:
    # password_bytes = password.encode('utf-8')
    # salt = bcrypt.gensalt()
    # hashed_password = bcrypt.hashpw(password_bytes, salt)
    # return hashed_password.decode('utf-8') # 通常存储为字符串
    raise NotImplementedError("函数 'hash_password' 尚未实现。")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    验证明文密码是否与哈希后的密码匹配。

    参数:
        plain_password (str): 需要验证的明文密码。
        hashed_password (str): 存储的哈希密码。

    返回:
        bool: 如果密码匹配则返回 True，否则返回 False。
    """
    # TODO: 实现密码验证逻辑
    # 示例使用 bcrypt:
    # plain_password_bytes = plain_password.encode('utf-8')
    # hashed_password_bytes = hashed_password.encode('utf-8')
    # try:
    #     return bcrypt.checkpw(plain_password_bytes, hashed_password_bytes)
    # except ValueError: # bcrypt 在哈希格式不正确时可能抛出 ValueError
    #     return False
    raise NotImplementedError("函数 'verify_password' 尚未实现。")

# 也可以考虑使用更现代的库如 argon2-cffi
# import argon2
#
# _ph = argon2.PasswordHasher()
#
# def hash_password_argon2(password: str) -> str:
#     """
#     使用 Argon2 哈希密码。
#     """
#     return _ph.hash(password)
#
# def verify_password_argon2(plain_password: str, hashed_password: str) -> bool:
#     """
#     使用 Argon2 验证密码。
#     """
#     try:
#         _ph.verify(hashed_password, plain_password)
#         return True
#     except argon2.exceptions.VerifyMismatchError:
#         return False
#     except argon2.exceptions.VerificationError: # 其他验证错误，例如哈希格式问题
#         # 可以记录日志或抛出自定义异常
#         # from .exceptions import HashingError
#         # raise HashingError("密码验证时发生错误。")
#         return False
#
# def needs_rehash_argon2(hashed_password: str) -> bool:
#     """
#     检查哈希密码是否需要使用更新的参数重新哈希。
#     """
#     return _ph.check_needs_rehash(hashed_password)