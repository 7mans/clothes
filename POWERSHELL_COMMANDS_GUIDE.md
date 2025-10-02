# PowerShell 命令修复指南

## 问题原因

PowerShell 不支持 `&&` 操作符（这是 bash/cmd 语法）。在 PowerShell 中需要使用分号 `;` 来分隔命令。

## 正确的 PowerShell 命令语法

### 启动后端服务器

```powershell
# 方法1: 分步执行
cd C:\Users\30780\Desktop\clothes\ai2cloth\backend
python working_server.py

# 方法2: 使用分号分隔
cd C:\Users\30780\Desktop\clothes\ai2cloth\backend; python working_server.py

# 方法3: 使用 uvicorn 启动原始服务器
cd C:\Users\30780\Desktop\clothes\ai2cloth\backend; python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 测试服务器连接

```powershell
# 测试健康检查端点
Invoke-WebRequest -Uri "http://localhost:8000/health" -Method GET

# 测试注册端点
$body = @{
    email = "test@example.com"
    password = "test123456"
    phone = "13800138000"
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:8000/api/v1/auth/register" -Method POST -Body $body -ContentType "application/json"
```

## 推荐解决方案

由于网络连接问题，建议直接使用前端的 Mock 模式：

### 1. 启动前端服务器

```powershell
cd C:\Users\30780\Desktop\clothes\ai2cloth\frontend
npm run serve
```

### 2. 在浏览器中启用 Mock 模式

打开 http://localhost:8080，然后在浏览器控制台执行：

```javascript
window.mockModeHelper.enableMockMode();
```

### 3. 测试登录注册功能

现在可以正常使用登录注册功能，数据会保存在浏览器本地存储中。

## 如果需要真实后端服务器

### 方法 1: 使用简化服务器

```powershell
cd C:\Users\30780\Desktop\clothes\ai2cloth\backend
python working_server.py
```

### 方法 2: 使用原始 FastAPI 服务器

```powershell
cd C:\Users\30780\Desktop\clothes\ai2cloth\backend
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 方法 3: 检查并修复网络问题

```powershell
# 检查端口占用
netstat -ano | findstr :8000

# 测试端口可用性
Test-NetConnection -ComputerName localhost -Port 8000

# 检查防火墙设置
Get-NetFirewallRule | Where-Object {$_.DisplayName -like "*Python*"}
```

