"""
API Shadify - SUDOKU
"""

import requests

url = 'https://shadify.dev/api/sudoku/generator'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if 'grid' in data:
        task = data['task']
        grid = data['grid']


        print('\nSudoku:')
        for tarefa in task:
            print(' '.join(map(str, tarefa)))

        print('\nResultado:')

        for row in grid:
            print(' '.join(map(str, row)))
else:
    print(f'Erro de conexão: {response.status_code}')

