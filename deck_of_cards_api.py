"""
API do Deck of Cards realiza algumas operações básicas, como criar um novo
baralho, embaralhar e desenhar cartas
"""
import requests

url_baralho_novo = 'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1'

response = requests.get(url_baralho_novo)

if response.status_code == 200:
    deck_info = response.json()
    deck_id = deck_info['deck_id']
    print(f'Baralho ID: {deck_id}')
else:
    print(f'Erro de conexão: {response}')

# Embaralhando
response = requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/shuffle/')

if response.status_code == 200:
    print(f'Baralho embaralhado com sucesso!')
else:
    print(f'Erro de conexão: {response.status_code}')

# Desenhando algumas cartas do baralho

response = requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2')

if response.status_code == 200:
    card_info = response.json()
    drawn_cards = card_info['cards']
    for card in drawn_cards:
        print(f'Carta desenhada: {card["value"]} of {card["suit"]}')
else:
    print(f'Erro de conexão: {response.status_code}')

