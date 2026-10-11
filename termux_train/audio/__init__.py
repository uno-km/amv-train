# Copyright (c) 2026 Uno Kim / AMEVA Foundation. All rights reserved.
# SPDX-License-Identifier: Apache-2.0 OR Commercial-License
"""
termux_train.audio
==================
On-device Audio Speech (STT Whisper & TTS Voice Adaptation) Fine-Tuning Engine.
Open-Source under Apache License 2.0.
"""

from .audio_lora import (
    WhisperCrossAttentionLoRA,
    WhisperSTTLoRAModel,
    TTSSpeakerAdaptationLoRA,
)
from .trainer import train_stt_lora, train_tts_lora

__all__ = [
    "WhisperCrossAttentionLoRA",
    "WhisperSTTLoRAModel",
    "TTSSpeakerAdaptationLoRA",
    "train_stt_lora",
    "train_tts_lora",
]
