from polymorphism_audio_11 import MP3File
class FlacFile:
    def __init__(self, filename):
        if not filename.endswith(".flac"):
            raise Exception("Invalid file format")

        self.filename = filename

    def play(self):
        print(f"playing {self.filename} as flac")


mp3_player = MP3File("myfile.mp3")
mp3_player.play()
flac_player = FlacFile("myfile.flac")
flac_player.play()