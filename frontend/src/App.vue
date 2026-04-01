<script setup lang="ts">
import { computed } from 'vue'
import { RouterView, useRoute } from 'vue-router'
import { NConfigProvider, NMessageProvider, darkTheme } from 'naive-ui'
import AppLayout from '@/layouts/AppLayout.vue'

const route = useRoute()

// 使用 meta.requiresAuth 判断是否需要布局
const showLayout = computed(() => route.meta.requiresAuth !== false)

const themeOverrides = {
  common: {
    primaryColor: '#667eea',
    primaryColorHover: '#7c8ff0',
    primaryColorPressed: '#5a71cc',
  },
  Card: {
    color: 'rgba(255, 255, 255, 0.03)',
    colorModal: 'rgba(255, 255, 255, 0.03)',
    borderColor: 'rgba(255, 255, 255, 0.08)',
    titleTextColor: '#fff',
    textColor: '#fff',
  },
  Input: {
    color: 'rgba(255, 255, 255, 0.05)',
    colorFocus: 'rgba(255, 255, 255, 0.08)',
    border: '1px solid rgba(255, 255, 255, 0.08)',
    borderHover: '1px solid rgba(255, 255, 255, 0.15)',
    borderFocus: '1px solid #667eea',
    textColor: '#fff',
    placeholderColor: 'rgba(255, 255, 255, 0.3)',
  },
  Button: {
    colorPrimary: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    colorHoverPrimary: 'linear-gradient(135deg, #7c8ff0 0%, #8a5cb3 100%)',
    colorPressedPrimary: 'linear-gradient(135deg, #5a71cc 0%, #6a4199 100%)',
  },
  Menu: {
    color: 'transparent',
    itemColorActive: 'rgba(102, 126, 234, 0.1)',
    itemTextColor: 'rgba(255, 255, 255, 0.7)',
    itemTextColorActive: '#667eea',
    itemIconColor: 'rgba(255, 255, 255, 0.5)',
    itemIconColorActive: '#667eea',
  },
  DataTable: {
    thColor: 'rgba(255, 255, 255, 0.03)',
    thColorHover: 'rgba(255, 255, 255, 0.05)',
    tdColor: 'transparent',
    tdColorHover: 'rgba(255, 255, 255, 0.03)',
    borderColor: 'rgba(255, 255, 255, 0.08)',
    thTextColor: 'rgba(255, 255, 255, 0.6)',
    tdTextColor: '#fff',
  },
}
</script>

<template>
  <NConfigProvider :theme="darkTheme" :theme-overrides="themeOverrides">
    <NMessageProvider>
      <AppLayout v-if="showLayout">
        <RouterView />
      </AppLayout>
      <RouterView v-else />
    </NMessageProvider>
  </NConfigProvider>
</template>

<style>
html, body, #app {
  height: 100%;
  margin: 0;
  background: #0a0a0f;
}
</style>