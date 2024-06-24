
### `audio_converter.py`
```python
import subprocess
import os

def convert_to_wav(input_path, output_path):
    """
    Convert an audio file to WAV format using ffmpeg.

    :param input_path: Path to the input audio file.
    :param output_path: Path to save the converted WAV file.
    """
    if not os.path.exists(input_path):
        print(f"Error: The input file does not exist at {input_path}")
        return

    try:
        command = [
            'ffmpeg',
            '-i', input_path,
            output_path,
            '-y'
        ]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            print(f"Error during audio conversion: {result.stderr.decode()}")
        else:
            print(f"Audio file converted to {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during audio conversion: {e}")
