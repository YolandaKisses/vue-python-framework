/**
 * 加密工具模块 - 使用 AES 对称加密
 * 前后端使用相同的密钥进行加密/解密
 */
import CryptoJS from 'crypto-js'

// 密钥 - 生产环境应使用环境变量
const SECRET_KEY = 'vue-python-fw-2024-secret-key-aes'

/**
 * 加密字符串
 * @param plainText - 明文字符串
 * @returns 加密后的 base64 字符串
 */
export function encrypt(plainText: string): string {
  const encrypted = CryptoJS.AES.encrypt(plainText, SECRET_KEY)
  return encrypted.toString()
}

/**
 * 解密字符串
 * @param cipherText - 加密的 base64 字符串
 * @returns 解密后的明文
 */
export function decrypt(cipherText: string): string {
  const decrypted = CryptoJS.AES.decrypt(cipherText, SECRET_KEY)
  return decrypted.toString(CryptoJS.enc.Utf8)
}

/**
 * 生成随机salt用于增强安全性
 */
export function generateSalt(): string {
  return CryptoJS.lib.WordArray.random(16).toString()
}

/**
 * 带salt的加密 - 更加安全
 * @param plainText - 明文
 * @param salt - 盐值
 */
export function encryptWithSalt(plainText: string, salt: string): string {
  const key = CryptoJS.PBKDF2(SECRET_KEY, salt, {
    keySize: 256 / 32,
    iterations: 1000,
  })
  const encrypted = CryptoJS.AES.encrypt(plainText, key)
  return encrypted.toString()
}

/**
 * 带salt的解密
 * @param cipherText - 密文
 * @param salt - 盐值
 */
export function decryptWithSalt(cipherText: string, salt: string): string {
  const key = CryptoJS.PBKDF2(SECRET_KEY, salt, {
    keySize: 256 / 32,
    iterations: 1000,
  })
  const decrypted = CryptoJS.AES.decrypt(cipherText, key)
  return decrypted.toString(CryptoJS.enc.Utf8)
}