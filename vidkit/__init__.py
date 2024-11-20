"""
VidKit - A Python package for generating videos from JSON specifications
"""

from .core import renderVideo, get_config, saveVideo

__version__ = "0.1.1"
__all__ = ["renderVideo", "get_config", "saveVideo"]

# Make renderVideo available at package level
render_video = renderVideo  # Alias for backward compatibility
