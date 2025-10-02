#!/usr/bin/env python3
"""
测试AI2Cloth认证系统的完整功能
包括注册、登录、token验证、过期处理等
"""
import requests
import json
import time
from datetime import datetime

BASE_URL = "http://localhost:8010/api/v1"

def test_register():
    """测试用户注册"""
    print("=== 测试用户注册 ===")
    
    register_data = {
        "email": "test@example.com",
        "password": "test123456",
        "phone": "13800138000"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/auth/register", json=register_data)
        print(f"注册响应状态码: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("注册成功!")
            print(f"Token: {data['access_token'][:50]}...")
            print(f"用户信息: {data['user']['username']} ({data['user']['email']})")
            return data['access_token']
        else:
            print(f"注册失败: {response.text}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("连接失败: 后端服务器未运行或端口不正确")
        return None
    except Exception as e:
        print(f"注册异常: {e}")
        return None

def test_login():
    """测试用户登录"""
    print("\n=== 测试用户登录 ===")
    
    login_data = {
        "email": "test@example.com",
        "password": "test123456"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
        print(f"登录响应状态码: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("登录成功!")
            print(f"Token: {data['access_token'][:50]}...")
            print(f"用户信息: {data['user']['username']} ({data['user']['email']})")
            return data['access_token']
        else:
            print(f"登录失败: {response.text}")
            return None
            
    except Exception as e:
        print(f"登录异常: {e}")
        return None

def test_protected_endpoint(token):
    """测试受保护的端点"""
    print("\n=== 测试受保护端点 ===")
    
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.get(f"{BASE_URL}/users/profile", headers=headers)
        print(f"获取用户信息响应状态码: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("获取用户信息成功!")
            print(f"用户: {data['username']} ({data['email']})")
            print(f"钻石数量: {data['diamonds']}")
            return True
        elif response.status_code == 401:
            print("Token无效或已过期 (401)")
            return False
        elif response.status_code == 403:
            print("Token已过期，需要重新登录 (403)")
            return False
        else:
            print(f"请求失败: {response.text}")
            return False
            
    except Exception as e:
        print(f"请求异常: {e}")
        return False

def test_logout(token):
    """测试用户登出"""
    print("\n=== 测试用户登出 ===")
    
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.post(f"{BASE_URL}/auth/logout", headers=headers)
        print(f"登出响应状态码: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("登出成功!")
            print(f"消息: {data['message']}")
            return True
        else:
            print(f"登出失败: {response.text}")
            return False
            
    except Exception as e:
        print(f"登出异常: {e}")
        return False

def test_token_after_logout(token):
    """测试登出后token是否失效"""
    print("\n=== 测试登出后token状态 ===")
    
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.get(f"{BASE_URL}/users/profile", headers=headers)
        print(f"使用已登出token请求状态码: {response.status_code}")
        
        if response.status_code == 401:
            print("✓ Token已失效，认证系统工作正常")
            return True
        else:
            print("✗ Token仍然有效，认证系统存在问题")
            return False
            
    except Exception as e:
        print(f"请求异常: {e}")
        return False

def main():
    """主测试函数"""
    print("AI2Cloth 认证系统测试")
    print("=" * 50)
    
    # 测试注册
    token = test_register()
    if not token:
        print("注册失败，尝试登录...")
        token = test_login()
    
    if not token:
        print("无法获取有效token，测试终止")
        return
    
    # 测试受保护端点
    if test_protected_endpoint(token):
        print("✓ Token验证正常")
    else:
        print("✗ Token验证失败")
        return
    
    # 测试登出
    if test_logout(token):
        print("✓ 登出功能正常")
    else:
        print("✗ 登出功能异常")
        return
    
    # 测试登出后token状态
    test_token_after_logout(token)
    
    print("\n" + "=" * 50)
    print("认证系统测试完成!")

if __name__ == "__main__":
    main()

