import json
from typing import Union, Dict, Any
from moviepy.editor import VideoFileClip, ImageClip, AudioFileClip, CompositeVideoClip
from PIL import Image
import numpy as np
import io
from mutagen.mp4 import MP4, MP4FreeForm

def _add_config_metadata(output_path: str, config: Dict[str, Any]) -> None:
    """Add the configuration as metadata to the MP4 file."""
    video = MP4(output_path)
    config_json = json.dumps(config).encode('utf-8')
    video["----:com.vidkit.config"] = MP4FreeForm(config_json)
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
        if "----:com.vidkit.config" not in video:
            raise KeyError("No VidKit configuration found in metadata")
        config_json = video["----:com.vidkit.config"][0]
        return json.loads(config_json.decode('utf-8'))
    except Exception as e:
        raise ValueError(f"Failed to read configuration from {filepath}: {str(e)}")

def renderVideo(config: Union[Dict, str]) -> bytes:
    """
    Generate a video based on the provided configuration.
    
    Args:
        config: Either a dictionary containing the video configuration or a JSON string
        
    Returns:
        bytes: The rendered video as bytes that can be written to a file
    """
    # If config is a string, parse it as JSON
    if isinstance(config, str):
        config = json.loads(config)
    
    # Get video parameters
    fps = config.get("framerate", 30)
    width, height = config.get("resolution", [1920, 1080])
    
    # Initialize clips list
    clips = []
    
    # Process frames
    if "frames" in config:
        for frame_config in config["frames"]:
            clip = ImageClip(frame_config["image"])
            if "duration" in frame_config:
                clip = clip.set_duration(frame_config["duration"])
            clips.append(clip)
    
    # Process audio if specified
    audio = None
    if "audio" in config:
        audio = AudioFileClip(config["audio"])
    
    # Create composite video by concatenating clips
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
    import os
    os.remove(temp_output)
    video.close()
    if audio:
        audio.close()
    
    return video_bytes

def saveVideo(video_bytes: bytes, output_path: str) -> None:
    """
    Save video bytes to a file.
    
    Args:
        video_bytes (bytes): The video data in bytes format.
        output_path (str): The path where the video should be saved.
    """
    with open(output_path, "wb") as f:
        f.write(video_bytes)
