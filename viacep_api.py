import requests

cep = input('Digite o seu cep: ')

url = f'https://viacep.com.br/viacep.com.br/ws/{cep}/json/'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if 'cep' in data:
        cep = data['cep']
        logradoudo = data['logradouro']
        complemento = data['complemento']
        bairro = data['bairro']
        localidade = data['localidade']
        uf = data['uf']
        ddd = data['ddd']

        print(f'CEP: {cep}')
        print(f'Logradouro: {logradoudo}')
        print(f'Complemento: {complemento}')
        print(f'Bairro: {bairro}')
        print(f'Localidade: {localidade}')
        print(f'UF: {uf}')
        print(f'DDD: {ddd}')
    else:
        print('Erro de dados')

else:
    print(f'Erro de conexão: {response.status_code}')