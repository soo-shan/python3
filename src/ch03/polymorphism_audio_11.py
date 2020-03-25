class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")

        self.filename = filename


class MP3File(AudioFile):
    ext = "mp3"

    def play(self):
        print(f"playing {self.filename} as mp3")


class WavFile(AudioFile):
    ext = "wav"

    def play(self):
        print(f"playing {self.filename} as wav")


class OggFile(AudioFile):
    ext = "ogg"

    def play(self):
        print(f"playing {self.filename} as ogg")


# ogg_player = OggFile("myfile.ogg")
# ogg_player.play()
#
# mp3_player = MP3File("myfile.mp3")
# mp3_player.play()
#
# wav_player = WavFile("myfile.wav")
# wav_player.play()
#
# not_wav_file = WavFile("myfile.pdf")