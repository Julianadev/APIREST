"""
API - Wordsearch , jogo de caça-palavras
"""

import requests

url = 'https://shadify.dev/api/wordsearch/generator'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if 'grid' in data:
        wordsCount = data['wordsCount']
        grid = data['grid']

        print(f'Contagem de palavras: {wordsCount}')

        for palavra in grid:
            print(' '.join(map(str,palavra)))
    else:
        print(f'Erro de dados')
else:
    print(f'Erro de conexão: {response.status_code}')