# VidKit

A Python library for rendering MP4 video from image configurations, optionally adding audio and storing the configuration in MP4 metadata.

## Install from source

```bash
git clone https://github.com/SpyC0der77/vidkit.git
cd vidkit
python -m pip install -e .
```

The package metadata declares Python 3.6+, but dependencies can require newer Python versions. Use a current Python environment and review dependency compatibility before rendering.

## Current compatibility limitation

The repo declares `moviepy>=2.0.0`, while [`vidkit/core.py`](vidkit/core.py) imports `moviepy.editor` and calls MoviePy 1.x methods such as `set_duration`, `resize`, and `set_audio`. A clean install with MoviePy 2.x therefore needs a code migration or a compatible dependency environment. The example below documents the library API; it does not resolve that incompatibility.

## Example

```python
from vidkit import renderVideo, saveVideo, get_config

config = {
    "name": "my_video",
    "format": "mp4",
    "framerate": 30,
    "resolution": [1280, 720],
    "frames": [{"image": "frame.jpg", "duration": 5}],
    "audio": "background.mp3",
}

video_bytes = renderVideo(config)
saveVideo(video_bytes, "output.mp4")
print(get_config("output.mp4"))
```

Remove `audio` for a silent video. Image and audio paths resolve relative to the working directory. `renderVideo` accepts a dictionary or a JSON string and returns bytes; `saveVideo` writes them to disk.

## Configuration

| Field | Value |
| --- | --- |
| `name` | Required video name |
| `format` | Required format field; the renderer currently writes MP4 |
| `framerate` | Required frames per second |
| `resolution` | Required `[width, height]` array |
| `frames` | Required non-empty list of image objects |
| `frames[].image` | Required existing image path |
| `frames[].duration` | Clip duration in seconds |
| `audio` | Optional existing audio path |

Multiple image clips are currently combined with `CompositeVideoClip`, rather than concatenated into a sequential slideshow. The renderer uses a fixed `temp_output.mp4` in the working directory, so concurrent renders in the same directory can conflict. `get_config` raises `ValueError` if it cannot read the metadata.

## Development

The source is in [`vidkit/core.py`](vidkit/core.py), and package metadata is in [`setup.py`](setup.py). The repo does not currently include `test.py` or a `[dev]` dependency extra.

## License

[MIT](LICENSE).
