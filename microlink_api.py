"""
API Microlink obtém dados estruturados extraidos de qualquer site.
"""

import requests

# URL base
url = 'https://api.microlink.io'

# URL do site de extração
site = input('Digite a URL do site que deseja extrair as informações: ')

params = {'url': site}

response = requests.get(url, params)

if response.status_code == 200:
    df = response.json()

    try:
        data = df.get('data', {})

        titulo = data.get('title', None)
        descricao = data.get('description', None)
        linguagem = data.get('lang', None)
        autor = data.get('author', None)
        dominio = data.get('publisher', None)
        logo = data.get('logo', None)

        print(f'Título: {titulo}')
        print(f'Descrição: {descricao}')
        print(f'Linguagem: {linguagem}')
        print(f'Autor: {autor}')
        print(f'Domínio: {dominio}')
        print(f'Imagem: {logo}')
    except KeyError as e:
        print(f'Erro de chave: {e}')
else:
    print(f'Erro de conexão: {response.status_code}')