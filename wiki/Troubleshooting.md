# Troubleshooting Guide

This guide helps you diagnose and fix common issues when using VidKit.

## Common Issues and Solutions

### 1. Installation Issues

#### Package Not Found
```
ERROR: Could not find a version that satisfies the requirement vidkit
```

**Solutions:**
1. Update pip:
   ```bash
   python -m pip install --upgrade pip
   ```

2. Check Python version compatibility:
   ```bash
   python --version
   ```
   - VidKit requires Python 3.6 or higher

3. Install from source:
   ```bash
   git clone https://github.com/SpyC0der77/vidkit.git
   cd vidkit
   pip install -e .
   ```

### 2. Video Generation Issues

#### Memory Errors

**Symptoms:**
- MemoryError when processing large videos
- System becomes unresponsive

**Solutions:**
1. Reduce image resolution:
   ```python
   from PIL import Image
   
   def resize_image(image_path, max_size):
       with Image.open(image_path) as img:
           # Calculate new size maintaining aspect ratio
           ratio = min(max_size/max(img.size))
           new_size = tuple([int(x*ratio) for x in img.size])
           return img.resize(new_size, Image.LANCZOS)
   ```

2. Process in batches:
   ```python
   def process_in_batches(frames, batch_size=10):
       for i in range(0, len(frames), batch_size):
           batch = frames[i:i+batch_size]
           # Process batch
   ```

#### Audio Sync Issues

**Symptoms:**
- Audio and video out of sync
- Audio cuts off early

**Solutions:**
1. Match total frame duration to audio:
   ```python
   from moviepy.editor import AudioFileClip
   
   def get_audio_duration(audio_path):
       audio = AudioFileClip(audio_path)
       duration = audio.duration
       audio.close()
       return duration
   
   def adjust_frame_durations(config):
       if "audio" in config:
           audio_duration = get_audio_duration(config["audio"])
           total_duration = sum(frame["duration"] for frame in config["frames"])
           
           if total_duration != audio_duration:
               ratio = audio_duration / total_duration
               for frame in config["frames"]:
                   frame["duration"] *= ratio
   ```

### 3. File Format Issues

#### Image Format Errors

**Symptoms:**
- "Unsupported image format" errors
- Black frames in output

**Solutions:**
1. Convert images to supported format:
   ```python
   from PIL import Image
   
   def ensure_compatible_format(image_path):
       with Image.open(image_path) as img:
           if img.format not in ['JPEG', 'PNG']:
               new_path = image_path.rsplit('.', 1)[0] + '.jpg'
               img.convert('RGB').save(new_path, 'JPEG')
               return new_path
       return image_path
   ```

#### Video Format Issues

**Symptoms:**
- Output video won't play
- Codec errors

**Solutions:**
1. Check codec compatibility:
   ```python
   from moviepy.editor import VideoFileClip
   
   def verify_output(video_path):
       try:
           clip = VideoFileClip(video_path)
           clip.close()
           return True
       except Exception as e:
           print(f"Video verification failed: {e}")
           return False
   ```

### 4. Performance Issues

#### Slow Processing

**Symptoms:**
- Video generation takes too long
- High CPU usage

**Solutions:**
1. Profile the code:
   ```python
   import cProfile
   import pstats
   
   def profile_generation(config):
       profiler = cProfile.Profile()
       profiler.enable()
       
       video_bytes = renderVideo(config)
       
       profiler.disable()
       stats = pstats.Stats(profiler).sort_stats('cumulative')
       stats.print_stats()
   ```

2. Optimize image sizes:
   ```python
   def optimize_images(config):
       for frame in config["frames"]:
           with Image.open(frame["image"]) as img:
               if img.size > config["resolution"]:
                   # Resize if larger than needed
                   resize_image(frame["image"], config["resolution"])
   ```

### 5. Configuration Issues

#### Invalid Configuration

**Symptoms:**
- ValueError with configuration errors
- Unexpected video output

**Solutions:**
1. Validate configuration:
   ```python
   def validate_config(config):
       required = ["name", "format", "framerate", "resolution", "frames"]
       
       # Check required fields
       missing = [f for f in required if f not in config]
       if missing:
           raise ValueError(f"Missing required fields: {missing}")
           
       # Validate resolution
       if not isinstance(config["resolution"], list) or len(config["resolution"]) != 2:
           raise ValueError("Resolution must be [width, height]")
           
       # Validate framerate
       if not isinstance(config["framerate"], (int, float)) or config["framerate"] <= 0:
           raise ValueError("Framerate must be positive number")
   ```

## Debugging Tools

### 1. Debug Mode

```python
import logging

def enable_debug():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
```

### 2. System Check

```python
def system_check():
    import psutil
    import platform
    
    print(f"Python Version: {platform.python_version()}")
    print(f"Available Memory: {psutil.virtual_memory().available / (1024*1024*1024):.2f} GB")
    print(f"CPU Cores: {psutil.cpu_count()}")
```

## Getting Help

If you're still experiencing issues:

1. Check the [GitHub Issues](https://github.com/SpyC0der77/vidkit/issues) for similar problems
2. Include the following when reporting issues:
   - VidKit version
   - Python version
   - Complete error traceback
   - Minimal configuration that reproduces the issue
3. Use the [GitHub Discussions](https://github.com/SpyC0der77/vidkit/discussions) for general questions

## Related Topics

- [Error Handling](Error-Handling) for detailed error handling strategies
- [Configuration Reference](Configuration-Reference) for proper configuration
- [API Reference](API-Reference) for function specifications
