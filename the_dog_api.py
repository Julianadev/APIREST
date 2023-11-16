"""
API The Dog obtém imagens aleatórias de cachorro
"""
import requests

url = 'https://api.thedogapi.com/v1/images/search?limit=10'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for imagem in data:
        img = imagem['url']
        print(img)
else:
    print(f'Erro de conexão: {response.status_code}')
