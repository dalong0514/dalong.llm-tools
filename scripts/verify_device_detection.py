#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
快速验证脚本 - 检查设备自动检测功能是否正确实现
"""
import os
import sys
import re
from pathlib import Path

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def check_file_exists(filepath):
    """检查文件是否存在"""
    if Path(filepath).exists():
        print(f"✓ {filepath}")
        return True
    else:
        print(f"✗ {filepath} - 文件不存在")
        return False

def check_import_in_file(filepath, import_statement):
    """检查文件中是否包含指定的导入语句"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            if import_statement in content:
                return True
    except Exception as e:
        print(f"  ⚠ 读取文件失败: {e}")
    return False

def check_device_parameter(filepath):
    """检查文件中的 device 参数是否正确配置"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

            # 检查是否有硬编码的 device="mps"
            if 'device="mps"' in content or "device='mps'" in content:
                print(f"  ✗ 发现硬编码的 device='mps'")
                return False

            # 检查是否有 device=None 的默认参数
            if 'device=None' in content:
                print(f"  ✓ 包含 device=None 默认参数")
                return True

            # 检查是否有 --device 命令行参数
            if '--device' in content or '"--device"' in content:
                print(f"  ✓ 包含 --device 命令行参数")
                return True

    except Exception as e:
        print(f"  ⚠ 读取文件失败: {e}")
    return False

def main():
    print("=" * 70)
    print("设备自动检测功能验证")
    print("=" * 70)

    all_passed = True

    # 1. 检查核心模块
    print("\n[1] 检查核心模块")
    if not check_file_exists("src/device.py"):
        all_passed = False
    else:
        # 验证核心函数
        try:
            from src.device import get_best_device
            print("  ✓ get_best_device 函数可导入")

            # 测试函数
            device = get_best_device()
            if device in ["cuda", "mps", "cpu"]:
                print(f"  ✓ 函数返回有效设备: {device}")
            else:
                print(f"  ✗ 函数返回无效设备: {device}")
                all_passed = False
        except Exception as e:
            print(f"  ✗ 导入或执行失败: {e}")
            all_passed = False

    # 2. 检查修改的脚本文件
    print("\n[2] 检查修改的脚本文件")
    scripts_to_check = [
        "scripts/audio2txt_tools.py",
        "scripts/whisper_zh_video_translate_deepseek.py",
        "scripts/whisper_en_video_translate_deepseek.py",
        "scripts/cli_whisper_en_video_translate_deepseek.py",
        "scripts/en_video_translate_deepseek.py",
    ]

    for script in scripts_to_check:
        print(f"\n  检查 {script}:")
        if not check_file_exists(f"  {script}"):
            all_passed = False
            continue

        # 检查是否导入了 get_best_device（部分脚本需要）
        if script in ["scripts/audio2txt_tools.py",
                      "scripts/whisper_en_video_translate_deepseek.py",
                      "scripts/cli_whisper_en_video_translate_deepseek.py",
                      "scripts/en_video_translate_deepseek.py"]:
            if check_import_in_file(script, "from src.device import get_best_device"):
                print(f"    ✓ 已导入 get_best_device")
            else:
                print(f"    ✗ 未导入 get_best_device")
                all_passed = False

        # 检查 device 参数配置
        if not check_device_parameter(script):
            all_passed = False

    # 3. 检查文档
    print("\n[3] 检查文档")
    docs = [
        "DEVICE_DETECTION.md",
        "IMPLEMENTATION_SUMMARY.md",
    ]
    for doc in docs:
        if not check_file_exists(f"  {doc}"):
            all_passed = False

    # 4. 检查测试文件
    print("\n[4] 检查测试文件")
    if not check_file_exists("  tests/test_device_detection.py"):
        all_passed = False

    # 5. 验证没有遗留的硬编码
    print("\n[5] 验证没有硬编码的 device='mps'")
    found_hardcoded = False
    for script in scripts_to_check:
        try:
            with open(script, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'device="mps"' in content or "device='mps'" in content:
                    print(f"  ✗ {script} 中发现硬编码")
                    found_hardcoded = True
        except:
            pass

    if not found_hardcoded:
        print("  ✓ 未发现硬编码的 device='mps'")
    else:
        all_passed = False

    # 最终结果
    print("\n" + "=" * 70)
    if all_passed:
        print("✓ 所有检查通过！设备自动检测功能已正确实现")
        print("\n下一步:")
        print("  1. 运行测试: python tests/test_device_detection.py")
        print("  2. 测试脚本: python scripts/whisper_zh_video_translate_deepseek.py --help")
        print("  3. 查看文档: cat DEVICE_DETECTION.md")
    else:
        print("✗ 部分检查未通过，请检查上述错误")
        sys.exit(1)
    print("=" * 70)

if __name__ == "__main__":
    main()
