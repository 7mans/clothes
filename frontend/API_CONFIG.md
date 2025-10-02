# 火山引擎豆包大模型 API 配置指南

本文档旨在帮助您快速配置和使用火山引擎豆包大模型 API，以便在本项目中启用真实的图片分析功能。

## 1. 获取 API 密钥

您需要拥有一个火山引擎账号，并开通豆包大模型服务。请按照以下步骤获取 API 密钥：

1.  **登录火山引擎控制台**: [https://console.volcengine.com/](https://console.volcengine.com/)
2.  **访问密钥管理**: 在右上角的用户菜单中，找到并点击“密钥管理”（或访问“访问控制” -> “身份管理” -> “用户” -> “管理 API 密钥”）。
3.  **创建主账号密钥**: 如果您还没有密钥，请创建一个新的 Access Key。请务必妥善保管您的 `Access Key ID` 和 `Secret Access Key`，后者只在创建时显示一次。

## 2. 获取模型 Endpoint ID

您需要创建一个模型发布，并获取其 Endpoint ID：

1.  **进入豆包大模型控制台**: 在产品服务中搜索“豆包大模型”。
2.  **模型广场**: 选择您需要的视觉模型（例如 `doubao-pro-4k`）。
3.  **创建模型发布**: 将模型发布为在线服务，并为其设置一个易于识别的名称。
4.  **获取 Endpoint ID**: 在模型发布成功后，您将获得一个格式为 `ep-xxxxxxxxxxxx-xxxxx` 的 Endpoint ID。请复制此 ID。

## 3. 配置环境变量

为了在前端项目中使用 API，您需要在项目根目录下创建一个名为 `.env.local` 的文件，并填入您的密钥和模型 ID。

1.  **创建文件**: 在 `frontend` 文件夹的同级目录下（即项目根目录）创建 `.env.local` 文件。

2.  **添加配置**: 在文件中添加以下内容，并将占位符替换为您的真实信息：

    ```
    # .env.local

    # 火山引擎 Access Key ID
    VUE_APP_VOLCENGINE_ACCESS_KEY_ID=YOUR_ACCESS_KEY_ID

    # 火山引擎 Secret Access Key
    VUE_APP_VOLCENGINE_SECRET_ACCESS_KEY=YOUR_SECRET_ACCESS_KEY
    ```

3.  **更新服务文件**: 打开 `frontend/src/services/volcengineApi.js` 文件，将 `MODEL_NAME` 常量的值替换为您的模型 Endpoint ID：

    ```javascript
    // frontend/src/services/volcengineApi.js

    // ...
    const MODEL_NAME = "ep-xxxxxxxxxxxx-xxxxx"; // <--- 请将这里替换为您的模型Endpoint ID
    // ...
    ```

## 4. 重启开发服务器

在修改或创建 `.env.local` 文件后，您需要**重新启动 Vue 的开发服务器**（通常是 `npm run serve`），以使环境变量生效。

完成以上步骤后，您的应用将能够调用火山引擎 API 进行真实的图片分析。如果 API 未配置或调用失败，应用将自动回退到使用模拟数据。
