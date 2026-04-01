<script setup lang="ts">
import { h } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

// SVG 图标组件
const DashboardIcon = () => h('svg', {
  viewBox: '0 0 24 24',
  fill: 'none',
  stroke: 'currentColor',
  'stroke-width': '2',
  style: { width: '20px', height: '20px' }
}, [
  h('rect', { x: '3', y: '3', width: '7', height: '7', rx: '1' }),
  h('rect', { x: '14', y: '3', width: '7', height: '7', rx: '1' }),
  h('rect', { x: '3', y: '14', width: '7', height: '7', rx: '1' }),
  h('rect', { x: '14', y: '14', width: '7', height: '7', rx: '1' })
])

const PeopleIcon = () => h('svg', {
  viewBox: '0 0 24 24',
  fill: 'none',
  stroke: 'currentColor',
  'stroke-width': '2',
  style: { width: '20px', height: '20px' }
}, [
  h('path', { d: 'M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2' }),
  h('circle', { cx: '9', cy: '7', r: '4' }),
  h('path', { d: 'M23 21v-2a4 4 0 0 0-3-3.87' }),
  h('path', { d: 'M16 3.13a4 4 0 0 1 0 7.75' })
])

const MenuIcon = () => h('svg', {
  viewBox: '0 0 24 24',
  fill: 'none',
  stroke: 'currentColor',
  'stroke-width': '2',
  style: { width: '24px', height: '24px' }
}, [
  h('line', { x1: '3', y1: '12', x2: '21', y2: '12' }),
  h('line', { x1: '3', y1: '6', x2: '21', y2: '6' }),
  h('line', { x1: '3', y1: '18', x2: '21', y2: '18' })
])

const LogoutIcon = () => h('svg', {
  viewBox: '0 0 24 24',
  fill: 'none',
  stroke: 'currentColor',
  'stroke-width': '2',
  style: { width: '20px', height: '20px' }
}, [
  h('path', { d: 'M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4' }),
  h('polyline', { points: '16 17 21 12 16 7' }),
  h('line', { x1: '21', y1: '12', x2: '9', y2: '12' })
])

const menuOptions = [
  {
    label: '仪表盘',
    key: '/dashboard',
    icon: DashboardIcon,
  },
  {
    label: '用户管理',
    key: '/users',
    icon: PeopleIcon,
  },
]

function handleMenuSelect(key: string) {
  router.push(key)
}

function handleLogout() {
  authStore.logout()
  router.push('/login')
}

const activeKey = route.path
</script>

<template>
  <div class="app-layout">
    <n-layout has-sider class="layout">
      <!-- Sidebar -->
      <n-layout-sider
        bordered
        collapse-mode="width"
        :collapsed-width="64"
        :width="220"
        show-trigger="bar"
        :native-scrollbar="false"
        class="sidebar"
      >
        <div class="logo">
          <n-icon :component="MenuIcon" :size="24" />
          <span class="logo-text">Vue-Python</span>
        </div>

        <n-menu
          :options="menuOptions"
          :value="activeKey"
          :collapsed-width="64"
          :collapsed-icon-size="22"
          @update:value="handleMenuSelect"
        />

        <div class="sidebar-footer">
          <n-button quaternary block @click="handleLogout">
            <template #icon>
              <n-icon :component="LogoutIcon" />
            </template>
            退出登录
          </n-button>
        </div>
      </n-layout-sider>

      <!-- Main Content -->
      <n-layout class="main-layout">
        <n-layout-header bordered class="header">
          <div class="header-left">
            <h2>{{ route.meta.title || '仪表盘' }}</h2>
          </div>
          <div class="header-right">
            <n-space>
              <n-tag :bordered="false" type="success">
                {{ authStore.user?.username || 'admin' }}
              </n-tag>
              <n-button quaternary circle @click="handleLogout">
                <template #icon>
                  <n-icon :component="LogoutIcon" />
                </template>
              </n-button>
            </n-space>
          </div>
        </n-layout-header>

        <n-layout-content class="content">
          <router-view />
        </n-layout-content>
      </n-layout>
    </n-layout>
  </div>
</template>

<style scoped>
.app-layout {
  height: 100vh;
  background: #0a0a0f;
}

.layout {
  height: 100%;
}

.sidebar {
  background: rgba(255, 255, 255, 0.02) !important;
  border-color: rgba(255, 255, 255, 0.08) !important;
}

.logo {
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  color: #fff;
  font-size: 16px;
  font-weight: 600;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.sidebar :deep(.n-menu) {
  background: transparent;
}

.sidebar :deep(.n-menu-item) {
  color: rgba(255, 255, 255, 0.7);
  margin: 4px 8px;
  border-radius: 8px;
}

.sidebar :deep(.n-menu-item:hover) {
  color: #fff;
  background: rgba(255, 255, 255, 0.05);
}

.sidebar :deep(.n-menu-item.n-menu-item--selected) {
  color: #667eea;
  background: rgba(102, 126, 234, 0.15);
}

.sidebar :deep(.n-menu-item-content::after) {
  display: none;
}

.sidebar-footer {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.sidebar-footer :deep(.n-button) {
  color: rgba(255, 255, 255, 0.6);
  width: 100%;
  justify-content: flex-start;
}

.sidebar-footer :deep(.n-button:hover) {
  color: #fff;
}

.main-layout {
  background: #0a0a0f;
}

.header {
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  background: rgba(255, 255, 255, 0.02) !important;
  border-color: rgba(255, 255, 255, 0.08) !important;
}

.header-left h2 {
  font-size: 18px;
  font-weight: 500;
  color: #fff;
  margin: 0;
}

.header-right {
  display: flex;
  align-items: center;
}

.content {
  padding: 0;
  background: transparent;
}
</style>