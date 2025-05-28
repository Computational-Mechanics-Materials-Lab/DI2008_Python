"""
DATAQ DI-2008 Driver
Adapted from original DATAQ Instruments Driver under the MIT License

Provides an interface for configuring and reading from DI-2008 Data Acquisition Devices (DAQs)

This file is part of the DI_2008_Driver, https://github.com/Computational-Mechanics-Materials-Lab/DI-2008-Driver

MIT License
"""

from .di_2008_driver import DI_2008
from .di_2008_layout_settings import (
    DI_2008Layout,
    DI_2008TCType,
    DI_2008ADCRange,
    DI_2008Channels,
    DI_2008AllChannels,
    DI_2008DigitalChannel,
    DI_2008ScanRateSettings,
    DI_2008FilterModes,
    DI_2008PSOption,
    DI_2008PSSettings,
)

__author__ = "Clark Hensley, J. Logan Betts, and Matthew W. Priddy"
__copyright__ = "Copyright 2025"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Clark Hensley"
__email__ = "ch3136@msstate.edu"
__status__ = "Production"

__all__ = [
    "DI_2008",
    "DI_2008Layout",
    "DI_2008TCType",
    "DI_2008ADCRange",
    "DI_2008Channels",
    "DI_2008AllChannels",
    "DI_2008DigitalChannel",
    "DI_2008ScanRateSettings",
    "DI_2008FilterModes",
    "DI_2008PSOption",
    "DI_2008PSSettings",
]
