<template>
  <header class="header">
    <div class="container">
      <div class="header-content">
        <!-- Logo -->
        <router-link to="/" class="logo">
          <div class="logo-icon">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
              <rect width="32" height="32" rx="8" fill="url(#gradient)"/>
              <path d="M8 12h16M8 16h16M8 20h12" stroke="white" stroke-width="2" stroke-linecap="round"/>
              <defs>
                <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" style="stop-color:#3b82f6"/>
                  <stop offset="100%" style="stop-color:#1d4ed8"/>
                </linearGradient>
              </defs>
            </svg>
          </div>
          <span class="logo-text">AI2Cloth</span>
        </router-link>

        <!-- Navigation -->
        <nav class="nav">
          <router-link to="/" class="nav-link" exact>{{ $t('header.home') }}</router-link>
          <router-link to="/analysis" class="nav-link">{{ $t('header.analysis') }}</router-link>
          <a href="#pricing" class="nav-link">{{ $t('header.pricing') }}</a>
        </nav>

        <!-- User Actions -->
        <div class="user-actions">
          <div class="language-selector">
            <button class="language-btn" @click="toggleLanguage">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"/>
                <line x1="2" y1="12" x2="22" y2="12"/>
                <path d="m8 2c0 5.523-4.477 10-10 10"/>
                <path d="m16 2c0 5.523 4.477 10 10 10"/>
              </svg>
              <span>{{ currentLanguage }}</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="6,9 12,15 18,9"/>
              </svg>
            </button>
            <div class="language-dropdown" :class="{ active: languageDropdownOpen }">
              <button @click="setLanguage('zh')" :class="{ active: currentLanguage === '中文' }">中文</button>
              <button @click="setLanguage('en')" :class="{ active: currentLanguage === 'EN' }">English</button>
            </div>
          </div>
          <router-link to="/login" class="btn btn-ghost">{{ $t('header.login') }}</router-link>
          <router-link to="/register" class="btn btn-primary">{{ $t('header.register') }}</router-link>
        </div>

        <!-- Mobile Menu Button -->
        <button class="mobile-menu-btn" @click="toggleMobileMenu">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>

      <!-- Mobile Menu -->
      <div class="mobile-menu" :class="{ active: mobileMenuOpen }">
        <router-link to="/" class="mobile-nav-link" @click="closeMobileMenu" exact>{{ $t('header.home') }}</router-link>
        <router-link to="/analysis" class="mobile-nav-link" @click="closeMobileMenu">{{ $t('header.analysis') }}</router-link>
        <a href="#pricing" class="mobile-nav-link" @click="closeMobileMenu">{{ $t('header.pricing') }}</a>
        <div class="mobile-actions">
          <div class="mobile-language-selector">
            <button class="language-btn mobile-btn" @click="toggleLanguage">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"/>
                <line x1="2" y1="12" x2="22" y2="12"/>
                <path d="m8 2c0 5.523-4.477 10-10 10"/>
                <path d="m16 2c0 5.523 4.477 10 10 10"/>
              </svg>
              <span>{{ currentLanguage }}</span>
            </button>
          </div>
          <router-link to="/login" class="btn btn-ghost mobile-btn">{{ $t('header.login') }}</router-link>
          <router-link to="/register" class="btn btn-primary mobile-btn">{{ $t('header.register') }}</router-link>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header',
  data() {
    return {
      mobileMenuOpen: false,
      languageDropdownOpen: false,
      currentLanguage: this.$i18n.getCurrentLanguage() === 'zh' ? '中文' : 'EN'
    }
  },
  methods: {
    toggleMobileMenu() {
      this.mobileMenuOpen = !this.mobileMenuOpen
    },
    
    closeMobileMenu() {
      this.mobileMenuOpen = false
    },
    
    toggleLanguage() {
      this.languageDropdownOpen = !this.languageDropdownOpen
    },
    
    setLanguage(lang) {
      // 使用国际化系统切换语言
      this.$i18n.setLanguage(lang)
      
      if (lang === 'zh') {
        this.currentLanguage = '中文'
      } else if (lang === 'en') {
        this.currentLanguage = 'EN'
      }
      this.languageDropdownOpen = false
    }
  },
  mounted() {
    // 点击外部关闭下拉菜单
    document.addEventListener('click', (e) => {
      if (!this.$el.contains(e.target)) {
        this.mobileMenuOpen = false
        this.languageDropdownOpen = false
      }
    })
  }
}
</script>

<style lang="scss" scoped>
.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--color-border);
  transition: all var(--transition-normal);
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 64px;
}

.logo {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  text-decoration: none;
  color: var(--color-text-primary);
  transition: all var(--transition-normal);
  
  &:hover {
    opacity: 0.8;
  }
  
  .logo-icon {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .logo-text {
    font-size: var(--font-size-xl);
    font-weight: var(--font-weight-bold);
    color: var(--color-text-primary);
  }
}

.nav {
  display: flex;
  align-items: center;
  gap: var(--spacing-lg);
}

.nav-link {
  color: var(--color-text-secondary);
  text-decoration: none;
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-medium);
  padding: var(--spacing-sm) var(--spacing-md);
  border-radius: var(--radius-md);
  transition: all var(--transition-normal);
  position: relative;
  
  &:hover {
    color: var(--color-text-primary);
    background: var(--color-bg-hover);
  }
  
  &.router-link-active, &.router-link-exact-active {
    color: var(--color-accent);
    font-weight: var(--font-weight-semibold);
    background: var(--color-accent-light);
    
    &::after {
      content: '';
      position: absolute;
      bottom: -2px;
      left: 50%;
      transform: translateX(-50%);
      width: 20px;
      height: 2px;
      background: var(--color-accent);
      border-radius: 1px;
    }
  }
}

