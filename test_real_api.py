#!/usr/bin/env python3
"""
测试真实的大模型API调用
"""
import asyncio
import sys
import os
sys.path.append('backend')

from app.services.doubao_vision_service import DoubaoVisionService

async def test_real_api():
    """测试真实的豆包API调用"""
    print("=== 测试真实大模型API调用 ===")
    
    # 创建豆包视觉服务实例
    doubao_service = DoubaoVisionService()
    
    # 检查凭证配置
    print("\n1. 检查API凭证配置:")
    has_credentials = doubao_service._check_credentials()
    print(f"凭证完整性: {'✅ 已配置' if has_credentials else '❌ 缺少配置'}")
    
    # 检查依赖包
    print("\n2. 检查依赖包:")
    try:
        import tos
        import volcenginesdkarkruntime
        print("✅ TOS SDK: 已安装")
        print("✅ Volcengine SDK: 已安装")
        deps_available = True
    except ImportError as e:
        print(f"❌ 依赖包缺失: {e}")
        deps_available = False
    
    # 测试API调用
    print("\n3. 测试API调用:")
    if has_credentials and deps_available:
        try:
            # 使用测试图片路径
            test_image = "test_image.jpg"
            result = await doubao_service.analyze_clothing_image(test_image)
            
            if result:
                print("✅ API调用成功")
                print(f"服装类型: {result.get('clothing_type')}")
                print(f"风格标签: {result.get('style_tags')}")
                print(f"颜色标签: {result.get('color_tags')}")
                print(f"分析内容长度: {len(result.get('detailed_analysis', ''))}")
            else:
                print("❌ API调用失败，返回空结果")
                
        except Exception as e:
            print(f"❌ API调用异常: {e}")
    else:
        print("⚠️  跳过API调用测试（缺少凭证或依赖）")
        
        # 测试模拟数据
        result = doubao_service._mock_analysis_result()
        print("✅ 模拟数据生成成功")
        print(f"模拟结果类型: {result.get('clothing_type')}")
    
    print("\n=== 测试完成 ===")

if __name__ == "__main__":
    asyncio.run(test_real_api())
