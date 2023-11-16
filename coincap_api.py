"""
API da CoinCap aonde busca informações sobre várias criptomoedas
"""
import requests

url = f'https://api.coincap.io/v2/assets'

response = requests.get(url)

if response.status_code == 200:
    info = response.json()

    if 'data' in info:
        crypto = info['data']

        for moeda in crypto:
            name = moeda['name']
            symbol = moeda['symbol']
            supply = moeda['supply']
            maxSupply = moeda['maxSupply']
            marketCapUsd = moeda['marketCapUsd']
            volumeUsd24Hr = moeda['volumeUsd24Hr']
            priceUsd = moeda['priceUsd']
            changePercent24Hr = moeda['changePercent24Hr']
            vwap24Hr = moeda['vwap24Hr']

            print(f'Nome: {name}')
            print(f'Símbolo: {symbol}')
            print(f'Supply: {supply}')
            print(f'Max Supply: {maxSupply}')
            print(f'Valor de mercado USD: {marketCapUsd}')
            print(f'Volume USD 24H: {volumeUsd24Hr}')
            print(f'Preço USD: {priceUsd}')
            print(f'Percentual de mudança: {changePercent24Hr}')
            print(f'VWAP 24H: {vwap24Hr}')
            print('\n' + '-'*30)
    else:
        print(f'Nenhuma informação de cripto encontrada')
else:
    print(f'Erro de conexão: {response.status_code}')







