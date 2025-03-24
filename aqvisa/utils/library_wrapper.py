"""
This is a wrapper for the AqLibrary class.
"""

import time
from ctypes.util import find_library
from typing import Any, List, Optional
from aqvisa.utils.ctypes_wrapper import C_DLL


class AqLibrary:
    """
    This is a wrapper for the AqLibrary class.
    """
    def __init__(self, libname: str) -> None:
        self.libname = libname
        self._load()

    def __str__(self) -> str:
        return f"Acute {self.libname} library"

    def _load(self) -> Any:
        lib_path = find_library(self.libname)

        # Check if library exists
        if lib_path is None:
            raise FileNotFoundError(f"Library {self.libname} not found.")

        self._dll = C_DLL(lib_path)
        time.sleep(0.05)

    def map_api(self,
                py_api_name: str,
                c_api_name: str,
                restype: Optional[Any] = None,
                argstype: Optional[List[Any]] = None) -> None:
        """
        This function maps the python APIs to the C APIs.
        """
        try:
            c_api = getattr(self._dll, c_api_name)
            c_api.argtypes = argstype
            c_api.restype = restype
            setattr(self, py_api_name, c_api)

        except AttributeError:
            print(f"Fail to create {py_api_name} mapping")
