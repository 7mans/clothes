#!/usr/bin/env python3
"""
测试后端服务器连接状态
"""
import requests
import time

def test_backend_connection():
    """测试后端服务器连接"""
    print("测试后端服务器连接...")
    
    try:
        # 测试健康检查端点
        response = requests.get("http://localhost:8000/health", timeout=5)
        print(f"健康检查响应: {response.status_code}")
        if response.status_code == 200:
            print("✓ 后端服务器运行正常")
            print(f"响应内容: {response.json()}")
            return True
        else:
            print(f"✗ 后端服务器响应异常: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("✗ 无法连接到后端服务器 (端口8000)")
        return False
    except Exception as e:
        print(f"✗ 连接测试异常: {e}")
        return False

def test_registration():
    """测试用户注册"""
    print("\n测试用户注册...")
    
    register_data = {
        "email": "test@example.com",
        "password": "test123456",
        "phone": "13800138000"
    }
    
    try:
        response = requests.post("http://localhost:8000/api/v1/auth/register", json=register_data, timeout=10)
        print(f"注册响应状态码: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("✓ 注册成功!")
            print(f"用户: {data['user']['username']} ({data['user']['email']})")
            return data['access_token']
        else:
            print(f"✗ 注册失败: {response.text}")
            return None
            
    except Exception as e:
        print(f"✗ 注册异常: {e}")
        return None

if __name__ == "__main__":
    print("AI2Cloth 后端连接测试")
    print("=" * 40)
    
    # 等待服务器启动
    print("等待后端服务器启动...")
    time.sleep(3)
    
    if test_backend_connection():
        token = test_registration()
        if token:
            print(f"\n✓ 完整测试成功! Token: {token[:50]}...")
        else:
            print("\n✗ 注册测试失败")
    else:
        print("\n✗ 后端服务器连接失败")

