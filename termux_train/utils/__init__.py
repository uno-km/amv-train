# Copyright (c) 2026 Uno Kim / AMEVA Foundation. All rights reserved.
# SPDX-License-Identifier: Apache-2.0 OR Commercial-License
"""
termux-train utilities module
=============================
"""

from .termux_env import is_termux, is_android, get_device_info
from .gradcheck import gradcheck

__all__ = [
    "is_termux",
    "is_android",
    "get_device_info",
    "gradcheck",
]
