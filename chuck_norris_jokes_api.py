"""
API que fornece piadas aleatórias relacionadas a Chuck Norris
"""
import requests

url = 'https://api.chucknorris.io/jokes/random/'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    conselho_chucknorris = data['value']
    print(f'Conselho Chuck Norris: {conselho_chucknorris}')
else:
    print(f'Erro de conexão: {response.status_code}')
