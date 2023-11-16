"""
API Rick and Morty obtém informações dos personagens da série
"""
import requests

url = 'https://rickandmortyapi.com/api/character/'

# Fazendo uma solicitação GET para obter a lista de personagens
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print(f'Erro de conexão: {response.status_code}')

# Solicitação para obter informações de um personagem específico
nome = input('Digite o nome do personagem: ')

# Encontrando o personagem na lista
personagem_encontrado = None
for personagem in data['results']:
    if personagem['name'] == nome:
        personagem_encontrado = personagem_encontrado
        break

if personagem_encontrado:
    # Extraindo informações relevantes do personagem
    nome_personagem = personagem_encontrado['name']
    status = personagem_encontrado['status']
    especie = personagem_encontrado['species']
    sexo = personagem_encontrado['gender']
    localizacao_personagem = personagem_encontrado['location']['name']
    imagem_personagem = personagem_encontrado['image']
    #episodios_personagem = personagem_encontrado['episode']

    print(f'Nome: {nome_personagem}')
    print(f'Status: {status}')
    print(f'Espécie: {especie}')
    print(f'Sexo: {sexo}')
    print(f'Localização: {localizacao_personagem}')
    print(f'Imagem: {imagem_personagem}')
    #print(f'Episódio: {episodios_personagem}')
else:
    print(f'Personagem não encontrado: {nome}')