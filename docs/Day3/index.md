---
title: Dia 3 Python Avançado - API
layout: default
nav_order: 4
has_children: false
nav_exclude: false
---

# Dia 3. Python Avançado. 🌐 Hackeie suas Ações, Voos e Hábitos
{: .no_toc }
🚀 Nesta lição, você desbloqueará o poder das APIs, automação e rastreamento de dados para dominar habilidades de Python do mundo real. Desde monitorar mercados até encontrar ofertas de voos e otimizar suas rotinas — prepare-se para codificar de forma mais inteligente e viver melhor. 🌐💡

---

<details open markdown="block">
<summary>
Índice
</summary>
{: .text-delta }
1. TOC
{:toc}
</details>

---

## 📚 Conceitos Abordados<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

O que é uma API?
- **API (Interface de Programação de Aplicações)** é um conjunto de regras que permite que diferentes entidades de software (como seu script Python e um aplicativo da web) se comuniquem.
- **Cliente**: A aplicação que envia requisições (por exemplo, seu script Python).
- **Servidor**: A aplicação que responde às requisições (por exemplo, o endpoint da API).

Como usar APIs?
As requisições HTTP típicas que os clientes enviam para os servidores são:
- **GET** – Recuperar dados
- **POST** – Enviar novos dados
- **PUT** – Atualizar dados existentes
- **DELETE** – Remover dados

Quando o cliente envia requisições para o servidor, elas também vão com cabeçalhos e payload. Cabeçalhos são pares chave-valor enviados entre o cliente e o servidor para fornecer informações sobre a requisição ou a resposta. Os cabeçalhos podem incluir coisas como tokens de autenticação (Authorization), tipo de conteúdo (Content-Type) ou chaves de API.

Por exemplo:

```python
import requests

# Endpoint da API do GitHub para obter repositórios de um usuário
url = "https://api.github.com/users/octocat/repos"

# Cabeçalhos personalizados
headers = {
    "User-Agent": "MeuAppPython/1.0",
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
```

### Respostas HTTP - Códigos de Status<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
As respostas HTTP são categorizadas por códigos de status, que são números de 3 dígitos agrupados em cinco classes:

<details markdown="block">
  <summary>
    100 Continue, 200 OK, 201 Created, 301 Redirection, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 500 Server Error
  </summary>

{: .important-title }
> Respostas HTTP
> 
> 1. Respostas **informativas** (1xx): Indicam que a requisição foi recebida e entendida, e o processo está continuando.
> - 100 Continue: O cliente deve continuar com sua requisição.
> - 101 Switching Protocols: O servidor está mudando de protocolos.
> 2. Respostas de **sucesso** (2xx): Indicam que a requisição foi recebida, entendida e aceita com sucesso.
> - 200 OK: A resposta de sucesso padrão.
> - 201 Created: A requisição foi atendida e resultou na criação de um novo recurso.
> - 204 No Content: O servidor processou a requisição com sucesso, mas não está retornando nenhum conteúdo.
> 3. Mensagens de **redirecionamento** (3xx): Indicam que uma ação adicional precisa ser tomada pelo cliente para completar a requisição, geralmente redirecionando para uma URL diferente.
> - 301 Moved Permanently: O recurso solicitado foi movido permanentemente para uma nova URL.
> - 302 Found: O recurso está temporariamente localizado em uma URL diferente.
> - 303 See Other: A resposta à requisição pode ser encontrada sob outro URI usando um método GET.
> 4. Respostas de **erro do cliente** (4xx): Indicam que a requisição do cliente continha sintaxe incorreta ou não pôde ser atendida.
> - 400 Bad Request: O servidor não consegue entender a requisição devido à sintaxe malformada.
> - 401 Unauthorized: O cliente deve se autenticar para obter a resposta solicitada.
> - 403 Forbidden: O cliente não tem direitos de acesso ao conteúdo.
> - 404 Not Found: O servidor não consegue encontrar o recurso solicitado.
> - 405 Method Not Allowed: O método de requisição é conhecido pelo servidor, mas foi desabilitado e não pode ser usado para o recurso solicitado.
> 5. Respostas de **erro do servidor** (5xx): Indicam que o servidor falhou em atender a uma requisição aparentemente válida.
> - 500 Internal Server Error: Uma mensagem de erro genérica, dada quando uma condição inesperada foi encontrada e nenhuma mensagem mais específica é adequada.
> - 502 Bad Gateway: O servidor, enquanto atuava como um gateway ou proxy, recebeu uma resposta inválida de um servidor upstream.
> - 503 Service Unavailable: O servidor não está pronto para lidar com a requisição, muitas vezes devido a manutenção ou sobrecarga.
</details>


Além do código de status, uma resposta HTTP também inclui:
1. **Linha de status**: Contém a versão do HTTP, o código de status numérico e uma frase de motivo textual (por exemplo, HTTP/1.1 200 OK).
2. **Cabeçalhos**: Fornecem informações adicionais sobre a resposta, como tipo de conteúdo, instruções de cache, informações do servidor, etc.
3. **Corpo da mensagem** (opcional): Contém os dados reais que estão sendo retornados, como uma página **HTML**, dados **JSON**, uma **imagem**, etc.


