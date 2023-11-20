"""
API PUNAPI - Trocadilhos
"""
import requests

url = 'https://punapi.rest/api/pun'

response = requests.get(url)

try:
    if response.status_code == 200:
        data = response.json()

        if 'pun' in data:
            trocadilho = data['pun']
            print(f'Trocadilho: {trocadilho}')

        else:
            print('Erro nos dados')
except (KeyError, IndexError, ConnectionError) as e:
    print(f'Ocorreu um erro: {e}')
