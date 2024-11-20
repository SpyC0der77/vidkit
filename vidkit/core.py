import json
from typing import Union, Dict
from moviepy.editor import VideoFileClip, ImageClip, AudioFileClip, CompositeVideoClip
from PIL import Image
import numpy as np
import io

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
