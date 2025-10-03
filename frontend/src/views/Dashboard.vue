<template>
  <div class="dashboard">
    <!-- Header -->
    <Header/>
    
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="container">
        <div class="hero-content">
          <div class="hero-text">
            <h1 class="hero-title animate-fadeInUp">
              {{ $t('hero.title') }}
            </h1>
            <p class="hero-subtitle animate-fadeInUp animate-delay-200">
              {{ $t('hero.subtitle') }}
            </p>
          </div>
          
          <div class="hero-action animate-scaleIn animate-delay-300">
            <router-link to="/analysis" class="start-journey-btn btn btn-primary btn-lg hover-lift">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
              </svg>
              {{ $t('hero.startJourney') }}
            </router-link>
            <p class="action-subtitle">{{ $t('hero.actionSubtitle') }}</p>
          </div>
        </div>
      </div>
      
      <!-- Background Elements -->
      <div class="hero-bg">
        <div class="bg-gradient"></div>
        <div class="bg-pattern"></div>
      </div>
    </section>

    <!-- How It Works Section -->
    <section class="how-it-works section">
      <div class="container">
        <div class="section-header text-center">
          <h2 class="heading-2">{{ $t('howItWorks.title') }}</h2>
          <p class="section-subtitle">{{ $t('howItWorks.subtitle') }}</p>
        </div>
        
        <div class="steps-grid">
          <div class="step-card hover-lift animate-fadeInUp" 
               v-for="(step, index) in steps" 
               :key="index"
               :class="`animate-delay-${(index + 1) * 100}`">
            <div class="step-number">{{ index + 1 }}</div>
            <div class="step-icon">
              <i :class="step.icon"></i>
            </div>
            <h3>{{ $t(step.titleKey) }}</h3>
            <p>{{ $t(step.descriptionKey) }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section class="features section">
      <div class="container">
        <div class="section-header text-center">
          <h2 class="heading-2">{{ $t('features.title') }}</h2>
          <p class="section-subtitle">{{ $t('features.subtitle') }}</p>
        </div>
        
        <div class="features-grid">
          <div class="feature-card hover-lift animate-slideInLeft" 
               v-for="(feature, index) in features" 
               :key="index"
               :class="index % 2 === 0 ? 'animate-slideInLeft' : 'animate-slideInRight'"
               :style="`animation-delay: ${index * 0.1}s`">
            <div class="feature-icon">
              <i :class="feature.icon"></i>
            </div>
            <h3>{{ $t(feature.titleKey) }}</h3>
            <p>{{ $t(feature.descriptionKey) }}</p>
          </div>
        </div>
      </div>
    </section>

        <!-- FAQ Section -->
    <section class="faq section">
      <div class="container">
        <div class="section-header text-center">
          <h2 class="heading-2">{{ $t('faq.title') }}</h2>
          <p class="section-subtitle">{{ $t('faq.subtitle') }}</p>
        </div>
        
        <div class="faq-list">
          <div class="faq-item" v-for="(faq, index) in faqs" :key="index" @click="toggleFaq(index)">
            <div class="faq-question">
              <span>{{ $t(faq.questionKey) }}</span>
              <i :class="['fas', faq.open ? 'fa-minus' : 'fa-plus']"></i>
            </div>
            <div class="faq-answer" :class="{ open: faq.open }">
              <p>{{ $t(faq.answerKey) }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <Footer/>


  </div>
</template>

<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'Dashboard',
  components: {
    Header,
    Footer
  },
  data() {
    return {
      steps: [
        {
          icon: 'fas fa-upload',
          titleKey: 'howItWorks.steps.upload.title',
          descriptionKey: 'howItWorks.steps.upload.description'
        },
        {
          icon: 'fas fa-brain',
          titleKey: 'howItWorks.steps.analyze.title',
          descriptionKey: 'howItWorks.steps.analyze.description'
        },
        {
          icon: 'fas fa-chart-line',
          titleKey: 'howItWorks.steps.report.title',
          descriptionKey: 'howItWorks.steps.report.description'
        }
      ],
      features: [
        {
          icon: 'fas fa-eye',
          titleKey: 'features.items.recognition.title',
          descriptionKey: 'features.items.recognition.description'
        },
        {
          icon: 'fas fa-palette',
          titleKey: 'features.items.styleAnalysis.title',
          descriptionKey: 'features.items.styleAnalysis.description'
        },
        {
          icon: 'fas fa-lightbulb',
          titleKey: 'features.items.suggestions.title',
          descriptionKey: 'features.items.suggestions.description'
        },
        {
          icon: 'fas fa-shopping-bag',
          titleKey: 'features.items.shopping.title',
          descriptionKey: 'features.items.shopping.description'
        }
      ],
      faqs: [
        {
          questionKey: 'faq.items.howItWorks.question',
          answerKey: 'faq.items.howItWorks.answer',
          open: true
        },
        {
          questionKey: 'faq.items.formats.question',
          answerKey: 'faq.items.formats.answer',
          open: false
        },
        {
          questionKey: 'faq.items.time.question',
          answerKey: 'faq.items.time.answer',
          open: false
        },
        {
          questionKey: 'faq.items.security.question',
          answerKey: 'faq.items.security.answer',
          open: false
        }
      ]
    }
  },
  methods: {
    toggleFaq(index) {
      this.faqs[index].open = !this.faqs[index].open
    }
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  min-height: 100vh;
  background: var(--color-bg-primary);
}

.hero-section {
  position: relative;
  min-height: 90vh;
  display: flex;
  align-items: center;
  padding-top: 64px;
  background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
}

.hero-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
  position: relative;
  z-index: 2;
}

.hero-text {
  margin-bottom: var(--spacing-3xl);
  
  .hero-title {
    font-size: var(--font-size-5xl);
    font-weight: var(--font-weight-bold);
    line-height: 1.2;
    margin-bottom: var(--spacing-lg);
    color: var(--color-text-primary);
    background: var(--gradient-accent);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  
  .hero-subtitle {
    font-size: var(--font-size-xl);
    color: var(--color-text-secondary);
    line-height: 1.6;
    max-width: 600px;
    margin: 0 auto;
  }
}

.hero-stats {
  display: flex;
  gap: var(--spacing-2xl);
  
  .stat {
    text-align: center;
    
    .stat-number {
      display: block;
      font-size: var(--font-size-3xl);
      font-weight: var(--font-weight-bold);
      color: var(--color-accent);
      margin-bottom: var(--spacing-xs);
    }
    
    .stat-label {
      font-size: var(--font-size-sm);
      color: var(--color-text-muted);
    }
  }
}

.hero-action {
  text-align: center;
  margin-top: var(--spacing-xl);
  
  .start-journey-btn {
    display: inline-flex;
    align-items: center;
    gap: var(--spacing-md);
    padding: var(--spacing-lg) var(--spacing-2xl);
    font-size: var(--font-size-xl);
    font-weight: var(--font-weight-semibold);
    border-radius: var(--radius-xl);
    background: var(--gradient-accent);
    color: white;
    text-decoration: none;
    box-shadow: var(--shadow-lg);
    transition: all var(--transition-normal);
    position: relative;
    overflow: hidden;
    
    &::before {
      content: '';
      position: absolute;
      top: 0;
      left: -100%;
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
      transition: left 0.5s;
    }
    
    &:hover {
      transform: translateY(-3px);
      box-shadow: var(--shadow-xl), var(--shadow-glow);
      
      &::before {
        left: 100%;
      }
    }
    
    svg {
      animation: pulse 2s infinite;
    }
  }
  
  .action-subtitle {
    margin-top: var(--spacing-md);
    color: var(--color-text-secondary);
    font-size: var(--font-size-base);
  }
}



.hero-bg {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1;
  
  .bg-gradient {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(ellipse at center, rgba(99, 102, 241, 0.1) 0%, transparent 70%);
  }
  
  .bg-pattern {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: radial-gradient(circle at 1px 1px, rgba(255, 255, 255, 0.05) 1px, transparent 0);
    background-size: 50px 50px;
    animation: float 20s ease-in-out infinite;
  }
}

@keyframes float {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(180deg); }
}

.section-header {
  margin-bottom: var(--spacing-3xl);
  
  .section-subtitle {
    font-size: var(--font-size-lg);
    color: var(--color-text-secondary);
    margin-top: var(--spacing-md);
  }
}

.steps-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--spacing-2xl);
}

