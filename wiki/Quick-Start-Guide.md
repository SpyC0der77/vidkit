# Quick Start Guide

This guide will help you get started with VidKit by walking through a simple example.

## Basic Usage

### 1. Import VidKit

```python
from vidkit import renderVideo, saveVideo
```

### 2. Create a Configuration

```python
config = {
    "name": "my_video",
    "format": "mp4",
    "framerate": 30,
    "resolution": [1920, 1080],
    "frames": [
        {
            "image": "frame1.jpg",
            "duration": 5
        },
        {
            "image": "frame2.jpg",
            "duration": 5
        }
    ],
    "audio": "background.mp3"  # Optional
}
```

### 3. Generate and Save the Video

```python
# Generate video
video_bytes = renderVideo(config)

# Save to file
saveVideo(video_bytes, "output.mp4")
```

## Complete Example

Here's a complete working example:

```python
from vidkit import renderVideo, saveVideo
from PIL import Image
import numpy as np

# Create test images
img1 = Image.new('RGB', (1920, 1080), color='red')
img1.save('frame1.jpg')

img2 = Image.new('RGB', (1920, 1080), color='blue')
img2.save('frame2.jpg')

# Define configuration
config = {
    "name": "test_video",
    "format": "mp4",
    "framerate": 30,
    "resolution": [1920, 1080],
    "frames": [
        {
            "image": "frame1.jpg",
            "duration": 2
        },
        {
            "image": "frame2.jpg",
            "duration": 2
        }
    ]
}

# Generate and save video
try:
    video_bytes = renderVideo(config)
    saveVideo(video_bytes, "output.mp4")
    print("Video generated successfully!")
except Exception as e:
    print(f"Error: {e}")
```

## Next Steps

- Check the [Configuration Reference](Configuration-Reference) for all available options
- Learn about [Advanced Usage](Advanced-Usage) features
- See [Error Handling](Error-Handling) for dealing with common issues
