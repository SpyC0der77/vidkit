import json
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip

def create_video_from_json(json_data, output_file, audio_file=None):
    # Extract data from JSON
    name = json_data['name']
    format_ = json_data['format']
    framerate = json_data['framerate']
    resolution = json_data['resolution']
    frames = json_data['frames']
    
    # List to hold the ImageClip objects
    clips = []
    
    # Create ImageClip for each frame with the specified duration
    for frame in frames:
        image = frame['image']
        duration = frame['duration']
        
        # Create an ImageClip for each image
        clip = ImageClip(image, duration=duration)
        clip = clip.resize(newsize=(resolution[0], resolution[1]))  # Set resolution
        clips.append(clip)
    
    # Concatenate all the clips into a video
    video = concatenate_videoclips(clips, method="compose")
    
    # If an audio file is provided, add it to the video
    if audio_file:
        audio = AudioFileClip(audio_file)
        video = video.set_audio(audio)
    
    # Set framerate and write the video file
    video.write_videofile(f"{name}.{format_}", fps=framerate)

# Load the JSON data from video.json
with open("video.json", "r") as file:
    video_data = json.load(file)

# Call the function to create the video and add audio
create_video_from_json(video_data, "output.mp4", audio_file=video_data["audio"])
