import os
import shutil
from moviepy.editor import *
from youtubesearchpython import *
from pytube import YouTube
import requests
from bs4 import BeautifulSoup

def search_yotube(lista_musica, artista):
    for musica in lista_musica:
        try:
            allSearch = Search(f"{artista} {musica} lyrics", limit=1)
            print(f"Realizando busca {artista} {musica} lyrics youtube")
            result = YouTube(allSearch.result().get("result")[0].get("link"))
            result.streams.filter(
                progressive=True, file_extension="mp4"
            ).first().download("mp4", filename=f"{musica}.mp4")
        except Exception:
            pass

def convert_to_mp3():
    path_mp4 = "./mp4"
    try:
        for file in os.listdir(path_mp4):
            abs_path = os.path.abspath(f"{path_mp4}")
            file_path = f"{abs_path}/{file}"
            video = VideoFileClip(file_path)
            video.audio.write_audiofile(
                "./mp3/{0}".format(file.replace("mp4", "mp3"))
            )
        shutil.rmtree(abs_path)
    except Exception:
        pass

def url(artista, qtd):
    lista_musica = []
    url = f"https://www.letras.mus.br/{artista}/mais_acessadas.html"
    page = requests.get(url)
    print(page)
    if "404" in page:
        print("Nome do artista incorreto")
    soup = BeautifulSoup(page.content, 'html.parser').find_all("div", class_="list-container")
    for job_element in soup:
        location_element = job_element.find_all("li", class_="cnt-list-row -song is-visible", limit=qtd)
        for i in location_element:
            company_element = i.find_all("a", class_="song-name")
            lista_musica.append(company_element[0].select_one("span").text)
    print(lista_musica)
    return lista_musica

artista = str(input("Nome do artista: "))
if " " in artista:
    artista = artista.replace(" ","-")
top_music = int(input("Numero top musica: "))
lista_musica = url(artista, top_music)
search_yotube(lista_musica, artista)
convert_to_mp3()
