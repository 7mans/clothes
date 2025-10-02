<template>
  <div class="shop-page">
    <!-- 导航栏 -->
    <Header />
    
    <!-- 主要内容区域 -->
    <div class="main-content">
      <div class="shop-container">
        <h1 class="page-title">社石商店</h1>
        <p class="page-subtitle">发现更多时尚单品，打造完美搭配</p>
        
        <!-- 商品网格 -->
        <div class="products-grid">
          <div v-for="product in products" :key="product.id" class="product-card">
            <div class="product-image">
              <img :src="product.image" :alt="product.name">
              <div class="product-overlay">
                <button class="view-btn">查看详情</button>
              </div>
            </div>
            <div class="product-info">
              <h3 class="product-name">{{ product.name }}</h3>
              <p class="product-price">¥{{ product.price }}</p>
              <div class="product-tags">
                <span v-for="tag in product.tags" :key="tag" class="tag">{{ tag }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from '@/components/Header.vue'

export default {
  name: 'Shop',
  components: {
    Header
  },
  data() {
    return {
      products: [
        {
          id: 1,
          name: '甜美泡泡袖连衣裙',
          price: 299,
          image: 'https://via.placeholder.com/300x400/FFB6C1/FFFFFF?text=连衣裙',
          tags: ['甜美', '少女风', '约会']
        },
        {
          id: 2,
          name: '复古高腰A字裙',
          price: 199,
          image: 'https://via.placeholder.com/300x400/DDA0DD/FFFFFF?text=A字裙',
          tags: ['复古', '优雅', '通勤']
        },
        {
          id: 3,
          name: '韩系宽松针织衫',
          price: 159,
          image: 'https://via.placeholder.com/300x400/98FB98/FFFFFF?text=针织衫',
          tags: ['休闲', '舒适', '日常']
        },
        {
          id: 4,
          name: '法式浪漫衬衫',
          price: 249,
          image: 'https://via.placeholder.com/300x400/F0E68C/FFFFFF?text=衬衫',
          tags: ['法式', '浪漫', '职场']
        },
        {
          id: 5,
          name: '街头风牛仔外套',
          price: 399,
          image: 'https://via.placeholder.com/300x400/87CEEB/FFFFFF?text=牛仔外套',
          tags: ['街头', '酷感', '百搭']
        },
        {
          id: 6,
          name: '温柔风毛衣',
          price: 279,
          image: 'https://via.placeholder.com/300x400/F5DEB3/FFFFFF?text=毛衣',
          tags: ['温柔', '保暖', '秋冬']
        }
      ]
    }
  }
}
</script>

<style lang="scss" scoped>
.shop-page {
  min-height: 100vh;
  background: linear-gradient(135deg, #8B7CF8 0%, #C084FC 50%, #A855F7 100%);
  color: white;
}

.main-content {
  padding-top: 60px;
  min-height: 100vh;
}

.shop-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 20px;
}

.page-title {
  font-size: 36px;
  font-weight: 700;
  text-align: center;
  margin: 0 0 16px 0;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.page-subtitle {
  font-size: 16px;
  opacity: 0.9;
  text-align: center;
  margin: 0 0 60px 0;
  font-weight: 300;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 30px;
}

.product-card {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  
  &:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
  }
}

.product-image {
  position: relative;
  height: 300px;
  overflow: hidden;
  
  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
  }
  
  .product-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity 0.3s ease;
  }
  
  &:hover .product-overlay {
    opacity: 1;
  }
  
  &:hover img {
    transform: scale(1.05);
  }
}

.view-btn {
  background: linear-gradient(45deg, #4facfe 0%, #00f2fe 100%);
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  
  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(79, 172, 254, 0.4);
  }
}

.product-info {
  padding: 20px;
  color: #333;
}

.product-name {
  font-size: 18px;
  font-weight: 600;
  margin: 0 0 8px 0;
  color: #333;
}

.product-price {
  font-size: 20px;
  font-weight: 700;
  color: #4facfe;
  margin: 0 0 12px 0;
}

.product-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.tag {
  background: #f0f0f0;
  color: #666;
  padding: 4px 8px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 500;
}

@media (max-width: 768px) {
  .shop-container {
    padding: 20px 16px;
  }
  
  .page-title {
    font-size: 28px;
  }
  
  .page-subtitle {
    font-size: 14px;
    margin-bottom: 40px;
  }
  
  .products-grid {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
  }
  
  .product-image {
    height: 250px;
  }
}
</style>
