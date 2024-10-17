from flask import Flask, make_response, jsonify, request, Response
import sys
import os

modulo = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'repository'))
sys.path.append(modulo)

import usuario 

# Instanciar 
app_api = Flask('api_database')
app_api.config['JSON_SORT_KEYS'] = False

# Implementar a lógica de programação

# -- Inicio: Serviços da api usuário ---------------------
# Serviço: Criar usuário
@app_api.route('/usuario', methods=['POST'])
def criar_usuario():
    # Construir um Request
    # Captura o JSON com os dados enviado pelo cliente
    usuario_json = request.json # corpo da requisição
    try:
        id_usuario = usuario.criar_usuario(usuario_json)
        sucesso = True
        _mensagem = 'Usuario inserido com sucesso'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Inclusão do usuario: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem,
                id = id_usuario
        )
    )
#Fim: criar_usuario()

# Serviço: Obter a lista de usuário
@app_api.route('/usuario', methods=['GET'])
def lista_usuarios():
    lista_usuario = list()
    lista_usuario = usuario.lista_usuarios()
    if len(lista_usuario) == 0:
        sucesso = False
        _mensagem = 'Lista de usuario vazia'
    else:
        sucesso = True
        _mensagem = 'Lista de usuario'

    # Construir um Response
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso, 
                mensagem = _mensagem,
                dados = lista_usuario
        )
    )
#Fim: lista_usuarios()

# Levantar/Executar API REST: api_database
app_api.run()
