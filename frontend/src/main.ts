import { createApp } from 'vue'
import { createPinia } from 'pinia'
import naive from 'naive-ui'
import App from './App.vue'
import router from './router'
import './assets/main.css'

const app = createApp(App)

app.use(createPinia())
app.use(naive)
app.use(router)

// 全局配置 - 暗色主题
const config = {
  theme: 'dark',
}

app.mount('#app')

// 动态设置主题
document.documentElement.classList.add('dark')