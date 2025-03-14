"""
This module contains the AqVISALibrary class.
"""

from ctypes import c_int, c_char_p, create_string_buffer
from aqvisa.apptype import AppType
from aqvisa.status_code import StatusCode
from aqvisa.utils import AqLibrary


class AqVISALibrary(AqLibrary):
    """
    This class contains the AqVISALibrary class.
    """

    def __init__(self) -> None:
        super().__init__("AqVISA64")
        self._functions = [
            ["_viCloseRM", "viCloseRM", c_int, None],
            ["_viErrCode", "viErrCode", c_int, None],
            ["_viGetCommandResult", "viGetCommandResult", c_int, None],
            ["_viOpenRM", "viOpenRM", c_int, None],
            ["_viRead", "viRead", c_int, [c_char_p, c_int]],
            ["_viSelectAppType", "viSelectAppType", c_int, [c_int]],
            ["_viWrite", "viWrite", c_int, [c_char_p]],
        ]

        for method in self._functions:
            self.map_api(*method)

    def viCloseRM(self) -> int:
        return getattr(self, "_viCloseRM")()

    def viErrCode(self) -> StatusCode:
        status = getattr(self, "_viErrCode")()
        return StatusCode(status)

    def viGetCommandResult(self) -> int:
        return getattr(self, "_viGetCommandResult")()

    def viOpenRM(self) -> int:
        return getattr(self, "_viOpenRM")()

    def viRead(self, count: int) -> bytes:
        buffer = create_string_buffer(count)
        ret_size = getattr(self, "_viRead")(buffer, count)
        return buffer.value if ret_size else b''

    def viSelectAppType(self, app_type: AppType) -> int:
        return getattr(self, "_viSelectAppType")(app_type.value)

    def viWrite(self, command: bytes) -> int:
        return getattr(self, "_viWrite")(command)


if __name__ == '__main__':
    manager = AqVISALibrary()
    s = manager.viSelectAppType(3)
    print(s, manager.viErrCode())
    s = manager.viOpenRM()
    print(s, manager.viErrCode())
    s = manager.viWrite(b"*WINDOW:SIZE?")
    print(s, manager.viErrCode())
    string = manager.viRead(1024)
    print(string, manager.viErrCode())
    s = manager.viCloseRM()
    print(s, manager.viErrCode())
