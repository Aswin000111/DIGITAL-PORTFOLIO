import sys
from cx_Freeze import setup, Executable

# Dependencies
build_exe_options = {
    "packages": ["os"],  # Add any additional packages your script requires
    "excludes": ["numpy.core._methods", "numpy.lib.format", "numpy._distributor_init"],  # Exclude MKL hooks
    "include_files": [],  # Add any additional files or data needed by your script
}

# Executable
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use this for GUI applications, remove for console applications

executables = [Executable("SkelCam.py", base=base)]

# Setup
setup(
    name="SkelCam",
    version="1.0",
    description="Skeletal tracking",
    options={"build_exe": build_exe_options},
    executables=executables
)
