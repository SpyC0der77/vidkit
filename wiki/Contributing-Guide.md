# Contributing Guide

Thank you for your interest in contributing to VidKit! This guide will help you get started with contributing to the project.

## Getting Started

### 1. Setting Up Development Environment

1. Fork the repository:
   - Visit [VidKit on GitHub](https://github.com/SpyC0der77/vidkit)
   - Click the "Fork" button

2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/vidkit.git
   cd vidkit
   ```

3. Set up development environment:
   ```bash
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install development dependencies
   pip install -e ".[dev]"
   ```

### 2. Running Tests

```bash
# Run all tests
python test.py

# Run specific test
python -m unittest test.py -k test_video_generation
```

## Development Guidelines

### Code Style

1. Follow PEP 8 guidelines
2. Use type hints where possible
3. Document all functions and classes
4. Keep functions focused and small
5. Write descriptive variable names

Example:
```python
from typing import Dict, Any

def process_config(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Process and validate video configuration.
    
    Args:
        config: Dictionary containing video configuration
        
    Returns:
        Processed configuration dictionary
        
    Raises:
        ValueError: If configuration is invalid
    """
    # Implementation
    pass
```

### Documentation

1. Update docstrings for any new functions
2. Add type hints
3. Include examples in docstrings
4. Update README.md if needed
5. Add new wiki pages for major features

### Testing

1. Write tests for new features
2. Update existing tests when changing behavior
3. Ensure all tests pass before submitting PR
4. Add edge cases to tests

Example test:
```python
import unittest
from vidkit import renderVideo

class TestVideoGeneration(unittest.TestCase):
    def test_invalid_config(self):
        """Test that invalid config raises ValueError"""
        invalid_config = {
            "name": "test",
            # Missing required fields
        }
        with self.assertRaises(ValueError):
            renderVideo(invalid_config)
```

## Pull Request Process

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes:
   - Write code
   - Add tests
   - Update documentation

3. Commit your changes:
   ```bash
   git add .
   git commit -m "Add feature: description"
   ```

4. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

5. Create Pull Request:
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Fill out the PR template

### PR Requirements

- [ ] Code follows style guidelines
- [ ] Tests are added/updated
- [ ] Documentation is updated
- [ ] All tests pass
- [ ] PR description explains changes
- [ ] Version number updated if needed

## Release Process

1. Update version number in `setup.py`
2. Update CHANGELOG.md
3. Create release notes
4. Tag release in git
5. Build and upload to PyPI

Example version bump:
```python
# setup.py
setup(
    name="vidkit",
    version="0.1.3",  # Increment version
    ...
)
```

## Community Guidelines

1. Be respectful and inclusive
2. Help others when possible
3. Report bugs and issues
4. Follow code of conduct
5. Ask questions in discussions

## Additional Resources

- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Python Testing Guide](https://docs.python.org/3/library/unittest.html)
- [Type Hints Guide](https://docs.python.org/3/library/typing.html)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)

## Getting Help

- Open an issue for bugs
- Use discussions for questions
- Join our community chat
- Contact maintainers

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
