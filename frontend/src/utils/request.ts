/**
 * HTTP 请求封装 - 二次封装 axios
 * - 自动携带 token
 * - 统一错误处理
 * - 请求/响应拦截
 */
import axios, { type AxiosInstance, type AxiosRequestConfig, type AxiosResponse } from 'axios'
import { useAuthStore } from '@/stores/auth'

// 创建 axios 实例
const service: AxiosInstance = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || '/',
  timeout: 15000,
  headers: {
    'Content-Type': 'application/json',
  },
})

// 请求队列（用于防重复请求）
const pendingRequests = new Map<string, () => void>()

/**
 * 生成请求唯一 key
 */
function generateRequestKey(config: AxiosRequestConfig): string {
  const { method, url, params, data } = config
  return `${method}-${url}-${JSON.stringify(params)}-${JSON.stringify(data)}`
}

/**
 * 移除请求
 */
function removePendingRequest(key: string) {
  const cancel = pendingRequests.get(key)
  if (cancel) {
    cancel()
    pendingRequests.delete(key)
  }
}

// 请求拦截器
service.interceptors.request.use(
  (config) => {
    // 移除重复请求
    const requestKey = generateRequestKey(config)
    removePendingRequest(requestKey)

    // 添加 cancel 函数到请求队列
    config.cancelToken = new axios.CancelToken((cancel) => {
      pendingRequests.set(requestKey, cancel)
    })

    // 从 Pinia 获取 token
    const authStore = useAuthStore()
    if (authStore.token) {
      config.headers.Authorization = `Bearer ${authStore.token}`
    }

    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// 响应拦截器
service.interceptors.response.use(
  (response: AxiosResponse) => {
    // 移除请求
    const requestKey = generateRequestKey(response.config)
    removePendingRequest(requestKey)

    // 根据响应状态码处理
    const { status, data } = response

    if (status === 200 || status === 201) {
      return response.data
    }

    return response.data
  },
  (error) => {
    // 移除请求
    const requestKey = generateRequestKey(error.config)
    removePendingRequest(requestKey)

    // 统一错误处理
    const authStore = useAuthStore()

    if (error.response) {
      const { status, data } = error.response

      switch (status) {
        case 401:
          // Token 过期或无效
          authStore.logout()
          window.location.href = '/login'
          return Promise.reject(new Error('登录已过期，请重新登录'))

        case 403:
          return Promise.reject(new Error('没有权限访问'))

        case 404:
          return Promise.reject(new Error('请求的资源不存在'))

        case 422:
          // 业务逻辑错误
          return Promise.reject(new Error(data.detail || '请求参数错误'))

        case 500:
          return Promise.reject(new Error('服务器内部错误'))

        default:
          return Promise.reject(new Error(data.detail || '网络错误'))
      }
    }

    if (error.code === 'ECONNABORTED') {
      return Promise.reject(new Error('请求超时'))
    }

    if (axios.isCancel(error)) {
      return Promise.reject(new Error('请求已取消'))
    }

    return Promise.reject(new Error('网络连接失败'))
  }
)

export default service

/**
 * 封装的请求方法
 */
export const request = {
  get<T = unknown>(url: string, config?: AxiosRequestConfig): Promise<T> {
    return service.get(url, config)
  },

  post<T = unknown>(url: string, data?: unknown, config?: AxiosRequestConfig): Promise<T> {
    return service.post(url, data, config)
  },

  put<T = unknown>(url: string, data?: unknown, config?: AxiosRequestConfig): Promise<T> {
    return service.put(url, data, config)
  },

  patch<T = unknown>(url: string, data?: unknown, config?: AxiosRequestConfig): Promise<T> {
    return service.patch(url, data, config)
  },

  delete<T = unknown>(url: string, config?: AxiosRequestConfig): Promise<T> {
    return service.delete(url, config)
  },
}

/**
 * 类型安全的请求封装
 */
export const api = request