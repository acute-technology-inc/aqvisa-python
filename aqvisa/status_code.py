"""
This module contains the status code for the AqVISA library.
"""

from enum import IntEnum


class StatusCode(IntEnum):
    """
    This collection of constants defines the status codes / error codes for
    the AqVISA library.
    """

    # Operation succeeded without error
    AQVI_NO_ERROR = 0

    # Error: OPENRM should only be called once to establish the software
    # connection
    AQVI_ALREADY_OPEN = 1

    # Error: The main software application was not started before calling the
    # viOPENRM
    AQVI_APPLICATION_NOT_STARTED = 2

    # Error: Failed to establish the connection to software application
    AQVI_FAILED_TO_CONNECT = 3

    # Error: The software connection is not valid yet, call viOpenRM first to
    # establish the connection
    AQVI_CONNECTION_NOT_VALID = 4

    # Error: The software application has been closed or re-started, need to
    # call viCloseRM and viOpenRM to establish the connection again
    AQVI_CONNECTION_LOST = 5

    # Error: Unable to send data to software application
    AQVI_FAILED_TO_COMMUNICATE = 6

    # Error: There's no any data returned from the software application
    AQVI_NO_RETURN_DATA = 7

    # Error: Input data buffer is NULL pointer and not valid
    AQVI_INPUT_NULL_POINTER = 8

    # Error: Input data buffer size is too small
    AQVI_DATA_BUFFER_TOO_SMALL = 9

    # Error: Select Application type should be done before OpenVM
    AQVI_SEL_APP_AFTER_VM_OPENED = 10

    # Error: Selected invalid Application type
    AQVI_SEL_APP_TYPE_INVALID = 11

    # Error: Previous Input Command Still Processing
    AQVI_PREVIOUS_CMD_PROCESSING = 12

    # Error: Input parameter unknown or not supported
    AQVI_INPUT_PARAMETER_UNKNOWN = 13

    # Error: Input parameter incompleted
    AQVI_INPUT_PARAMETER_INCOMPLETED = 14

    # Error: Input request timeout
    AQVI_TIMEOUT = 15

    # Command Error: Not supported in current SW (ex. for TBA)
    AQVI_NOT_SUPPORTED = 1000

    # Command Error: Input command incomplete
    AQVI_INCOMPLETE_COMMAND = 1001

    # Command Error: Input command requires exist SubWindow
    AQVI_SUBWND_INVALID = 1002

    # Command Error: Input command ask to add new SubWindow page, but software
    # already exceed maximum page count
    AQVI_SUBWND_CNT_EXCEED = 1003

    # Command Error: Input command ignored while software busy
    AQVI_SW_BUSY = 1004

    # Command Error: Input command requires exist Logic Analyzer SubWindow
    AQVI_LASUBWND_INVALID = 1005

    # Command Error: Input command requires exist Protocol Analyzer SubWindow
    AQVI_PASUBWND_INVALID = 1006

    # Command Error: Input command requires exist Decode Report
    AQVI_DECODE_REPORT_INVALID = 1007

    # Command Error: Input commands requires exist Timing Report
    AQVI_TIMING_REPORT_INVALID = 1008

    # Command Error: Input command format error
    AQVI_INPUT_COMMAND_FORMAT_ERROR = 1009

    # Command Error: Input file directory invalid
    AQVI_INPUT_FILE_DIR_INVALID = 1010

    # Command Error: Sending Capture Start command while capture already in
    # progress
    AQVI_CAPTURE_ALREADY_RUNNING = 1011

    # Command Error: Sending Capture Stop command while capture is not running
    AQVI_CAPTURE_NOT_RUNNING = 1012

    # Command Error: Input Row or Column index invalid
    AQVI_ROW_COL_INDEX_INVALID = 1013

    # Command Error: Input index selection invalid
    AQVI_SELECT_INDEX_INVALID = 1014

    # Command Error: Missing input parameters or not enough input parameter
    AQVI_INPUT_PARAMETER_INVALID = 1015

    # Command Error: Input setting file format error
    AQVI_INPUT_SETTING_FILE_FORMAT_ERROR = 1016

    # Command Error: Unable to access File unable to reach select file
    # directory or selected unsupported file type
    AQVI_FILE_ACCESS_ERROR = 1017

    # Command Error: Input commands requires exist Transition Report
    AQVI_TRANSITION_REPORT_INVALID = 1018

    # Command Error: Input commands requires exist Measurement Report
    AQVI_MEASUREMENT_REPORT_INVALID = 1019

    # Command Error: Selected Label Name not valid
    AQVI_SELECT_LABEL_INVALID = 1020

    # Command Error: Selected Range Condition Error, can't mix Line and Cursor
    # Range Condition
    AQVI_SELECT_RANGE_ERROR = 1021

    # Command Error: Selected Channel Name in Cursor Search is not valid
    AQVI_SELECT_CHANNEL_NAME_INVALID = 1022

    # Command Error: Cursor Search Failed unable to find more valid match
    AQVI_CURSOR_SEARCH_FAILED = 1023

    # Command Error: Waveform Data Not Ready
    AQVI_WAVEFORM_NOT_READY = 1024

    # Command Error: software is not configured in EV mode
    AQVI_NOT_IN_EV_MODE = 1025

    # Command Error: software doesn't have any valid EV analysis result
    AQVI_NO_EV_ANALYSIS_RESULT = 1026

    # Command Error: selected Device S/N not presented in device list
    AQVI_SELECT_DEV_NOT_EXIST = 1027

    # Error: Unsupported feature, feature is not supported in current model or
    # demo mode
    AQVI_UNSUPPORT_FEATURE = 9995

    # Error: Unfinished Feature
    AQVI_UNFINISHED_FEATURE = 9996

    # Error: Unknown Command
    AQVI_UNKNOWN_COMMAND_ERROR = 9997

    # Error: Unknown Error
    AQVI_UNKNOWN_ERROR = 9998

    # Error: DLL initialization not finished, please retry again later
    AQVI_DLL_NOT_READY = 9999