.step-card {
  text-align: center;
  padding: var(--spacing-2xl);
  background: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  transition: all var(--transition-normal);
  
  &:hover {
    transform: translateY(-8px);
    box-shadow: var(--shadow-xl);
    border-color: var(--color-accent);
  }
  
  .step-number {
    width: 40px;
    height: 40px;
    background: var(--gradient-accent);
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: var(--font-weight-bold);
    margin: 0 auto var(--spacing-lg);
  }
  
  .step-icon {
    font-size: 32px;
    color: var(--color-accent);
    margin-bottom: var(--spacing-lg);
  }
  
  h3 {
    font-size: var(--font-size-xl);
    font-weight: var(--font-weight-semibold);
    color: var(--color-text-primary);
    margin-bottom: var(--spacing-md);
  }
  
  p {
    color: var(--color-text-secondary);
    line-height: 1.6;
  }
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: var(--spacing-2xl);
}

.feature-card {
  padding: var(--spacing-2xl);
  background: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  transition: all var(--transition-normal);
  
  &:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
    border-color: var(--color-border-light);
  }
  
  .feature-icon {
    width: 60px;
    height: 60px;
    background: var(--color-accent-light);
    color: var(--color-accent);
    border-radius: var(--radius-lg);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    margin-bottom: var(--spacing-lg);
  }
  
  h3 {
    font-size: var(--font-size-xl);
    font-weight: var(--font-weight-semibold);
    color: var(--color-text-primary);
    margin-bottom: var(--spacing-md);
  }
  
  p {
    color: var(--color-text-secondary);
    line-height: 1.6;
  }
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2000;
  backdrop-filter: blur(10px);
}

