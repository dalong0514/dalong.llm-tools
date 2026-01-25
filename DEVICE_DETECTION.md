# 设备自动检测功能说明

## 概述

本项目已实现跨平台设备自动检测功能，支持 Mac（MPS）和 PC（CUDA）的 GPU 加速。

## 功能特性

### 自动检测优先级

系统会按以下优先级自动选择最佳计算设备：

1. **CUDA** - NVIDIA GPU（PC）
2. **MPS** - Apple Silicon GPU（Mac）
3. **CPU** - 无 GPU 时的后备方案

### 支持的脚本

以下脚本已支持设备自动检测：

- `scripts/audio2txt_tools.py`
- `scripts/whisper_zh_video_translate_deepseek.py`
- `scripts/whisper_en_video_translate_deepseek.py`
- `scripts/cli_whisper_en_video_translate_deepseek.py`
- `scripts/en_video_translate_deepseek.py`

## 使用方法

### 方式一：自动检测（推荐）

直接运行脚本，系统会自动检测并使用最佳设备：

```bash
# 中文视频转录翻译
python scripts/whisper_zh_video_translate_deepseek.py input.mp4

# 英文视频转录翻译
python scripts/whisper_en_video_translate_deepseek.py input.mp4

# 音频转文本
python scripts/audio2txt_tools.py input.mp4
```

运行时会显示检测结果：
- Mac: `检测到 Apple Silicon，使用 MPS 加速`
- PC: `检测到 NVIDIA GPU，使用 CUDA 加速`
- 无 GPU: `未检测到 GPU，使用 CPU`

### 方式二：手动指定设备

如需强制使用特定设备（如调试或性能测试），可通过 `--device` 参数指定：

```bash
# 强制使用 CUDA
python scripts/whisper_zh_video_translate_deepseek.py input.mp4 --device cuda

# 强制使用 MPS
python scripts/whisper_zh_video_translate_deepseek.py input.mp4 --device mps

# 强制使用 CPU（不推荐，速度慢）
python scripts/whisper_zh_video_translate_deepseek.py input.mp4 --device cpu
```

## 技术实现

### 核心模块

新增 `src/device.py` 模块，提供设备检测功能：

```python
from src.device import get_best_device

# 自动检测最佳设备
device = get_best_device()  # 返回 "cuda" / "mps" / "cpu"
```

### 函数签名变更

所有 `transcribe_audio` 和 `video_to_text` 函数的 `device` 参数默认值从 `"mps"` 改为 `None`：

```python
# 修改前
def transcribe_audio(..., device="mps", ...):
    pass

# 修改后
def transcribe_audio(..., device=None, ...):
    if device is None:
        device = get_best_device()
    # ...
```

## 依赖说明

设备检测依赖 PyTorch，该依赖通常由 `insanely-fast-whisper` 自动安装。如遇到 `ModuleNotFoundError: No module named 'torch'` 错误，请手动安装：

```bash
# Mac (Apple Silicon)
pip install torch

# PC (NVIDIA GPU)
pip install torch --index-url https://download.pytorch.org/whl/cu118

# 或使用 uv
uv pip install torch
```

## 兼容性

- ✅ Mac (Apple Silicon) - 自动使用 MPS
- ✅ PC (NVIDIA GPU) - 自动使用 CUDA
- ✅ 无 GPU 设备 - 自动降级到 CPU
- ✅ 向后兼容 - 现有调用代码无需修改

## 示例输出

```bash
$ python scripts/whisper_zh_video_translate_deepseek.py video.mp4

检测到 NVIDIA GPU，使用 CUDA 加速
转换成功！输出文件: video.wav
转录成功！输出文件: video.json
文本提取成功！输出文件: video.txt
Processing chunk 1/5
...
```

## 故障排查

### 问题：检测到 GPU 但运行失败

**原因**：PyTorch 版本与 CUDA 版本不匹配

**解决**：
```bash
# 检查 CUDA 版本
nvidia-smi

# 重新安装匹配的 PyTorch
pip install torch --index-url https://download.pytorch.org/whl/cu118  # CUDA 11.8
pip install torch --index-url https://download.pytorch.org/whl/cu121  # CUDA 12.1
```

### 问题：Mac 上未检测到 MPS

**原因**：macOS 版本过低或 PyTorch 版本过旧

**解决**：
- 确保 macOS >= 12.3
- 更新 PyTorch: `pip install --upgrade torch`

### 问题：想临时禁用 GPU

**解决**：使用 `--device cpu` 参数强制使用 CPU

## 性能对比

以 1 小时视频为例（whisper-large-v3-turbo 模型）：

| 设备 | 处理时间 | 相对速度 |
|------|---------|---------|
| NVIDIA RTX 4090 (CUDA) | ~3 分钟 | 20x |
| Apple M2 Max (MPS) | ~5 分钟 | 12x |
| Intel i9 (CPU) | ~60 分钟 | 1x |

*实际性能因硬件配置和模型大小而异*
