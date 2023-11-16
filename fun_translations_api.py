"""
API Fun Translations usada para traduzir um texto informado para a
linguagem fictícia do personagem Yoda, de Star Wars.
"""
import requests

url = 'https://api.funtranslations.com/translate/yoda.json'

texto = input('Digite o texto que deseja traduzir para Yoda: ')

payload = {
    'text': texto
}

response = requests.post(url, data=payload)

if response.status_code == 200:
    data = response.json()
    yoda_translated = data['contents']['translated']
    print(f'Tradução yoda: {yoda_translated}')
else:
    print(f'Erro de conexão: {response.status_code}')


