# -*- coding: utf-8 -*-
"""
设备检测工具模块
用于自动检测和选择最佳计算设备（CUDA/MPS/CPU）
"""
import torch


def get_best_device() -> str:
    """
    自动检测最佳计算设备

    优先级: CUDA > MPS > CPU

    Returns:
        str: 设备名称 ("cuda", "mps", 或 "cpu")
    """
    if torch.cuda.is_available():
        device = "cuda"
        print(f"检测到 NVIDIA GPU，使用 CUDA 加速")
    elif torch.backends.mps.is_available():
        device = "mps"
        print(f"检测到 Apple Silicon，使用 MPS 加速")
    else:
        device = "cpu"
        print(f"未检测到 GPU，使用 CPU")

    return device
