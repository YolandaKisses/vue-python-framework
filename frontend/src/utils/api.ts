import axios, { type AxiosInstance, type AxiosRequestConfig } from 'axios'

const api: AxiosInstance = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || '',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Request interceptor
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => Promise.reject(error)
)

// Response interceptor
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token')
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

export default api

// Helper function for API calls
export async function apiGet<T>(url: string, config?: AxiosRequestConfig) {
  const response = await api.get<T>(url, config)
  return response.data
}

export async function apiPost<T>(url: string, data?: unknown, config?: AxiosRequestConfig) {
  const response = await api.post<T>(url, data, config)
  return response.data
}

export async function apiPut<T>(url: string, data?: unknown, config?: AxiosRequestConfig) {
  const response = await api.put<T>(url, data, config)
  return response.data
}

export async function apiPatch<T>(url: string, data?: unknown, config?: AxiosRequestConfig) {
  const response = await api.patch<T>(url, data, config)
  return response.data
}

export async function apiDelete<T>(url: string, config?: AxiosRequestConfig) {
  const response = await api.delete<T>(url, config)
  return response.data
}