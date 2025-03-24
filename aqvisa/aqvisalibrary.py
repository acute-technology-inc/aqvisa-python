"""
This module defines the AqVISALibrary class.

AqVISALibrary is a Python wrapper for AqVISA / AqVISA dynamic library,
which simplifies the access to the AqVISA functions from Python.
"""

from ctypes import c_int, c_char_p, create_string_buffer
from aqvisa.apptype import AppType
from aqvisa.status_code import StatusCode
from aqvisa.utils.library_wrapper import AqLibrary


class AqVISALibrary(AqLibrary):
    """
    Main class for AqVISALibrary to access Acute's instruments.

    Creating AqVISALibrary object will attempt to load the AqVISA library.
    """

    def __init__(self) -> None:
        """
        Initialize the AqVISALibrary object and resolves the methods from
        the library.

        Here we only handle AqVISA64 (64-bit on Windows).

        TODO: Support other platforms.
        """
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

    def close(self) -> int:
        """
        Disconnect from the application.

        This function corresponds to viCloseRM function
        of the AqVISA library.

        :return: 1 on success, otherwise 0.
        """
        return getattr(self, "_viCloseRM")()

    def get_status_code(self) -> StatusCode:
        """
        Retrieve the AqVISA latest status code.

        This function corresponds to viErrCode function
        of the AqVISA library.

        :return: AqVISA status code.
        """
        status = getattr(self, "_viErrCode")()
        return StatusCode(status)

    def get_command_result(self) -> int:
        """
        Get the execution result after the command is executed.

        This function corresponds to viGetCommandResult function
        of the AqVISA library.

        :return: The result after the command is executed. If the command does
                 not return any data, it will return an empty bytes object.
        """
        return getattr(self, "_viGetCommandResult")()

    def open(self) -> int:
        """
        Connect to the application.

        This function corresponds to viOpenRM function of the AqVISA library.

        :return: 1 on success, otherwise 0.
        """
        return getattr(self, "_viOpenRM")()

    def read(self, count: int) -> bytes:
        """
        Get the result after the command is executed.

        This function corresponds to viRead function
        of the AqVISA library.

        :param count: The number of bytes to read.
        :return: The result after the command is executed. If the command does
                 not return any data, it will return an empty bytes object.
        """

        buffer = create_string_buffer(count)
        ret_size = getattr(self, "_viRead")(buffer, count)
        return buffer.value if ret_size else b''

    def select_app_type(self, app_type: AppType) -> int:
        """
        Setup the target connection application.

        This function corresponds to viSelectAppType function
        of the AqVISA library.

        :param app_type: The application type to select.
        :return: 1 on success, otherwise 0.
        """
        return getattr(self, "_viSelectAppType")(app_type.value)

    def write(self, command: bytes) -> int:
        """
        Send AqLAVISA command to the application.

        This function corresponds to viWrite function
        of the AqVISA library.

        :param command: The command to send to the application.
        :return: The number of bytes written to the application.
        """
        return getattr(self, "_viWrite")(command)
