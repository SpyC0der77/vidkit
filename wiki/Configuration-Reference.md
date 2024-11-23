# Configuration Reference

This document provides a detailed reference for all configuration options in VidKit.

## Configuration Structure

```json
{
    "name": "string",
    "format": "string",
    "framerate": "number",
    "resolution": "[width, height]",
    "frames": "array",
    "audio": "string (optional)"
}
```

## Required Parameters

### name
- **Type**: string
- **Description**: Name of the video project
- **Example**: `"my_video"`

### format
- **Type**: string
- **Supported Values**: Currently only "mp4"
- **Example**: `"mp4"`

### framerate
- **Type**: number
- **Description**: Frames per second
- **Range**: 1-120
- **Example**: `30`

### resolution
- **Type**: array [width, height]
- **Description**: Video dimensions in pixels
- **Format**: `[width, height]`
- **Example**: `[1920, 1080]`

### frames
- **Type**: array of frame objects
- **Description**: List of frames to include in the video
- **Example**:
  ```json
  "frames": [
      {
          "image": "frame1.jpg",
          "duration": 5
      }
  ]
  ```

## Optional Parameters

### audio
- **Type**: string
- **Description**: Path to audio file
- **Supported Formats**: mp3, wav
- **Example**: `"background.mp3"`

## Frame Object Properties

Each frame in the `frames` array must have these properties:

### image
- **Type**: string
- **Description**: Path to image file
- **Supported Formats**: jpg, jpeg, png
- **Example**: `"frame1.jpg"`

### duration
- **Type**: number
- **Description**: Duration in seconds
- **Range**: > 0
- **Example**: `5`

## Complete Example

```json
{
    "name": "promotional_video",
    "format": "mp4",
    "framerate": 30,
    "resolution": [1920, 1080],
    "frames": [
        {
            "image": "intro.jpg",
            "duration": 3
        },
        {
            "image": "main_content.jpg",
            "duration": 5
        },
        {
            "image": "outro.jpg",
            "duration": 2
        }
    ],
    "audio": "background_music.mp3"
}
```

## Validation Rules

1. **name**: Must be a non-empty string
2. **format**: Must be "mp4"
3. **framerate**: Must be a positive number
4. **resolution**: Both width and height must be positive integers
5. **frames**: Must contain at least one frame
6. **audio**: If provided, file must exist and be in a supported format

## Best Practices

1. Use consistent image resolutions matching your video resolution
2. Keep frame durations reasonable (typically 1-10 seconds)
3. Ensure total video duration matches audio duration if using audio
4. Use relative paths for image and audio files
5. Keep filenames simple and avoid special characters

## Related Topics

- [Advanced Usage](Advanced-Usage) for more complex configurations
- [Error Handling](Error-Handling) for dealing with configuration errors
- [Troubleshooting](Troubleshooting) for common configuration issues
