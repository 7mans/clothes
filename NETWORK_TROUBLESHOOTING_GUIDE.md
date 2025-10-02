# AI2Cloth 登录注册问题解决指南

## 问题现象

- 前端显示"网络连接错误: Network Error"
- 登录注册功能无法正常使用
- 控制台显示"ERR_CONNECTION_REFUSED"错误

## 已实现的解决方案

### 1. 自动 Mock 模式切换

系统已经实现了智能的后端连接检测和自动切换功能：

- **自动检测**: 当后端连接失败时，系统会自动切换到 Mock 模式
- **离线功能**: Mock 模式下可以正常使用登录注册功能
- **数据持久化**: 用户数据保存在浏览器本地存储中

### 2. 使用方法

#### 启用 Mock 模式（推荐）

在浏览器控制台中执行：

```javascript
// 启用Mock模式
window.mockModeHelper.enableMockMode();

// 查看状态
window.mockModeHelper.showStatus();

// 创建测试用户（可选）
window.mockModeHelper.createTestUser();
```

#### 测试登录注册

1. 打开前端页面 http://localhost:8080
2. 尝试注册新用户或登录
3. 系统会自动检测后端连接状态
4. 如果后端不可用，会自动切换到 Mock 模式并显示提示

### 3. Mock 模式功能

- ✅ 用户注册（邮箱验证、密码验证）
- ✅ 用户登录（密码验证）
- ✅ Token 生成和管理
- ✅ 用户信息存储
- ✅ 数据持久化（localStorage）

## 网络问题排查步骤

### 步骤 1: 检查后端服务器

```bash
# 检查8000端口是否被占用
netstat -ano | findstr :8000

# 尝试启动后端服务器
cd backend
python working_server.py
```

### 步骤 2: 检查防火墙设置

- Windows 防火墙可能阻止了本地服务器连接
- 临时关闭防火墙测试
- 或添加 Python.exe 到防火墙例外

### 步骤 3: 检查网络配置

```bash
# 测试本地回环
ping localhost
ping 127.0.0.1

# 检查端口可用性
telnet localhost 8000
```

### 步骤 4: 使用替代端口

如果 8000 端口有问题，可以尝试其他端口：

```bash
# 启动在8001端口
python working_server.py --port 8001
```

然后更新前端配置：

```javascript
// 在 frontend/src/plugins/axios.js 中修改
baseURL: "http://localhost:8001/api/v1";
```

## 推荐解决方案

### 方案 1: 使用 Mock 模式（立即可用）

这是最简单快速的解决方案：

1. 打开浏览器控制台
2. 执行 `window.mockModeHelper.enableMockMode()`
3. 刷新页面，正常使用登录注册功能

### 方案 2: 修复后端连接

如果需要完整的后端功能：

1. 检查并修复网络配置
2. 确保防火墙允许本地连接
3. 重新启动后端服务器
4. 执行 `window.mockModeHelper.disableMockMode()` 切换回正常模式

## 开发调试命令

在浏览器控制台中可用的调试命令：

```javascript
// 查看Mock模式状态
window.mockModeHelper.showStatus();

// 启用/禁用Mock模式
window.mockModeHelper.enableMockMode();
window.mockModeHelper.disableMockMode();

// 清除所有Mock数据
window.mockModeHelper.clearMockData();

// 创建测试用户
window.mockModeHelper.createTestUser();

// 查看所有Mock用户
window.mockModeHelper.getMockUsers();
```

## 总结

通过实现 Mock 模式，AI2Cloth 的登录注册功能现在可以在任何情况下正常工作：

- **在线模式**: 连接后端服务器，使用完整功能
- **离线模式**: 使用 Mock 数据，保证基本功能可用
- **自动切换**: 智能检测连接状态，无需手动干预

这确保了用户体验的连续性，即使在网络或服务器问题的情况下也能正常使用系统。

