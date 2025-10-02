<template>
  <div class="history-list-container">
    <div class="history-header">
      <h2 class="header-title">历史记录</h2>
      <button @click="refreshHistory" class="refresh-button" :disabled="loading">
        <i class="fas fa-sync-alt" :class="{ 'fa-spin': loading }"></i>
        刷新
      </button>
    </div>
    <div v-if="loading" class="loading-container">
      <div class="loading-spinner"></div>
      <p>加载历史记录中...</p>
    </div>
    <div v-else-if="error" class="error-container">
      <p>{{ error }}</p>
      <button @click="fetchHistory">重试</button>
    </div>
    <ul v-else-if="history.length > 0" class="history-items">
      <li 
        v-for="item in history" 
        :key="item.id"
        class="history-item"
        :class="{ 'active': selectedId === item.id }"
        @click="selectItem(item.id)"
      >
        <div class="item-thumbnail">
          <img :src="item.image_url" alt="thumbnail">
        </div>
        <div class="item-info">
          <p class="item-filename">{{ item.filename }}</p>
          <p class="item-timestamp">{{ formatTimestamp(item.created_at) }}</p>
        </div>
      </li>
    </ul>
    <div v-else class="no-history">
      <p>暂无历史记录</p>
    </div>
  </div>
</template>

<script>
import { analysisApi } from '@/services/apiService';

export default {
  name: 'HistoryList',
  props: {
    selectedId: {
      type: String,
      default: null
    }
  },
  data() {
    return {
      history: [],
      loading: false,
      error: null
    };
  },
  created() {
    this.fetchHistory();
  },
  methods: {
    async fetchHistory() {
      this.loading = true;
      this.error = null;
      try {
        const response = await analysisApi.getHistory();
        this.history = response.data.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
      } catch (err) {
        this.error = '无法加载历史记录，请稍后再试。';
        console.error('获取历史记录失败:', err);
      } finally {
        this.loading = false;
      }
    },
    refreshHistory() {
      this.fetchHistory();
    },
    selectItem(id) {
      this.$emit('item-selected', id);
    },
    formatTimestamp(isoString) {
      if (!isoString) return '';
      const date = new Date(isoString);
      return date.toLocaleString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
      });
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/styles/global.scss';

.history-list-container {
  width: 100%;
  height: 100%;
  background: $color-bg-main;
  border-right: 1px solid $color-border;
  display: flex;
  flex-direction: column;
}

.history-header {
  padding: $spacing-base $spacing-lg;
  border-bottom: 1px solid $color-border;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-shrink: 0;

  .header-title {
    font-size: $font-size-lg;
    font-weight: 600;
    color: $color-text-primary;
    margin: 0;
  }

  .refresh-button {
    background: none;
    border: 1px solid $color-border;
    color: $color-text-secondary;
    padding: $spacing-xs $spacing-sm;
    border-radius: $border-radius-base;
    cursor: pointer;
    font-size: $font-size-sm;
    display: flex;
    align-items: center;
    gap: $spacing-xs;
    transition: all 0.2s ease;

    &:hover {
      background: $color-bg-hover;
      color: $color-primary;
    }

    &:disabled {
      cursor: not-allowed;
      opacity: 0.6;
    }
  }
}

.loading-container, .error-container, .no-history {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: $spacing-lg;
  text-align: center;
  color: $color-text-muted;
}

.history-items {
  list-style: none;
  margin: 0;
  padding: 0;
  overflow-y: auto;
  flex-grow: 1;

  .history-item {
    display: flex;
    align-items: center;
    padding: $spacing-base $spacing-lg;
    border-bottom: 1px solid $color-border;
    cursor: pointer;
    transition: background-color 0.2s ease;

    &:hover {
      background-color: $color-bg-hover;
    }

    &.active {
      background-color: $color-primary-light;
      border-right: 3px solid $color-primary;
    }

    .item-thumbnail {
      width: 48px;
      height: 48px;
      border-radius: $border-radius-base;
      overflow: hidden;
      margin-right: $spacing-base;
      flex-shrink: 0;

      img {
        width: 100%;
        height: 100%;
        object-fit: cover;
      }
    }

    .item-info {
      overflow: hidden;
      .item-filename {
        font-size: $font-size-base;
        font-weight: 500;
        color: $color-text-primary;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        margin: 0 0 $spacing-xs 0;
      }

      .item-timestamp {
        font-size: $font-size-sm;
        color: $color-text-muted;
        margin: 0;
      }
    }
  }
}
</style>
