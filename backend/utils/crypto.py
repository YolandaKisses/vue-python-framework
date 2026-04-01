"""加密工具模块 - 使用 AES 对称加密，解密前端传递的加密密码"""

import base64
import json
from typing import Any

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


# 密钥 - 必须与前端一致
SECRET_KEY = b"vue-python-fw-2024-secret-key-aes"


def _pad(data: bytes) -> bytes:
    """PKCS7 填充"""
    block_size = 16
    padding_length = block_size - (len(data) % block_size)
    padding = bytes([padding_length] * padding_length)
    return data + padding


def _unpad(data: bytes) -> bytes:
    """移除 PKCS7 填充"""
    padding_length = data[-1]
    return data[:-padding_length]


def encrypt(plain_text: str) -> str:
    """
    加密字符串（后端内部使用）

    Args:
        plain_text: 明文字符串

    Returns:
        加密后的 base64 字符串
    """
    iv = b"1234567890123456"  # 16 bytes IV
    cipher = Cipher(
        algorithms.AES(SECRET_KEY),
        modes.CBC(iv),
        backend=default_backend(),
    )
    encryptor = cipher.encryptor()
    encrypted = encryptor.update(_pad(plain_text.encode())) + encryptor.finalize()
    return base64.b64encode(encrypted).decode()


def decrypt(cipher_text: str) -> str:
    """
    解密字符串

    Args:
        cipher_text: 加密的 base64 字符串

    Returns:
        解密后的明文
    """
    iv = b"1234567890123456"
    encrypted_data = base64.b64decode(cipher_text)
    cipher = Cipher(
        algorithms.AES(SECRET_KEY),
        modes.CBC(iv),
        backend=default_backend(),
    )
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(encrypted_data) + decryptor.finalize()
    return _unpad(decrypted).decode()


def decrypt_json(cipher_text: str) -> dict[str, Any]:
    """
    解密 JSON 字符串

    Args:
        cipher_text: 加密的 JSON 字符串

    Returns:
        解密后的字典
    """
    decrypted = decrypt(cipher_text)
    return json.loads(decrypted)