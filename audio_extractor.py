import subprocess
import os

def extract_audio_segment(input_path, start_time, end_time, output_path):
    """
    Extract a segment from an audio file.

    :param input_path: Path to the input audio file.
    :param start_time: Start time of the segment in seconds.
    :param end_time: End time of the segment in seconds.
    :param output_path: Path to save the extracted audio segment.
    """
    if not os.path.exists(input_path):
        print(f"Error: The input file does not exist at {input_path}")
        return

    try:
        command = [
            'ffmpeg',
            '-i', input_path,
            '-ss', str(start_time),
            '-to', str(end_time),
            '-c', 'copy',
            output_path,
            '-y'
        ]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            print(f"Error during audio extraction: {result.stderr.decode()}")
        else:
            print(f"Audio segment saved to {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during audio extraction: {e}")
