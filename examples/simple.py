"""
This example demonstrates how to use the AqVISALibrary class to select the
application type, open the resource manager, write a command, read the
response, and close the resource manager.
"""

import sys
from aqvisa import AqVISALibrary

# Initialize the AqVISALibrary
manager = AqVISALibrary()

# Select the application type
success = manager.viSelectAppType(3)

if not success:
    print(f"viSelectAppType failed: {success}")
    sys.exit(1)

# Open the resource manager
success = manager.viOpenRM()
if not success:
    print(f"viOpenRM failed: {success}")
    sys.exit(1)

# Write the command *IDN?
success = manager.viWrite(b"*IDN?")
if not success:
    print(f"viWrite failed, error code: {manager.viErrCode()}")

# Read the response
string = manager.viRead(1024)
print(f"viRead: {string}")

# Close the resource manager
_ = manager.viCloseRM()
