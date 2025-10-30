import requests

URL_BASE = "https://pax.ulaval.ca/quoridor/api/a25"

def créer_une_partie(IDUL, secret):
    try:
        reponses = requests.post(f"{URL_BASE}/jeux", auth=(IDUL, secret))

        if reponses.status_code == 200:
            informations = reponses.json()
            return informations['id'], informations
        elif reponses.status_code == 401:
            raise PermissionError(reponses.text)
        elif reponses.status_code == 406:
            raise RuntimeError(reponses.text)
        else:
            raise ConnectionError()
