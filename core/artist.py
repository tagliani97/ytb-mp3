import time
import requests
from bs4 import BeautifulSoup
from artifact.utils import Utils


class RequestArtist:
    def __init__(self, artist, top_music):
        self.artist = artist
        self.top_music = top_music

    def request_letras_mus_br(self):
        try:
            url = (
                f"https://www.letras.mus.br/{self.artist}/mais_acessadas.html"
            )
            time.sleep(2)
            page = requests.get(url)
            error_print = Utils.map_errors(str(page.status_code))
            if error_print:
                raise ValueError("Incorrect artist name")
        except ValueError as e:
            raise (e)
        else:
            return page

    def consume_letras_mus_br(self, page):

        list_music = []
        try:
            soup = BeautifulSoup(page.content, "html.parser").find_all(
                "div", class_="list-container"
            )
            for job_element in soup:
                location_element = job_element.find_all(
                    "li",
                    class_="cnt-list-row -song is-visible",
                    limit=self.top_music,
                )
                for song in location_element:
                    company_element = song.find_all("a", class_="song-name")
                    list_music.append(
                        company_element[0].select_one("span").text
                    )
        except Exception as e:
            print(e)
        else:
            return list_music
