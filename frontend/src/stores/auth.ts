import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { api } from '@/utils/request'

interface User {
  id: number
  username: string
  email: string
  is_active: boolean
}

interface LoginResponse {
  access_token: string
  token_type: string
}

export const useAuthStore = defineStore('auth', () => {
  // 从 localStorage 初始化 token
  const token = ref<string | null>(localStorage.getItem('token'))
  const user = ref<User | null>(null)
  const loading = ref(false)

  const isAuthenticated = computed(() => !!token.value)

  /**
   * 登录
   * @param username - 用户名（明文）
   * @param password - 密码（已加密）
   */
  async function login(username: string, encryptedPassword: string): Promise<boolean> {
    loading.value = true
    try {
      // 发送加密后的密码到后端
      const response = await api.post<LoginResponse>('/api/v1/auth/login', {
        username,
        password: encryptedPassword,
      })

      // 存储 token
      token.value = response.access_token
      localStorage.setItem('token', response.access_token)

      // 获取用户信息
      await fetchUser()

      return true
    } catch (error) {
      console.error('Login failed:', error)
      return false
    } finally {
      loading.value = false
    }
  }

  /**
   * 获取当前用户信息
   */
  async function fetchUser() {
    if (!token.value) return
    try {
      const userData = await api.get<User>('/api/v1/auth/me')
      user.value = userData
    } catch (error) {
      console.error('Failed to fetch user:', error)
      logout()
    }
  }

  /**
   * 登出
   */
  function logout() {
    token.value = null
    user.value = null
    localStorage.removeItem('token')
  }

  return {
    token,
    user,
    loading,
    isAuthenticated,
    login,
    fetchUser,
    logout,
  }
})