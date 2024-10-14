from flask import Blueprint, request, jsonify

# Criar um blueprint para a rota de criar usuário
create_user_route = Blueprint('create_user', __name__)

@create_user_route.route('/createUser', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    # Lógica para criar o usuário
    return jsonify({'message': f'Usuário {username} criado com sucesso!'})
