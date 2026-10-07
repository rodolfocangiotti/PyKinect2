import platform

from pykinect2.tools.exceptions import PyKinect2Exception


def get_platform_bits() -> int:
    architecture, _ = platform.architecture()
    if architecture == "32bit":
        return 32
    if architecture == "64bit":
        return 64
    raise PyKinect2Exception(f"Unexpected architecture: {architecture}")
