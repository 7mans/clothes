<template>
  <div class="analysis-result-container">
    <!-- 左侧边栏 -->
    <div class="left-sidebar">
      <!-- 图片展示 -->
      <div class="image-display-panel">
        <img :src="uploadedImage" alt="用户上传的图片" class="uploaded-image-preview">
      </div>
      
      <!-- 关键信息面板 -->
      <div class="key-info-panel">
        <h3 class="info-title">关键信息</h3>
        <div class="info-item">
          <span class="info-label">文件名:</span>
          <span class="info-value">person.jpg</span>
        </div>
        <div class="info-item">
          <span class="info-label">ID:</span>
          <span class="info-value">api_1759051129603</span>
        </div>
      </div>
    </div>

    <!-- 分析报告 -->
    <div class="analysis-report">
      <!-- 分析报告标题 -->
      <div class="report-header">
        <h2 class="report-title">时尚分析报告</h2>
        <div class="report-subtitle">分析于 2025年9月28日 17:18</div>
      </div>

      <!-- 整体概述 -->
      <div class="report-section">
        <div class="section-header">
          <div class="section-icon">🎯</div>
          <h3 class="section-title">整体概述</h3>
        </div>
        <div class="section-content">
          <p>整体搭配将柔美仙系与个性酷感巧妙融合，粉色碎花欧根纱裙的浪漫轻盈，通过方领、泡泡袖、前短后长拖尾设计强化甜美元素，搭配白色蕾丝袜与黑色厚底鞋，形成 "甜中带酷" 的风格反差，既保留少女感又注入街头个性，是当下流行的 "甜酷仙系风" 典型呈现。</p>
        </div>
      </div>

      <!-- 服装识别（添加商品卡片） -->
      <div class="report-section">
        <div class="section-header">
          <div class="section-icon">🧥</div>
          <h3 class="section-title">服装识别</h3>
        </div>
        <div class="section-content">
          <div class="clothing-items">
            <!-- 连衣裙卡片 -->
            <div class="clothing-card">
              <div class="clothing-name">
                <strong>连衣裙:</strong> 粉色碎花方领泡泡袖前短后长欧根纱裙
              </div>
              <!-- 商品推荐区 -->
              <div class="product-recommend">
                <div class="product-list">
                  <a 
                    v-for="(item, idx) in getTaobaoProducts('粉色碎花方领泡泡袖前短后长欧根纱裙')" 
                    :key="idx" 
                    :href="item.link" 
                    target="_blank" 
                    class="product-item"
                  >
                    <img :src="item.img" alt="商品图片" class="product-img">
                    <p class="product-title">{{item.title}}</p>
                  </a>
                </div>
                <a 
                  :href="getTaobaoSearchLink('粉色碎花方领泡泡袖前短后长欧根纱裙')" 
                  target="_blank" 
                  class="more-btn"
                >
                  查看更多 →
                </a>
              </div>
            </div>

            <!-- 袜子卡片 -->
            <div class="clothing-card">
              <div class="clothing-name">
                <strong>袜子:</strong> 白色中筒针织袜
              </div>
              <div class="product-recommend">
                <div class="product-list">
                  <a 
                    v-for="(item, idx) in getTaobaoProducts('白色中筒针织袜')" 
                    :key="idx" 
                    :href="item.link" 
                    target="_blank" 
                    class="product-item"
                  >
                    <img :src="item.img" alt="商品图片" class="product-img">
                    <p class="product-title">{{item.title}}</p>
                  </a>
                </div>
                <a 
                  :href="getTaobaoSearchLink('白色中筒针织袜')" 
                  target="_blank" 
                  class="more-btn"
                >
                  查看更多 →
                </a>
              </div>
            </div>

            <!-- 鞋履卡片 -->
            <div class="clothing-card">
              <div class="clothing-name">
                <strong>鞋履:</strong> 黑色厚底系带皮鞋
              </div>
              <div class="product-recommend">
                <div class="product-list">
                  <a 
                    v-for="(item, idx) in getTaobaoProducts('黑色厚底系带皮鞋')" 
                    :key="idx" 
                    :href="item.link" 
                    target="_blank" 
                    class="product-item"
                  >
                    <img :src="item.img" alt="商品图片" class="product-img">
                    <p class="product-title">{{item.title}}</p>
                  </a>
                </div>
                <a 
                  :href="getTaobaoSearchLink('黑色厚底系带皮鞋')" 
                  target="_blank" 
                  class="more-btn"
                >
                  查看更多 →
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 风格分析 -->
      <div class="report-section">
        <div class="section-header">
          <div class="section-icon">🎨</div>
          <h3 class="section-title">风格分析</h3>
        </div>
        <div class="section-content">
          <div class="style-analysis">
            <div class="style-item">
              <h4>风格定位</h4>
              <p>甜酷仙系风</p>
            </div>
            <div class="style-item">
              <h4>设计亮点</h4>
              <p>方领设计露出精致锁骨，强化柔美气质；泡泡袖增加复古减龄感，蓬松造型平衡裙身轻盈感；前短后长拖尾设计制造视觉层次，行走时拖尾灵动飘逸；碎花元素 + 欧根纱材质，让裙装自带朦胧浪漫滤镜</p>
            </div>
            <div class="style-item">
              <h4>风格碰撞</h4>
              <p>柔美仙系裙装搭配黑色厚底鞋，用鞋履的厚重感、休闲感中和裙装甜腻感，白色蕾丝袜衔接裙装与鞋履，增添精致细节，整体实现 "甜而不齁，酷而不硬" 的风格平衡。</p>
            </div>
          </div>
        </div>
      </div>

      <!-- 搭配建议 -->
      <div class="report-section">
        <div class="section-header">
          <div class="section-icon">💡</div>
          <h3 class="section-title">搭配建议</h3>
        </div>
        <div class="section-content">
          <div class="styling-tips">
            <div class="tip-item">
              <strong>配饰层面：</strong>可添加金属链条腰链，在方领裙的空白处制造视觉焦点，同时优化身材比例；或搭配蝴蝶结发饰，强化甜美元素，与泡泡袖风格呼应
            </div>
            <div class="tip-item">
              <strong>外搭选择：</strong>早晚温差大时，搭配短款牛仔外套，延续 "甜酷" 主线，牛仔的硬朗感与裙装柔美形成二次碰撞；或选同色系粉色薄款针织开衫，增加温柔氛围的同时提升实用性
            </div>
            <div class="tip-item">
              <strong>发型调整：</strong>将长发烫成大波浪卷，自然垂落肩头，强化浪漫感；若追求个性，可尝试高马尾造型，结合厚底鞋突出酷感，与裙装柔美形成反差。
            </div>
          </div>
        </div>
      </div>

      <!-- 适用场合 -->
      <div class="report-section">
        <div class="section-header">
          <div class="section-icon">☀️</div>
          <h3 class="section-title">适用场合</h3>
        </div>
        <div class="section-content">
          <div class="occasions">
            <div class="occasion-item">艺术展览 / 画廊参观</div>
            <div class="occasion-item">轻奢下午茶约会</div>
            <div class="occasion-item">小众主题派对（如复古少女风派对）</div>
          </div>
        </div>
      </div>

      <!-- 场景化穿搭推荐（添加商品卡片） -->
      <div class="report-section">
        <div class="section-header">
          <div class="section-icon">📅</div>
          <h3 class="section-title">场景化穿搭推荐</h3>
        </div>
        <div class="section-content">
          <div class="scenario-recommendations">
            <!-- 春日野餐 -->
            <div class="scenario-item">
              <h4>春日野餐</h4>
              <div class="outfit-details">
                <!-- 浅薄荷绿针织短开衫卡片 -->
                <div class="clothing-card">
                  <div class="clothing-name">浅薄荷绿针织短开衫</div>
                  <div class="product-recommend">
                    <div class="product-list">
                      <a 
                        v-for="(item, idx) in getTaobaoProducts('浅薄荷绿针织短开衫')" 
                        :key="idx" 
                        :href="item.link" 
                        target="_blank" 
                        class="product-item"
                      >
                        <img :src="item.img" alt="商品图片" class="product-img">
                        <p class="product-title">{{item.title}}</p>
                      </a>
                    </div>
                    <a 
                      :href="getTaobaoSearchLink('浅薄荷绿针织短开衫')" 
                      target="_blank" 
                      class="more-btn"
                    >
                      查看更多 →
                    </a>
                  </div>
                </div>

                <!-- 同色系碎花裙卡片 -->
                <div class="clothing-card">
                  <div class="clothing-name">同色系碎花裙（保留原图风格元素）</div>
                  <div class="product-recommend">
                    <div class="product-list">
                      <a 
                        v-for="(item, idx) in getTaobaoProducts('同色系碎花裙 仙系')" 
                        :key="idx" 
                        :href="item.link" 
                        target="_blank" 
                        class="product-item"
                      >
                        <img :src="item.img" alt="商品图片" class="product-img">
                        <p class="product-title">{{item.title}}</p>
                      </a>
                    </div>
                    <a 
                      :href="getTaobaoSearchLink('同色系碎花裙 仙系')" 
                      target="_blank" 
                      class="more-btn"
                    >
                      查看更多 →
                    </a>
                  </div>
                </div>

                <!-- 草编坡跟凉鞋卡片 -->
                <div class="clothing-card">
                  <div class="clothing-name">草编坡跟凉鞋</div>
                  <div class="product-recommend">
                    <div class="product-list">
                      <a 
                        v-for="(item, idx) in getTaobaoProducts('草编坡跟凉鞋 女')" 
                        :key="idx" 
                        :href="item.link" 
                        target="_blank" 
                        class="product-item"
                      >
                        <img :src="item.img" alt="商品图片" class="product-img">
                        <p class="product-title">{{item.title}}</p>
                      </a>
                    </div>
                    <a 
                      :href="getTaobaoSearchLink('草编坡跟凉鞋 女')" 
                      target="_blank" 
                      class="more-btn"
                    >
                      查看更多 →
                    </a>
                  </div>
                </div>

                <!-- 藤编手提篮包卡片 -->
                <div class="clothing-card">
                  <div class="clothing-name">藤编手提篮包</div>
                  <div class="product-recommend">
                    <div class="product-list">
                      <a 
                        v-for="(item, idx) in getTaobaoProducts('藤编手提篮包 野餐')" 
                        :key="idx" 
                        :href="item.link" 
                        target="_blank" 
                        class="product-item"
                      >
                        <img :src="item.img" alt="商品图片" class="product-img">
                        <p class="product-title">{{item.title}}</p>
                      </a>
                    </div>
                    <a 
                      :href="getTaobaoSearchLink('藤编手提篮包 野餐')" 
                      target="_blank" 
                      class="more-btn"
                    >
                      查看更多 →
                    </a>
                  </div>
                </div>
              </div>

              <div class="scenario-reasons">
                <div class="reason">
                  <strong>理由 1：</strong>浅薄荷绿开衫适配人物甜美气质，短款设计不压身高，与裙装碎花元素呼应强化春日氛围；草编坡跟鞋舒适且增高，适配野餐行走需求，同时材质自然感与野餐场景契合。
                </div>
                <div class="reason">
                  <strong>理由 2：</strong>针织开衫保暖又能应对户外早晚温差，藤编包可装野餐小物，整体风格清新自然，与野餐 "亲近自然" 的氛围感高度匹配。
                </div>
              </div>
            </div>

            <!-- 夏日音乐节 -->
            <div class="scenario-item">
              <h4>夏日音乐节</h4>
              <div class="outfit-details">
                <!-- 做旧牛仔马甲卡片 -->
                <div class="clothing-card">
                  <div class="clothing-name">做旧牛仔马甲</div>
                  <div class="product-recommend">
                    <div class="product-list">
                      <a 
                        v-for="(item, idx) in getTaobaoProducts('做旧牛仔马甲 女')" 
                        :key="idx" 
                        :href="item.link" 
                        target="_blank" 
                        class="product-item"
                      >
                        <img :src="item.img" alt="商品图片" class="product-img">
                        <p class="product-title">{{item.title}}</p>
                      </a>
                    </div>
                    <a 
                      :href="getTaobaoSearchLink('做旧牛仔马甲 女')" 
                      target="_blank" 
                      class="more-btn"
                    >
                      查看更多 →
                    </a>
                  </div>
                </div>

                <!-- 原粉色碎花裙卡片 -->
                <div class="clothing-card">
                  <div class="clothing-name">原粉色碎花裙</div>
                  <div class="product-recommend">
                    <div class="product-list">
                      <a 
                        v-for="(item, idx) in getTaobaoProducts('粉色碎花裙 甜酷')" 
                        :key="idx" 
                        :href="item.link" 
                        target="_blank" 
                        class="product-item"
                      >
                        <img :src="item.img" alt="商品图片" class="product-img">
                        <p class="product-title">{{item.title}}</p>
                      </a>
                    </div>
                    <a 
                      :href="getTaobaoSearchLink('粉色碎花裙 甜酷')" 
                      target="_blank" 
                      class="more-btn"
                    >
                      查看更多 →
                    </a>
                  </div>
                </div>

                <!-- 彩色串珠项链卡片 -->
                <div class="clothing-card">
                  <div class="clothing-name">彩色串珠项链</div>
                  <div class="product-recommend">
                    <div class="product-list">
                      <a 
                        v-for="(item, idx) in getTaobaoProducts('彩色串珠项链 甜酷')" 
                        :key="idx" 
                        :href="item.link" 
                        target="_blank" 
                        class="product-item"
                      >
                        <img :src="item.img" alt="商品图片" class="product-img">
                        <p class="product-title">{{item.title}}</p>
                      </a>
                    </div>
                    <a 
                      :href="getTaobaoSearchLink('彩色串珠项链 甜酷')" 
                      target="_blank" 
                      class="more-btn"
                    >
                      查看更多 →
                    </a>
                  </div>
                </div>

                <!-- 厚底马丁靴卡片 -->
                <div class="clothing-card">
                  <div class="clothing-name">厚底马丁靴</div>
                  <div class="product-recommend">
                    <div class="product-list">
                      <a 
                        v-for="(item, idx) in getTaobaoProducts('厚底马丁靴 女 甜酷')" 
                        :key="idx" 
                        :href="item.link" 
                        target="_blank" 
                        class="product-item"
                      >
                        <img :src="item.img" alt="商品图片" class="product-img">
                        <p class="product-title">{{item.title}}</p>
                      </a>
                    </div>
                    <a 
                      :href="getTaobaoSearchLink('厚底马丁靴 女 甜酷')" 
                      target="_blank" 
                      class="more-btn"
                    >
                      查看更多 →
                    </a>
                  </div>
                </div>
              </div>

              <div class="scenario-reasons">
                <div class="reason">
                  <strong>理由 1：</strong>做旧牛仔马甲增加街头酷感，与厚底鞋风格统一，强化 "甜酷" 标签；彩色串珠项链点亮造型，适配人物活泼气质，同时分散视觉焦点让身材比例更协调。
                </div>
                <div class="reason">
                  <strong>理由 2：</strong>牛仔马甲抗风且能应对音乐节人多拥挤时的 "层次感需求"，马丁靴耐磨适合场地行走，整体造型在热烈音乐节场景中既吸睛又实用，"甜酷" 风格与音乐节自由张扬的氛围完美契合。
                </div>
              </div>
            </div>

            <!-- 文艺书店打卡 -->
            <div class="scenario-item">
              <h4>文艺书店打卡</h4>
              <div class="outfit-details">
                <!-- 浅卡其色亚麻西装外套卡片 -->
                <div class="clothing-card">
                  <div class="clothing-name">浅卡其色亚麻西装外套</div>
                  <div class="product-recommend">
                    <div class="product-list">
                      <a 
                        v-for="(item, idx) in getTaobaoProducts('浅卡其色亚麻西装外套 文艺')" 
                        :key="idx" 
                        :href="item.link" 
                        target="_blank" 
                        class="product-item"
                      >
                        <img :src="item.img" alt="商品图片" class="product-img">
                        <p class="product-title">{{item.title}}</p>
                      </a>
                    </div>
                    <a 
                      :href="getTaobaoSearchLink('浅卡其色亚麻西装外套 文艺')" 
                      target="_blank" 
                      class="more-btn"
                    >
                      查看更多 →
                    </a>
                  </div>
                </div>

                <!-- 原粉色碎花裙卡片 -->
                <div class="clothing-card">
                  <div class="clothing-name">原粉色碎花裙</div>
                  <div class="product-recommend">
                    <div class="product-list">
                      <a 
                        v-for="(item, idx) in getTaobaoProducts('粉色碎花裙 文艺')" 
                        :key="idx" 
                        :href="item.link" 
                        target="_blank" 
                        class="product-item"
                      >
                        <img :src="item.img" alt="商品图片" class="product-img">
                        <p class="product-title">{{item.title}}</p>
                      </a>
                    </div>
                    <a 
                      :href="getTaobaoSearchLink('粉色碎花裙 文艺')" 
                      target="_blank" 
                      class="more-btn"
                    >
                      查看更多 →
                    </a>
                  </div>
                </div>

                <!-- 乐福鞋卡片 -->
                <div class="clothing-card">
                  <div class="clothing-name">乐福鞋</div>
                  <div class="product-recommend">
                    <div class="product-list">
                      <a 
                        v-for="(item, idx) in getTaobaoProducts('乐福鞋 女 文艺')" 
                        :key="idx" 
                        :href="item.link" 
                        target="_blank" 
                        class="product-item"
                      >
                        <img :src="item.img" alt="商品图片" class="product-img">
                        <p class="product-title">{{item.title}}</p>
                      </a>
                    </div>
                    <a 
                      :href="getTaobaoSearchLink('乐福鞋 女 文艺')" 
                      target="_blank" 
                      class="more-btn"
                    >
                      查看更多 →
                    </a>
                  </div>
                </div>

                <!-- 皮质剑桥包卡片 -->
                <div class="clothing-card">
                  <div class="clothing-name">皮质剑桥包</div>
                  <div class="product-recommend">
                    <div class="product-list">
                      <a 
                        v-for="(item, idx) in getTaobaoProducts('皮质剑桥包 文艺 女')" 
                        :key="idx" 
                        :href="item.link" 
                        target="_blank" 
                        class="product-item"
                      >
                        <img :src="item.img" alt="商品图片" class="product-img">
                        <p class="product-title">{{item.title}}</p>
                      </a>
                    </div>
                    <a 
                      :href="getTaobaoSearchLink('皮质剑桥包 文艺 女')" 
                      target="_blank" 
                      class="more-btn"
                    >
                      查看更多 →
                    </a>
                  </div>
                </div>
              </div>

              <div class="scenario-reasons">
                <div class="reason">
                  <strong>理由 1：</strong>浅卡其亚麻西装弱化正式感，增添文艺气质，宽松版型适配人物柔美风格且修饰身形；乐福鞋优雅显腿直，适配书店 "轻正式" 氛围，同时满足长时间站立试读的舒适需求。
                </div>
                <div class="reason">
                  <strong>理由 2：</strong>亚麻材质透气适合室内环境，剑桥包能装书籍笔记本，整体造型 "文艺轻熟"，与书店安静知性的氛围感呼应，碎花裙的柔美又为书店场景注入灵动活力。
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 重新分析按钮 -->
      <div class="report-actions">
        <button class="restart-button" @click="$emit('restart')">
          <i class="fas fa-redo"></i>
          重新分析
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AnalysisResult',
  props: {
    uploadedImage: {
      type: String,
      required: true
    }
  },
  emits: ['restart'],
  methods: {
    /**
     * 生成淘宝搜索链接（编码中文关键词）
     * @param {String} keyword - 搜索关键词
     * @returns {String} 淘宝搜索URL
     */
    getTaobaoSearchLink(keyword) {
      const encodedKeyword = encodeURIComponent(keyword);
      return `https://s.taobao.com/search?q=${encodedKeyword}&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306`;
    },

    /**
     * 模拟淘宝商品数据（实际项目可替换为接口请求）
     * @param {String} keyword - 商品关键词
     * @returns {Array} 3个商品模拟数据
     */
    getTaobaoProducts(keyword) {
      // 模拟商品图（使用picsum随机图，实际项目替换为接口返回的商品图）
      const randomImgId = Math.floor(Math.random() * 1000);
      return [
        {
          title: `精选${keyword} 热销款`,
          img: `https://picsum.photos/id/${randomImgId + 10}/200/200`,
          link: this.getTaobaoSearchLink(`${keyword} 热销`)
        },
        {
          title: `显瘦${keyword} 小众设计`,
          img: `https://picsum.photos/id/${randomImgId + 20}/200/200`,
          link: this.getTaobaoSearchLink(`${keyword} 小众设计`)
        },
        {
          title: `百搭${keyword} 高性价比`,
          img: `https://picsum.photos/id/${randomImgId + 30}/200/200`,
          link: this.getTaobaoSearchLink(`${keyword} 高性价比`)
        }
      ];
    }
  }
}
</script>

