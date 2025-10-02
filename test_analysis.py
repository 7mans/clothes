#!/usr/bin/env python3
"""
测试图片分析功能
"""
import asyncio
import sys
import os
sys.path.append('backend')

from app.services.ai_service import AIService
from app.core.database import SessionLocal
from app.models.analysis import Analysis
from app.models.user import User

async def test_analysis():
    """测试分析功能"""
    print("开始测试图片分析功能...")
    
    # 创建AI服务实例
    ai_service = AIService()
    
    # 创建测试分析记录
    db = SessionLocal()
    try:
        # 查找测试用户
        user = db.query(User).first()
        if not user:
            print("未找到测试用户")
            return
        
        # 创建测试分析记录
        analysis = Analysis(
            user_id=user.id,
            image_path="test_image.jpg",
            image_url="/static/uploads/test_image.jpg",
            original_filename="test_image.jpg",
            file_size=1024,
            status="processing",
            diamonds_cost=1
        )
        
        db.add(analysis)
        db.commit()
        db.refresh(analysis)
        
        print(f"创建测试分析记录 - ID: {analysis.id}")
        
        # 执行分析
        await ai_service.analyze_image_async(analysis.id, "test_image.jpg")
        
        # 检查结果
        db.refresh(analysis)
        print(f"分析状态: {analysis.status}")
        print(f"服装类型: {analysis.clothing_type}")
        print(f"AI分析数据存在: {'是' if analysis.ai_analysis else '否'}")
        
        if analysis.ai_analysis:
            print(f"分析结果键: {list(analysis.ai_analysis.keys())}")
            if 'description' in analysis.ai_analysis:
                print(f"描述: {analysis.ai_analysis['description'][:100]}...")
        
    except Exception as e:
        print(f"测试失败: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    asyncio.run(test_analysis())
