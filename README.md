# VidKit 

A simple and powerful Python package for generating videos from JSON configurations. VidKit makes it easy to create videos by combining images, setting durations, and adding audio tracks.

## Installation

```bash
pip install vidkit
```

## Quick Start

```python
from vidkit import renderVideo, saveVideo

# Define your video configuration
config = {
    "name": "my_video",
    "format": "mp4",
    "framerate": 30,  # Note: 'framerate' instead of 'fps'
    "resolution": [1920, 1080],  # Note: array instead of object
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
    "audio": "background.mp3"
}

# Generate and save the video
video_bytes = renderVideo(config)
saveVideo(video_bytes, "output.mp4")
```

## Features

- Simple JSON-based configuration
- Support for multiple image frames
- Audio track integration
- Fast video generation using moviepy
- Flexible resolution settings
- Configurable frame rates
- Metadata preservation
- Error handling and validation

## Configuration Options

The video configuration accepts the following parameters:

| Parameter | Type | Description | Required | Default |
|-----------|------|-------------|-----------|---------|
| name | string | Name of the video | Yes | - |
| format | string | Output format (currently 'mp4') | Yes | - |
| framerate | number | Frame rate in FPS | Yes | - |
| resolution | [width, height] | Video dimensions in pixels | Yes | - |
| frames | array | List of frame objects | Yes | - |
| audio | string | Path to audio file | No | None |

### Frame Object Properties

| Property | Type | Description | Required | Default |
|----------|------|-------------|-----------|---------|
| image | string | Path to image file | Yes | - |
| duration | number | Duration in seconds | Yes | - |

## Advanced Usage

### 1. Error Handling

```python
from vidkit import renderVideo, saveVideo

try:
    video_bytes = renderVideo(config)
    saveVideo(video_bytes, "output.mp4")
except ValueError as e:
    print(f"Configuration error: {e}")
except FileNotFoundError as e:
    print(f"File not found: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
```

### 2. Retrieving Video Configuration

VidKit automatically stores the configuration in the video's metadata. You can retrieve it using:

```python
from vidkit import get_config

try:
    config = get_config("output.mp4")
    print("Video configuration:", config)
except KeyError:
    print("No VidKit configuration found in metadata")
except ValueError as e:
    print(f"Error reading configuration: {e}")
```

### 3. Configuration as JSON File

You can also store your configuration in a JSON file:

```python
import json
from vidkit import renderVideo

# Load configuration from file
with open("video_config.json", "r") as f:
    config = json.load(f)

# Generate video
video_bytes = renderVideo(config)
```

Example `video_config.json`:
```json
{
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
    "audio": "background.mp3"
}
```

## Common Issues and Solutions

1. **Image Not Found**
   - Ensure all image paths in the configuration are correct and accessible
   - Use absolute paths or paths relative to your script's location

2. **Audio Sync Issues**
   - Make sure the total duration of frames matches your audio duration
   - Use the same framerate throughout your project

3. **Memory Issues**
   - When working with high-resolution images, consider reducing their size
   - Process videos in smaller segments if needed

## Requirements

- Python >= 3.6
- moviepy >= 2.0.0
- Pillow >= 9.2.0
- numpy >= 1.25.0
- mutagen >= 1.45.0 (for metadata handling)

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the tests (`python test.py`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Setup

```bash
# Clone the repository
git clone https://github.com/SpyC0der77/vidkit.git
cd vidkit

# Install development dependencies
pip install -e ".[dev]"

# Run tests
python test.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created by Carter Stach ([@SpyC0der77](https://github.com/SpyC0der77))

## Support

- **Issues**: If you encounter any issues or have questions, please [open an issue](https://github.com/SpyC0der77/vidkit/issues) on GitHub
- **Discussions**: For general questions and discussions, use the [GitHub Discussions](https://github.com/SpyC0der77/vidkit/discussions) page
- **Security**: For security-related issues, please email carter.stach@gmail.com

## Changelog

### 0.1.2
- Fixed metadata handling in MP4 files
- Improved error messages
- Updated documentation

### 0.1.1
- Initial release
- Basic video generation functionality
- Audio support
- Metadata storage
