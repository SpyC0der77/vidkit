# API Reference

This document provides detailed information about VidKit's API functions.

## Core Functions

### renderVideo

```python
def renderVideo(config: Union[Dict, str]) -> bytes
```

Generates a video based on the provided configuration.

#### Parameters
- **config**: Either a dictionary containing the video configuration or a JSON string
  - See [Configuration Reference](Configuration-Reference) for detailed config options

#### Returns
- **bytes**: The rendered video as bytes that can be written to a file

#### Raises
- **ValueError**: If configuration is invalid
- **FileNotFoundError**: If image or audio files are not found
- **TypeError**: If configuration format is incorrect

#### Example
```python
from vidkit import renderVideo

config = {
    "name": "test_video",
    "format": "mp4",
    "framerate": 30,
    "resolution": [1920, 1080],
    "frames": [
        {
            "image": "frame1.jpg",
            "duration": 2
        }
    ]
}

video_bytes = renderVideo(config)
```

### saveVideo

```python
def saveVideo(video_bytes: bytes, output_path: str) -> None
```

Saves video bytes to a file.

#### Parameters
- **video_bytes**: The video data in bytes format
- **output_path**: The path where the video should be saved

#### Raises
- **ValueError**: If video_bytes is invalid
- **OSError**: If unable to write to output_path

#### Example
```python
from vidkit import saveVideo

saveVideo(video_bytes, "output.mp4")
```

### get_config

```python
def get_config(filepath: str) -> Dict[str, Any]
```

Extract the configuration used to generate the video from its metadata.

#### Parameters
- **filepath**: Path to the MP4 file

#### Returns
- **dict**: The configuration used to generate the video

#### Raises
- **KeyError**: If no VidKit configuration is found in the metadata
- **ValueError**: If the file is not an MP4 file or doesn't exist

#### Example
```python
from vidkit import get_config

config = get_config("output.mp4")
print(config)
```

## Error Handling

All functions may raise these common exceptions:

### Common Exceptions

1. **ValueError**
   - Invalid configuration values
   - Invalid file formats
   - Invalid parameters

2. **FileNotFoundError**
   - Missing image files
   - Missing audio files
   - Invalid file paths

3. **OSError**
   - File permission issues
   - Disk space issues
   - I/O errors

4. **TypeError**
   - Invalid parameter types
   - Malformed configuration

## Best Practices

1. **Error Handling**
   ```python
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

2. **Configuration Validation**
   ```python
   from vidkit import renderVideo, get_config

   # Generate video
   video_bytes = renderVideo(config)
   saveVideo(video_bytes, "output.mp4")

   # Verify configuration was saved correctly
   saved_config = get_config("output.mp4")
   assert saved_config == config
   ```

## Related Topics

- [Quick Start Guide](Quick-Start-Guide) for basic usage
- [Configuration Reference](Configuration-Reference) for config options
- [Error Handling](Error-Handling) for detailed error handling strategies
