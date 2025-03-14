"""
Cross platform helper for ctypes interface
"""

import ctypes
import sys

if sys.platform == 'win32':
    C_FUNCTYPE, C_DLL = ctypes.WINFUNCTYPE, ctypes.WinDLL
else:
    C_FUNCTYPE, C_DLL = ctypes.CFUNCTYPE, ctypes.CDLL

__all__ = ["C_FUNCTYPE", "C_DLL"]