<details markdown="block">
  <summary>
    O cabeçalho `Content-Type` usa um tipo MIME (Multipurpose Internet Mail Extensions) para informar ao cliente que tipo de dados está sendo enviado.
  </summary>


Aqui está um detalhamento de outros possíveis corpos de mensagem, frequentemente categorizados por seu `Content-Type`:

{: .important-title }
> Tipo de conteúdo
> 
> 1. Formatos baseados em texto:
> - text/plain: Texto simples e não formatado. Bom para mensagens simples, logs ou quando nenhuma formatação específica é necessária.
> - text/css: Folhas de Estilo em Cascata, usadas para estilizar documentos HTML.
> - text/javascript: Código JavaScript, frequentemente usado para scripts do lado do cliente em aplicações web.
> - text/csv: Valores Separados por Vírgula, um formato comum para dados tabulares.
> - text/xml: XML (Extensible Markup Language), um formato de dados estruturados. Embora menos comum que o JSON para novas APIs, ainda é amplamente utilizado em sistemas mais antigos e para aplicações específicas (por exemplo, feeds RSS).
> 2. Formatos específicos de aplicação:
> - application/xml: Semelhante ao text/xml, mas indica que o conteúdo é um documento XML genérico, não especificamente para exibição como texto.
> - application/json: JavaScript Object Notation, um formato leve de intercâmbio de dados. É extremamente comum para APIs e troca de dados entre serviços web.
> - application/pdf: Portable Document Format, para documentos destinados a serem visualizados ou impressos de forma consistente.
> - application/octet-stream: Este é um tipo de dados binários genérico. É frequentemente usado quando o servidor não conhece o tipo específico de dados binários, ou quando se espera que o cliente lide com o download como um arquivo bruto (por exemplo, um download de arquivo onde o navegador solicita ao usuário para salvar).
> - application/zip: Arquivos de arquivo compactados.
> - application/vnd.*: Tipos MIME específicos do fornecedor. São usados quando uma empresa ou organização define seu próprio formato de dados exclusivo. Por exemplo, > - application/vnd.openxmlformats-officedocument.spreadsheetml.sheet para um arquivo Excel XLSX.
> - application/graphql: Para consultas e respostas GraphQL.
> - application/wasm: Formato binário WebAssembly.
> 3. Formatos de imagem:
> - image/jpeg: Imagens JPEG.
> - image/png: Imagens PNG.
> - image/gif: Imagens GIF.
> - image/svg+xml: Gráficos Vetoriais Escaláveis, imagens vetoriais baseadas em XML.
> - image/webp: Imagens WebP.
> 4. Formatos de áudio e vídeo:
> - audio/mpeg: Áudio MP3.
> - audio/ogg: Áudio Ogg Vorbis.
> - video/mp4: Vídeo MP4.
> - video/webm: Vídeo WebM.
> - video/ogg: Vídeo Ogg Theora.
> 5. Mensagens multipartes:
> - multipart/form-data: Embora frequentemente visto em corpos de requisição para uploads de arquivos, também pode aparecer em corpos de resposta se o servidor estiver enviando de volta várias partes distintas como uma única resposta (menos comum para navegação web padrão, mais para APIs especializadas).
> - multipart/mixed: Um tipo multipartes genérico para enviar várias partes do corpo independentes.
> 
> Considerações importantes:
> - Cabeçalho Content-Length: Se um corpo de mensagem estiver presente e seu tamanho for conhecido, o cabeçalho Content-Length especifica o tamanho exato em bytes.
> - Transfer-Encoding: chunked: Se o servidor não souber o tamanho total do corpo da resposta com antecedência (por exemplo, para streaming de dados), ele usará a codificação de transferência em pedaços, onde o corpo é enviado em uma série de pedaços, cada um com seu próprio indicador de tamanho.
> - Sem corpo para certos códigos de status: Como mencionado, códigos de status como 204 No Content ou 304 Not Modified indicam explicitamente que não haverá corpo de mensagem.
> - Mensagens de erro: Mesmo para respostas de erro (4xx ou 5xx), o corpo pode conter mensagens de erro legíveis por humanos, frequentemente em formato HTML ou JSON, para ajudar o cliente ou o usuário a entender o que deu errado.
> 
> A flexibilidade do HTTP, combinada com a vasta gama de tipos MIME, permite que os servidores enviem praticamente qualquer tipo de dados como resposta, tornando-o um protocolo altamente versátil para a internet.

</details>



### Manipulação de JSON<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
Um arquivo JSON (JavaScript Object Notation) é um arquivo de texto que armazena dados em um formato estruturado e legível usando pares chave-valor.
É usado para:
- Trocar dados entre servidores e aplicativos da web
- Arquivos de configuração
- Armazenar dados estruturados em APIs ou aplicações

O Python incorpora uma biblioteca padrão para manipulação de JSON.

```python
import json

# Converte dict para JSON 1
with open('data1.json', 'w') as f:
    json.dump({"nome": "Alice"}, f)

# Converte dict para JSON 2
# Serializa para JSON
json_string = json.dumps({"nome": "Alice"})

# Desserializa de JSON
data = json.loads(json_string)

# Salva em arquivo
with open("data2.json", "w") as f:
    json.dump(data, f, indent=4)

# Lê arquivo JSON
with open('data2.json') as f:
    data = json.load(f)
    print(data['nome'])
```

