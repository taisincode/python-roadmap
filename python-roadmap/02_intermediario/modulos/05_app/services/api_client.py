import requests
from utils.tratamento import tratar_erro

URL = "https://api.github.com"

def obter_dados():
    try:
        resposta = requests.get(URL, timeout=5)
        resposta.raise_for_status()  # levanta erro para status != 200
        return resposta.json()
    except requests.exceptions.RequestException as e:
        return tratar_erro(e)