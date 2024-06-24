# Speech-to-Text-Transcription-Tool-v2
A robust and efficient tool for transcribing audio files into text using advanced machine learning models. This repository includes functionality for converting audio formats, extracting specific segments, and identifying speakers.

## Description
This repository provides a comprehensive tool for converting audio files to text. It leverages state-of-the-art machine learning models to deliver accurate and efficient transcriptions. Key features include:

- **Audio Format Conversion:** Easily convert audio files between different formats (e.g., MP3 to WAV).
- **Segment Extraction:** Extract specific segments from audio files for targeted transcription.
- **Speaker Identification:** Identify and label different speakers in the audio.

## Features
- **Easy-to-use Interface:** Simplified commands for audio processing and transcription.
- **High Accuracy:** Utilizes advanced models like OpenAI's Whisper for precise transcriptions.
- **Customizable Parameters:** Adjust settings like language, model size, and number of speakers.
- **Memory Efficient:** Handles large audio files efficiently by processing in segments.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/manuelarguelles/speechtotext_v2.git
    cd speechtotext_v2
    ```
2. Install the necessary packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
### Converting Audio Format
```python
from audio_converter import convert_to_wav

convert_to_wav('path/to/input.mp3', 'path/to/output.wav')
