"""
This module defines the supported application type of Acute's application
for the AqVISA library.
"""

from enum import IntEnum


class AppType(IntEnum):
    """
    This enum defines the supported application type of Acute's application.
    """

    # TravelLogic Application
    TRAVELLOGIC = 0

    # BusFinder & Logic Analyzer Application
    BUSFINDER_LOGICANALYZER = 1

    # TravelBus Application
    TRAVELBUS = 2

    # Mixed Signal Oscilloscope (MSO) Application
    MIXEDSIGNALOSCILLOSCOPE = 3

    # Digital Storage Oscilloscope (DSO) Application
    DIGTIALSTORAGEOSCILLOSCOPE = 101
