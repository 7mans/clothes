<template>
  <div class="register">
    <div class="register-container">
      <div class="register-form">
        <h2>注册</h2>
        <form @submit.prevent="handleRegister">
          <div class="form-group">
            <label for="username">用户名</label>
            <input
              type="text"
              id="username"
              v-model="form.username"
              required
              :disabled="loading"
            />
          </div>
          <div class="form-group">
            <label for="email">邮箱</label>
            <input
              type="email"
              id="email"
              v-model="form.email"
              required
              :disabled="loading"
            />
          </div>
          <div class="form-group">
            <label for="password">密码</label>
            <input
              type="password"
              id="password"
              v-model="form.password"
              required
              :disabled="loading"
            />
          </div>
          <div class="form-group">
            <label for="confirmPassword">确认密码</label>
            <input
              type="password"
              id="confirmPassword"
              v-model="form.confirmPassword"
              required
              :disabled="loading"
            />
          </div>
          <button type="submit" class="btn btn-primary" :disabled="loading">
            <i v-if="loading" class="fas fa-spinner fa-spin"></i>
            {{ loading ? '注册中...' : '注册' }}
          </button>
        </form>
        <div class="register-links">
          <router-link to="/login">已有账户？立即登录</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import apiService from '@/services/apiService'

export default {
  name: 'Register',
  data() {
    return {
      form: {
        username: '',
        email: '',
        password: '',
        confirmPassword: ''
      },
      loading: false
    }
  },
  methods: {
    ...mapActions(['login', 'setError']),
    async handleRegister() {
      if (this.form.password !== this.form.confirmPassword) {
        this.setError('密码不匹配')
        return
      }

      this.loading = true
      try {
        const response = await apiService.register(this.form)
        this.login({
          user: response.user,
          token: response.token
        })
        this.$router.push('/dashboard')
      } catch (error) {
        this.setError(error.response?.data?.message || '注册失败')
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
.register {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.register-container {
  background: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
  width: 100%;
  max-width: 400px;
}

.register-form h2 {
  text-align: center;
  margin-bottom: 2rem;
  color: #333;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #555;
  font-weight: 600;
}

.form-group input {
  width: 100%;
  padding: 12px;
  border: 2px solid #e1e5e9;
  border-radius: 5px;
  font-size: 1rem;
  transition: border-color 0.3s ease;
}

.form-group input:focus {
  outline: none;
  border-color: #667eea;
}

.btn {
  width: 100%;
  padding: 12px;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.3s ease;
}

.btn:hover:not(:disabled) {
  background: #5a6fd8;
}

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.register-links {
  text-align: center;
  margin-top: 1.5rem;
}

.register-links a {
  color: #667eea;
  text-decoration: none;
}

.register-links a:hover {
  text-decoration: underline;
}
</style>
