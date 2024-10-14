from flask import Blueprint, request, jsonify

# Criando o blueprint para a rota de deleção de usuário
delete_user_route = Blueprint('delete_user', __name__)

@delete_user_route.route('/deleteUser/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Aqui você pode adicionar a lógica de deleção do usuário do banco de dados
    # Exemplo: Deletar o usuário pelo `user_id`

    return jsonify({'message': f'Usuário {user_id} deletado com sucesso!'})
