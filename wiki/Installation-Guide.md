# Installation Guide

## Requirements

Before installing VidKit, ensure you have the following prerequisites:

- Python >= 3.6
- pip (Python package installer)

## Dependencies

VidKit requires the following Python packages:

- moviepy >= 2.0.0
- Pillow >= 9.2.0
- numpy >= 1.25.0
- mutagen >= 1.45.0

Don't worry about installing these manually - they will be automatically installed when you install VidKit.

## Installation Methods

### 1. Using pip (Recommended)

The simplest way to install VidKit is using pip:

```bash
pip install vidkit
```

### 2. Installing from Source

If you want to install the latest development version:

```bash
git clone https://github.com/SpyC0der77/vidkit.git
cd vidkit
pip install -e .
```

### 3. Development Installation

For development purposes, install with additional development dependencies:

```bash
pip install -e ".[dev]"
```

## Verifying Installation

To verify that VidKit is installed correctly, run Python and try importing it:

```python
from vidkit import renderVideo
print("VidKit installed successfully!")
```

## Troubleshooting

If you encounter any installation issues:

1. **Dependency Conflicts**
   ```bash
   pip install --upgrade vidkit
   ```

2. **Permission Issues**
   ```bash
   pip install --user vidkit
   ```

3. **Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install vidkit
   ```

## Next Steps

Once installed, check out the [Quick Start Guide](Quick-Start-Guide) to begin using VidKit.