.user-actions {
  display: flex;
  align-items: center;
  gap: var(--spacing-md);
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-sm) var(--spacing-lg);
  border: none;
  border-radius: var(--radius-md);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  text-decoration: none;
  cursor: pointer;
  transition: all var(--transition-normal);
  white-space: nowrap;
  
  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
}

.btn-primary {
  background: var(--gradient-accent);
  color: white;
  box-shadow: var(--shadow-sm);
  
  &:hover:not(:disabled) {
    box-shadow: var(--shadow-md);
    transform: translateY(-1px);
  }
}

.btn-ghost {
  background: transparent;
  color: var(--color-text-secondary);
  border: 1px solid transparent;
  
  &:hover:not(:disabled) {
    color: var(--color-text-primary);
    background: var(--color-bg-hover);
  }
}

.mobile-menu-btn {
  display: none;
  flex-direction: column;
  gap: 4px;
  background: none;
  border: none;
  cursor: pointer;
  padding: var(--spacing-sm);
  
  span {
    width: 24px;
    height: 2px;
    background: var(--color-text-primary);
    border-radius: 1px;
    transition: all var(--transition-normal);
  }
}

.mobile-menu {
  display: none;
  padding: var(--spacing-lg) 0;
  border-top: 1px solid var(--color-border);
  background: var(--color-bg-primary);
  
  &.active {
    display: block;
  }
}

.mobile-nav-link {
  display: block;
  color: var(--color-text-secondary);
  text-decoration: none;
  padding: var(--spacing-md) 0;
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-medium);
  border-bottom: 1px solid var(--color-border);
  transition: all var(--transition-normal);
  position: relative;
  
  &:hover {
    color: var(--color-text-primary);
  }
  
  &.router-link-active, &.router-link-exact-active {
    color: var(--color-accent);
    font-weight: var(--font-weight-semibold);
    
    &::before {
      content: '';
      position: absolute;
      left: 0;
      top: 50%;
      transform: translateY(-50%);
      width: 3px;
      height: 20px;
      background: var(--color-accent);
      border-radius: 2px;
    }
  }
  
  &:last-of-type {
    border-bottom: none;
  }
}

.mobile-actions {
  margin-top: var(--spacing-lg);
  padding-top: var(--spacing-lg);
  border-top: 1px solid var(--color-border);
  display: flex;
  flex-direction: column;
  gap: var(--spacing-sm);
}

.mobile-btn {
  width: 100%;
  justify-content: center;
}

// 语言选择器样式
.language-selector {
  position: relative;
}

.language-btn {
  display: flex;
  align-items: center;
  gap: var(--spacing-xs);
  padding: var(--spacing-sm) var(--spacing-md);
  background: transparent;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  color: var(--color-text-secondary);
  font-size: var(--font-size-sm);
  cursor: pointer;
  transition: all var(--transition-normal);
  
  &:hover {
    color: var(--color-text-primary);
    border-color: var(--color-border-dark);
    background: var(--color-bg-hover);
  }
  
  svg:last-child {
    transition: transform var(--transition-normal);
  }
  
  &.active svg:last-child {
    transform: rotate(180deg);
  }
}

.language-dropdown {
  position: absolute;
  top: calc(100% + 8px);
  right: 0;
  background: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
  min-width: 120px;
  opacity: 0;
  visibility: hidden;
  transform: translateY(-10px);
  transition: all var(--transition-normal);
  z-index: 1001;
  
  &.active {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
  }
  
  button {
    display: block;
    width: 100%;
    padding: var(--spacing-sm) var(--spacing-md);
    background: none;
    border: none;
    color: var(--color-text-secondary);
    font-size: var(--font-size-sm);
    text-align: left;
    cursor: pointer;
    transition: all var(--transition-normal);
    
    &:hover {
      color: var(--color-text-primary);
      background: var(--color-bg-hover);
    }
    
    &.active {
      color: var(--color-accent);
      background: var(--color-accent-light);
    }
    
    &:first-child {
      border-radius: var(--radius-md) var(--radius-md) 0 0;
    }
    
    &:last-child {
      border-radius: 0 0 var(--radius-md) var(--radius-md);
    }
  }
}

.mobile-language-selector {
  .language-btn {
    justify-content: center;
    width: 100%;
  }
}

// 响应式设计
@media (max-width: 768px) {
  .nav, .user-actions {
    display: none;
  }
  
  .mobile-menu-btn {
    display: flex;
  }
  
  .mobile-menu {
    display: none;
    
    &.active {
      display: block;
    }
  }
}

@media (max-width: 480px) {
  .header-content {
    height: 60px;
  }
  
  .logo {
    .logo-icon {
      width: 36px;
      height: 36px;
      font-size: 16px;
    }
    
    .logo-text {
      font-size: var(--font-size-lg);
    }
  }
}
</style>
