import asyncio
import requests
from re import compile


API_URL_PATTERN = compile(r'https:\/\/media\.radiofrance-podcast\.net[^"]*\.(m4a|mp3)')


async def save_podcast(file_path: str, link: str) -> None:
    with requests.get(link, stream=True) as response:
        response.raise_for_status()
        with open(file_path, "wb") as fp:
            for chunk in response.iter_content(chunk_size=8192):
                fp.write(chunk)
    print(f"Téléchargement réussi ! {file_path}")


def get_podcast_name(user_url, media_url) -> str:
    user_url = user_url.split("/")
    user_url = "-".join(user_url[5:])
    user_url = "-".join(user_url.split("-")[:-1])

    if media_url.endswith(".m4a"):
        ext = ".m4a"
    elif media_url.endswith(".mp3"):
        ext = ".mp3"
    else:
        ext = ""
    
    return user_url.replace("-", " ") + ext



def get_podcast_api_url(user_url):
    """Searches the api url for the podcast in the page source code."""
    response = requests.get(user_url)
    response.raise_for_status()
    result = API_URL_PATTERN.search(response.text)
    if result:
        return result[0]
    else:
        raise Exception(f"Une erreur s'est produite lors du téléchargement : {user_url}")
