from functions.integration.users import get_user, create_user, update_user, delete_user

def handle_get_user(user_id: str):
    try:
        # Chama a função de users.py que faz a requisição HTTP para buscar o usuário
        user_data = get_user(user_id)
        # Aplica qualquer lógica adicional, como formatação ou tratamento de dados
        return user_data
    except Exception as e:
        # Aqui você pode adicionar qualquer tratamento de erro ou log adicional
        print(f"Erro ao obter o usuário {user_id}: {str(e)}")
        raise

def handle_create_user(name: str, email: str, password: str):
    try:
        # Chama a função de users.py para criar o usuário
        new_user = create_user(name, email, password)
        # Lógica adicional, se necessário
        return new_user
    except Exception as e:
        # Tratamento de erros ou logs
        print(f"Erro ao criar o usuário {name}: {str(e)}")
        raise

def handle_update_user(user_id: str, name: str = None, email: str = None, password: str = None):
    try:
        # Chama a função de users.py para atualizar o usuário
        updated_user = update_user(user_id, name, email, password)
        # Lógica adicional, se necessário
        return updated_user
    except Exception as e:
        # Tratamento de erros ou logs
        print(f"Erro ao atualizar o usuário {user_id}: {str(e)}")
        raise

def handle_delete_user(user_id: str):
    try:
        # Chama a função de users.py para deletar o usuário
        result = delete_user(user_id)
        # Lógica adicional, se necessário
        return result
    except Exception as e:
        # Tratamento de erros ou logs
        print(f"Erro ao deletar o usuário {user_id}: {str(e)}")
        raise
