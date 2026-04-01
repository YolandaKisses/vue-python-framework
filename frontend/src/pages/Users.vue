<script setup lang="ts">
import { ref, computed, defineComponent, h } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { NDataTable, NButton, NTag, NIcon } from 'naive-ui'
import type { User } from '@/types'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

const users = ref<User[]>([])
const loading = ref(false)
const searchValue = ref('')

// 模拟数据
const mockUsers: User[] = [
  { id: 1, username: 'admin', email: 'admin@example.com', is_active: true },
  { id: 2, username: 'user01', email: 'user01@example.com', is_active: true },
  { id: 3, username: 'user02', email: 'user02@example.com', is_active: false },
  { id: 4, username: 'test', email: 'test@example.com', is_active: true },
]

// SVG 图标
const EditIcon = defineComponent({
  render() {
    return h('svg', {
      viewBox: '0 0 24 24',
      fill: 'none',
      stroke: 'currentColor',
      'stroke-width': '2',
      style: { width: '16px', height: '16px' }
    }, [
      h('path', { d: 'M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7' }),
      h('path', { d: 'M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z' })
    ])
  }
})

const DeleteIcon = defineComponent({
  render() {
    return h('svg', {
      viewBox: '0 0 24 24',
      fill: 'none',
      stroke: 'currentColor',
      'stroke-width': '2',
      style: { width: '16px', height: '16px' }
    }, [
      h('polyline', { points: '3 6 5 6 21 6' }),
      h('path', { d: 'M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2' })
    ])
  }
})

const columns = [
  { title: 'ID', key: 'id', width: 80 },
  { title: '用户名', key: 'username' },
  { title: '邮箱', key: 'email' },
  {
    title: '状态',
    key: 'is_active',
    width: 100,
    render(row: User) {
      return h(NTag, {
        type: row.is_active ? 'success' : 'error',
        size: 'small',
      }, { default: () => row.is_active ? '启用' : '禁用' })
    }
  },
  {
    title: '操作',
    key: 'actions',
    width: 120,
    render(row: User) {
      return h('div', { class: 'action-buttons' }, [
        h(NButton, {
          size: 'small',
          quaternary: true,
          onClick: () => handleEdit(row)
        }, { icon: () => h(NIcon, { component: EditIcon }) }),
        h(NButton, {
          size: 'small',
          quaternary: true,
          type: 'error',
          onClick: () => handleDelete(row)
        }, { icon: () => h(NIcon, { component: DeleteIcon }) })
      ])
    }
  }
]

onMounted(async () => {
  loading.value = true
  try {
    users.value = mockUsers
  } finally {
    loading.value = false
  }
})

function handleEdit(user: User) {
  console.log('Edit user:', user)
}

function handleDelete(user: User) {
  console.log('Delete user:', user)
}
</script>

<template>
  <div class="users-page">
    <div class="page-header">
      <div class="header-left">
        <h1>用户管理</h1>
        <p>管理系统用户账号</p>
      </div>
      <n-button type="primary">
        <template #icon>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 16px; height: 16px">
            <line x1="12" y1="5" x2="12" y2="19"></line>
            <line x1="5" y1="12" x2="19" y2="12"></line>
          </svg>
        </template>
        新增用户
      </n-button>
    </div>

    <n-card :bordered="false" class="content-card">
      <div class="toolbar">
        <n-input
          v-model:value="searchValue"
          placeholder="搜索用户..."
          clearable
          style="width: 300px"
        />
      </div>

      <n-data-table
        :columns="columns"
        :data="users"
        :loading="loading"
        :bordered="false"
        :single-line="false"
      />
    </n-card>
  </div>
</template>

<script lang="ts">
import { onMounted } from 'vue'
export default {
  setup() {
    return {}
  }
}
</script>

<style scoped>
.users-page {
  padding: 24px;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

.header-left h1 {
  font-size: 24px;
  font-weight: 600;
  color: #fff;
  margin-bottom: 4px;
}

.header-left p {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.5);
}

.content-card {
  background: rgba(255, 255, 255, 0.03);
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.content-card :deep(.n-card__content) {
  padding: 20px;
}

.toolbar {
  margin-bottom: 20px;
}

.content-card :deep(.n-data-table) {
  background: transparent;
}

.content-card :deep(.n-data-table-th) {
  background: rgba(255, 255, 255, 0.03);
  color: rgba(255, 255, 255, 0.6);
  border-color: rgba(255, 255, 255, 0.08);
}

.content-card :deep(.n-data-table-td) {
  background: transparent;
  color: #fff;
  border-color: rgba(255, 255, 255, 0.08);
}

.content-card :deep(.n-data-table-tr:hover .n-data-table-td) {
  background: rgba(255, 255, 255, 0.03);
}

.action-buttons {
  display: flex;
  gap: 8px;
}
</style>