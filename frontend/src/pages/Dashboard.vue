<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { apiGet } from '@/utils/api'
import type { HealthCheck } from '@/types'

const authStore = useAuthStore()
const health = ref<HealthCheck | null>(null)

onMounted(async () => {
  try {
    health.value = await apiGet<HealthCheck>('/api/v1/health/detailed')
  } catch (error) {
    console.error('Failed to fetch health:', error)
  }
})
</script>

<template>
  <div class="dashboard">
    <h1>欢迎回来, {{ authStore.user?.username || '用户' }}</h1>
    <div class="dashboard-content">
      <div class="card">
        <h3>系统状态</h3>
        <p v-if="health">状态: <span class="status-ok">{{ health.status }}</span></p>
        <p v-if="health">版本: {{ health.version }}</p>
      </div>
      <div class="card">
        <h3>功能模块</h3>
        <ul>
          <li>用户管理</li>
          <li>数据分析</li>
          <li>系统设置</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>
.dashboard {
  padding: 2rem;
}

.dashboard h1 {
  margin-bottom: 2rem;
  color: #333;
}

.dashboard-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.card {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.card h3 {
  margin-bottom: 1rem;
  color: #555;
}

.status-ok {
  color: #27ae60;
  font-weight: bold;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  padding: 0.5rem 0;
  color: #666;
}
</style>