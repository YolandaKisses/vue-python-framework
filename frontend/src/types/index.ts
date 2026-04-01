// Type definitions for API responses

export interface User {
  id: number
  email: string
  username: string
  is_active: boolean
  created_at?: string
  updated_at?: string
}

export interface UserCreate {
  email: string
  username: string
  password: string
}

export interface UserUpdate {
  email?: string
  username?: string
  is_active?: boolean
}

export interface Token {
  access_token: string
  token_type: string
}

export interface LoginForm {
  email: string
  password: string
}

export interface ApiError {
  detail: string
}

export interface HealthCheck {
  status: string
  version?: string
}