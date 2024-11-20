"""
VidKit - A Python package for generating videos from JSON specifications
"""

from .core import renderVideo

__version__ = "0.1.0"
__all__ = ["renderVideo"]

# Make renderVideo available at package level
render_video = renderVideo  # Alias for backward compatibility
