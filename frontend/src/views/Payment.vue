<template>
  <div class="payment">
    <div class="payment-container">
      <h1>会员升级</h1>
      
      <div class="pricing-plans">
        <div class="plan-card" :class="{ recommended: plan.recommended }" v-for="plan in plans" :key="plan.id">
          <div v-if="plan.recommended" class="recommended-badge">推荐</div>
          <h3>{{ plan.name }}</h3>
          <div class="price">
            <span class="currency">¥</span>
            <span class="amount">{{ plan.price }}</span>
            <span class="period">/{{ plan.period }}</span>
          </div>
          <ul class="features">
            <li v-for="feature in plan.features" :key="feature">
              <i class="fas fa-check"></i>
              {{ feature }}
            </li>
          </ul>
          <button 
            @click="selectPlan(plan)" 
            class="btn"
            :class="plan.recommended ? 'btn-primary' : 'btn-secondary'"
          >
            选择计划
          </button>
        </div>
      </div>

      <div v-if="selectedPlan" class="payment-form">
        <h2>支付信息</h2>
        <form @submit.prevent="handlePayment">
          <div class="form-group">
            <label>支付方式</label>
            <div class="payment-methods">
              <div class="payment-method" :class="{ active: paymentMethod === 'alipay' }" @click="paymentMethod = 'alipay'">
                <i class="fab fa-alipay"></i>
                <span>支付宝</span>
              </div>
              <div class="payment-method" :class="{ active: paymentMethod === 'wechat' }" @click="paymentMethod = 'wechat'">
                <i class="fab fa-weixin"></i>
                <span>微信支付</span>
              </div>
            </div>
          </div>
          
          <div class="order-summary">
            <h3>订单摘要</h3>
            <div class="summary-item">
              <span>{{ selectedPlan.name }}</span>
              <span>¥{{ selectedPlan.price }}</span>
            </div>
            <div class="summary-total">
              <span>总计</span>
              <span>¥{{ selectedPlan.price }}</span>
            </div>
          </div>

          <button type="submit" class="btn btn-primary btn-large" :disabled="!paymentMethod || loading">
            <i v-if="loading" class="fas fa-spinner fa-spin"></i>
            {{ loading ? '处理中...' : '立即支付' }}
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import apiService from '@/services/apiService'

export default {
  name: 'Payment',
  data() {
    return {
      plans: [
        {
          id: 'basic',
          name: '基础版',
          price: 29,
          period: '月',
          features: [
            '每月10次分析',
            '基础搭配建议',
            '历史记录保存',
            '邮件支持'
          ]
        },
        {
          id: 'pro',
          name: '专业版',
          price: 99,
          period: '月',
          recommended: true,
          features: [
            '无限次分析',
            '高级搭配建议',
            '个性化推荐',
            '风格趋势分析',
            '优先客服支持',
            '专属风格顾问'
          ]
        },
        {
          id: 'premium',
          name: '尊享版',
          price: 299,
          period: '月',
          features: [
            '包含专业版所有功能',
            '一对一风格咨询',
            '定制搭配方案',
            '品牌合作优惠',
            '线下活动邀请',
            '24/7专属客服'
          ]
        }
      ],
      selectedPlan: null,
      paymentMethod: '',
      loading: false
    }
  },
  methods: {
    selectPlan(plan) {
      this.selectedPlan = plan
    },
    async handlePayment() {
      if (!this.paymentMethod || !this.selectedPlan) return

      this.loading = true
      try {
        const paymentData = {
          plan_id: this.selectedPlan.id,
          payment_method: this.paymentMethod,
          amount: this.selectedPlan.price
        }
        
        await apiService.createPayment(paymentData)
        
        // 这里应该跳转到支付页面或显示二维码
        // 为了演示，我们直接显示成功消息
        this.$router.push('/dashboard')
        
      } catch (error) {
        console.error('Payment failed:', error)
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
.payment {
  min-height: 100vh;
  background: #f8f9fa;
  padding: 2rem;
}

.payment-container {
  max-width: 1200px;
  margin: 0 auto;
}

.payment-container h1 {
  text-align: center;
  margin-bottom: 3rem;
  color: #333;
}

.pricing-plans {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}

.plan-card {
  background: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  text-align: center;
  position: relative;
  transition: transform 0.3s ease;
}

.plan-card:hover {
  transform: translateY(-5px);
}

.plan-card.recommended {
  border: 2px solid #667eea;
  transform: scale(1.05);
}

.recommended-badge {
  position: absolute;
  top: -10px;
  left: 50%;
  transform: translateX(-50%);
  background: #667eea;
  color: white;
  padding: 5px 15px;
  border-radius: 15px;
  font-size: 0.8rem;
  font-weight: bold;
}

.plan-card h3 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: #333;
}

.price {
  margin-bottom: 2rem;
}

.currency {
  font-size: 1.2rem;
  color: #666;
}

.amount {
  font-size: 3rem;
  font-weight: bold;
  color: #333;
}

.period {
  font-size: 1rem;
  color: #666;
}

.features {
  list-style: none;
  padding: 0;
  margin-bottom: 2rem;
  text-align: left;
}

.features li {
  padding: 0.5rem 0;
  color: #555;
}

.features i {
  color: #28a745;
  margin-right: 0.5rem;
}

.btn {
  padding: 12px 24px;
  border: none;
  border-radius: 5px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.3s ease;
  width: 100%;
}

.btn-primary {
  background: #667eea;
  color: white;
}

.btn-primary:hover {
  background: #5a6fd8;
}

.btn-secondary {
  background: #6c757d;
  color: white;
}

.btn-secondary:hover {
  background: #5a6268;
}

.payment-form {
  background: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  max-width: 500px;
  margin: 0 auto;
}

.payment-form h2 {
  margin-bottom: 2rem;
  color: #333;
  text-align: center;
}

.form-group {
  margin-bottom: 2rem;
}

.form-group label {
  display: block;
  margin-bottom: 1rem;
  color: #555;
  font-weight: 600;
}

.payment-methods {
  display: flex;
  gap: 1rem;
}

.payment-method {
  flex: 1;
  padding: 1rem;
  border: 2px solid #e1e5e9;
  border-radius: 8px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.payment-method:hover {
  border-color: #667eea;
}

.payment-method.active {
  border-color: #667eea;
  background: #f8f9ff;
}

.payment-method i {
  font-size: 2rem;
  margin-bottom: 0.5rem;
  display: block;
}

.order-summary {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 2rem;
}

.order-summary h3 {
  margin-bottom: 1rem;
  color: #333;
}

.summary-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
  color: #666;
}

.summary-total {
  display: flex;
  justify-content: space-between;
  font-weight: bold;
  font-size: 1.1rem;
  color: #333;
  border-top: 1px solid #e1e5e9;
  padding-top: 0.5rem;
  margin-top: 1rem;
}

.btn-large {
  font-size: 1.1rem;
  padding: 15px 30px;
}

@media (max-width: 768px) {
  .payment {
    padding: 1rem;
  }
  
  .pricing-plans {
    grid-template-columns: 1fr;
  }
  
  .plan-card.recommended {
    transform: none;
  }
  
  .payment-methods {
    flex-direction: column;
  }
}
</style>
