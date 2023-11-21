"""
API Evil Insult - Gera insultos aleatórios
"""
import requests

url = 'https://evilinsult.com/generate_insult.php?lang=pt&type=json'

response = requests.get(url)

if response.status_code == 200:
    try:
        data = response.json()

        if 'insult' in data:
            insulto = data['insult']

            print(f'Insulto: {insulto}')

    except (KeyError, IndexError, ConnectionError) as e:
        print(f'Ocorreu um erro: {e}')
else:
    print('erro de conexao')


