# 设备自动检测功能 - 使用指南

## 🎯 功能概述

已实现跨平台设备自动检测，支持 Mac（MPS）和 PC（CUDA）的 GPU 加速。

## ✨ 核心特性

- ✅ **自动检测**：优先级 CUDA > MPS > CPU
- ✅ **手动指定**：`--device cuda|mps|cpu`
- ✅ **向后兼容**：现有代码无需修改
- ✅ **零配置**：开箱即用

## 🚀 快速开始

### 基础用法（推荐）

```bash
# 中文视频转录翻译
python scripts/whisper_zh_video_translate_deepseek.py video.mp4

# 英文视频转录翻译
python scripts/whisper_en_video_translate_deepseek.py video.mp4

# 纯音频转文本
python scripts/audio2txt_tools.py audio.mp4
```

**运行效果：**
- Mac: `检测到 Apple Silicon，使用 MPS 加速`
- PC: `检测到 NVIDIA GPU，使用 CUDA 加速`
- 无 GPU: `未检测到 GPU，使用 CPU`

### 高级用法

```bash
# 强制使用 CUDA
python scripts/whisper_zh_video_translate_deepseek.py video.mp4 --device cuda

# 强制使用 CPU（调试用）
python scripts/whisper_zh_video_translate_deepseek.py video.mp4 --device cpu

# 多说话人分离
python scripts/whisper_zh_video_translate_deepseek.py video.mp4 --num-speakers 2

# 组合使用
python scripts/whisper_zh_video_translate_deepseek.py video.mp4 \
    --device cuda \
    --num-speakers 2 \
    --output_dir ./output
```

## 📊 兼容性

| 平台 | 支持状态 | 设备 |
|------|---------|------|
| Mac (Apple Silicon) | ✅ | MPS |
| PC (NVIDIA GPU) | ✅ | CUDA |
| 无 GPU 设备 | ✅ | CPU |

## 🧪 测试验证

```bash
# 测试设备检测
python tests/test_device_detection.py

# 查看帮助
python scripts/whisper_zh_video_translate_deepseek.py --help
```

## 📚 详细文档

| 文档 | 说明 |
|------|------|
| `QUICKSTART.md` | 快速开始指南（推荐） |
| `DEVICE_DETECTION.md` | 详细使用说明 |
| `IMPLEMENTATION_SUMMARY.md` | 技术实现细节 |
| `FINAL_REPORT.md` | 完整实现报告 |
| `CHECKLIST.md` | 验证和提交清单 |

## 🔧 常见问题

### Q: 如何查看当前会使用哪个设备？

```bash
python -c "from src.device import get_best_device; get_best_device()"
```

### Q: 如何强制使用 CPU？

```bash
python scripts/whisper_zh_video_translate_deepseek.py video.mp4 --device cpu
```

### Q: 提示 "No module named 'torch'"？

```bash
pip install torch
# 或
uv pip install torch
```

## 📦 实现细节

### 新增文件
- `src/device.py` - 设备检测核心模块
- 5 个文档文件（30KB+）
- 2 个测试脚本

### 修改文件
- `scripts/audio2txt_tools.py`
- `scripts/whisper_zh_video_translate_deepseek.py`
- `scripts/whisper_en_video_translate_deepseek.py`
- `scripts/cli_whisper_en_video_translate_deepseek.py`
- `scripts/en_video_translate_deepseek.py`

### 代码统计
- 修改：5 个文件
- 新增：+81 行
- 删除：-11 行
- 净增：+70 行

## 🎉 总结

现在你可以在 Mac 和 PC 上使用相同的命令运行脚本，系统会自动选择最佳设备。

**下一步：**
1. 运行测试：`python tests/test_device_detection.py`
2. 查看文档：`cat QUICKSTART.md`
3. 开始使用：`python scripts/whisper_zh_video_translate_deepseek.py video.mp4`

---

**实现时间**：2026-01-25  
**实现方案**：命令行参数 + 自动检测  
**状态**：✅ 完成
