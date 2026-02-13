import asyncio
from pathlib import Path
from argparse import ArgumentParser
from re import compile
from .rfdl import * 

INPUT_URL_PATTERN = compile(r"^https:\/\/www\.radiofrance\.fr\/(franceculture|franceinter)\/podcasts.*[0-9]{7}$")


def create_parser() -> ArgumentParser:
    """Crée un analyseur syntaxique qui prend deux arguments : podcasts (obligatoire) et sortie (facultatif)."""
    parser = ArgumentParser(
        prog="rfdl",
        description="Un CLI simple qui permet de télécharger des podcasts depuis radiofrance"
    )
    parser.add_argument(
        "podcasts",
        help="Le ou les liens vers le ou les podcasts que vous souhaitez télécharger. Vous pouvez fournir plusieurs liens en les séparant par un saut de ligne."
    )
    parser.add_argument(
        "-o", "--output",
        default=".",  #  current directory
        help="Le dossier de sortie dans lequel vous souhaitez enregistrer vos téléchargements. Par défaut, il s'agit du répertoire du dossier actuel."
        )
    return parser


async def cli() -> None:
    """Contains all the logic of the cli."""
    parser = create_parser()
    args = parser.parse_args()
    podcasts_links: str = args.podcasts
    output_folder: Path = Path.cwd() / args.output
    output_folder.mkdir(exist_ok=True)
    
    podcasts_links = podcasts_links.strip().split("\n")
    for podcast_link in podcasts_links:
        if INPUT_URL_PATTERN.match(podcast_link):
            download_url = get_podcast_api_url(podcast_link)
            file_path: Path = output_folder/get_podcast_name(podcast_link)
            await save_podcast(file_path, download_url)
        else:
            print(f"[ERREUR] L'URL donnée est invalide:\n {podcast_link}")


def run():
    """Exécute l'interface CLI de manière asynchrone."""
    asyncio.run(cli())