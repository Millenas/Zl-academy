from flask import Flask, make_response, jsonify, request, Response
import sys
import os
import requests


# Atualizar o path do projeto para localizar os módulos da pasta
# repository
modulo = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'repository'))
sys.path.append(modulo)

import usuario 
import produto

# Instanciar 
app_api = Flask('api_database')
app_api.config['JSON_SORT_KEYS'] = False

# Implementar a lógica de programação

# --------------------------------------------------------
#           Inicio: Serviços da api usuário 
# --------------------------------------------------------

# Inserir usuário
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
        _mensagem = f'Erro: Inclusao do usuario: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem ,
                id = id_usuario
        )
    )
# Fim: criar_usuario()

# Atualizar usuário
@app_api.route('/usuario', methods=['PUT'])
def atualizar_usuario():
    # Construir um Request
    # Captura o JSON com os dados enviado pelo cliente
    usuario_json = request.json # corpo da requisição
    id = int(usuario_json['id'])
    try:
        if usuario.existe_usuario(id) == True:
            usuario.atualizar_usuario(usuario_json)
            sucesso = True
            _mensagem = 'Usuario alterado com sucesso'
        else:
            sucesso = False
            _mensagem = 'Usuario nao existe'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Alteracao do usuario: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem
        )
    )

# Deletar usuário
@app_api.route('/usuario/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    try:
        if usuario.existe_usuario(id) == True:
            usuario.deletar_usuario(id)
            sucesso = True
            _mensagem = 'Usuario deletado com sucesso'
        else:
            sucesso = False
            _mensagem = 'Usuario nao existe'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Exclusao de usuario: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem
        )
    )

# Serviço: Obter usuário pelo id
@app_api.route('/usuario/<int:id>', methods=['GET'])
def obter_usuario_id(id):
    # Declarando uma tupla vazia
    usuario_id = ()
    sucesso = False
    if usuario.existe_usuario(id) == True:
        usuario_id = usuario.obter_usuario_id(id)
        sucesso = True
        _mensagem = 'Usuario encontrado com sucesso'
    else:
        sucesso = False
        _mensagem = 'Usuario existe'
    # Construir um Response
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso, 
                mensagem = _mensagem,
                dados = usuario_id
        )
    )
# Fim: obter_usuario_id(id)

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
# Fim: lista_usuarios()

# -- Fim: Serviços da api usuário ------------------------


# --------------------------------------------------------
#           Inicio: Serviços da api produto 
# --------------------------------------------------------
# Incluir um novo Produto
@app_api.route('/produto', methods=['POST'])
def criar_produto():
    # Construir um Request
    # Captura o JSON com os dados enviado pelo cliente
    produto_json = request.json # corpo da requisição
    id_produto=0
    try:
        id_produto = produto.criar_produto(produto_json)
        sucesso = True
        _mensagem = 'Produto inserido com sucesso'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Inclusao do produto: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem ,
                id = id_produto
        )
    )

# Alterar um Produto
@app_api.route('/produto', methods=['PUT'])
def atualizar_produto():
    # Construir um Request
    # Captura o JSON com os dados enviado pelo cliente
    produto_json = request.json # corpo da requisição
    id = int(produto_json['id'])
    try:
        if produto.existe_produto(id) == True:
            print('p2')
            produto.atualizar_produto(produto_json)
            sucesso = True
            _mensagem = 'Produto alterado com sucesso'
        else:
            print('p3')
            sucesso = False
            _mensagem = 'Produto nao existe'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Falha na alteracao do produto: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem 
        )
    )
# Fim: atualizar_produto()

# Alterar o preco do dolar do Produto
@app_api.route('/produto/preco_dolar', methods=['PUT'])
def atualizar_preco_dolar_produto():
    # Construir um Request
    # Captura o JSON com os dados enviado pelo cliente
    novo_preco_dolar_json = request.json # corpo da requisição
    id = int(novo_preco_dolar_json['id'])
    try:
        if produto.existe_produto(id) == True:
            produto.atualizar_preco_dolar(novo_preco_dolar_json)
            sucesso = True
            _mensagem = 'Preco do dolar do Produto alterado com sucesso'
        else:
            sucesso = False
            _mensagem = 'Produto nao existe'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Falha na alteracao do preco do dolar do produto: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem 
        )
    )
# Fim: atualizar_produto()

