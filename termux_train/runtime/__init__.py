# Copyright (c) 2026 Uno Kim / AMEVA Foundation. All rights reserved.
# SPDX-License-Identifier: Apache-2.0 OR Commercial-License
"""
termux_train.runtime
====================
Mobile Execution Runtime & Safe Checkpointing Subsystem.
Provides atomic crash-resilient checkpointing, rollback guarantees, and MobileTrainer lifecycle management.
"""

from .checkpoint import (
    save_checkpoint,
    load_checkpoint,
    save_lora_checkpoint,
    load_lora_checkpoint,
    CheckpointError,
    CheckpointIntegrityError,
    CheckpointSchemaError,
    CheckpointRollbackError,
)
from .trainer import MobileTrainer

__all__ = [
    "save_checkpoint",
    "load_checkpoint",
    "save_lora_checkpoint",
    "load_lora_checkpoint",
    "CheckpointError",
    "CheckpointIntegrityError",
    "CheckpointSchemaError",
    "CheckpointRollbackError",
    "MobileTrainer",
]
