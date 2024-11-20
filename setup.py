from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="vidkit",
    version="0.1.1",
    author="Carter Stach",
    author_email="carter.stach@gmail.com",  # Replace with your email
    description="A Python package for generating videos from JSON specifications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SpyC0der77/vidkit",  # Replace with your repository URL
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.6",
    install_requires=[
        "moviepy>=2.0.0",
        "Pillow>=9.2.0",
        "numpy>=1.25.0",
        "mutagen>=1.45.0"
    ],
    keywords="video generation, json, moviepy, video editing",
)
