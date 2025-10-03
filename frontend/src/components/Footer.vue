<template>
  <footer class="footer">
    <div class="container footer-inner">
      <div class="brand">
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
        <div class="brand-text">
          <h4>AI2Cloth</h4>
          <p>AI驱动的时尚分析平台</p>
        </div>
      </div>

      <nav class="footer-nav">
        <router-link to="/" class="footer-link">首页</router-link>
        <router-link to="/analysis" class="footer-link">开始分析</router-link>
        <a href="#pricing" class="footer-link">定价</a>
      </nav>

      <div class="socials">
        <a href="#" class="social-btn" aria-label="Twitter">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
            <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
          </svg>
        </a>
        <a href="#" class="social-btn" aria-label="GitHub">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
          </svg>
        </a>
        <a href="#" class="social-btn" aria-label="LinkedIn">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
            <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
          </svg>
        </a>
      </div>
    </div>

    <div class="container footer-bottom">
      <span>© {{ new Date().getFullYear() }} AI2Cloth. 保留所有权利。</span>
      <div class="policies">
        <a href="#" class="policy-link">隐私政策</a>
        <a href="#" class="policy-link">服务条款</a>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style lang="scss" scoped>
.footer {
  margin-top: var(--spacing-3xl);
  border-top: 1px solid var(--color-border);
  background: var(--color-bg-secondary);
}

.footer-inner {
  padding: var(--spacing-2xl) 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--spacing-xl);
}

.brand {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);

  .logo-icon {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .brand-text {
    h4 {
      margin: 0;
      color: var(--color-text-primary);
      font-size: var(--font-size-lg);
      font-weight: var(--font-weight-bold);
    }
    p {
      margin: 0;
      color: var(--color-text-secondary);
      font-size: var(--font-size-sm);
    }
  }
}

.footer-nav {
  display: flex;
  gap: var(--spacing-lg);

  .footer-link {
    color: var(--color-text-secondary);
    text-decoration: none;
    transition: color var(--transition-normal);

    &:hover {
      color: var(--color-text-primary);
    }
  }
}

.socials {
  display: flex;
  gap: var(--spacing-sm);

  .social-btn {
    width: 32px;
    height: 32px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border-radius: var(--radius-md);
    color: var(--color-text-secondary);
    background: transparent;
    border: 1px solid var(--color-border);
    transition: all var(--transition-normal);

    &:hover {
      color: var(--color-text-primary);
      background: var(--color-bg-hover);
      border-color: var(--color-border-dark);
    }
  }
}

.footer-bottom {
  border-top: 1px solid var(--color-border);
  padding: var(--spacing-lg) 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: var(--color-text-muted);
  font-size: var(--font-size-sm);

  .policies {
    display: flex;
    gap: var(--spacing-lg);

    .policy-link {
      color: var(--color-text-muted);
      text-decoration: none;
      transition: color var(--transition-normal);

      &:hover {
        color: var(--color-text-primary);
      }
    }
  }
}

@media (max-width: 768px) {
  .footer-inner {
    flex-direction: column;
    align-items: flex-start;
  }
  .footer-bottom {
    flex-direction: column;
    gap: var(--spacing-md);
    align-items: flex-start;
  }
}
</style>
