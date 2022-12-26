import pytest
from search import Download

@pytest.fixture(
    params=["artist", "top_music", "name_music"],
    ids=["artist", "top_music", "name_music"]
)
def test_mount_list_search(request):
    print(request.param['artist'])
    assert False
    # list_compare, videoid = Download(fixture_value).download_youtube()
    # assert videoid != ""
    # assert list_compare[0] == name_music

# def test_artist_list
