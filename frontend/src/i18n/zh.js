export default {
  // Header
  header: {
    home: '首页',
    analysis: '开始分析',
    shop: '商店',
    pricing: '定价',
    login: '登录',
    register: '注册'
  },
  
  // Hero Section
  hero: {
    title: 'AI驱动的时尚分析平台',
    subtitle: '上传服装图片，获得专业的时尚分析报告。AI为您解析风格、推荐搭配，发现时尚灵感。',
    startJourney: '开始时尚之旅吧',
    actionSubtitle: '探索AI驱动的时尚分析体验'
  },
  
  // How It Works Section
  howItWorks: {
    title: '如何使用',
    subtitle: '三个简单步骤，获得专业时尚分析',
    steps: {
      upload: {
        title: '上传图片',
        description: '选择或拖拽服装图片到上传区域'
      },
      analyze: {
        title: 'AI分析',
        description: '先进的AI模型分析服装风格和特征'
      },
      report: {
        title: '获得报告',
        description: '查看详细的时尚分析和搭配建议'
      }
    }
  },
  
  // Features Section
  features: {
    title: '强大功能',
    subtitle: 'AI技术驱动的专业时尚分析',
    items: {
      recognition: {
        title: '智能识别',
        description: '精准识别服装类型、颜色、材质等特征'
      },
      styleAnalysis: {
        title: '风格分析',
        description: '专业的时尚风格定位和趋势分析'
      },
      suggestions: {
        title: '搭配建议',
        description: '个性化的搭配推荐和造型建议'
      },
      shopping: {
        title: '购物推荐',
        description: '智能推荐相似单品和购买链接'
      }
    }
  },
  
  // FAQ Section
  faq: {
    title: '常见问题',
    subtitle: '您想知道的，我们都已为您解答',
    items: {
      howItWorks: {
        question: 'AI2Cloth 是如何工作的？',
        answer: '您只需上传一张服装图片，我们的AI模型就会对它进行全面分析，包括风格、颜色、材质和场合。然后，我们会为您生成一份详细的报告和个性化的搭配建议。'
      },
      formats: {
        question: '支持哪些图片格式？',
        answer: '我们支持常见的图片格式，如 JPG、PNG 和 WEBP。为获得最佳分析效果，请确保图片清晰，服装主体突出。'
      },
      time: {
        question: '分析需要多长时间？',
        answer: '通常情况下，AI分析过程只需要几秒钟。在高峰时段或处理高分辨率图片时，可能需要稍长一些时间。'
      },
      security: {
        question: '我的上传数据安全吗？',
        answer: '我们非常重视您的隐私安全。您上传的图片仅用于本次分析，我们不会存储或将其用于其他目的。所有数据传输都经过加密处理。'
      }
    }
  },
  
  // Analysis Page
  analysis: {
    title: 'AI 服装分析',
    subtitle: '上传一张服装图片，让AI为您提供专业的时尚分析',
    backToHome: '返回首页',
    upload: {
      title: '点击或拖拽上传图片',
      subtitle: '支持 JPG、PNG、WEBP 格式，最大 10MB'
    },
    analyzing: {
      title: 'AI正在分析中...',
      subtitle: '正在识别服装特征...'
    },
    startAnalysis: '开始分析',
    errors: {
      invalidFile: '请上传图片文件',
      fileTooLarge: '图片大小不能超过10MB',
      analysisFailed: '分析失败，请重试'
    }
  }
}
