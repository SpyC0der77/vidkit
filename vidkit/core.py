"""
VidKit Core Module - Video generation from JSON configurations

This module provides the core functionality for generating videos from JSON configurations,
including frame composition, audio integration, and metadata handling.
"""

import json
from typing import Union, Dict, Any, List, Tuple
from moviepy.editor import VideoFileClip, ImageClip, AudioFileClip, CompositeVideoClip
from PIL import Image
import numpy as np
import io
from mutagen.mp4 import MP4, MP4FreeForm
import os
from pathlib import Path

class ConfigError(Exception):
    """Exception raised for errors in the video configuration."""
    pass

def validate_config(config: Dict[str, Any]) -> None:
    """
    Validate the video configuration.
    
    Args:
        config (Dict[str, Any]): The configuration dictionary to validate
        
    Raises:
        ConfigError: If the configuration is invalid
    """
    required_fields = ["name", "format", "framerate", "resolution"]
    for field in required_fields:
        if field not in config:
            raise ConfigError(f"Missing required field: {field}")
            
    if "frames" not in config or not config["frames"]:
        raise ConfigError("No frames specified in configuration")
        
    for frame in config["frames"]:
        if "image" not in frame:
            raise ConfigError("Frame missing required 'image' field")
        if not os.path.exists(frame["image"]):
            raise ConfigError(f"Image file not found: {frame['image']}")

def _add_config_metadata(output_path: str, config: Dict[str, Any]) -> None:
    """Add the configuration as metadata to the MP4 file."""
    video = MP4(output_path)
    config_json = json.dumps(config).encode('utf-8')
    video["----:mean:com.vidkit:name:config"] = MP4FreeForm(config_json)
    video.save()

def get_config(filepath: str) -> Dict[str, Any]:
    """
    Extract the configuration used to generate the video from its metadata.
    
    Args:
        filepath (str): Path to the MP4 file.
        
    Returns:
        dict: The configuration used to generate the video.
        
    Raises:
        KeyError: If no VidKit configuration is found in the metadata.
        ValueError: If the file is not an MP4 file or doesn't exist.
    """
    try:
        video = MP4(filepath)
        if "----:mean:com.vidkit:name:config" not in video:
            raise KeyError("No VidKit configuration found in metadata")
        config_json = video["----:mean:com.vidkit:name:config"][0]
        return json.loads(config_json.decode('utf-8'))
    except Exception as e:
        raise ValueError(f"Failed to read configuration from {filepath}: {str(e)}")

def renderVideo(config: Union[Dict, str], validate: bool = True) -> bytes:
    """
    Generate a video based on the provided configuration.
    
    Args:
        config: Either a dictionary containing the video configuration or a JSON string
        validate: Whether to validate the configuration before rendering (default: True)
        
    Returns:
        bytes: The rendered video as bytes that can be written to a file
        
    Raises:
        ConfigError: If the configuration is invalid
        ValueError: If the config string cannot be parsed as JSON
    """
    # If config is a string, parse it as JSON
    if isinstance(config, str):
        try:
            config = json.loads(config)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON configuration: {str(e)}")
    
    if validate:
        validate_config(config)
    
    # Get video parameters with defaults
    fps = config.get("framerate", 30)
    width, height = config.get("resolution", [1920, 1080])
    
    # Initialize clips list
    clips = []
    
    # Process frames
    if "frames" in config:
        for frame_config in config["frames"]:
            try:
                clip = ImageClip(frame_config["image"])
                if "duration" in frame_config:
                    clip = clip.set_duration(frame_config["duration"])
                clip = clip.resize(newsize=(width, height))  # Ensure correct resolution
                clips.append(clip)
            except Exception as e:
                raise ConfigError(f"Error processing frame {frame_config.get('image')}: {str(e)}")
    
    # Process audio if specified
    audio = None
    if "audio" in config:
        audio_path = config["audio"]
        if not os.path.exists(audio_path):
            raise ConfigError(f"Audio file not found: {audio_path}")
        try:
            audio = AudioFileClip(audio_path)
        except Exception as e:
            raise ConfigError(f"Error loading audio file: {str(e)}")
    
    # Create composite video
    try:
        video = clips[0] if len(clips) == 1 else CompositeVideoClip(clips)
        
        if audio:
            video = video.set_audio(audio)
        
        # Create a temporary file to store the video
        temp_output = "temp_output.mp4"
        video.write_videofile(temp_output, codec="libx264", fps=fps)
        
        # Add the configuration as metadata
        _add_config_metadata(temp_output, config)
        
        # Read the file as bytes
        with open(temp_output, "rb") as f:
            video_bytes = f.read()
        
        # Clean up
        os.remove(temp_output)
        video.close()
        if audio:
            audio.close()
        
        return video_bytes
        
    except Exception as e:
        # Clean up on error
        if os.path.exists("temp_output.mp4"):
            os.remove("temp_output.mp4")
        raise ConfigError(f"Error rendering video: {str(e)}")

def saveVideo(video_bytes: bytes, output_path: str) -> None:
    """
    Save video bytes to a file.
    
    Args:
        video_bytes (bytes): The video data in bytes format.
        output_path (str): The path where the video should be saved.
    """
    with open(output_path, "wb") as f:
        f.write(video_bytes)
