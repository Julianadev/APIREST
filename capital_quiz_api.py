import requests

url = 'https://shadify.dev/api/countries/capital-quiz'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if 'country' in data:
        country = data['country']
        flag = data['flag']
        variants = data['variants']
        answer = data['answer']

        total = 0

        print('Quiz qual a capital: ')
        print(f'\nPaís: {country}')
        print(f'\nBandeira: {flag}')

        for i, p in enumerate(variants, 1):
            print(f'\n{i} - {p}')


        print(f'\nResposta Correta: {answer}')
    else:
        print('Erro de dados')
else:
    print(f'Erro de conexão: {response.status_code}')