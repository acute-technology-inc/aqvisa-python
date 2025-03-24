<h1 align=center>Acute VISA Python Package</h1>

[![License](https://img.shields.io/badge/License-BSD_2--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)
[![PyPI](https://img.shields.io/pypi/v/aqvisa?label=pypi%20package)](https://pypi.org/project/aqvisa/)

Acute VISA (AqVISA) offers an intuitive interface for seamless management of controlling our applications. This Python package providing higher level management to AqVISA library.

- Acute official website: https://www.acute.com.tw/en/
- Acute software download: https://www.acute.com.tw/en/install
- Acute VISA SDK installer download: https://www.acute.com.tw/en/sdkDLL
- Bug reports: https://github.com/acute-technology-inc/aqvisa-python/issues

## Installation

- Run the installer.

    Please refer to the [installation page](https://www.acute.com.tw/en/sdkDLL) to download the installer. The installer
    is named as `aqvisa-installer-<version>.exe`.
    
    By default, the installer will install the dynamic library and the dependency libraries to the following directory:
    ```
    C:\Users\<username>\AppData\Local\Acute\SDK\AqVISA
    ```
    
    The installer has an option to add the installation directory to the system PATH.
    This is recommended for most users to locate the dynamic library easily.

- Install the Python Package
    
    You can install aqvisa as a python package using a package manager called `pip`, which installs packages from the Python Packaging Index (PyPI).
    
    Type the following command in your terminal:
    ```bash
    pip install aqvisa
    ```

## Examples

| **Use Case** | **Description** |
| ------------ | --------------- |
| [Basic Write / Read](https://github.com/acute-technology-inc/aqvisa-python/blob/main/examples/helloworld.py) | Demonstrates basic usage | 

## FAQ

### Library AqVISA64 not found

If you encounter the following error:

```
FileNotFoundError: Library AqVISA64 not found
```

This means that the dynamic library is not installed. Please refer to the [installation page](https://www.acute.com.tw/en/sdkDLL) to download the installer.
