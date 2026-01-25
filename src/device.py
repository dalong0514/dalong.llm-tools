# -*- coding: utf-8 -*-
import torch


def get_best_device() -> str:
    """自动检测最佳计算设备，优先级：CUDA → MPS → CPU

    注意：insanely-fast-whisper 对 CUDA 设备只接受数字 ID（如 "0"），
    它内部会自动加上 "cuda:" 前缀
    """
    if torch.cuda.is_available():
        return "0"
    elif torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def get_default_whisper_model_path(device: str = None) -> str:
    """根据设备返回默认的 Whisper 模型路径"""
    if device is None:
        device = get_best_device()

    if device == "mps":
        return "/Users/Daglas/dalong.com/D.MyLibrary/dalong.modelsets/whisper-large-v3-turbo"
    else:
        # cuda 或 cpu (PC/WSL)
        return "/mnt/d/dalong.com/D.MyLibrary/dalong.modelsets/whisper-large-v3-turbo"
