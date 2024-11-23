# Error Handling

This guide covers common errors you might encounter when using VidKit and how to handle them.

## Common Exceptions

### 1. Configuration Errors

```python
try:
    video_bytes = renderVideo(config)
except ValueError as e:
    if "framerate" in str(e):
        print("Invalid framerate specified")
    elif "resolution" in str(e):
        print("Invalid resolution format")
    else:
        print(f"Configuration error: {e}")
```

Common configuration errors:
- Missing required fields
- Invalid value types
- Out of range values
- Malformed JSON

### 2. File-Related Errors

```python
try:
    video_bytes = renderVideo(config)
except FileNotFoundError as e:
    if "image" in str(e):
        print(f"Image file not found: {e}")
    elif "audio" in str(e):
        print(f"Audio file not found: {e}")
    else:
        print(f"File not found: {e}")
```

Common file errors:
- Missing image files
- Missing audio files
- Invalid file paths
- Permission issues

### 3. Memory Errors

```python
try:
    video_bytes = renderVideo(config)
except MemoryError:
    print("Not enough memory to process video")
    # Try reducing resolution or splitting into smaller segments
```

Memory optimization tips:
- Reduce image resolution
- Process fewer frames at once
- Free unused resources
- Use streaming when possible

### 4. Output Errors

```python
try:
    saveVideo(video_bytes, "output.mp4")
except OSError as e:
    if "space" in str(e).lower():
        print("Not enough disk space")
    elif "permission" in str(e).lower():
        print("Permission denied")
    else:
        print(f"Output error: {e}")
```

Common output errors:
- Insufficient disk space
- Permission denied
- Invalid output path
- File already exists

## Best Practices

### 1. Comprehensive Error Handling

```python
from vidkit import renderVideo, saveVideo

def generate_video(config, output_path):
    try:
        # Validate configuration
        if not isinstance(config, dict):
            raise TypeError("Configuration must be a dictionary")
            
        # Generate video
        video_bytes = renderVideo(config)
        
        # Save video
        saveVideo(video_bytes, output_path)
        
        return True
        
    except ValueError as e:
        print(f"Configuration error: {e}")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except OSError as e:
        print(f"System error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        
    return False
```

### 2. Validation Before Processing

```python
def validate_config(config):
    required_fields = ["name", "format", "framerate", "resolution", "frames"]
    
    # Check required fields
    for field in required_fields:
        if field not in config:
            raise ValueError(f"Missing required field: {field}")
    
    # Validate framerate
    if not isinstance(config["framerate"], (int, float)) or config["framerate"] <= 0:
        raise ValueError("Framerate must be a positive number")
    
    # Validate resolution
    if not isinstance(config["resolution"], list) or len(config["resolution"]) != 2:
        raise ValueError("Resolution must be a list of [width, height]")
    
    # Validate frames
    if not config["frames"]:
        raise ValueError("At least one frame is required")
```

### 3. Cleanup on Error

```python
import os

def safe_video_generation(config, output_path):
    temp_files = []
    try:
        # Generate video
        video_bytes = renderVideo(config)
        saveVideo(video_bytes, output_path)
        
    except Exception as e:
        # Clean up any temporary files
        for file in temp_files:
            try:
                if os.path.exists(file):
                    os.remove(file)
            except Exception:
                pass
        raise e
```

## Debugging Tips

1. **Enable Verbose Logging**
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   ```

2. **Check File Paths**
   ```python
   import os
   
   def verify_paths(config):
       for frame in config["frames"]:
           if not os.path.exists(frame["image"]):
               print(f"Warning: Image not found: {frame['image']}")
   ```

3. **Memory Monitoring**
   ```python
   import psutil
   
   def check_memory():
       memory = psutil.virtual_memory()
       if memory.percent > 90:
           print("Warning: Low memory")
   ```

## Related Topics

- [Configuration Reference](Configuration-Reference) for proper config format
- [API Reference](API-Reference) for function specifications
- [Troubleshooting](Troubleshooting) for common issues
