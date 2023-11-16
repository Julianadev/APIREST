"""
API Goweather obtém informações meteorológicas de uma cidade especificada
pelo usuário.
"""
import requests

city = input('Digite a cidade: ')

url = f'https://goweather.herokuapp.com/weather/{city}'

response = requests.get(url)

if response.status_code == 200:
    clima_info = response.json()

    if 'temperature' in clima_info and 'description' in clima_info and 'wind' in clima_info:
        temp = clima_info['temperature']
        wind = clima_info['wind']
        desc = clima_info['description']

        print(f'Cidade: {city}')
        print(f'Temperatura: {temp}')
        print(f'Ventos: {wind}')
        print(f'Descrição: {desc}')

        if 'forecast' in clima_info:
            print('\nPrevisão para os próximos dias: ')
            for forecast in clima_info['forecast']:
                dia = forecast['day']
                temp = forecast['temperature']
                wind = forecast['wind']
                print(f'Dia {dia}: Temperatura: {temp}, Vento: {wind}')

    else:
        print(f'Cidade não encontrada: {city}')
else:
    print(f'Erro de conexão: {response.status_code}')


