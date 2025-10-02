#!/usr/bin/env python3
"""
测试基于Vue2项目重写的豆包API集成
"""
import asyncio
import sys
import os
sys.path.append('backend')

from app.services.doubao_direct_service import DoubaoDirectService
from app.services.ai_service import AIService

async def test_doubao_integration():
    """测试豆包API集成"""
    print("=== 测试豆包API集成（基于Vue2项目重写） ===")
    
    # 1. 测试直接调用服务
    print("\n1. 测试DoubaoDirectService:")
    doubao_direct = DoubaoDirectService()
    print(f"API Key: {'已配置' if doubao_direct.api_key else '未配置'}")
    print(f"Base URL: {doubao_direct.base_url}")
    print(f"Model ID: {doubao_direct.model_id}")
    
    # 2. 测试AI服务集成
    print("\n2. 测试AIService集成:")
    ai_service = AIService()
    
    # 创建测试图片（如果不存在）
    test_image_path = "test_image.jpg"
    if not os.path.exists(test_image_path):
        print("⚠️  测试图片不存在，创建一个简单的测试图片")
        from PIL import Image
        img = Image.new('RGB', (300, 300), color='white')
        img.save(test_image_path)
    
    # 3. 测试分析功能
    print(f"\n3. 测试图片分析功能:")
    try:
        result = await ai_service.analyze_clothing_image(test_image_path)
        
        if result:
            print("✅ 分析成功")
            print(f"服装类型: {result.get('clothing_type')}")
            print(f"风格标签: {result.get('style_tags')}")
            print(f"颜色标签: {result.get('color_tags')}")
            print(f"材质标签: {result.get('material_tags')}")
            print(f"图片中的服装: {result.get('clothes_in_image', [])}")
            print(f"场景推荐数量: {len(result.get('outfit_scenes', {}))}")
            print(f"分析内容长度: {len(result.get('detailed_analysis', ''))}")
            
            # 显示部分分析内容
            if result.get('detailed_analysis'):
                analysis_preview = result['detailed_analysis'][:200] + "..." if len(result['detailed_analysis']) > 200 else result['detailed_analysis']
                print(f"分析内容预览: {analysis_preview}")
                
        else:
            print("❌ 分析失败")
            
    except Exception as e:
        print(f"❌ 分析异常: {e}")
    
    # 4. 测试环境变量配置
    print(f"\n4. 环境变量检查:")
    ark_key = os.getenv('ARK_API_KEY')
    print(f"ARK_API_KEY: {'已配置' if ark_key else '未配置（使用默认值）'}")
    
    if ark_key:
        print("✅ 可以进行真实API调用")
    else:
        print("⚠️  使用默认API Key，可能需要配置真实的密钥")
    
    print("\n=== 测试完成 ===")

if __name__ == "__main__":
    asyncio.run(test_doubao_integration())
