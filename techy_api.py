"""
API Techy - Gera conselhos de um dev
"""
import requests

url = 'https://techy-api.vercel.app//api/json'

response = requests.get(url)

if response.status_code == 200:
    date = response.json()

    if 'message' in date:
        mensagem = date['message']

        print(f'Conselho de um dev: {mensagem}')
    else:
        print('Erro de dados')
else:
    print(f'Erro de conexão: {response.status_code}')