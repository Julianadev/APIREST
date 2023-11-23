"""
API SWAPI - Dados dos personagens de Star Wars
"""
import requests

url = f'https://swapi.dev/api/people/'

nome = input('Digite o nome do personagem: ')

url_personagem = f'{url}?search={nome}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if 'results' in data and data['results']:
        personagem = data['results'][0]

        print(f'Nome: {personagem["name"]}')
        print(f'Altura: {personagem["height"]}')
        print(f'Cor do cabelo: {personagem["hair_color"]}')
        print(f'Cor da pele: {personagem["skin_color"]}')
        print(f'Cor dos olhos: {personagem["eye_color"]}')
        print(f'Ano do aniversário: {personagem["birth_year"]}')
        print(f'Sexo: {personagem["gender"]}')
        print(f'Planeta Natal: {personagem["homeworld"]}')
        print(f'Filmes: {personagem["films"]}')
        print(f'Espécie: {personagem["species"]}')
        print(f'Veículos: {personagem["vehicles"]}')
    else:
        print(f'Erro de dados')
else:
    print(f'Erro de conexão: {response.status_code}')


