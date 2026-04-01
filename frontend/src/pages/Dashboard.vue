<script setup lang="ts">
import { ref, onMounted, h } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { api } from '@/utils/request'
import type { HealthCheck } from '@/types'

const authStore = useAuthStore()
const health = ref<HealthCheck | null>(null)
const loading = ref(false)

onMounted(async () => {
  loading.value = true
  try {
    health.value = await api.get<HealthCheck>('/api/v1/health/detailed')
  } catch (error) {
    console.error('Failed to fetch health:', error)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="dashboard">
    <n-space vertical :size="24">
      <!-- Header -->
      <div class="dashboard-header">
        <div>
          <h1>欢迎回来，{{ authStore.user?.username || '用户' }}</h1>
          <p>今天是美好的一天</p>
        </div>
        <n-tag type="success" size="small">
          在线
        </n-tag>
      </div>

      <!-- Stats Grid -->
      <n-grid :cols="4" :x-gap="20" :y-gap="20" responsive="screen" item-responsive>
        <n-gi span="4 m:2 l:1">
          <n-card class="stat-card" :bordered="false">
            <div class="stat-content">
              <div class="stat-icon stat-icon-1">
                <n-icon :size="24">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                    <circle cx="9" cy="7" r="4"></circle>
                    <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                    <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                  </svg>
                </n-icon>
              </div>
              <div class="stat-info">
                <span class="stat-value">1,234</span>
                <span class="stat-title">用户总数</span>
              </div>
            </div>
          </n-card>
        </n-gi>
        <n-gi span="4 m:2 l:1">
          <n-card class="stat-card" :bordered="false">
            <div class="stat-content">
              <div class="stat-icon stat-icon-2">
                <n-icon :size="24">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
                  </svg>
                </n-icon>
              </div>
              <div class="stat-info">
                <span class="stat-value">856</span>
                <span class="stat-title">活跃用户</span>
              </div>
            </div>
          </n-card>
        </n-gi>
        <n-gi span="4 m:2 l:1">
          <n-card class="stat-card" :bordered="false">
            <div class="stat-content">
              <div class="stat-icon stat-icon-3">
                <n-icon :size="24">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
                  </svg>
                </n-icon>
              </div>
              <div class="stat-info">
                <span class="stat-value">12.5k</span>
                <span class="stat-title">系统访问</span>
              </div>
            </div>
          </n-card>
        </n-gi>
        <n-gi span="4 m:2 l:1">
          <n-card class="stat-card" :bordered="false">
            <div class="stat-content">
              <div class="stat-icon stat-icon-4">
                <n-icon :size="24">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="3"></circle>
                    <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
                  </svg>
                </n-icon>
              </div>
              <div class="stat-info">
                <span class="stat-value">8</span>
                <span class="stat-title">系统设置</span>
              </div>
            </div>
          </n-card>
        </n-gi>
      </n-grid>

      <!-- Main Content -->
      <n-grid :cols="3" :x-gap="20" :y-gap="20" responsive="screen" item-responsive>
        <!-- System Status -->
        <n-gi span="3 l:2">
          <n-card title="系统状态" :bordered="false" class="content-card">
            <n-skeleton v-if="loading" :height="200" />
            <div v-else class="status-content">
              <div class="status-item">
                <span class="status-label">服务状态</span>
                <n-tag type="success">正常运行</n-tag>
              </div>
              <div class="status-item">
                <span class="status-label">版本信息</span>
                <span class="status-value">{{ health?.version || '1.0.0' }}</span>
              </div>
              <div class="status-item">
                <span class="status-label">环境</span>
                <span class="status-value">开发环境</span>
              </div>
              <div class="status-item">
                <span class="status-label">API 状态</span>
                <n-tag :type="health?.status === 'ok' ? 'success' : 'error'">
                  {{ health?.status || 'unknown' }}
                </n-tag>
              </div>
            </div>
          </n-card>
        </n-gi>

        <!-- Features -->
        <n-gi span="3 l:1">
          <n-card title="功能模块" :bordered="false" class="content-card">
            <n-space vertical :size="12">
              <div class="feature-item">
                <div class="feature-icon feature-icon-1">
                  <n-icon :size="20">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                      <circle cx="9" cy="7" r="4"></circle>
                      <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                      <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                    </svg>
                  </n-icon>
                </div>
                <div class="feature-info">
                  <span class="feature-title">用户管理</span>
                  <span class="feature-desc">管理系统用户信息</span>
                </div>
              </div>
              <div class="feature-item">
                <div class="feature-icon feature-icon-2">
                  <n-icon :size="20">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <line x1="18" y1="20" x2="18" y2="10"></line>
                      <line x1="12" y1="20" x2="12" y2="4"></line>
                      <line x1="6" y1="20" x2="6" y2="14"></line>
                    </svg>
                  </n-icon>
                </div>
                <div class="feature-info">
                  <span class="feature-title">数据分析</span>
                  <span class="feature-desc">查看数据统计报表</span>
                </div>
              </div>
              <div class="feature-item">
                <div class="feature-icon feature-icon-3">
                  <n-icon :size="20">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <circle cx="12" cy="12" r="3"></circle>
                      <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
                    </svg>
                  </n-icon>
                </div>
                <div class="feature-info">
                  <span class="feature-title">系统设置</span>
                  <span class="feature-desc">配置系统参数</span>
                </div>
              </div>
            </n-space>
          </n-card>
        </n-gi>
      </n-grid>
    </n-space>
  </div>
</template>

<style scoped>
.dashboard {
  padding: 24px;
}

.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.dashboard-header h1 {
  font-size: 24px;
  font-weight: 600;
  color: #fff;
  margin-bottom: 4px;
}

.dashboard-header p {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.5);
}

.stat-card {
  background: rgba(255, 255, 255, 0.03);
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.stat-card :deep(.n-card__content) {
  padding: 20px;
}

.stat-content {
  display: flex;
  align-items: center;
  gap: 16px;
}

.stat-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.stat-icon-1 {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.stat-icon-2 {
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}

.stat-icon-3 {
  background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
}

.stat-icon-4 {
  background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
}

.stat-info {
  display: flex;
  flex-direction: column;
}

.stat-value {
  font-size: 24px;
  font-weight: 600;
  color: #fff;
}

.stat-title {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.5);
}

.content-card {
  background: rgba(255, 255, 255, 0.03);
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.content-card :deep(.n-card-header) {
  padding: 20px 20px 0;
}

.content-card :deep(.n-card-header__main) {
  color: #fff;
  font-size: 16px;
  font-weight: 600;
}

.content-card :deep(.n-card__content) {
  padding: 20px;
}

.status-content {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.status-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.status-item:last-child {
  border-bottom: none;
}

.status-label {
  color: rgba(255, 255, 255, 0.5);
}

.status-value {
  color: #fff;
}

.feature-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  background: rgba(255, 255, 255, 0.03);
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s;
}

.feature-item:hover {
  background: rgba(255, 255, 255, 0.08);
}

.feature-icon {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
}

.feature-icon-1 {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.feature-icon-2 {
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}

.feature-icon-3 {
  background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
}

.feature-info {
  display: flex;
  flex-direction: column;
}

.feature-title {
  color: #fff;
  font-weight: 500;
}

.feature-desc {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.4);
}
</style>