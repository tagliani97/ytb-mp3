import yaml
import os
import shutil
from moviepy.editor import *
from yaml.loader import SafeLoader


class ReadYmlPath:
    @staticmethod
    def read_path():
        config_filepath = "path.yml"
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, config_filepath)
        with open(filename) as f:
            yml_conf = yaml.load(f, Loader=SafeLoader)
        return yml_conf


class Utils:
    @staticmethod
    def map_errors(error):
        dict_map = {"404": "Incorrect name artist"}
        return dict_map.get(error)

    @staticmethod
    def convert_to_mp3_and_create_path():
        path_mp4 = ReadYmlPath.read_path().get("path_mp4")
        path_mp3 = ReadYmlPath.read_path().get("path_mp3")
        try:
            abs_path_mp4 = os.path.abspath(path_mp4)
            abs_path_mp3 = os.path.abspath(path_mp3)
            if not os.path.exists(abs_path_mp3):
                os.mkdir(abs_path_mp3)
            for file in os.listdir(path_mp4):
                file_path = f"{abs_path_mp4}/{file}"
                video = VideoFileClip(file_path)
                video.audio.write_audiofile(
                    "{}".format(file_path.replace("mp4", "mp3"))
                )
            shutil.rmtree(abs_path_mp4)
        except Exception as e:
            print(e)
