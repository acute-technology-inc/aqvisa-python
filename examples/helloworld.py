"""
This example demonstrates how to use the AqVISALibrary class to select the
application type, open the resource manager, write a command, read the
response, and close the resource manager.
"""

import sys
from aqvisa import AqVISALibrary
from aqvisa import AppType

# Initialize the AqVISALibrary
manager = AqVISALibrary()

# Select the application type
success = manager.select_app_type(AppType.MIXEDSIGNALOSCILLOSCOPE)

if not success:
    print(f"viSelectAppType failed: {success}")
    sys.exit(1)

# Connect to the selected application
success = manager.open()
if not success:
    print(f"viOpenRM failed: {success}")
    sys.exit(1)

# Send the command `*IDN?` to the application
print("viWrite *IDN?")
success = manager.write(command=b"*IDN?")
if not success:
    print(f"viWrite failed, error code: {manager.get_status_code()}")

# Read the response
# The response of `*IDN?` command is like
# Model: <Model Name>, Serial No.: <Device Serial Number>;
# If the application is in demo mode, the response will be like
# Model: Demo, Serial No.: Demo;
response = manager.read(count=1024)
print(f"viRead Response: {response}")

# Disconnect from the application
_ = manager.close()
