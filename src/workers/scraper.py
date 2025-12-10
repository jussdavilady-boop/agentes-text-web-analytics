"""
Scraper Agent
-------------
Extrae texto visible desde una página web.
"""

import requests
from bs4 import BeautifulSoup


def simple_scrape(url: str):
    """
    Scraper simple con manejo de errores.
    Solo extrae texto visible y retorna un máximo de 1000 caracteres.
    """
    try:
        response = requests.get(url, timeout=10, headers={"User-Agent": "AgentDemo/1.0"})
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        text = " ".join(soup.stripped_strings)

        return {
            "url": url,
            "text": text[:1000]  # límite de seguridad
        }

    except Exception as e:
        return {
            "url": url,
            "text": "",
            "error": str(e)
        }
