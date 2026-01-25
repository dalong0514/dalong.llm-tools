# 快速开始指南

## 设备自动检测功能

本项目已实现跨平台设备自动检测，Mac 和 PC 可以无缝使用相同的命令。

## 快速测试

### 1. 测试设备检测

```bash
# 测试设备检测功能
python tests/test_device_detection.py
```

预期输出（PC with NVIDIA GPU）：
```
============================================================
设备检测测试
============================================================
检测到 NVIDIA GPU，使用 CUDA 加速

✓ 自动检测结果: cuda
✓ 设备类型验证通过
...
```

预期输出（Mac with Apple Silicon）：
```
============================================================
设备检测测试
============================================================
检测到 Apple Silicon，使用 MPS 加速

✓ 自动检测结果: mps
✓ 设备类型验证通过
...
```

### 2. 测试音频转录

```bash
# 准备一个测试视频文件
# 运行转录（自动检测设备）
python scripts/whisper_zh_video_translate_deepseek.py test_video.mp4

# 或指定输出目录
python scripts/whisper_zh_video_translate_deepseek.py test_video.mp4 --output_dir ./output
```

### 3. 查看帮助信息

```bash
# 查看所有可用参数
python scripts/whisper_zh_video_translate_deepseek.py --help
```

输出示例：
```
usage: whisper_zh_video_translate_deepseek.py [-h] [--language LANGUAGE]
                                               [--model_path MODEL_PATH]
                                               [--output_dir OUTPUT_DIR]
                                               [--num-speakers NUM_SPEAKERS]
                                               [--min-speakers MIN_SPEAKERS]
                                               [--device {cuda,mps,cpu}]
                                               input_video

将视频文件转换为文字转录

positional arguments:
  input_video           输入视频文件路径

optional arguments:
  --device {cuda,mps,cpu}
                        计算设备 (默认: 自动检测)
  ...
```

## 常用命令

### 中文视频转录翻译

```bash
# 基础用法（自动检测设备）
python scripts/whisper_zh_video_translate_deepseek.py video.mp4

# 指定输出目录
python scripts/whisper_zh_video_translate_deepseek.py video.mp4 --output_dir ./output

# 多说话人分离（2人）
python scripts/whisper_zh_video_translate_deepseek.py video.mp4 --num-speakers 2

# 强制使用 CPU（调试用）
python scripts/whisper_zh_video_translate_deepseek.py video.mp4 --device cpu
```

### 英文视频转录翻译

```bash
# 基础用法
python scripts/whisper_en_video_translate_deepseek.py video.mp4

# 指定语言
python scripts/whisper_en_video_translate_deepseek.py video.mp4 --language en

# 多说话人分离
python scripts/whisper_en_video_translate_deepseek.py video.mp4 --num-speakers 3
```

### 纯音频转文本

```bash
# 转录音频文件
python scripts/audio2txt_tools.py audio.mp4

# 指定设备
python scripts/audio2txt_tools.py audio.mp4 --device cuda
```

## 性能对比

以 1 小时视频为例（whisper-large-v3-turbo 模型）：

| 设备 | 预估处理时间 |
|------|-------------|
| NVIDIA RTX 4090 (CUDA) | ~3-5 分钟 |
| NVIDIA RTX 3080 (CUDA) | ~5-8 分钟 |
| Apple M2 Max (MPS) | ~5-7 分钟 |
| Apple M1 Pro (MPS) | ~8-12 分钟 |
| Intel i9 (CPU) | ~60-90 分钟 |

*实际性能因硬件配置、视频质量和模型大小而异*

## 故障排查

### 问题 1：ModuleNotFoundError: No module named 'torch'

**解决方案：**
```bash
# 安装 PyTorch
pip install torch

# 或使用 uv
uv pip install torch
```

### 问题 2：CUDA out of memory

**解决方案：**
```bash
# 降低 batch size（默认为 4）
python scripts/whisper_zh_video_translate_deepseek.py video.mp4 --batch-size 2

# 或强制使用 CPU
python scripts/whisper_zh_video_translate_deepseek.py video.mp4 --device cpu
```

### 问题 3：Mac 上未检测到 MPS

**原因：** macOS 版本过低或 PyTorch 版本过旧

**解决方案：**
- 确保 macOS >= 12.3
- 更新 PyTorch: `pip install --upgrade torch`

### 问题 4：检测到 GPU 但运行失败

**原因：** PyTorch 版本与 CUDA 版本不匹配

**解决方案：**
```bash
# 检查 CUDA 版本
nvidia-smi

# 安装匹配的 PyTorch
# CUDA 11.8
pip install torch --index-url https://download.pytorch.org/whl/cu118

# CUDA 12.1
pip install torch --index-url https://download.pytorch.org/whl/cu121
```

## 高级用法

### 批量处理多个视频

```bash
# 创建批处理脚本
for video in *.mp4; do
    python scripts/whisper_zh_video_translate_deepseek.py "$video" --output_dir ./output
done
```

### 自定义模型路径

```bash
# 使用本地模型
python scripts/whisper_zh_video_translate_deepseek.py video.mp4 \
    --model_path /path/to/your/whisper-model
```

### 说话人分离

```bash
# 精确指定说话人数量（2人对话）
python scripts/whisper_zh_video_translate_deepseek.py video.mp4 --num-speakers 2

# 指定最小说话人数量（至少3人）
python scripts/whisper_zh_video_translate_deepseek.py video.mp4 --min-speakers 3

# 注意：--num-speakers 和 --min-speakers 不能同时使用
```

## 输出文件说明

运行脚本后会生成以下文件：

```
video.mp4                    # 原始视频
├── video.json              # Whisper 转录原始输出（JSON 格式）
├── video.txt               # 提取的纯文本转录
├── video_origin.md         # 整理后的转录文本（带时间戳）
└── video.md                # 最终翻译结果
```

## 更多信息

- 详细使用说明：`DEVICE_DETECTION.md`
- 实现技术细节：`IMPLEMENTATION_SUMMARY.md`
- 项目指南：`CLAUDE.md`

## 反馈与支持

如遇到问题，请检查：
1. PyTorch 是否正确安装
2. CUDA/MPS 驱动是否正常
3. 模型文件路径是否正确
4. 输入视频格式是否支持

可以通过以下方式获取更多信息：
```bash
# 查看 PyTorch 信息
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA: {torch.cuda.is_available()}'); print(f'MPS: {torch.backends.mps.is_available()}')"

# 查看 GPU 信息（NVIDIA）
nvidia-smi

# 查看系统信息（Mac）
system_profiler SPHardwareDataType
```
