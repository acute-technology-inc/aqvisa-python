"""
This module contains the application type for the AqVISA library.
"""

from enum import IntEnum


class AppType(IntEnum):
    """
    This enum contains the application type for the AqVISA library.
    """

    # TravelLogic Application
    TRAVELLOGIC = 0

    # BusFinder & Logic Analyzer Application
    BUSFINDER_LOGICANALYZER = 1

    # TravelBus Application
    TRAVELBUS = 2

    # Mixed Signal Oscilloscope Application
    MIXEDSIGNALOSCILLOSCOPE = 3