<style lang="scss" scoped>
.analysis-result-container {
  display: flex;
  gap: 32px; /* 左右区域间距 */
  align-items: flex-start;
  width: 95%;
  max-width: 1800px;
  margin: 40px auto 0 auto;
  padding: 0 24px;
  box-sizing: border-box; /* 确保padding不影响整体宽度 */
}

.left-sidebar {
  flex: 0 0 350px; /* 固定宽度，不随页面伸缩 */
  display: flex;
  flex-direction: column; /* 图片在上，信息在下 */
  gap: 24px; /* 内部元素间距 */
  width: 100%; /* 确保占满分配的宽度 */
  position: sticky;
  top: 20px; /* 可根据需求调整与顶部的距离 */
  align-self: flex-start; /* 确保粘性定位生效（父容器需为flex布局） */
}
.image-display-panel,
.key-info-panel {
  background: var(--color-bg-card, #ffffff);
  border-radius: var(--radius-xl, 16px);
  padding: var(--spacing-lg, 24px);
  border: 1px solid var(--color-border, #e5e7eb);
  box-shadow: var(--shadow-card, 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.03));
  transition: transform 0.3s ease, box-shadow 0.3s ease, opacity 0.3s ease;
  will-change: transform, box-shadow; /* 优化动画性能 */
  break-inside: avoid; /* 防止分页截断 */
  
  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
  }
}

