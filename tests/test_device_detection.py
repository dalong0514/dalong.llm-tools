# -*- coding: utf-8 -*-
"""
设备检测功能测试
"""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.device import get_best_device


def test_device_detection():
    """测试设备自动检测功能"""
    print("=" * 60)
    print("设备检测测试")
    print("=" * 60)

    # 测试自动检测
    device = get_best_device()
    print(f"\n✓ 自动检测结果: {device}")

    # 验证返回值
    assert device in ["cuda", "mps", "cpu"], f"无效的设备类型: {device}"
    print(f"✓ 设备类型验证通过")

    # 显示详细信息
    try:
        import torch
        print(f"\n详细信息:")
        print(f"  - PyTorch 版本: {torch.__version__}")
        print(f"  - CUDA 可用: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"  - CUDA 版本: {torch.version.cuda}")
            print(f"  - GPU 数量: {torch.cuda.device_count()}")
            print(f"  - GPU 名称: {torch.cuda.get_device_name(0)}")
        print(f"  - MPS 可用: {torch.backends.mps.is_available()}")
    except Exception as e:
        print(f"\n⚠ 无法获取详细信息: {e}")

    print("\n" + "=" * 60)
    print("✓ 所有测试通过")
    print("=" * 60)


if __name__ == "__main__":
    test_device_detection()
