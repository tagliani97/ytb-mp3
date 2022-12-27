# import pytest
# import os
# from artist import RequestArtist



# def pytest_generate_tests(metafunc):
#     idlist = []
#     argvalues = []
#     for scenario in metafunc.cls.scenarios:
#         idlist.append(scenario[0])
#         items = scenario[1].items()
#         argnames = [x[0] for x in items]
#         argvalues.append([x[1] for x in items])
#     metafunc.parametrize(argnames, argvalues, ids=idlist, scope="class")


# scenario_basic = (
#     "basic",
#     {"artist": "ana", "music": 0, "name_music": "They say"},
# )
# scenario_intermediate = (
#     "intermediate",
#     {"artist": "ana", "music": 0, "name_music": "They say, The trooper"},
# )
# scenario_advanced_1 = (
#     "advanced1",
#     {"artist": "ana", "music": 2, "name_music": "They say"},
# )
# scenario_advanced_2 = (
#     "advanced2",
#     {"artist": "ana, metallica, iron maden", "music": 5, "name_music": "They say, Rockstar"},
# )


# class TestWithScenariosArtist:
#     scenarios = [scenario_basic]

#     def test_request_artist_in_letras_br(self, artist, music, name_music):
#         compare = RequestArtist(
#             artist,
#             music,
#             name_music,
#         ).request_letras_mus_br()
#         assert str(compare.status_code) == "200"

#     # def test_consume_artist_in_letras_br(self, artist, music, name_music):
#     #     if music:
#     #         expected = music
#     #         list_compare = Download(
#     #             artist,
#     #             music,
#     #             name_music,
#     #         ).consume_letras_mus_br()
#     #         assert len(list_compare) == expected

#     # def test_list_search_youtube_by_name_music(
#     #     self, artist, music, name_music
#     # ):
#     #     expected = name_music.split(",")
#     #     list_compare = Download(
#     #         artist,
#     #         music,
#     #         name_music,
#     #     ).download_youtube()
#     #     if music:
#     #         assert len(list_compare) == (music + len(expected))
#     #     else:
#     #         assert list_compare == expected

#     # def test_verify_file_path_mp4_mp3(self, artist, music, name_music):
#     #     expected = name_music.split(",")
#     #     path_mp3 = os.path.abspath("./mp3")
#     #     compare = Download(
#     #         artist,
#     #         music,
#     #         name_music,
#     #     ).convert_to_mp3_and_create_path()
#     #     for name_value in expected:
#     #         assert os.path.isfile(
#     #             "{0}/{1}.mp3".format(path_mp3, name_value.strip())
#     #         )

#     # def test_download_artist_in_letras_br(self, artist, music, name_music):
#     #     if music:
#     #         path_mp3 = os.path.abspath("./mp3")
#     #         list_compare = Download(
#     #             artist,
#     #             music,
#     #             name_music,
#     #         ).consume_letras_mus_br()
#     #         for name_value in list_compare:
#     #             assert os.path.isfile(
#     #                 "{0}/{1}.mp3".format(path_mp3, name_value)
#     #             )
