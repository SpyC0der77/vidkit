# VidKit 

A simple and powerful Python package for generating videos from JSON configurations. VidKit makes it easy to create videos by combining images, setting durations, and adding audio tracks.

## Installation

```bash
pip install vidkit
```

## Quick Start

```python
from vidkit import renderVideo

# Define your video configuration
config = {
    "name": "my_video",
    "format": "mp4",
    "fps": 30,
    "resolution": {
        "width": 1920,
        "height": 1080
    },
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

# Generate the video
video = renderVideo(config)

# Save to file
with open("output.mp4", "wb") as f:
    f.write(video)
```

## Features

- Simple JSON-based configuration
- Support for multiple image frames
- Audio track integration
- Fast video generation using moviepy
- Flexible resolution settings
- Configurable frame rates

## Configuration Options

The video configuration accepts the following parameters:

| Parameter | Type | Description | Required |
|-----------|------|-------------|-----------|
| name | string | Name of the video | Yes |
| format | string | Output format (currently 'mp4') | Yes |
| framerate | number | Frame rate in FPS | Yes |
| resolution | [width, height] | Video dimensions in pixels | Yes |
| frames | array | List of frame objects | Yes |
| audio | string | Path to audio file | No |

### Frame Object Properties

| Property | Type | Description | Required |
|----------|------|-------------|-----------|
| image | string | Path to image file | Yes |
| duration | number | Duration in seconds | Yes |

## Requirements

- Python >= 3.6
- moviepy >= 2.0.0
- Pillow >= 9.2.0
- numpy >= 1.25.0

## Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch
3. Submit a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created by Carter Stach ([@SpyC0der77](https://github.com/SpyC0der77))

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/SpyC0der77/vidgen/issues) on GitHub.
