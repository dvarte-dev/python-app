import requests
from functions.integration.fetcher import fetcher

# Função para buscar um usuário por ID
def get_user(user_id: str):
    try:
        return fetcher(f'/api/users/{user_id}', 'GET')
    except Exception as e:
        raise Exception(f'Error fetching user: {str(e)}')

# Função para criar um novo usuário
def create_user(name: str, email: str, password: str):
    try:
        body = {'name': name, 'email': email, 'password': password}
        return fetcher('/api/users', 'POST', body)
    except Exception as e:
        raise Exception(f'Error creating user: {str(e)}')

# Função para atualizar um usuário existente
def update_user(user_id: str, name: str = None, email: str = None, password: str = None):
    try:
        body = {'name': name, 'email': email, 'password': password}
        return fetcher(f'/api/users/{user_id}', 'PUT', body)
    except Exception as e:
        raise Exception(f'Error updating user: {str(e)}')

# Função para deletar um usuário
def delete_user(user_id: str):
    try:
        return fetcher(f'/api/users/{user_id}', 'DELETE')
    except Exception as e:
        raise Exception(f'Error deleting user: {str(e)}')
