import requests
import json
import os

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:
    dados_jason = response.json()
    dados_restaurante = {}
    for item in dados_jason:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })
else:
    print(f'O erro foi {response.status_code}')

# Cria a pasta se ainda não existir
os.makedirs('dados_restaurantes', exist_ok=True)

# Salva os arquivos dentro da pasta
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'dados_restaurantes/{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4, ensure_ascii=False)
