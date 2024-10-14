from flask import Blueprint, request, jsonify

update_user_route = Blueprint('update_user', __name__)

@update_user_route.route('/updateUser/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    new_username = data.get('username')
    # Lógica para atualizar o usuário
    return jsonify({'message': f'Usuário {user_id} atualizado para {new_username}'})
