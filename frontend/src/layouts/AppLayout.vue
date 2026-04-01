<script setup lang="ts">
import { RouterLink, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
const router = useRouter()

function handleLogout() {
  authStore.logout()
  router.push('/login')
}
</script>

<template>
  <div class="app-layout">
    <header class="header">
      <div class="logo">Vue-Python 全栈</div>
      <nav class="nav">
        <RouterLink to="/dashboard">仪表盘</RouterLink>
        <RouterLink to="/users">用户</RouterLink>
      </nav>
      <div class="user-info">
        <span>{{ authStore.user?.username || '用户' }}</span>
        <button @click="handleLogout" class="logout-btn">退出</button>
      </div>
    </header>
    <main class="main">
      <slot />
    </main>
  </div>
</template>

<style scoped>
.app-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 2rem;
  height: 60px;
  background: #2c3e50;
  color: white;
}

.logo {
  font-size: 1.25rem;
  font-weight: bold;
}

.nav {
  display: flex;
  gap: 1.5rem;
}

.nav a {
  color: #bdc3c7;
  text-decoration: none;
  transition: color 0.3s;
}

.nav a:hover, .nav a.router-link-active {
  color: white;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.logout-btn {
  padding: 0.5rem 1rem;
  background: #e74c3c;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.3s;
}

.logout-btn:hover {
  background: #c0392b;
}

.main {
  flex: 1;
  background: #f5f6fa;
}
</style>