.modal-content {
  background: var(--color-bg-card);
  border-radius: var(--radius-2xl);
  max-width: 90vw;
  max-height: 90vh;
  overflow: auto;
  position: relative;
  box-shadow: var(--shadow-xl);
}

.modal-close {
  position: absolute;
  top: var(--spacing-lg);
  right: var(--spacing-lg);
  width: 40px;
  height: 40px;
  background: var(--color-bg-hover);
  border: none;
  border-radius: 50%;
  color: var(--color-text-primary);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
  transition: all var(--transition-normal);
  
  &:hover {
    background: var(--color-border);
    transform: scale(1.1);
  }
}

// 响应式设计
@media (max-width: 1024px) {
  .features-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .hero-section {
    padding-top: 80px;
    min-height: 80vh;
  }
  
  .hero-text .hero-title {
    font-size: var(--font-size-4xl);
  }
  
  .hero-text .hero-subtitle {
    font-size: var(--font-size-lg);
  }
  
  .steps-grid {
    grid-template-columns: 1fr;
    gap: var(--spacing-lg);
  }
  
  .upload-area {
    padding: var(--spacing-lg);
  }
  

}

@media (max-width: 480px) {
  .hero-section {
    padding-top: 60px;
  }
  
  .upload-container {
    padding: var(--spacing-lg);
  }
  
  .modal-content {
    max-width: 95vw;
    max-height: 95vh;
    margin: var(--spacing-md);
  }
}

.faq-list {
  max-width: 800px;
  margin: 0 auto;
}

.faq-item {
  background: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  margin-bottom: var(--spacing-md);
  cursor: pointer;
  transition: all var(--transition-normal);
  overflow: hidden;
  
  &:hover {
    border-color: var(--color-accent);
  }
}

.faq-question {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--spacing-lg);
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-medium);
  color: var(--color-text-primary);
}

.faq-answer {
  max-height: 0;
  transition: max-height 0.5s ease-in-out, padding 0.5s ease-in-out;
  
  p {
    padding: 0 var(--spacing-lg) var(--spacing-lg);
    color: var(--color-text-secondary);
    line-height: 1.7;
    margin: 0;
  }
  
  &.open {
    max-height: 200px; /* Adjust as needed */
    padding-bottom: var(--spacing-lg);
  }
}
</style>