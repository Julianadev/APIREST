"""
API Kanye West obtém conselhos de Kanye West
"""
import requests

url = 'https://api.kanye.rest'

response = requests.get(url)

if response.status_code == 200:
    df = response.json()

    if 'quote' in df:
        conselho = df['quote']
        print(f'Conselho de Kanye West: {conselho}')
    else:
        print('Informações inválidas')
else:
    print(f'Erro de conexão: {response.status_code}')