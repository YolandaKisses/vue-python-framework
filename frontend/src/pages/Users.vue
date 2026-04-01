<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { api } from '@/utils/request'
import { SearchOutline, AddOutline, CreateOutline, TrashOutline } from '@vicons/ionicons5'
import type { User } from '@/types'

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

onMounted(async () => {
  loading.value = true
  try {
    // 模拟数据
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
          <n-icon :component="AddOutline" />
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
        >
          <template #prefix>
            <n-icon :component="SearchOutline" />
          </template>
        </n-input>
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
import { defineComponent, h } from 'vue'
import { NButton, NTag, NIcon } from 'naive-ui'
import { CreateOutline, TrashOutline } from '@vicons/ionicons5'

const createColumns = () => {
  return [
    {
      title: 'ID',
      key: 'id',
      width: 80,
    },
    {
      title: '用户名',
      key: 'username',
    },
    {
      title: '邮箱',
      key: 'email',
    },
    {
      title: '状态',
      key: 'is_active',
      width: 100,
      render: (row: User) => {
        return h(NTag, {
          type: row.is_active ? 'success' : 'error',
          size: 'small',
        }, { default: () => row.is_active ? '启用' : '禁用' })
      },
    },
    {
      title: '操作',
      key: 'actions',
      width: 120,
      render: (row: User) => {
        return h('div', { class: 'action-buttons' }, [
          h(NButton, {
            size: 'small',
            quaternary: true,
            onClick: () => console.log('edit', row.id),
          }, { icon: () => h(NIcon, { component: CreateOutline }) }),
          h(NButton, {
            size: 'small',
            quaternary: true,
            type: 'error',
            onClick: () => console.log('delete', row.id),
          }, { icon: () => h(NIcon, { component: TrashOutline }) }),
        ])
      },
    },
  ]
}

export default defineComponent({
  setup() {
    return {
      columns: createColumns(),
    }
  },
})
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