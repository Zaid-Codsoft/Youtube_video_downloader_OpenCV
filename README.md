# Video Downloader and Player

This project is a simple web application that allows users to download videos from various sources by providing a video URL. The frontend is built using HTML and JavaScript, while the backend is implemented in Python using Flask and the `yt-dlp` library.

## Features

- User-friendly interface for downloading videos.
- Displays a loading message while the video is being processed.
- Downloads videos in MP4 format.
- Plays the downloaded video using OpenCV.

## Prerequisites

Before running this application, ensure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) (a fork of youtube-dl)
- [OpenCV](https://opencv.org/) for video playback

You can install the required Python packages using pip:

```bash
pip install Flask yt-dlp opencv-python
git clone https://github.com/yourusername/video-downloader.git
cd video-downloader
python -m venv venv
