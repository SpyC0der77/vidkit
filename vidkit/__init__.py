"""
VidKit - A Python package for generating videos from JSON specifications
"""

from .core import renderVideo, get_config, saveVideo

__version__ = "0.1.3"  # Security update: Pillow vulnerability fixes
__all__ = ["renderVideo", "get_config", "saveVideo"]

# Make renderVideo available at package level
render_video = renderVideo  # Alias for backward compatibility
