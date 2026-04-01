<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useMessage } from 'naive-ui'
import { useAuthStore } from '@/stores/auth'
import { encrypt } from '@/utils/crypto'

const router = useRouter()
const authStore = useAuthStore()
const message = useMessage()

const username = ref('')
const password = ref('')
const loading = ref(false)

// 输入验证
const isValid = computed(() => username.value.trim() && password.value.trim())

async function handleLogin() {
  if (!isValid.value) return

  loading.value = true
  try {
    // 加密密码
    const encryptedPassword = encrypt(password.value)
    const success = await authStore.login(username.value, encryptedPassword)

    if (success) {
      message.success('登录成功')
      router.push('/dashboard')
    } else {
      message.error('用户名或密码错误')
    }
  } catch (e) {
    message.error('登录失败，请稍后重试')
    console.error(e)
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="login-page">
    <div class="login-bg">
      <div class="bg-gradient"></div>
      <div class="bg-pattern"></div>
    </div>

    <div class="login-container">
      <n-card class="login-card" :bordered="false">
        <div class="card-content">
          <div class="logo-section">
            <div class="logo">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M12 2L2 7L12 12L22 7L12 2Z"></path>
                <path d="M2 17L12 22L22 17"></path>
                <path d="M2 12L12 17L22 12"></path>
              </svg>
            </div>
            <h1>Vue-Python</h1>
            <p>全栈应用管理平台</p>
          </div>

          <n-form ref="formRef" :model="{}" :show-label="false">
            <n-form-item path="username">
              <n-input
                v-model:value="username"
                placeholder="请输入用户名"
                size="large"
                :bordered="false"
                @keydown.enter="handleLogin"
              >
                <template #prefix>
                  <svg class="input-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                    <circle cx="12" cy="7" r="4"></circle>
                  </svg>
                </template>
              </n-input>
            </n-form-item>

            <n-form-item path="password">
              <n-input
                v-model:value="password"
                type="password"
                placeholder="请输入密码"
                size="large"
                :bordered="false"
                show-password-on="click"
                @keydown.enter="handleLogin"
              >
                <template #prefix>
                  <svg class="input-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <rect x="3" y="11" width="18" height="11" rx="2"></rect>
                    <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                  </svg>
                </template>
              </n-input>
            </n-form-item>

            <div class="form-extra">
              <n-checkbox :checked="false">记住我</n-checkbox>
              <a class="forgot-link">忘记密码？</a>
            </div>

            <n-button
              type="primary"
              block
              size="large"
              :loading="loading"
              :disabled="!isValid"
              @click="handleLogin"
            >
              登 录
            </n-button>
          </n-form>

          <div class="card-footer">
            <span>测试账号: </span>
            <n-tag type="info" size="small">admin / 123456</n-tag>
          </div>
        </div>
      </n-card>

      <p class="copyright">© 2024 Vue-Python Framework</p>
    </div>
  </div>
</template>

<style scoped>
.login-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #0a0a0f;
  position: relative;
  overflow: hidden;
}

.login-bg {
  position: absolute;
  inset: 0;
  overflow: hidden;
}

.bg-gradient {
  position: absolute;
  width: 600px;
  height: 600px;
  top: -200px;
  right: -200px;
  background: radial-gradient(circle, rgba(103, 126, 234, 0.3) 0%, transparent 70%);
  filter: blur(60px);
  animation: float 8s ease-in-out infinite;
}

.bg-pattern {
  position: absolute;
  inset: 0;
  background-image: radial-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px);
  background-size: 40px 40px;
}

@keyframes float {
  0%, 100% { transform: translate(0, 0); }
  50% { transform: translate(20px, 20px); }
}

.login-container {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 400px;
  padding: 20px;
}

.login-card {
  background: rgba(255, 255, 255, 0.03);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
}

.login-card :deep(.n-card__content) {
  padding: 40px;
}

.card-content {
  display: flex;
  flex-direction: column;
  gap: 32px;
}

.logo-section {
  text-align: center;
}

.logo {
  width: 80px;
  height: 80px;
  margin: 0 auto 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 10px 30px -10px rgba(102, 126, 234, 0.5);
}

.logo svg {
  width: 40px;
  height: 40px;
}

.logo-section h1 {
  font-size: 24px;
  font-weight: 600;
  color: #fff;
  margin-bottom: 8px;
}

.logo-section p {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.5);
}

.login-card :deep(.n-input) {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 12px;
}

.login-card :deep(.n-input:hover),
.login-card :deep(.n-input:focus) {
  background: rgba(255, 255, 255, 0.08);
}

.login-card :deep(.n-input__input-el) {
  color: #fff;
}

.login-card :deep(.n-input__input-el::placeholder) {
  color: rgba(255, 255, 255, 0.3);
}

.input-icon {
  width: 18px;
  height: 18px;
  color: rgba(255, 255, 255, 0.4);
}

.form-extra {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.login-card :deep(.n-checkbox__label) {
  color: rgba(255, 255, 255, 0.5);
}

.forgot-link {
  color: #667eea;
  font-size: 14px;
  text-decoration: none;
}

.forgot-link:hover {
  text-decoration: underline;
}

.login-card :deep(.n-button) {
  height: 48px;
  border-radius: 12px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border: none;
  font-size: 16px;
  font-weight: 500;
}

.login-card :deep(.n-button:hover) {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px -10px rgba(102, 126, 234, 0.5);
}

.card-footer {
  text-align: center;
  padding-top: 24px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;
}

.card-footer span {
  color: rgba(255, 255, 255, 0.4);
  font-size: 13px;
}

.copyright {
  text-align: center;
  margin-top: 24px;
  font-size: 13px;
  color: rgba(255, 255, 255, 0.3);
}
</style>