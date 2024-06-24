import whisper
import torch
import pyannote.audio
import contextlib
import wave
import datetime
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from pyannote.audio.pipelines.speaker_verification import PretrainedSpeakerEmbedding
from pyannote.audio import Audio
from pyannote.core import Segment
import gc
import os

class AudioTranscriber:
    def __init__(self, path, num_speakers=1, language='Spanish', model_size='tiny'):
        """
        Initialize the AudioTranscriber.

        :param path: Path to the input audio file.
        :param num_speakers: Number of speakers in the audio.
        :param language: Language of the audio.
        :param model_size: Size of the Whisper model to use.
        """
        self.path = path
        self.num_speakers = num_speakers
        self.language = language
        self.model_size = model_size
        self.audio = Audio()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.embedding_model = PretrainedSpeakerEmbedding(
            "speechbrain/spkrec-ecapa-voxceleb", device=self.device)
        self.model = whisper.load_model(model_size)
        if path[-3:] != 'wav':
            self.path = self.convert_to_wav(path)

    def convert_to_wav(self, path):
        """
        Convert the input audio file to WAV format if it is not already in WAV format.

        :param path: Path to the input audio file.
        :return: Path to the converted WAV file.
        """
        filename = path.rsplit('.', 1)[0]
        new_path = f"{filename}.wav"
        if not os.path.exists(new_path):
            subprocess.call(['ffmpeg', '-i', path, new_path, '-y'])
        return new_path

    def transcribe(self):
        """
        Transcribe the audio file to text.

        :return: List of transcription segments with speaker labels.
        """
        try:
            result = self.model.transcribe(self.path)
            segments = result["segments"]
            with contextlib.closing(wave.open(self.path, 'r')) as f:
                frames = f.getnframes()
                rate = f.getframerate()
                duration = frames / float(rate)
            embeddings = self.get_embeddings(segments, duration)
            clustering = AgglomerativeClustering(self.num_speakers).fit(embeddings)
            labels = clustering.labels_
            for i in range(len(segments)):
                segments[i]["speaker"] = 'SPEAKER ' + str(labels[i] + 1)
            return segments
        except Exception as e:
            print(f"Error during transcription: {e}")
            return []

    def get_embeddings(self, segments, duration):
        """
        Get speaker embeddings for each segment in the audio.

        :param segments: List of transcription segments.
        :param duration: Duration of the audio file.
        :return: Array of speaker embeddings.
        """
        embeddings = np.zeros(shape=(len(segments), 192))
        for i, segment in enumerate(segments):
            embeddings[i] = self.segment_embedding(segment, duration)
        return np.nan_to_num(embeddings)

    def segment_embedding(self, segment, duration):
        """
        Get the speaker embedding for a specific segment in the audio.

        :param segment: Transcription segment.
        :param duration: Duration of the audio file.
        :return: Speaker embedding for the segment.
        """
        start = segment["start"]
        end = min(duration, segment["end"])
        clip = Segment(start, end)
        waveform, sample_rate = self.audio.crop(self.path, clip)
        return self.embedding_model(waveform[None])

    def save_transcription(self, segments, output_filename):
        """
        Save the transcription to a text file.

        :param segments: List of transcription segments with speaker labels.
        :param output_filename: Path to save the transcription text file.
        """
        try:
            with open(output_filename, "w") as f:
                for (i, segment) in enumerate(segments):
                    if i == 0 or segments[i - 1]["speaker"] != segment["speaker"]:
                        f.write("\n" + segment["speaker"] + ' ' + str(datetime.timedelta(seconds=round(segment["start"]))) + '\n')
                    f.write(segment["text"][1:] + ' ')
            print(f"Transcription saved to {output_filename}")
        except Exception as e:
            print(f"Error saving transcription: {e}")
