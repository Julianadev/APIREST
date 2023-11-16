"""
 API "Bored API" para obter uma atividade aleatória com base no número de participantes fornecido
"""

import requests

participantes = int(input('Digite quantas pessoas vão participar: '))
url = f'https://www.boredapi.com/api/activity?partipants={participantes}'


response = requests.get(url)

if response.status_code == 200:
    response_json = response.json()

    if 'activity' in response_json:
        atividade = response_json['activity']
        tipo = response_json['type']
        participantes = participantes
        acessibilidade = response_json['accessibility']

        print(f'Atividade: {atividade}')
        print(f'Tipo: {tipo}')
        print(f'Participantes: {participantes}')
        print(f'Acessibilidade: {acessibilidade}')
else:
    print(f'Erro de conexão: {response.status_code}')