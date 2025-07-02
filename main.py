from fastapi import FastAPI, Query
import json
import os

app = FastAPI()

CAMINHO_PASTA = "dados_restaurantes"

@app.get('/api/hello')
def hello_word():
    '''
    Endpoint que exibe uma mensagem incrível do mundo da programação
    '''
    return {'Hello': 'World'}

@app.get('/api/restaurantes/')
def get_restaurante(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardápios dos restaurantes a partir de arquivos locais
    '''
    if restaurante is None:
        # Retorna todos os cardápios disponíveis
        arquivos = os.listdir(CAMINHO_PASTA)
        todos = {}
        for arquivo in arquivos:
            if arquivo.endswith('.json'):
                nome = arquivo.replace('.json', '')
                with open(os.path.join(CAMINHO_PASTA, arquivo), 'r', encoding='utf-8') as f:
                    todos[nome] = json.load(f)
        return {'Restaurantes': todos}
    
    # Caso um restaurante específico tenha sido solicitado
    nome_arquivo = f"{restaurante}.json"
    caminho_arquivo = os.path.join(CAMINHO_PASTA, nome_arquivo)

    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            cardapio = json.load(f)
        return {'Restaurante': restaurante, 'Cardapio': cardapio}
    else:
        return {'Erro': f"Restaurante '{restaurante}' não encontrado."}
