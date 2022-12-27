from core.artist import RequestArtist
from youtubesearchpython import *
from pytube import YouTube
from core.artifact.utils import Utils


class Download:
    def __init__(self, artist, top_music, name_music):
        self.artist = artist
        self.top_music = top_music
        self.name_music = name_music
        self.lambda__to_strip = lambda x: x.strip()

    def prepare_download_artist(self):
        music_artist = dict()
        for artist in self.artist:
            artist = self.lambda__to_strip(artist)
            init_request = RequestArtist(artist, self.top_music)
            response = init_request.request_letras_mus_br()
            if self.top_music:
                music_artist[artist] = init_request.consume_letras_mus_br(
                    response
                )
        return music_artist

    def prepare_download(self):
        if self.artist:
            music_artist = self.prepare_download_artist()
        if self.name_music:
            music = [
                self.lambda__to_strip(name_music)
                for name_music in self.name_music
            ]
        return music_artist, music

    def download_result(self, search_youtube, music):
        result = YouTube(search_youtube.result().get("result")[0].get("link"))
        result.streams.filter(
            progressive=True, file_extension="mp4"
        ).first().download("mp4", filename="{}.mp4".format(music.strip()))

    def download_youtube(self, *args):
        try:
            for music in args:
                if isinstance(music, dict):
                    for artist, name_music_list in music.items():
                        for name_music in name_music_list:
                            search_youtube = Search(
                                f"{artist} {name_music} lyrics", limit=1
                            )
                            print(
                                f"Searching {artist} {name_music} lyrics youtube"
                            )
                            self.download_result(search_youtube, name_music)
                elif isinstance(music, list):
                    for name_music in music:
                        search_youtube = Search(
                            f"{name_music} lyrics", limit=1
                        )
                        print(f"Searching {name_music} lyrics youtube")
                        self.download_result(search_youtube, name_music)
        except Exception as e:
            print(f"Error {e}")
        else:
            Utils.convert_to_mp3_and_create_path()
