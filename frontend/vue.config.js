/**
 * @description Vue CLI 配置文件
 */

module.exports = {
  transpileDependencies: [
    'openai'
  ],
  devServer: {
    port: 8080,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
      '/static': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      }
    }
  }
};
