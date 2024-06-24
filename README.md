# Speech-to-Text Transcription Tool v2

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

# Convert an MP3 file to WAV format
convert_to_wav('path/to/input.mp3', 'path/to/output.wav')



## Extracting Audio Segment
python
Copiar código
from audio_extractor import extract_audio_segment

# Extract a segment from an audio file
extract_audio_segment('path/to/input.wav', start_time=120, end_time=720, output_path='path/to/output_segment.wav')
Transcribing Audio
python
Copiar código
from transcriber import AudioTranscriber

## Create an instance of the AudioTranscriber
transcriber = AudioTranscriber('path/to/audio.wav', model_size='tiny', num_speakers=1)

# Transcribe the audio file
segments = transcriber.transcribe()

# Save the transcription to a text file
transcriber.save_transcription(segments, 'path/to/transcription.txt')
