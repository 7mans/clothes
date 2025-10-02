# AI2Cloth - 智能服饰推荐网站

![Logo](frontend/src/assets/logo.svg)

## 1. 项目简介

AI2Cloth 是一个基于人工智能的服饰推荐网站。用户可以上传服饰图片，系统会通过大模型 API 智能分析图片的风格、类型、颜色等标签，并基于这些信息从公共商品库中推荐相似或可搭配的商品。

**核心功能:**

- **用户系统**: 支持注册、登录，并为新用户赠送体验钻石。
- **AI 分析**: 上传图片，消耗钻石，获取详细的服饰分析报告。
- **商品推荐**: 根据 AI 分析结果，展示推荐的商品列表。
- **钻石商店**: 通过支付宝接口购买钻石，以使用更多分析服务。
- **历史记录**: 用户可以随时查看过去的分析历史和推荐结果。

---

## 2. 技术栈

- **前端**: Vue 2, Vue Router, Vuex, Element UI, Axios, SCSS
- **后端**: Python 3, FastAPI, SQLAlchemy, SQLite, Uvicorn
- **部署**: Nginx, Gunicorn (推荐)
- **测试**: Pytest (后端), Vue Test Utils & Jest (前端)

---

## 3. 项目结构

```
ai2cloth/
├── backend/                # FastAPI 后端项目
│   ├── app/                # 核心应用代码
│   ├── static/             # 静态文件（如上传的图片）
│   ├── tests/              # 后端测试
│   └── requirements.txt    # Python 依赖
├── frontend/               # Vue 前端项目
│   ├── src/                # 核心源代码
│   ├── public/
│   └── tests/              # 前端测试
├── nginx/                  # Nginx 生产环境配置
└── README.md               # 项目文档
```

---

## 4. 本地环境启动指南

### 环境要求

- Python 3.8+
- Node.js 14+
- Git

### 后端启动

1.  **进入后端目录**

    ```bash
    cd ai2cloth/backend
    ```

2.  **创建并激活虚拟环境**

    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    # venv\Scripts\activate    # Windows
    ```

3.  **安装依赖**

    ```bash
    pip install -r requirements.txt
    ```

4.  **启动 FastAPI 服务**

    ```bash
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    ```

    后端服务将在 `http://localhost:8000` 运行。
    API 文档地址: `http://localhost:8000/docs`

### 前端启动

1.  **进入前端目录** (在新的终端窗口中)

    ```bash
    cd ai2cloth/frontend
    ```

2.  **安装依赖**

    ```bash
    npm install
    ```

3.  **启动开发服务器**

    ```bash
    npm run serve
    ```

    前端开发服务器将在 `http://localhost:8080` 运行，并已配置好代理，可直接访问后端 API。

---

## 5. 测试

### 后端测试

```bash
cd ai2cloth/backend
pytest
```

### 前端单元测试

```bash
cd ai2cloth/frontend
npm run test:unit
```

---

## 6. 部署

生产环境部署建议使用 Gunicorn 运行 FastAPI 应用，并使用 Nginx 作为反向代理。

1.  **构建前端静态文件**

    ```bash
    cd ai2cloth/frontend
    npm run build
    ```

2.  **部署后端**
    使用 Gunicorn 启动后端服务，例如：

    ```bash
    gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker -b 127.0.0.1:8000
    ```

3.  **配置 Nginx**
    将 `nginx/default.conf` 文件复制到 Nginx 配置目录 (如 `/etc/nginx/conf.d/`)，并根据服务器实际情况修改文件路径和域名。

    确保将前端构建出的 `dist` 目录内容部署到 Nginx 配置的 `root` 路径下 (如 `/var/www/ai2cloth/frontend/dist`)。

4.  **重启 Nginx**
    ```bash
    sudo systemctl restart nginx
    ```