# Deletar produto pelo id
@app_api.route('/produto/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    try:
        if produto.existe_produto(id) == True:
            produto.deletar_usuario(id)
            sucesso = True
            _mensagem = 'Produto deletado com sucesso'
        else:
            sucesso = False
            _mensagem = 'Produto nao existe'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Exclusão de usuario: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem
        )
    ) 
# Fim: deletar_produto(id)  

# Serviço: Obter produto pelo id
@app_api.route('/produto/<int:id>', methods=['GET'])
def obter_produto_id(id):
    # Declarando uma tupla vazia
    produto_id = ()
    sucesso = False
    if produto.existe_produto(id) == True:
        produto_id = produto.obter_produto_id(id)
        sucesso = True
        _mensagem = 'Produto encontrado com sucesso'
    else:
        sucesso = False
        _mensagem = 'Produto nao existe'
    # Construir um Response
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso, 
                mensagem = _mensagem,
                dados = produto_id
        )
    )
# Fim: obter_produto_id(id)

# Serviço: Obter uma lista de produtos ordenada pela descricao
@app_api.route('/produto', methods=['GET'])
def lista_produtos():
    lista_produto = list()
    lista_produto = produto.listar_produto()
    if len(lista_produto) == 0:
        sucesso = False
        _mensagem = 'Lista de produto vazia'
    else:
        sucesso = True
        _mensagem = 'Lista de produto'

    # Construir um Response
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso, 
                mensagem = _mensagem,
                dados = lista_produto
        )
    )
# Fim: lista_produtos()
#Serviço: Incluir múltiplos produtos
# Inserir múltiplos produtos
@app_api.route('/produtos', methods=['POST'])
def criar_varios_produtos():
    produtos_json = request.json
    if not produtos_json or not isinstance(produtos_json, list):
        return make_response(jsonify(status=False, mensagem='Dados de produtos inválidos'), 400)

    try:
        ids_produtos = []
        for produto_json in produtos_json:
            # Verifica se todos os campos necessários estão presentes
            if not all(k in produto_json for k in ('descricao', 'unidade', 'quantidade', 'preco_real')):
                return make_response(jsonify(status=False, mensagem='Dados de algum produto inválidos'), 400)
            id_produto = produto.criar_produto(produto_json)  # Chama a função de inserir produto
            ids_produtos.append(id_produto)

        return make_response(jsonify(status=True, mensagem='Produtos inseridos com sucesso', ids=ids_produtos), 201)
    except Exception as ex:
        return make_response(jsonify(status=False, mensagem=f'Erro: Inclusão dos produtos: {ex}'), 500)

#Fim: criar_varios_produtos()
# Serviço: Obter a cotação do dólar
@app_api.route('/cotacao/dolar', methods=['GET'])
def obter_cotacao_dolar():
    url_cotacao = "https://economia.awesomeapi.com.br/last/USD-BRL"
    try:
        response = requests.get(url_cotacao)
        response.raise_for_status()
        cotacao = response.json()
        preco_dolar = float(cotacao['USDBRL']['high'])

        return make_response(jsonify(status=True, mensagem='Cotação do dólar obtida com sucesso', preco_dolar=preco_dolar))
    except Exception as ex:
        return make_response(jsonify(status=False, mensagem=f'Erro ao obter a cotação do dólar: {ex}'))

# Serviço: Atualizar o preço do dólar nos produtos
@app_api.route('/produto/preco_dolar', methods=['PUT'])
def atualizar_precos_dolar():
    cotacao_response = requests.get("http://127.0.0.1:5000/cotacao/dolar")
    if not cotacao_response.json().get('status'):
        return make_response(jsonify(status=False, mensagem='Erro ao obter a cotação do dólar'))
    
    preco_dolar = cotacao_response.json()['preco_dolar']
    produtos = produto.listar_produto()

    for produto_item in produtos:
        preco_real = produto_item['preco_real']
        novo_preco_dolar = preco_real * preco_dolar
        
        update_payload = {
            "id": produto_item['id'],
            "preco_dolar": novo_preco_dolar
        }
        produto.atualizar_preco_dolar(update_payload)

    return make_response(jsonify(status=True, mensagem='Preços dos produtos atualizados com sucesso'))



# -- Fim: Serviços da api produto ------------------------


# Levantar/Executar API REST: api_database
app_api.run()



