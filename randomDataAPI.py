"""
Random Data API - Obtém dados fakes
"""
import requests

url = 'https://random-data-api.com/api/v2/users'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print(f'Nome completo: {data["first_name"]} {data["last_name"]}')
    print(f'Usuário: {data["username"]}')
    print(f'E-mail: {data["email"]}')
    print(f'Telefone: {data["phone_number"]}')
    print(f'Data de Nascimento: {data["date_of_birth"]}')

    employment = data.get("employment", {})
    print(f'Cargo: {employment.get("title")}')
    print(f'Habilidade-chave: {employment.get("key_skill")}')

    address = data.get("address", {})
    print(f'Cidade: {address.get("city")}')
    print(f'Estado: {address.get("state")}')
    print(f'País: {address.get("country")}')

    credit_card = data.get("credit_card", {})
    print(f'Número do Cartão de Crédito: {credit_card.get("cc_number")}')

    subscription = data.get("subscription", {})
    print(f'Plano de Assinatura: {subscription.get("plan")}')
    print(f'Status da Assinatura: {subscription.get("status")}')
    print(f'Método de Pagamento: {subscription.get("payment_method")}')
    print(f'Termo da Assinatura: {subscription.get("term")}')

else:
    print(f'Erro de conexão: {response.status_code}')
