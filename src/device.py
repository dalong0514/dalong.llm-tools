# -*- coding: utf-8 -*-
import torch


def get_best_device() -> str:
    """自动检测最佳计算设备，优先级：CUDA → MPS → CPU"""
    if torch.cuda.is_available():
        return "cuda"
    elif torch.backends.mps.is_available():
        return "mps"
    return "cpu"
