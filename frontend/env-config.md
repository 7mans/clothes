# 环境变量配置说明

## 火山引擎 API 配置

为了使用火山引擎豆包大模型 API，您需要创建环境变量配置文件：

### 1. 创建 `.env.local` 文件

在 `frontend` 目录下创建 `.env.local` 文件，内容如下：

```bash
# 火山引擎豆包大模型API配置
VUE_APP_ARK_API_KEY=your_actual_api_key_here

# 可选配置（如果需要自定义）
VUE_APP_ARK_BASE_URL=https://ark.cn-beijing.volces.com/api/v3
VUE_APP_MODEL_ENDPOINT_ID=your_model_endpoint_id
```

### 2. 获取 API 密钥

1. 访问火山引擎控制台
2. 进入豆包大模型服务
3. 创建 API 密钥
4. 将密钥替换上面的 `your_actual_api_key_here`

### 3. 重启开发服务器

配置完成后，重启前端开发服务器：

```bash
npm run serve
```

## 注意事项

- `.env.local` 文件不会被提交到版本控制
- API 密钥请妥善保管，不要泄露
- 在生产环境中建议通过后端代理 API 请求以保护密钥安全
