import requests

def fetcher(url, method, headers=None, body=None):
    try:
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, json=body, headers=headers)
        elif method == "PUT":
            response = requests.put(url, json=body, headers=headers)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        else:
            raise ValueError(f"Método HTTP {method} não suportado")

        response.raise_for_status()  # Levanta erro se a requisição falhar
        return response.json()  # Retorna a resposta JSON, se existir

    except requests.exceptions.RequestException as e:
        raise Exception(f"Erro na requisição HTTP: {str(e)}")
