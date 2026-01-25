# 设备自动检测功能实现总结

## 实现方案

已成功实现**方案二：命令行参数 + 自动检测**，同时支持自动检测和手动指定设备。

## 修改文件清单

### 新增文件

1. **`src/device.py`** - 核心设备检测模块
   - 提供 `get_best_device()` 函数
   - 按优先级自动检测：CUDA > MPS > CPU
   - 输出友好的检测提示信息

2. **`DEVICE_DETECTION.md`** - 使用说明文档
   - 功能介绍和使用方法
   - 故障排查指南
   - 性能对比参考

3. **`tests/test_device_detection.py`** - 测试脚本
   - 验证设备检测功能
   - 显示详细的硬件信息

### 修改文件

所有包含 `transcribe_audio` 函数的脚本均已更新：

1. **`scripts/audio2txt_tools.py`**
   - 导入 `get_best_device`
   - `transcribe_audio` 的 `device` 参数默认值改为 `None`
   - 添加自动检测逻辑
   - `video_to_text` 增加 `device` 参数
   - `parse_arguments` 增加 `--device` 选项

2. **`scripts/whisper_zh_video_translate_deepseek.py`**
   - `video_translate` 传递 `device` 参数
   - `parse_arguments` 增加 `--device` 选项

3. **`scripts/whisper_en_video_translate_deepseek.py`**
   - 导入 `get_best_device`
   - `transcribe_audio` 的 `device` 参数默认值改为 `None`
   - 添加自动检测逻辑
   - `video_to_text` 增加 `device` 参数
   - `video_translate` 传递 `device` 参数
   - `parse_arguments` 增加 `--device` 选项

4. **`scripts/cli_whisper_en_video_translate_deepseek.py`**
   - 导入 `get_best_device`
   - `transcribe_audio` 的 `device` 参数默认值改为 `None`
   - 添加自动检测逻辑
   - `video_to_text` 增加 `device` 参数
   - `video_translate` 传递 `device` 参数
   - `parse_arguments` 增加 `--device` 选项

5. **`scripts/en_video_translate_deepseek.py`**
   - 导入 `get_best_device`
   - `transcribe_audio` 的 `device` 参数默认值改为 `None`
   - 添加自动检测逻辑
   - `video_to_text` 增加 `device` 参数
   - `parse_arguments` 增加 `--device` 选项

## 核心改动

### 1. 设备检测模块 (`src/device.py`)

```python
def get_best_device() -> str:
    """自动检测最佳计算设备，优先级: CUDA > MPS > CPU"""
    if torch.cuda.is_available():
        return "cuda"
    elif torch.backends.mps.is_available():
        return "mps"
    return "cpu"
```

### 2. 函数签名变更

**修改前：**
```python
def transcribe_audio(..., device="mps", ...):
    pass
```

**修改后：**
```python
def transcribe_audio(..., device=None, ...):
    if device is None:
        device = get_best_device()
    # ...
```

### 3. 命令行参数增强

所有脚本的 `parse_arguments()` 函数都新增了：

```python
parser.add_argument(
    "--device",
    type=str,
    default=None,
    choices=["cuda", "mps", "cpu"],
    help="计算设备 (默认: 自动检测)",
)
```

## 使用示例

### 自动检测（推荐）

```bash
# 中文视频转录
python scripts/whisper_zh_video_translate_deepseek.py video.mp4

# 英文视频转录
python scripts/whisper_en_video_translate_deepseek.py video.mp4

# 音频转文本
python scripts/audio2txt_tools.py video.mp4
```

### 手动指定设备

```bash
# 强制使用 CUDA
python scripts/whisper_zh_video_translate_deepseek.py video.mp4 --device cuda

# 强制使用 MPS
python scripts/whisper_zh_video_translate_deepseek.py video.mp4 --device mps

# 强制使用 CPU
python scripts/whisper_zh_video_translate_deepseek.py video.mp4 --device cpu
```

## 兼容性保证

- ✅ **向后兼容**：现有调用代码无需修改
- ✅ **跨平台**：Mac 和 PC 自动适配
- ✅ **降级支持**：无 GPU 时自动使用 CPU
- ✅ **灵活控制**：支持手动指定设备

## 测试验证

运行测试脚本验证功能：

```bash
python tests/test_device_detection.py
```

预期输出示例（PC with NVIDIA GPU）：
```
============================================================
设备检测测试
============================================================
检测到 NVIDIA GPU，使用 CUDA 加速

✓ 自动检测结果: cuda
✓ 设备类型验证通过

详细信息:
  - PyTorch 版本: 2.x.x
  - CUDA 可用: True
  - CUDA 版本: 11.8
  - GPU 数量: 1
  - GPU 名称: NVIDIA GeForce RTX 4090
  - MPS 可用: False

============================================================
✓ 所有测试通过
============================================================
```

## 性能提升

相比固定使用 MPS，新方案在不同平台上的性能：

| 平台 | 修改前 | 修改后 | 提升 |
|------|--------|--------|------|
| Mac (M2 Max) | MPS | MPS | 无变化 |
| PC (RTX 4090) | ❌ 不可用 | CUDA | ✅ 可用 |
| 无 GPU | ❌ 报错 | CPU | ✅ 降级 |

## 依赖说明

- 依赖 PyTorch 进行设备检测
- PyTorch 通常由 `insanely-fast-whisper` 自动安装
- 如需手动安装：`pip install torch`

## 后续建议

1. **测试验证**：在 Mac 和 PC 上分别测试脚本运行
2. **性能基准**：记录不同设备的实际处理时间
3. **文档更新**：将 `DEVICE_DETECTION.md` 链接添加到主 README
4. **CI/CD**：考虑在 CI 中添加设备检测测试

## 提交建议

```bash
# 查看修改
git status
git diff

# 添加文件
git add src/device.py
git add scripts/*.py
git add DEVICE_DETECTION.md
git add tests/test_device_detection.py

# 提交
git commit -m "Add cross-platform device auto-detection

- 新增 src/device.py 设备自动检测模块
- 支持 CUDA (PC) 和 MPS (Mac) 自动识别
- 所有 whisper 转录脚本增加 --device 参数
- 向后兼容，默认自动检测最佳设备
- 添加使用文档和测试脚本"

# 推送
git push origin devs
```