Existem outras bibliotecas para manipulação de JSON, como [simplejson](https://pypi.org/project/simplejson/), [pandas](https://pandas.pydata.org/), [requests](https://pypi.org/project/requests/), [ujson](https://github.com/ultrajson/ultrajson), [orjson](https://github.com/ijl/orjson) e [demjson](https://github.com/dmeranda/demjson)

<details markdown="block">
  <summary>
    Veja exemplos com pandas e request
  </summary>
```python
import pandas as pd
df = pd.read_json("data.json")
```
```python
import requests
response = requests.get("https://api.example.com/data")
data = response.json()
```

</details>

Para uma visualização mais fácil, [https://jsonformatter.org/json-viewer](https://jsonformatter.org/json-viewer) é bastante útil.


### Tratamento de Exceções<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
Ao programar, é uma boa prática introduzir mensagens para e estruturas de tratamento de erros como a abaixo. Isso reduz o tempo na localização e correção de erros que podem surgir do próprio código ou das respostas do servidor.
```python
try:
    response = requests.get("https://someapi.com/data")
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"Ocorreu um erro HTTP: {e}")
except KeyError:
    print("Faltando uma chave na resposta.")
except IndexError:
    print("Índice da lista fora do intervalo.")
except Exception as e:
    print(f"Algo deu errado: {e}")
```


### Tipos de Autenticação<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
Os métodos de autenticação mais comuns são:
- 🔑**Chave de API**: Uma chave única (como uma senha) é passada na requisição, geralmente no cabeçalho ou na URL. Isso é usado para controle de acesso básico para APIs públicas. Não é muito seguro e deve sempre usar HTTPS. Veja o exemplo abaixo com o openweather. Você terá que se inscrever e obter sua chave de API em https://home.openweathermap.org/api_keys.

```python
import requests
base_url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "Londres",
    "appid": "SUA_CHAVE_DE_API",
    "units": "metric" # Você pode mudar para "imperial" para Fahrenheit
}
response = requests.get(base_url, params=params)
if response.status_code == 200:
    data = response.json()
    print(f"Clima em {params['q']}: {data['weather'][0]['description']}")
else:
    print("Erro:", response.status_code, response.text)
```

- 🍪**Autenticação Básica e Autenticação Baseada em Sessão (Cookie)**: que agora é rara e considerada insegura e nunca usada.

<details markdown="block">
  <summary>
    clique para ver um exemplo de Autenticação Básica
  </summary>

```python
import requests

url = "https://api.example.com/user"
response = requests.get(url, auth=('seu_usuario', 'sua_senha'))

print(response.status_code, response.json())
```

</details>

<details markdown="block">
  <summary>
    clique para ver um exemplo de Autenticação Baseada em Sessão
  </summary>

```python
import requests

# Passo 1: Faça login e obtenha um cookie de sessão
session = requests.Session()
login_url = "https://example.com/login"
payload = {
    "username": "seu_usuario",
    "password": "sua_senha"
}

response = session.post(login_url, data=payload)

# Passo 2: Acesse a página protegida usando a mesma sessão
protected_url = "https://example.com/profile"
profile_response = session.get(protected_url)

print(profile_response.status_code, profile_response.text)
```

</details>


- 🛡️**Tokens CSRF**: são um valor único e imprevisível que o servidor gera e inclui em cada formulário ou requisição de API, onde o servidor entrega um token ao cliente após o login, que é então usado em requisições HTTP subsequentes. Esses tokens/cookies geralmente expiram após algum tempo.

<details markdown="block">
  <summary>
    clique para ver um exemplo de CSRF usando flask
  </summary>
Para executar este exemplo, você precisa instalar o Flask:
```bash
pip install Flask Flask-WTF
```


A aplicação Flask que atuará como servidor é:

{% raw %}
```python
from flask import Flask, render_template_string, request, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import secrets

# Aplicação Flask básica
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16) # Necessário para proteção CSRF

# Define o formulário com proteção CSRF
class NameForm(FlaskForm):
    name = StringField('Seu Nome', validators=[DataRequired()])
    submit = SubmitField('Enviar')

```
```python

# Rota para exibir e manipular o formulário
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        flash(f"Olá, {form.name.data}!", "success")
        return redirect('/')
    return render_template_string('''
        <!doctype html>
        <title>Exemplo de CSRF</title>
        {% with messages = get_flashed_messages(with_categories=true) %}
          {% for category, message in messages %}
            <div style="color:green">{{ message }}</div>
          {% endfor %}
        {% endwith %}
        <form method="POST">
            {{ form.hidden_tag() }}
            {{ form.name.label }} {{ form.name(size=20) }}
            {{ form.submit() }}
        </form>
    ''', form=form)

if __name__ == '__main__':
    app.run(debug=True)
```
{% endraw %}

Execute com
```bash
 python csrf_flask_example.py
 ```

 e então abra no navegador digitando no endereço http://127.0.0.1:5000/
Se você inspecionar o código do site no navegador clicando com o botão direito na caixa e clicando em inspecionar, ou fazendo Ctrl+Shift+I. Em seguida, selecionando a aba Elementos, você encontrará uma linha como

```html
<input id="csrf_token" name="csrf_token" type="hidden" value="algo_como_4jh56yFj3...">
```

![Token CSRF no inspetor do navegador](CSRF_screenshot.png)


</details>


- **OAuth**: é um processo de várias etapas frequentemente realizado em um aplicativo da web. É tipicamente usado com serviços como Google, Facebook, aplicativos iOS. Veremos um exemplo mais prático disso mais tarde.

<details markdown="block">
  <summary>
    clique para OAuth 2.0
  </summary>
O código Python abaixo é apenas para explicação do processo. Ele não será executado. Por favor, veja e tente exemplos reais no próximo ponto.

```python
import requests
import webbrowser

# Passo 1: Redirecionar o usuário para a URL de autorização
client_id = "SEU_CLIENT_ID"
redirect_uri = "http://localhost:8080/callback"
auth_url = (
    f"https://auth.example.com/oauth/authorize?response_type=code"
    f"&client_id={client_id}&redirect_uri={redirect_uri}&scope=read"
)
webbrowser.open(auth_url)

# Passo 2: O usuário faz login e é redirecionado para uma URL como:
# http://localhost:8080/callback?code=CODIGO_DE_AUTORIZACAO
# Você deve extrair manualmente este `code` para a próxima etapa.

# Passo 3: Trocar o código de autorização por um token de acesso
auth_code = input("Cole o código de autorização aqui: ")
token_url = "https://auth.example.com/oauth/token"
data = {
    "grant_type": "authorization_code",
    "code": auth_code,
    "redirect_uri": redirect_uri,
    "client_id": client_id,
    "client_secret": "SEU_CLIENT_SECRET"
}

response = requests.post(token_url, data=data)
token_data = response.json()
access_token = token_data['access_token']

# Passo 4: Use o token
headers = {"Authorization": f"Bearer {access_token}"}
protected_url = "https://api.example.com/userinfo"
user_data = requests.get(protected_url, headers=headers)
print(user_data.json())
```

</details>


### Variáveis de Ambiente<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
Variáveis de ambiente permitem que você armazene dados sensíveis (como chaves de API, senhas, segredos) fora do seu código-fonte.
Em vez de fazer isso ❌:

```python
API_KEY = "minha-chave-de-api-super-secreta-123"
```

Você faz isso ✅:

```python
import os
API_KEY = os.getenv("API_KEY")
```

Em seguida, defina a chave em seu ambiente:

```bash
export API_KEY=minha-chave-de-api-super-secreta-123
```

| Benefício | Por que é importante |
| --- | --- |
| **Segurança** | Mantém segredos fora do código-fonte (por exemplo, repositório do GitHub) |
| **Configurabilidade** | Você pode alterar chaves ou configurações **sem alterar o código** |
| **Específico do Ambiente** | Valores diferentes para desenvolvimento, homologação, produção |
| **Reutilização** | Mesmo código-base, configurações diferentes com base no ambiente |
| **Amigável para a Nuvem** | Todas as principais plataformas de nuvem suportam o gerenciamento de segredos por meio de variáveis de ambiente |

Para desenvolvimento local, você pode armazenar segredos em um arquivo `.env`:
`.env`
```ini
API_KEY=abcdef123456
DB_PASSWORD=minha_senha_db
```

Carregue-o em Python
```bash
pip install python-dotenv
```

```python
from dotenv import load_dotenv
import os

load_dotenv() # carrega do arquivo .env
api_key = os.getenv("API_KEY")
```

{: .warning}
> NUNCA escreva segredos diretamente no seu código. Se você cometer um segredo no GitHub:
> 🔓 Qualquer um pode vê-lo,
> 🤖 Bots escaneiam constantemente repositórios públicos em busca de segredos,
> 💣 Provedores de API podem revogar ou abusar das chaves e
> ☠️ Você pode ser cobrado ou atacado (por exemplo, se as chaves da AWS forem vazadas)

{: .warning}
> Agentes de codificação de IA 🕵️ têm a tendência de codificar chaves de API. SEMPRE revise seu código!!

{: .warning}
> Garanta que o `.gitignore` exclua o `.env` de ser enviado para o GitHub


---
### 🍏 1. Painel de Hábitos e Nutrição usando Google Sheets e Nutritionix<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

O objetivo deste exercício é criar um aplicativo de texto para rastrear sua ingestão diária de alimentos e exercícios. Usaremos as seguintes APIs:

- **Nutritionix**: Para analisar itens de comida e exercício
- **Google Sheets (via Sheety)**: Para armazenar dados


#### Nutritionix<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Teremos que criar uma conta gratuita no [Nutritionix](https://www.nutritionix.com/business/api) e, em seguida, criar uma [chave de API](https://developer.nutritionix.com/admin/access_details) e salvá-las no arquivo `.env`.

![Chave de API do Nutritionix](Nutritionix_API_key.png)

Arquivo `.env`
```python
NUTRITIONIX_KEY="ec3***"
NUTRITIONIX_ID="8b***"
```

Em seguida, podemos fazer alguns testes de ENDPOINT, conforme explicado na [documentação de primeiros passos](https://docx.syndigo.com/developers/docs/get-started), para os quais podemos usar o Postman para testar alguns [Endpoints](https://docx.syndigo.com/developers/docs/natural-language-for-nutrients).

![Postman](Nutritionix_Postman.png)

Depois de entendermos os cabeçalhos e a sintaxe de autenticação, passamos para o código Python da seguinte forma:

```python
import requests, os
import datetime
from dotenv import load_dotenv
import json

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Nutritionix
NUTRITIONIX_NLP_NUTRIENTS_URL_ENDPOINT = " https://trackapi.nutritionix.com/v2/natural/nutrients"
headers = {
    "Content-Type": 'application/json',
    "x-app-id": os.environ.get("NUTRITIONIX_ID"),
    "x-app-key": os.environ.get("NUTRITIONIX_KEY"),
}
print(headers)
query = input("O que você comeu? ")
data = {"query": query}
nutrition_response = requests.post(NUTRITIONIX_NLP_NUTRIENTS_URL_ENDPOINT, headers=headers,json=data )
calories = nutrition_response.json()["foods"][0]["nf_calories"]
print(f"Calorias consumidas em {query}: {calories}")


NUTRITIONIX_NLP_EXERCISE_URL_ENDPOINT = " https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_config = {"query": input("Quais exercícios você fez (você pode incluir duração e/ou distância)?: "),}

exercise_response = requests.post(NUTRITIONIX_NLP_EXERCISE_URL_ENDPOINT, headers=headers, json=exercise_config)

user_input = exercise_response.json()["exercises"][0]["user_input"]
duration = exercise_response.json()["exercises"][0]["duration_min"]
calories = exercise_response.json()["exercises"][0]["nf_calories"]
print(f"Exercício: {user_input}, Duração: {duration}, Calorias: {calories}")

# Salva a resposta em um arquivo JSON
with open('nlp_food.json', 'w') as f:
    json.dump(nutrition_response.json(), f, indent=4)
with open('nlp_exercise.json', 'w') as f:
    json.dump(exercise_response.json(), f, indent=4)

```

#### Google Sheets com SHEETY<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Para armazenar os dados, usaremos o Google Sheets e a API Sheety. Teremos que nos inscrever gratuitamente no [Sheety](https://sheety.co/) e criar um projeto.

![Projeto Sheety](Sheety_new_project.png)

Que precisa ser vinculado a uma Planilha Google. Também criaremos as tabelas que queremos preencher.

![Planilha Google](Google_sheets_setup.png)

Em seguida, teremos que criar um código de autenticação no Sheety.

![código de autenticação](Sheety_Authentication.png)

E permitir requisições POST nele.

![Requisição POST Sheety](Sheety_Allow_post_request.png)

Em seguida, montamos os cabeçalhos e o payload e escrevemos as requisições POST para preencher a planilha do Google.

```python
# Google Sheets
SHEETY_AUTH_TOKEN = os.environ.get("SHEETY_AUTH_TOKEN")
SHEETY_NUTRITION_ENDPOINT_API = os.environ.get("SHEETY_NUTRITION_URL")
SHEETY_EXERCISE_ENDPOINT_API = os.environ.get("SHEETY_EXERCISE_URL")

headers = {
    "Authorization": SHEETY_AUTH_TOKEN,
}


#Registra a data e a hora atuais
date = datetime.datetime.now()
formatted_date = date.strftime("%d/%m/%Y")
time = date.strftime("%H:%M:%S")

nutrition_data = {
    "nutrition": {
      "date": formatted_date,
      "time": time,
      "food": query,
      "calories": calories,
    }
  }

workout_data = {
    "exercise": {
      "date": formatted_date,
      "time": time,
      "exercise": user_input,
      "duration": duration,
      "calories": calories,
    }
  }


# Adiciona nova linha à planilha com os dados inseridos
#print(headers)
new_response = requests.post(url=SHEETY_NUTRITION_ENDPOINT_API, json=nutrition_data, headers=headers)
new_response = requests.post(url=SHEETY_EXERCISE_ENDPOINT_API, json=workout_data, headers=headers)
#print(new_response.text)

```


---


### 📈 2. Ações e Notícias com Alertas de Whatsapp<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

#### APIs Usadas<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
- **Alpha Vantage**: Dados de ações em tempo real
- **API de Notícias FINNHUB**: Notícias financeiras
- **API de Bot do Twilio**: Envio de mensagens

#### Preços de ações com Alpha Vantage<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

A configuração da API do alphavantage é relativamente simples. Você simplesmente preenche o [Formulário](https://www.alphavantage.co/support/) para obter a chave que precisa ir para o seu arquivo `.env`.

<details markdown="block">
  <summary>
    Formulário de chave de API do Alpha Vantage
  </summary>

![Formulário_de_Chave_de_API_Alpha_Vantage](Alpha_Vantage_Key.png)

</details>


```python
from dotenv import load_dotenv
import requests, os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Preço da ação
stock_params = {"symbol": "APPL", "apikey": os.getenv("ALPHA_API_KEY")}
stock_response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY", params=stock_params)
data = stock_response.json()
yesterday = list(data["Time Series (Daily)"].keys())[0]
price = float(data["Time Series (Daily)"][yesterday]["4. close"])
print(f"Preço de fechamento da APPL ontem {yesterday}: ${price}")
```
Arquivo `.env`
```python
ALPHA_API_KEY="***"
TWILIO_ACCOUNT_SID="***"
TWILIO_AUTH_TOKEN="***"
FINNHUB_API_KEY="***"
```

#### Obter notícias financeiras<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
Na segunda parte deste exemplo, vamos aprender a nos conectar ao [Finhub](https://finnhub.io/dashboard), que fornece notícias financeiras com um nível gratuito. Você precisará então criar uma chave de API.

![Chave de API Finnhub](FINNHUB_API_key.png)

Desta vez, vamos usar seu [repositório python](https://github.com/Finnhub-Stock-API/finnhub-python) muito bem documentado, primeiro instalando-o.

```bash
pip install finnhub-python
```
E então, um de seus exemplos de código é usado.

```python
# API de Notícias
import finnhub
import datetime

# Obter datas
today = datetime.datetime.now().strftime('%Y-%m-%d')
yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

# Configurar cliente
finnhub_client = finnhub.Client(api_key=os.environ.get("FINNHUB_API_KEY"))
# Notícias da Empresa
# Precisa usar _from em vez de from para evitar conflito
latest_news = finnhub_client.company_news('AAPL', _from=yesterday, to=today)
print(f"Últimas notícias para AAPL de {yesterday} a {today}:")

for news in latest_news[:5]:
    print(f"Título: {news['headline']}")
    print(f"Fonte: {news['source']}")
    print(f"Data: {news['datetime']}")
    print(f"Resumo: {news['summary']}")
    print("-" * 50)
```
O que resulta em


```
Últimas notícias para AAPL de 2025-06-08 a 2025-06-09:
Título: A Nova Linguagem de Design da Apple
Fonte: Finnhub
Data: 1749486328
Resumo: Espera-se que a Apple apresente um novo redesenho de seu software em todos os seus produtos na WWDC deste ano. Mark Gurman, da Bloomberg, explica....
--------------------------------------------------
Título: Construindo um Portfólio de Dividendos de $75.000: Aprimorando o SCHD com as Melhores Escolhas de Alto Rendimento de Junho
Fonte: SeekingAlpha
Data: 1749481200
Resumo: O SCHD continua sendo uma opção de investimento particularmente atraente para investidores de longo prazo. Confira como construir um portfólio de dividendos de $75.000 com o SCHD como núcleo.
```

#### Enviar e-mails, Whatsapps, SMS, Vídeo, Áudio com o Twilio<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Agora vamos tentar usar o [Twilio](https://www.twilio.com/en-us), que tem uma API muito poderosa para enviar e-mails, mensagens de Whatsapp, SMS e muito mais.

Na [primeira vez](https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn?frameUrl=%2Fconsole%2Fsms%2Fwhatsapp%2Flearn%3Fx-target-region%3Dus1) que você usar, após configurar as Chaves, você terá que fazer login com uma conta do Whatsapp. Ele pedirá para você abrir um código QR e o guiará pelo processo. Você também pode enviar uma mensagem de texto com `join finally-gold` para `+14155238886`<br>

<img src="Twilio_Mobile_Phone1.jpg" alt="Twilio Connect Whatsapp" width="40%">


Em seguida, você pode [testar requisições](https://console.twilio.com/us1/develop/sms/content-template-builder/template/HX38f4a38e390bfec8bfe8760c5d013619) na web que você pode aplicar diretamente ao seu código.

![Teste do Twilio na Web](Twilio_Test_Web.png)


<img src="Twilio_Mobile_Phone2.jpg" alt="Twilio Enviar para Whatsapp" width="40%">

O Twilio tem vários modelos para as mensagens e também permite que você crie os seus próprios.

![Construtor de Modelos de Conteúdo](Twilio_Content_Template_Builder.png)

Se implementarmos este código em nosso script, em vez de usá-lo diretamente na área de testes do portal, ele se parecerá com o trecho abaixo:

{% raw %}
```python
# Enviar mensagem via WhatsApp do Twilio
from twilio.rest import Client

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token =  os.environ.get('TWILIO_AUTH_TOKEN')
print("SID da conta Twilio:", account_sid)
print("Token de autenticação Twilio:", auth_token)
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    #content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e', # Seu agendamento está chegando em {1} às {2}
    #content_variables='{"1":"12/1","2":"3pm"}',
    #content_sid='HX350d429d32e64a552466cafecbe95f3c', # Obrigado pelo seu pedido. Sua entrega está agendada para {1} às {2}
    #content_variables='{"1":"12/1","2":"3pm"}',
    #content_sid='HX229f5a04fd0510ce1b071852155d3e75', # {1} é o seu código de verificação. Para sua segurança, não compartilhe este código.
    #content_variables='{"1":"409173"}',    
    content_sid='HX38f4a38e390bfec8bfe8760c5d013619', # Preço de fechamento da APPL: ${{1}}
    content_variables=f'{{"1":"{price}"}}',
    to='whatsapp:+44SEU NÚMERO DE TELEFONE VAI AQUI'
)

print(message.sid)
```
{% endraw %}


---



### ✈️ 3. Buscador de Voos Baratos e Alertas por E-mail<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

#### APIs Usadas e processo de desenvolvimento<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
Neste exemplo, criaremos um aplicativo de texto que usa a API da Amadeus para busca de voos e envia alertas por e-mail usando a API do Gmail. Para chegar a esse ponto, aprenderemos como navegar na documentação do GitHub e obter suporte de LLMs e Agentes para cada uma das etapas envolvidas:
- Autenticar na Amadeus
- Para buscar voos fazendo uma Requisição e usando **datetime** para gerenciamento de datas.
- Processar a resposta em um **arquivo json**, um **arquivo csv**
- Para enviar uma notificação por e-mail com **smtp**.

A primeira coisa seria solicitar a um LLM (seja Claude, Gemini ou Chat GPT) na web ou no GitHub Copilot dentro do VSCode. Pediríamos que ele criasse um script em python para buscar voos em uma data específica com o serviço de API que decidimos. Os que eu olhei foram [Tequila](https://tequila.kiwi.com/), que precisa de registro manual por e-mail, [Skyscanner](https://www.partners.skyscanner.net/product/travel-api), que precisa de uma conta empresarial, e [Amadeus](https://developers.amadeus.com/register), que atualmente (09/06/2025) é gratuito e fácil de [registrar](https://developers.amadeus.com/register). Seguimos os passos em [Comece](https://developers.amadeus.com/get-started/get-started-with-self-service-apis-335) para obter as chaves.

![Chaves-Amadeus](Amadeus_key.png)

Em seguida, as adicionamos ao arquivo `.env` no mesmo diretório do script python ou no `PATH`.

```python
AMADEUS_API_KEY="b4t2..."
AMADEUS_API_SECRET="qxD..."
EMAIL_ADDRESS="m...@gmail.com"
GMAIL_PASSWORD="cyjb ..."
OPENWEATHER_API_KEY="24a..."
```

O código que foi gerado em todas as tentativas com os LLMs e agentes não funcionou, mas forneceu alguma estrutura e mencionou a biblioteca do GitHub [amadeus4dev](https://github.com/amadeus4dev/amadeus-python/tree/master), que contém [manual](https://github.com/amadeus4dev/amadeus-python/tree/master) e [exemplos](https://github.com/amadeus4dev/amadeus-code-examples) simples.

Nós o instalamos executando a seguinte linha no bash:
```python
pip install amadeus
```
#### Requisição e arquivo json<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
Então, obtemos o seguinte código que se conecta à Amadeus e exporta a resposta para um arquivo json.


```python
from amadeus import Client, ResponseError
import os, smtplib
from dotenv import load_dotenv
from datetime import datetime, timedelta
import json
import csv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

amadeus = Client(
    client_id= os.getenv("AMADEUS_API_KEY"),
    client_secret= os.getenv("AMADEUS_API_SECRET")    
)


try:
    # -------------------------------------------------------------
    # Buscar voos
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode='LON',
        destinationLocationCode='SCQ',
        departureDate=(datetime.now() + timedelta(days=10)).strftime("%Y-%m-%d"),
        adults=1,
        currencyCode='GBP')
    
    # -------------------------------------------------------------
    # Salvar resposta em um arquivo JSON
    with open('flight_offers.json', 'w') as f:
        json.dump(response.data, f, indent=4)
```

<details markdown="block">
  <summary>
    Arquivo de resposta Json
  </summary>

```json
[
    {
        "type": "flight-offer",
        "id": "1",
        "source": "GDS",
        "instantTicketingRequired": false,
        "nonHomogeneous": false,
        "oneWay": false,
        "isUpsellOffer": false,
        "lastTicketingDate": "2025-06-10",
        "lastTicketingDateTime": "2025-06-10",
        "numberOfBookableSeats": 9,
        "itineraries": [
            {
                "duration": "PT2H10M",
                "segments": [
                    {
                        "departure": {
                            "iataCode": "LGW",
                            "terminal": "S",
                            "at": "2025-06-19T15:25:00"
                        },
                        "arrival": {
                            "iataCode": "SCQ",
                            "at": "2025-06-19T18:35:00"
                        },
                        "carrierCode": "VY",
                        "number": "7107",
                        "aircraft": {
                            "code": "320"
                        },
                        "operating": {
                            "carrierCode": "VY"
                        },
                        "duration": "PT2H10M",
                        "id": "9",
                        "numberOfStops": 0,
                        "blacklistedInEU": false
                    }
                ]
            }
        ],
        "price": {
            "currency": "GBP",
            "total": "106.38",
            "base": "73.00",
            "fees": [
                {
                    "amount": "0.00",
                    "type": "SUPPLIER"
                },
                {
                    "amount": "0.00",
                    "type": "TICKETING"
                }
            ],
            "grandTotal": "106.38"
        },
        "pricingOptions": {
            "fareType": [
                "PUBLISHED"
            ],
            "includedCheckedBagsOnly": true
        },
        "validatingAirlineCodes": [
            "VY"
        ],
        "travelerPricings": [
            {
                "travelerId": "1",
                "fareOption": "STANDARD",
                "travelerType": "ADULT",
                "price": {
                    "currency": "GBP",
                    "total": "106.38",
                    "base": "73.00"
                },
                "fareDetailsBySegment": [
                    {
                        "segmentId": "9",
                        "cabin": "ECONOMY",
                        "fareBasis": "OWFLX",
                        "class": "O",
                        "includedCheckedBags": {
                            "weight": 25,
                            "weightUnit": "KG"
                        },
                        "includedCabinBags": {
                            "quantity": 1
                        }
                    }
                ]
            }
        ]
    }
]
```
</details>

#### Exportar para um arquivo csv<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>


Agora pedimos ao agente de IA LLM para criar uma tabela em um arquivo csv com os campos desejados e fornecemos o arquivo .py e o .json para contexto. E obtivemos o resultado abaixo.

```python
    # -------------------------------------------------------------
    # Extrair dados de voos para CSV
    csv_data = []
    for offer in response.data:
        price_grand_total = offer['price']['grandTotal']
        
        # Processar cada itinerário
        for itinerary in offer['itineraries']:
            # Para cada segmento no itinerário
            for segment in itinerary['segments']:
                # Obter informações básicas do segmento
                dep_iata = segment['departure']['iataCode']
                dep_time = segment['departure']['at']
                arr_iata = segment['arrival']['iataCode']
                arr_time = segment['arrival']['at']
                carrier_code = segment['carrierCode']
                
                # Obter informações de bagagem do primeiro preço do viajante
                baggage_info = {}
                cabin_bags_qty = None
                checked_bags_weight = None
                checked_bags_weight_unit = None
                
                if 'travelerPricings' in offer:
                    for pricing in offer['travelerPricings']:
                        for fare_detail in pricing['fareDetailsBySegment']:
                            if fare_detail['segmentId'] == segment['id']:
                                if 'includedCheckedBags' in fare_detail:
                                    if 'weight' in fare_detail['includedCheckedBags']:
                                        checked_bags_weight = fare_detail['includedCheckedBags']['weight']
                                        checked_bags_weight_unit = fare_detail['includedCheckedBags'].get('weightUnit', 'N/A')
                                    elif 'quantity' in fare_detail['includedCheckedBags']:
                                        checked_bags_weight = fare_detail['includedCheckedBags']['quantity']
                                        checked_bags_weight_unit = 'PIECES'
                                
                                if 'includedCabinBags' in fare_detail and 'quantity' in fare_detail['includedCabinBags']:
                                    cabin_bags_qty = fare_detail['includedCabinBags']['quantity']
                
                # Adicionar aos dados do CSV
                csv_data.append({
                    'departure_iatacode': dep_iata,
                    'departure_at': dep_time,
                    'arrival_iatacode': arr_iata,
                    'arrival_at': arr_time,
                    'carriercode': carrier_code,
                    'price_grandtotal': price_grand_total,
                    'included_checkedbags_weight': checked_bags_weight,
                    'included_checkedbags_weightunit': checked_bags_weight_unit,
                    'included_cabinbags_quantity': cabin_bags_qty
                })
    
    # Escrever para CSV
    csv_fields = ['departure_iatacode', 'departure_at', 'arrival_iatacode', 'arrival_at', 
                 'carriercode', 'price_grandtotal', 'included_checkedbags_weight', 
                 'included_checkedbags_weightunit', 'included_cabinbags_quantity']
    with open('flight_data.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_fields)
        writer.writeheader()
        writer.writerows(csv_data)
    
    print(f"Dados de voo extraídos e salvos em flight_data.csv")
```

#### Enviar alertas por e-mail<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Da mesma forma, pedimos ao Gemini para adicionar um alerta por e-mail se o preço do voo for inferior a 150 GBP usando SMTP e Gmail. Ele veio com o código abaixo e só temos que garantir que as senhas no arquivo `.env` estão corretas.


```python
    # -------------------------------------------------------------
    # Verificar se algum voo está abaixo do limite de preço e enviar notificação por e-mail
    for offer in response.data:
        price_grand_total = float(offer['price']['grandTotal'])
        if price_grand_total < 150:
            try:
                with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                    connection.starttls()
                    connection.login(user=os.getenv("EMAIL_ADDRESS"), password=os.getenv("GMAIL_PASSWORD"))
                    connection.sendmail(
                        from_addr=os.getenv("EMAIL_ADDRESS"),
                        to_addrs="toemail@gmail.com",
                        msg=f"Subject:Alerta de Voo Barato!\n\nApenas {price_grand_total}GBP para voar para Santiago de Compostela!\n Em {dep_time} com {offer['itineraries'][0]['segments'][0]['carrierCode']}.\n\n"
                    )
                print(f"Alerta de e-mail enviado para voo com preço de £{price_grand_total}")
            except Exception as e:
                print(f"Falha ao enviar alerta de e-mail: {e}")
    
except ResponseError as error:
    print(error)
```

Quando tentamos pela primeira vez com nossa senha normal, recebemos um erro do servidor

```bash
Falha ao enviar alerta por e-mail: (534, b'5.7.9 Senha específica do aplicativo necessária. Para mais informações, acesse\n5.7.9 https://support.google.com/mail/?p=InvalidSecondFactor 5b1f17b1804b1-4526e0563cesm112983275e9.1 - gsmtp')
```

o que nos levou a um site onde temos que configurar uma senha para um aplicativo de desenvolvimento.
![Senha-de-App-do-Gmail](Gmail_App_API.png)



---

## ✅ Resumo<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

| Conceito | Ferramentas Usadas |
|---|---|
| Fundamentos de API | `requests`, `json`, tratamento de erros |
| Autenticação | Chave de API, Autenticação Básica |
| JSON | `json.load`, `json.dump` |
| Armazenamento de Dados | `.env`, Google Sheets via Sheety, arquivo csv |
| Comunicação | E-mail (SMTP), Twilio |


> 🚀 Este tutorial une a teoria à prática usando aplicações empolgantes e com propósito. Agora você tem as ferramentas para construir seus próprios projetos alimentados por API!
