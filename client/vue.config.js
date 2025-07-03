module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000', // Django-сервер локально
        changeOrigin: true,
        pathRewrite: { '^/api': '/api' },
      },
    },
  },
  outputDir: 'dist', // это важно для продакшн-сборки
};
