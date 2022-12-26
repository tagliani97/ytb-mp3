import os
import shutil
from moviepy.editor import *
from youtubesearchpython import *
from pytube import YouTube
import requests
from bs4 import BeautifulSoup


class Download:
    def __init__(self, artista, top_music, name_music):
        self.artista = artista
        self.top_music = top_music
        self.name_music = name_music
        self.path_mp4 = "./mp4"

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

    def convert_to_mp3(self):
        try:
            abs_path = os.path.abspath(f"{self.path_mp4}")
            for file in os.listdir(self.path_mp4):
                file_path = f"{abs_path}/{file}"
                video = VideoFileClip(file_path)
                path_mp3 = "{}".format(file_path.replace("mp4", "mp3"))
                video.audio.write_audiofile(
                    path_mp3
                )
            shutil.rmtree(abs_path)
        except Exception as e:
            print(e)
        
    def map_errors(self, error):
        dict_map = {
            "404": "Nome do artista incorreto"
        }
        return dict_map.get(error)

    def consume_letras_br(self):

        list_music = []
        url = f"https://www.letras.mus.br/{self.artista}/mais_acessadas.html"
        try:
            page = requests.get(url)
            error_print = self.map_errors(page)
            soup = BeautifulSoup(page.content, "html.parser").find_all(
                "div", class_="list-container"
            )
            
            for job_element in soup:
                location_element = job_element.find_all(
                    "li",
                    class_="cnt-list-row -song is-visible",
                    limit=self.top_music,
                )
                for i in location_element:
                    company_element = i.find_all("a", class_="song-name")
                    list_music.append(company_element[0].select_one("span").text)
        except Exception as e:
            print(e)
        return list_music
    
    def download_youtube(self):

            list_music = []
            if self._top_music and self._name_music:
                list_music = self.consume_letras_br()
                list_music.append(self._name_music)
            elif self._top_music:
                list_music = self.consume_letras_br()
            elif self._name_music:
                list_music = self._name_music
            if list_music:               
                for musica in list_music:
                    print(musica)
                    try:
                        allSearch = Search(f"{self.artista} {musica} lyrics", limit=1)
                        print(
                            f"Realizando busca {self.artista} {musica} lyrics youtube"
                        )
                        result = YouTube(
                            allSearch.result().get("result")[0].get("link")
                        )
                        result.streams.filter(
                            progressive=True, file_extension="mp4"
                        ).first().download("mp4", filename=f"{musica}.mp4")
                    except Exception as e:
                        print("Error {e}")
                self.convert_to_mp3()
                return list_music
