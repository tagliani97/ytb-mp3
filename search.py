from download import Download


class Control:
    def __init__(self, artista, top_music, name_music):
        self.artista = artista
        self.top_music = top_music
        self.name_music = name_music

    @property
    def artista(self):
        return self._artista

    @artista.setter
    def artista(self, value):
        if value and isinstance(value, str):
            self._artista = value.split(",")
        else:
            self._artista = None

    @property
    def name_music(self):
        return self._name_music

    @name_music.setter
    def name_music(self, value):
        if value and isinstance(value, str):
            self._name_music = value.split(",")
        else:
            self._name_music = []

    @property
    def top_music(self):
        return self._top_music

    @top_music.setter
    def top_music(self, value):
        if value != 0 and isinstance(value, int):
            self._top_music = value
        else:
            self._top_music = None

    def init_download(self):
        init_download = Download(
            self._artista, self._top_music, self._name_music
        )
        music_artist, music = init_download.prepare_download()
        init_download.download_youtube(music_artist, music)
        return init_download


Control("metallica", 10,"eye of beholder").init_download()