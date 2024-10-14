from flask import Blueprint, request, jsonify

get_user_route = Blueprint('get_user', __name__)

@get_user_route.route('/getUser/<user_id>', methods=['GET'])
def get_user(user_id):
    # Lógica para pegar o usuário pelo ID
    return jsonify({'user_id': user_id, 'username': 'exemplo'})
