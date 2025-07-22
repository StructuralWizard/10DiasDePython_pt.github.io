import requests

# Endpoint da API do GitHub para obter repositórios de um usuário
url = "https://api.github.com/users/octocat/repos"

# Cabeçalhos personalizados
headers = {
    "User-Agent": "MyPythonApp/1.0",
    "Accept": "application/vnd.github.v3+json"
}

# Faz a requisição GET
response = requests.get(url, headers=headers)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()
    # Imprime os 3 primeiros repositórios com nome e URL
    for repo in data[:3]:
        print(f"Nome: {repo['name']} - URL: {repo['html_url']}")
else:
    print("A requisição falhou com o código de status:", response.status_code)
