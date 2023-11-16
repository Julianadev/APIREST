"""
API The meal db obtém informações de pratos de comida
"""

import requests

# Pesquisar por categoria
response = requests.get('https://www.themealdb.com/api/json/v1/1/categories.php')

if response.status_code == 200:
    food_categoria = response.json()
    categorias = food_categoria['categories']

    for categoria in categorias:
        print(f'{categoria}')

else:
    print(f'Erro de conexão: {response.status_code}')

nome = input('Digite o nome da refeição: ')

# Pesquisando por nome
response = requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={nome}')

if response.status_code == 200:
    food_info = response.json()
else:
    print(f'Erro de conexão: {response.status_code}')

if 'meals' in food_info:
    refeicao_encontrada = food_info['meals'][0]

if refeicao_encontrada:
    nome_refeicao = refeicao_encontrada['strMeal']
    alternativa_para_bebidas = refeicao_encontrada.get("strDrinkAlternate", "")
    categoria = refeicao_encontrada["strCategory"]
    area = refeicao_encontrada["strArea"]
    instrucao = refeicao_encontrada["strInstructions"]
    imagem = refeicao_encontrada["strMealThumb"]
    youtube = refeicao_encontrada["strYoutube"]

    # Lista de ingredientes
    lista_ingredientes = [refeicao_encontrada[f"strIngredient{i}"] for i in range(1, 21) if
                          refeicao_encontrada.get(f"strIngredient{i}")]

    print(f'Nome: {nome_refeicao}')
    print(f'Alternativa para Bebidas: {alternativa_para_bebidas}')
    print(f'Categoria: {categoria}')
    print(f'Área: {area}')
    print(f'Instruções: {instrucao}')
    print(f'Imagem: {imagem}')
    print(f'Link do YouTube: {youtube}')
    print(f'Lista de Ingredientes: {", ".join(lista_ingredientes)}')
else:
    print(f'Refeição não encontrada: {nome}')