/* 图片面板特殊优化 */
.image-display-panel {
  /* 确保图片容器在滚动时保持稳定 */
  min-height: 200px;
  display: flex;
  flex-direction: column;
  
  .uploaded-image-preview {
    width: 100%;
    border-radius: var(--radius-lg, 12px);
    object-fit: cover;
    transition: transform 0.4s ease, box-shadow 0.3s ease;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    
    &:hover {
      transform: scale(1.02);
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
  }
}

/* 滚动时的渐入效果 */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.image-display-panel,
.key-info-panel {
  animation: fadeInUp 0.5s ease forwards;
  opacity: 0;
}

.image-display-panel {
  animation-delay: 0.1s;
}

.key-info-panel {
  animation-delay: 0.2s;
}

/* 响应式调整 */
@media (max-width: 1200px) {
  .left-sidebar {
    position: static;
    max-height: none;
    overflow-y: visible;
    width: 100%;
    flex-direction: row;
    padding-right: 0;
  }
  
  .image-display-panel,
  .key-info-panel {
    animation: none;
    opacity: 1;
  }
}

@media (max-width: 768px) {
  .left-sidebar {
    flex-direction: column;
  }
}


.uploaded-image-preview {
  width: 100%;
  border-radius: var(--radius-lg, 12px);
  object-fit: cover;
  transition: transform 0.4s ease;
  
  &:hover {
    transform: scale(1.03);
  }
}

.info-title {
  color: var(--color-text-primary, #1a1a1a);
  font-size: var(--font-size-lg, 18px);
  font-weight: var(--font-weight-semibold, 600);
  margin: 0 0 var(--spacing-md, 16px) 0;
  padding-bottom: var(--spacing-sm, 8px);
  border-bottom: 2px solid var(--color-accent, #3b82f6);
  display: inline-block;
}

.info-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--spacing-sm, 8px);
  padding: var(--spacing-xs, 4px) 0;
  border-bottom: 1px dashed var(--color-border-light, #f0f0f0);
  
  &:last-child {
    margin-bottom: 0;
    border-bottom: none;
  }
}

.info-label {
  color: var(--color-text-secondary, #666666);
  font-size: var(--font-size-sm, 14px);
}

.info-value {
  color: var(--color-text-primary, #1a1a1a);
  font-size: var(--font-size-sm, 14px);
  font-weight: var(--font-weight-medium, 500);
}

.analysis-report {
  flex: 1;
  background: var(--color-bg-card, #ffffff);
  border-radius: var(--radius-xl, 16px);
  padding: var(--spacing-2xl, 48px);
  border: 1px solid var(--color-border, #e5e7eb);
  box-shadow: var(--shadow-card, 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.03));

  .report-header {
    text-align: center;
    margin-bottom: var(--spacing-2xl, 48px);
    padding-bottom: var(--spacing-xl, 32px);
    position: relative;
    
    &::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 80px;
      height: 3px;
      background: var(--gradient-accent, linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%));
      border-radius: 3px;
    }

    .report-title {
      font-size: var(--font-size-3xl, 30px);
      font-weight: var(--font-weight-bold, 700);
      color: var(--color-text-primary, #1a1a1a);
      margin: 0 0 var(--spacing-sm, 8px) 0;
      background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
      display: inline-block;
      position: relative;
      
      &::after {
        content: '';
        position: absolute;
        bottom: 5px;
        left: 0;
        width: 100%;
        height: 10px;
        background: rgba(59, 130, 246, 0.1);
        z-index: -1;
        transform: skew(-12deg) rotate(-1deg);
      }
    }

    .report-subtitle {
      font-size: var(--font-size-sm, 14px);
      color: var(--color-text-secondary, #666666);
      letter-spacing: 0.5px;
    }
  }

  .report-section {
    margin-bottom: var(--spacing-3xl, 64px);
    position: relative;
    padding-top: var(--spacing-sm, 8px);

    .section-header {
      display: flex;
      align-items: center;
      margin-bottom: var(--spacing-xl, 32px);
      padding-bottom: var(--spacing-md, 16px);
      border-bottom: 1px solid var(--color-border-light, #f3f4f6);
      position: relative;
      
      &::after {
        content: '';
        position: absolute;
        bottom: -1px;
        left: 0;
        width: 60px;
        height: 2px;
        background: var(--gradient-accent, linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%));
      }

      .section-icon {
        font-size: var(--font-size-2xl, 24px);
        margin-right: var(--spacing-md, 16px);
        width: 36px;
        height: 36px;
        text-align: center;
        line-height: 36px;
        background: rgba(59, 130, 246, 0.1);
        border-radius: 50%;
        color: var(--color-accent, #3b82f6);
      }

      .section-title {
        font-size: var(--font-size-2xl, 24px);
        font-weight: var(--font-weight-bold, 700);
        color: var(--color-text-primary, #1a1a1a);
        margin: 0;
        letter-spacing: -0.5px;
      }
    }

    .section-content {
      font-size: var(--font-size-xl, 20px);
      line-height: 1.8;
      color: var(--color-text-secondary, #666666);
      padding-left: var(--spacing-sm, 8px);

      p {
        margin: 0 0 var(--spacing-md, 16px) 0;
        transition: color 0.2s ease;
        
        &:hover {
          color: var(--color-text-primary, #333);
        }
      }

      strong {
        color: var(--color-text-primary, #1a1a1a);
        font-weight: var(--font-weight-semibold, 600);
        position: relative;
        padding: 0 3px;
        
        &::after {
          content: '';
          position: absolute;
          bottom: 0;
          left: 0;
          width: 100%;
          height: 3px;
          background: rgba(59, 130, 246, 0.2);
          z-index: -1;
        }
      }
    }

    .scenario-recommendations {
      display: flex;
      flex-direction: column;
      gap: var(--spacing-3xl, 64px);
    }

    .scenario-item {
      padding: var(--spacing-xl, 32px);
      background: var(--color-bg-light, #f9fafb);
      border-radius: var(--radius-xl, 16px);
      border: 1px solid var(--color-border, #e5e7eb);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      
      &:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.03);
      }
    }

    .scenario-header h4 {
      font-size: var(--font-size-xl, 22px);
      font-weight: var(--font-weight-semibold, 600);
      color: var(--color-text-primary, #1a1a1a);
      margin: 0 0 var(--spacing-md, 16px) 0;
      display: inline-block;
      position: relative;
      
      &::after {
        content: '';
        position: absolute;
        bottom: -5px;
        left: 0;
        width: 40px;
        height: 2px;
        background: var(--color-accent, #3b82f6);
        border-radius: 2px;
      }
    }

    .scenario-outfit {
      display: block;
      font-size: var(--font-size-xl, 20px);
      margin-bottom: var(--spacing-lg, 24px);
      color: var(--color-text-primary, #1a1a1a);
    }

    .scenario-reasons {
      padding-left: var(--spacing-sm, 8px);
    }

    .reason {
      margin-bottom: var(--spacing-md, 16px);
    }

    .reason:last-child {
      margin-bottom: 0;
    }
  }

  /* 服装卡片样式优化 */
  .clothing-card {
    width: 100%;
    background: var(--color-bg-light, #f9fafb);
    border-radius: var(--radius-lg, 12px);
    border: 1px solid var(--color-border, #e5e7eb);
    padding: var(--spacing-md, 16px);
    margin-bottom: var(--spacing-lg, 24px);
    box-sizing: border-box;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
    
    &::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: var(--gradient-accent, linear-gradient(180deg, #3b82f6 0%, #1d4ed8 100%));
      opacity: 0;
      transition: opacity 0.3s ease;
    }
    
    &:hover {
      transform: translateY(-3px);
      box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.03);
      
      &::before {
        opacity: 1;
      }
    }
  }

  .clothing-name {
    font-size: var(--font-size-lg, 18px);
    color: var(--color-text-primary, #1a1a1a);
    margin-bottom: var(--spacing-sm, 8px);
    padding-bottom: var(--spacing-sm, 8px);
    border-bottom: 1px dashed var(--color-border-light, #f3f4f6);
    font-weight: 500;
  }

  /* 商品推荐区样式优化 */
  .product-recommend {
    display: flex;
    align-items: center;
    gap: var(--spacing-md, 16px);
    margin-top: var(--spacing-sm, 8px);
  }

  .product-list {
    flex: 1;
    display: flex;
    gap: var(--spacing-md, 16px);
    overflow-x: auto;
    padding-bottom: var(--spacing-sm, 8px);
    scrollbar-width: thin;
    scrollbar-color: var(--color-accent-light, rgba(59, 130, 246, 0.3)) transparent;
    
    &::-webkit-scrollbar {
      height: 6px;
    }
    
    &::-webkit-scrollbar-track {
      background: transparent;
    }
    
    &::-webkit-scrollbar-thumb {
      background-color: var(--color-accent-light, rgba(59, 130, 246, 0.3));
      border-radius: 3px;
    }
  }

  .product-item {
    flex: 0 0 120px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-decoration: none;
    gap: var(--spacing-xs, 4px);
    position: relative;
    transition: transform 0.3s ease;
    
    &:hover {
      transform: translateY(-5px) scale(1.02);
    }
    
    &::after {
      content: '查看商品';
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%) scale(0.8);
      background: rgba(59, 130, 246, 0.9);
      color: white;
      width: 90%;
      height: 90%;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: var(--radius-sm, 8px);
      font-size: 12px;
      opacity: 0;
      transition: all 0.3s ease;
    }
    
    &:hover::after {
      opacity: 1;
      transform: translate(-50%, -50%) scale(1);
    }
  }

  .product-img {
    width: 100%;
    height: 120px;
    object-fit: cover;
    border-radius: var(--radius-sm, 8px);
    border: 1px solid var(--color-border-light, #f3f4f6);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  }

  .product-title {
    font-size: var(--font-size-xs, 12px);
    color: var(--color-text-primary, #1a1a1a);
    text-align: center;
    line-height: 1.4;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    padding: 0 4px;
  }

  /* 查看更多按钮样式优化 */
  .more-btn {
    flex: 0 0 auto;
    padding: var(--spacing-xs, 4px) var(--spacing-md, 16px);
    background: var(--gradient-accent, linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%));
    color: white;
    border-radius: var(--radius-full, 999px);
    font-size: var(--font-size-sm, 14px);
    font-weight: var(--font-weight-medium, 500);
    text-decoration: none;
    white-space: nowrap;
    transition: all 0.3s ease;
    box-shadow: 0 2px 5px rgba(59, 130, 246, 0.2);
    position: relative;
    overflow: hidden;
    
    &::before {
      content: '';
      position: absolute;
      top: 0;
      left: -100%;
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
      transition: all 0.5s ease;
    }
    
    &:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 8px rgba(59, 130, 246, 0.3);
      
      &::before {
        left: 100%;
      }
    }
  }

  .clothing-items p {
    margin-bottom: var(--spacing-sm, 8px);
  }

  .style-analysis .style-item {
    margin-bottom: var(--spacing-lg, 24px);
    padding: var(--spacing-md, 16px);
    border-radius: var(--radius-lg, 12px);
    background: var(--color-bg-light, #f9fafb);
    transition: transform 0.3s ease;
    
    &:hover {
      transform: translateX(5px);
    }
    
    h4 {
      font-size: var(--font-size-lg, 18px);
      font-weight: var(--font-weight-semibold, 600);
      color: var(--color-accent, #3b82f6);
      margin: 0 0 var(--spacing-sm, 8px) 0;
      display: flex;
      align-items: center;
      
      &::before {
        content: '•';
        margin-right: 8px;
        font-size: 20px;
      }
    }
    
    p {
      color: var(--color-text-secondary, #666666);
    }
  }

  .styling-tips .tip-item {
    margin-bottom: var(--spacing-md, 16px);
    padding: var(--spacing-md, 16px);
    padding-left: var(--spacing-xl, 32px);
    position: relative;
    border-radius: var(--radius-lg, 12px);
    background: var(--color-bg-light, #f9fafb);
    transition: all 0.3s ease;
    
    &:hover {
      background: rgba(59, 130, 246, 0.03);
      transform: translateX(3px);
    }
    
    &::before {
      content: '💡';
      position: absolute;
      left: var(--spacing-md, 16px);
      top: 50%;
      transform: translateY(-50%);
      font-size: var(--font-size-lg, 18px);
    }
  }

  .occasions {
    display: flex;
    flex-wrap: wrap;
    gap: var(--spacing-sm, 12px);
    
    .occasion-item {
      background: var(--color-accent-light, rgba(59, 130, 246, 0.1));
      color: var(--color-accent, #3b82f6);
      padding: var(--spacing-sm, 8px) var(--spacing-md, 16px);
      border-radius: var(--radius-2xl, 24px);
      font-size: var(--font-size-sm, 14px);
      font-weight: var(--font-weight-medium, 500);
      border: 1px solid transparent;
      transition: all 0.3s ease;
      cursor: default;
      
      &:hover {
        background: var(--color-accent, #3b82f6);
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.2);
      }
    }
  }

  .scenario-recommendations .scenario-item {
    margin-bottom: var(--spacing-lg, 24px);
    
    h4 {
      font-size: var(--font-size-xl, 20px);
      font-weight: var(--font-weight-semibold, 600);
      color: var(--color-accent, #3b82f6);
      margin: 0 0 var(--spacing-md, 16px) 0;
      display: inline-block;
    }
  }

  .outfit-details p {
    font-size: var(--font-size-lg, 18px);
    margin-bottom: var(--spacing-sm, 8px);
  }

  .scenario-reasons .reason {
    margin-bottom: var(--spacing-sm, 16px);
    padding: var(--spacing-sm, 8px) var(--spacing-md, 16px);
    padding-left: var(--spacing-xl, 32px);
    position: relative;
    font-size: var(--font-size-base, 16px);
    border-radius: var(--radius-md, 8px);
    transition: background 0.3s ease;
    
    &:hover {
      background: rgba(59, 130, 246, 0.03);
    }
    
    &::before {
      content: '✓';
      position: absolute;
      left: var(--spacing-md, 16px);
      top: 50%;
      transform: translateY(-50%);
      color: var(--color-accent, #3b82f6);
      font-weight: bold;
      background: rgba(59, 130, 246, 0.1);
      width: 20px;
      height: 20px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
    }
  }

  .report-actions {
    text-align: center;
    margin-top: var(--spacing-xl, 32px);
    padding-top: var(--spacing-xl, 32px);
    border-top: 1px solid var(--color-border, #e5e7eb);

    .restart-button {
      background: var(--gradient-accent, linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%));
      color: white;
      border: none;
      padding: var(--spacing-md, 16px) var(--spacing-xl, 32px);
      border-radius: var(--radius-2xl, 24px);
      font-size: var(--font-size-base, 16px);
      font-weight: var(--font-weight-medium, 500);
      cursor: pointer;
      transition: all 0.3s ease;
      display: inline-flex;
      align-items: center;
      gap: var(--spacing-sm, 8px);
      box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.2);
      position: relative;
      overflow: hidden;
      
      &::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: all 0.5s ease;
      }
      
      &:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.3);
        
        &::before {
          left: 100%;
        }
      }
      
      &:active {
        transform: translateY(-1px);
      }

      i {
        font-size: var(--font-size-sm, 14px);
      }
    }
  }
}

@media (max-width: 1200px) {
  .analysis-result-container {
    flex-direction: column;
    gap: 24px;
    padding: 0 20px;
  }

  .left-sidebar {
    position: static;
    width: 100%;
    max-width: 600px;
    height: auto;
    flex-direction: row;
    gap: 20px;
    margin: 0 auto;
  }

  .image-display-panel {
    flex: 1;
    min-width: 280px;
  }

  .key-info-panel {
    flex: 0 0 280px;
  }

  .analysis-report {
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
  }

  .product-recommend {
    flex-direction: column;
    align-items: flex-start;
  }

  .more-btn {
    align-self: flex-end;
    margin-top: var(--spacing-sm, 8px);
    padding: 6px 20px;
  }
}

@media (max-width: 768px) {
  .left-sidebar {
    flex-direction: column;
    gap: 16px;
  }

  .image-display-panel,
  .key-info-panel {
    flex: none;
    width: 100%;
  }

  .analysis-report {
    padding: 24px 16px;
    
    .report-header .report-title {
      font-size: 24px;
    }
    
    .report-section .section-header {
      .section-title {
        font-size: 20px;
      }
    }
    
    .scenario-recommendations .scenario-item {
      padding: 20px 16px;
    }

    .product-item {
      flex: 0 0 100px;
    }

    .product-img {
      height: 100px;
    }
  }
}

@media (max-width: 480px) {
  .analysis-report {
    padding: 20px 12px;
    
    .report-header .report-title {
      font-size: 22px;
    }
    
    .report-section .section-header {
      flex-direction: column;
      align-items: flex-start;
      gap: 10px;
      
      .section-icon {
        margin-right: 0;
      }
      
      .section-title {
        font-size: 18px;
      }
    }
    
    .occasions {
      flex-direction: column;
      gap: 10px;
    }
    
    .scenario-recommendations .scenario-item {
      padding: 16px 12px;
    }

    .product-item {
      flex: 0 0 80px;
    }

    .product-img {
      height: 80px;
    }

    .product-title {
      font-size: var(--font-size-xs, 10px);
    }

    .section-content {
      font-size: var(--font-size-base, 16px) !important;
    }
  }
}

</style>