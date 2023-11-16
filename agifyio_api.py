"""
API Agify é usada para estimar a idade provável de uma pessoa com base em seu nome.
Ela retorna informações estatísticas sobre a probabilidade de uma pessoa com um determinado
nome ter uma certa faixa etária
"""
import requests

nome = input('Digite seu nome: ')
pais = input('Digite seu país: ')

url = f'https://api.agify.io?name={nome}'
if pais:
    url += f'&country_id={pais}'

response = requests.get(url)

if response.status_code == 200:
    info_name = response.json()
    print(info_name)
else:
    print(f'Erro de conexão: {response.status_code}')