import pytest
from core.artist import RequestArtist

@pytest.mark.parametrize(
    "artist, expected",
    [("gabriel", 200), ("adsds", 404), ("a dd dd", 404)],
)
def test_request_artist_in_letras_br(artist, expected):
    compare = RequestArtist(
        artist,
        1,
    ).request_letras_mus_br()
    compare.consume_letras_mus_br(compare)
    assert compare.status_code == expected
