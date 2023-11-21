"""
API UselesFacts - Gera fatos aleatórios que são verdadeiros
"""
import requests

url = 'https://uselessfacts.jsph.pl//api/v2/facts/random'

response = requests.get(url)

if response.status_code == 200:
    date = response.json()

    if 'id' in date:
        text = date['text']
        source = date['source']
        source_url = date['source_url']
        language = date['language']
        link = date['permalink']

        print(f'Texto = {text}')
        print(f'Fonte = {source}')
        print(f'Fonte URL = {source_url}')
        print(f'Linguagem = {language}')
        print(f'Link = {link}')
    else:
        print('Erro de dados')
else:
    print(f'Erro de conexão: {response.status_code}')
