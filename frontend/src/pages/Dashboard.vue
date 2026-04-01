<script setup lang="ts">
import { ref, onMounted } from 'vue'
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

// SVG 图标组件
const UserIcon = () => ({
  type: 'svg' as const,
  props: {
    viewBox: '0 0 24 24',
    fill: 'none',
    stroke: 'currentColor',
    'stroke-width': '2',
    style: { width: '24px', height: '24px' }
  },
  children: [
    { type: 'path', props: { d: 'M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2' } },
    { type: 'circle', props: { cx: '9', cy: '7', r: '4' } },
    { type: 'path', props: { d: 'M23 21v-2a4 4 0 0 0-3-3.87' } },
    { type: 'path', props: { d: 'M16 3.13a4 4 0 0 1 0 7.75' } }
  ]
})

const ChartIcon = () => ({
  type: 'svg' as const,
  props: {
    viewBox: '0 0 24 24',
    fill: 'none',
    stroke: 'currentColor',
    'stroke-width': '2',
    style: { width: '24px', height: '24px' }
  },
  children: [
    { type: 'polyline', props: { points: '22 12 18 12 15 21 9 3 6 12 2 12' } }
  ]
})

const BoxIcon = () => ({
  type: 'svg' as const,
  props: {
    viewBox: '0 0 24 24',
    fill: 'none',
    stroke: 'currentColor',
    'stroke-width': '2',
    style: { width: '24px', height: '24px' }
  },
  children: [
    { type: 'path', props: { d: 'M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z' } }
  ]
})

const SettingIcon = () => ({
  type: 'svg' as const,
  props: {
    viewBox: '0 0 24 24',
    fill: 'none',
    stroke: 'currentColor',
    'stroke-width': '2',
    style: { width: '24px', height: '24px' }
  },
  children: [
    { type: 'circle', props: { cx: '12', cy: '12', r: '3' } },
    { type: 'path', props: { d: 'M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z' } }
  ]
})

const stats = [
  { title: '用户总数', value: '1,234', icon: UserIcon, color: '#667eea' },
  { title: '活跃用户', value: '856', icon: ChartIcon, color: '#f093fb' },
  { title: '系统访问', value: '12.5k', icon: BoxIcon, color: '#4facfe' },
  { title: '系统设置', value: '8', icon: SettingIcon, color: '#a8edea' },
]

const features = [
  { title: '用户管理', desc: '管理系统用户信息', icon: UserIcon },
  { title: '数据分析', desc: '查看数据统计报表', icon: ChartIcon },
  { title: '系统设置', desc: '配置系统参数', icon: SettingIcon },
]
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
        <n-gi v-for="stat in stats" :key="stat.title" span="4 m:2 l:1">
          <n-card class="stat-card" :bordered="false">
            <div class="stat-content">
              <div class="stat-icon" :style="{ background: `linear-gradient(135deg, ${stat.color} 0%, ${stat.color}88 100%)` }">
                <n-icon :size="24" depth="3">
                  <component :is="stat.icon" />
                </n-icon>
              </div>
              <div class="stat-info">
                <span class="stat-value">{{ stat.value }}</span>
                <span class="stat-title">{{ stat.title }}</span>
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
              <div v-for="feature in features" :key="feature.title" class="feature-item">
                <div class="feature-icon">
                  <n-icon :size="20">
                    <component :is="feature.icon" />
                  </n-icon>
                </div>
                <div class="feature-info">
                  <span class="feature-title">{{ feature.title }}</span>
                  <span class="feature-desc">{{ feature.desc }}</span>
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
  color: #fff;
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
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
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