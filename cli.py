import click
from core.search import Download

@click.command("download")
@click.option(
    "--artist", required=True, help="Name of the artist"
)
@click.option(
    "--top_music",
    default=0,
    required=False,
    type=int,
    help="Count of top music"
)
@click.option(
    "--name_music",
    default=None,
    required=False,
    type=str,
    help="Name music"
)
def download(artist, top_music, name_music):
    Download(artist, top_music, name_music).download_youtube()


if __name__ == "__main__":
    download()
