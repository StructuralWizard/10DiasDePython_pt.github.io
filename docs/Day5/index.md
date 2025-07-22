---
title: Dia 5 Web Scraping com Beautiful Soup e Selenium
layout: default
nav_order: 6
has_children: false
nav_exclude: false
---

# Dia 5. Web Scraping. 🕷️ Beautiful Soup e Selenium
{: .no_toc }

Bem-vindo ao Dia 5! Hoje, você aprenderá a extrair dados de sites usando Python. Começaremos com o Beautiful Soup para páginas estáticas e, em seguida, avançaremos para o Selenium para sites dinâmicos e interativos. Ao final, você será capaz de coletar dados da web para seus próprios projetos!

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

## 🌱 O que é Web Scraping?
Web scraping é o processo de coletar informações de sites automaticamente. É útil para coletar dados que não estão disponíveis por meio de uma API.

- **Beautiful Soup**: Analisa documentos HTML e XML. Ótimo para páginas estáticas.
- **Selenium**: Automatiza navegadores. Útil para sites dinâmicos que exigem interação (cliques, digitação, etc.).

---

## 🥣 Noções Básicas do Beautiful Soup <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
Para analisar e navegar em HTML/XML com Python
Requer: `beautifulsoup4` e um analisador como `lxml` ou o `html.parser` embutido do Python.

### 🧩 O que você pode fazer com o Beautiful Soup?
Aqui está um resumo de suas principais capacidades:

* **Analisar HTML e XML:** O Beautiful Soup pega o conteúdo HTML ou XML bruto e o transforma em uma "árvore de análise" navegável, composta por objetos Python. Essa árvore torna simples o acesso e a manipulação de partes específicas do documento.

* **Navegar na Árvore de Análise:** Você pode se mover facilmente pela estrutura HTML/XML:
    * **Por nome da tag:** Encontre elementos como `<div>`, `<a>` ou `<p>`.
    * **Por atributos:** Localize elementos com base em seu `id`, `class`, `href` ou qualquer outro atributo.
    * **Por conteúdo de texto:** Pesquise por palavras ou frases específicas dentro dos elementos.
    * **Usando relacionamentos:** Navegue para cima (pai), para baixo (filhos, descendentes) ou para os lados (irmãos) na árvore.

* **Pesquisar por Elementos Específicos:** O Beautiful Soup oferece métodos poderosos como `find()` (para obter a primeira correspondência) e `find_all()` (para obter todas as correspondências) para identificar os dados exatos que você está procurando. Você pode combinar isso com vários filtros (nomes de tags, atributos, seletores CSS, expressões regulares ou até mesmo funções personalizadas) para uma seleção precisa.

* **Extrair Dados:** Depois de encontrar os elementos que deseja, você pode extrair facilmente:
    * **Conteúdo de texto:** Obtenha o texto visível dentro de uma tag (por exemplo, `soup.title.string`).
    * **Valores de atributos:** Acesse os valores de atributos como `href` de uma tag `<a>` ou `src` de uma tag `<img>`.

* **Lidar com HTML Malformado:** Uma das forças do Beautiful Soup é sua capacidade de lidar com "sopa de tags"—HTML mal estruturado ou incompleto. Ele tenta fazer sentido e construir uma árvore de análise utilizável.

* **Integrar com Outras Bibliotecas:**
    * **Requests:** Frequentemente usado com a biblioteca `requests` para buscar o conteúdo HTML de uma URL antes que o Beautiful Soup o analise.
    * **Selenium:** Para sites dinâmicos que dependem muito de JavaScript para renderização, você pode usar o Selenium (uma ferramenta de automação de navegador) para carregar a página e, em seguida, passar o HTML renderizado para o Beautiful Soup para análise.
    * **Pandas:** Os dados extraídos podem ser facilmente estruturados e armazenados em DataFrames do Pandas para análise posterior ou exportação para formatos como CSV ou Excel.

---

### 🧰 Usos Comuns do Beautiful Soup

O Beautiful Soup é usado principalmente para:

* **Web Scraping:** Este é seu principal propósito. Você pode usá-lo para:
    * Coletar informações de produtos (nomes, preços, descrições) de sites de comércio eletrônico.
    * Extrair artigos de notícias, postagens de blog ou artigos de pesquisa.
    * Coletar listas de empregos ou dados imobiliários.
    * Realizar análise de sentimento raspando avaliações ou comentários.
* **Mineração de Dados:** Transformar dados da web não estruturados em conjuntos de dados organizados para análise.
* **Agregação de Conteúdo:** Construir ferramentas que extraem conteúdo de várias fontes online para um local centralizado.

Em resumo, o Beautiful Soup capacita os desenvolvedores Python a interagir programaticamente com o conteúdo da web, tornando-o uma ferramenta essencial para quem deseja extrair e trabalhar com dados da internet.

### 📦 Instale os pacotes necessários
```bash
pip install beautifulsoup4 requests lxml
```

### 📄 Exemplo: Raspando um Arquivo HTML Local
Suponha que você tenha um arquivo chamado `website.html`:

```python
from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
```

### 🧼 Limpando HTML
```python
clean_text = soup.get_text(strip=True)
```

### 🔍 Encontrando Elementos
Você pode procurar por tags, classes, ids e muito mais:

```python
# Encontra a primeira tag <a>
anchor = soup.find("a")
print(anchor)

# Encontra todas as tags <a>
all_anchors = soup.find_all("a")
for tag in all_anchors:
    # .getText() obtém o texto visível dentro da tag
    print(tag.getText())
    # .get() recupera o valor de um atributo (por exemplo, href)
    print(tag.get("href"))
```

#### Pesquisar por atributos (id, classe, etc.)
```python
# Encontrar por id
heading = soup.find(name="h1", id="name")

# Encontrar por classe (nota: use class_ porque 'class' é uma palavra reservada)
section = soup.find(name="h3", class_="heading")

# Encontrar todos os elementos com uma classe específica
items = soup.find_all(class_="item")
```

#### Pesquisar usando seletores CSS
```python
# Use .select() para seletores CSS
links = soup.select("a.storylink")  # Todas as tags <a> com a classe 'storylink'
ids = soup.select("#main")          # Elemento com o id 'main'
classes = soup.select(".heading")   # Todos os elementos com a classe 'heading'
```

### 🌳 Navegando na Árvore
```python
tag.name         # Nome da tag
tag.attrs        # Atributos da tag como dict
tag['href']      # Atributo específico

tag.text         # Todo o texto dentro da tag (recursivo)
tag.string       # Apenas a string direta
tag.parent
tag.children      # Gerador de filhos
tag.contents      # Lista de filhos
tag.next_sibling
tag.previous_sibling

```


### 🔗 Navegando e Seguindo Links
Você pode extrair e seguir links combinando `.get("href")` com `requests`:

```python
for tag in soup.find_all("a"):
    link = tag.get("href")
    if link and link.startswith("http"):
        print("Seguindo:", link)
        # Você pode buscar a página vinculada com requests.get(link)
```

Para mais referências, consulte a <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" target="_blank">documentação</a>.


---

## 🌐 Raspando Sites ao Vivo <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Para raspar um site ao vivo, use a biblioteca `requests` para buscar a página:

```python
import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

# Obtém todos os títulos dos artigos
titles = soup.find_all("a", class_="storylink")
for title in titles:
    print(title.getText())
```

---

## ⚖️ Web Scraping é Legal? <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

- Raspe apenas dados públicos.
- Respeite o `robots.txt` e os termos do site.
- Não sobrecarregue os servidores (adicione atrasos se estiver raspando muitas páginas).
- Use os dados raspados de forma responsável.

---

## 🤖 Selenium para Sites Dinâmicos <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Alguns sites carregam conteúdo com JavaScript ou exigem interação. O Selenium permite que você controle um navegador real para lidar com esses casos.

Ao contrário do Beautiful Soup, que se limita a raspar dados, o Selenium permite a interação com páginas da web, como digitar, clicar e rolar. Ele permite a automação de ações contínuas e fluxos de trabalho inteiros de uma determinada tarefa ou trabalho. Ele efetivamente controla um navegador para realizar ações como um usuário humano.

O Selenium pode automatizar quase tudo que um humano pode fazer em um site, como preencher formulários, transferir informações ou jogar jogos baseados na web.

### 🚗 Introdução ao Selenium WebDriver

* **O que é:** O Selenium WebDriver é uma ferramenta de automação e teste bem conhecida para desenvolvedores da web.
* **Por que usá-lo (em vez do Beautiful Soup):** Ao contrário do Beautiful Soup, que se limita a raspar dados, o Selenium permite a interação com páginas da web, como digitar, clicar e rolar. Ele permite a automação de ações contínuas e fluxos de trabalho inteiros de uma determinada tarefa ou trabalho. Ele efetivamente controla um navegador para realizar ações como um usuário humano.
* **Capacidades:** O Selenium pode automatizar quase tudo que um humano pode fazer em um site, como preencher formulários, transferir informações ou jogar jogos baseados na web.

### 🔧 Instalação e Configuração do Selenium

1.  **Instale o Navegador Chrome:** Embora o Selenium funcione com outros navegadores como Firefox ou Safari, o Chrome é recomendado para consistência e uso das Ferramentas de Desenvolvedor do Chrome. Baixe o driver do Chrome em [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads) e coloque-o em seu PATH.
2.  **Instale o Pacote Selenium:**
    * Importe `selenium` em seu arquivo Python (por exemplo, `main.py`).
    * Instale o pacote usando a opção de lâmpada fornecida em seu IDE.
```bash
pip install selenium
```
3.  **Importe o Módulo WebDriver:** Altere a declaração de importação para `from selenium import webdriver`.
4.  **Crie uma Instância do Driver:** Inicialize um objeto de driver do Chrome: `driver = webdriver.Chrome()`.
    * **Chromedriver:** Ele atua como uma ponte entre o código Selenium и o navegador Chrome, dizendo ao Selenium como interagir com o navegador. Existem diferentes drivers para diferentes navegadores (por exemplo, Safari, Firefox).
5.  **Controle do Navegador:**
    * `driver.close()`: Fecha a aba ativa.
    * `driver.quit()`: Encerra o navegador inteiro. É preferível usar `quit()` após concluir as tarefas para garantir uma nova instância do navegador para futuras execuções.

### 🔎 Exemplo: Abrir uma Página e Encontrar um Elemento
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time as time_module

# Inicia o navegador
browser = webdriver.Chrome()
browser.get("https://www.python.org")

# Encontra elementos
event_times = browser.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = browser.find_elements(By.CSS_SELECTOR, ".event-widget li a")

for time, name in zip(event_times, event_names):
    print(time.text, name.text)

# Espera 3 segundos antes de fechar
time_module.sleep(3)

browser.quit()
```

### 🔍 Encontrando e Selecionando Elementos em um Site

**Localizando Elementos:**

O Selenium oferece várias estratégias para encontrar elementos HTML em uma página da web. Depois de identificar um elemento com a ferramenta de inspeção do navegador, você pode copiar seu XPath ou outro identificador e usá-lo com:

* **Método `find_element()`:** Usado para encontrar um único elemento.
* **Classe `By`:** Importante para especificar a estratégia de localização (por exemplo, `By.CLASS_NAME`, `By.ID`, `By.NAME`, `By.LINK_TEXT`).
* **Exemplos:**
    * **Por Nome da Classe:** Para obter o preço de um item na Amazon, você pode encontrar elementos com classes como "a-price-whole" (para dólares) e "a-price-fraction" (para centavos).
    * **Acessando o Conteúdo de Texto:** Depois de encontrar um elemento, use `.text` para recuperar o conteúdo de texto dentro desse elemento HTML.
    * **Por Nome:** Útil para campos de entrada de formulário.
    * **Por Texto do Link:** Especificamente para clicar em links pelo texto visível.
* **Método `find_elements()`:** Para cada método `find_element()`, existe um `find_elements()` correspondente que retorna uma lista de todos os elementos correspondentes.
* **Inspecionando Elementos:** Use as Ferramentas de Desenvolvedor do Chrome (botão direito -> Inspecionar) para examinar a estrutura HTML e identificar IDs, nomes de classes ou outros atributos para elementos.

### 🖱️ Automatizando Interações (Digitação e Cliques)

* **Clicando em Elementos:**
    * Depois de identificar um elemento, use o método `.click()` no objeto do elemento.
    * O Selenium pode clicar em links com base em seu `LINK_TEXT`.
* **Digitando em Campos de Entrada:**
    * Primeiro, encontre o elemento do campo de entrada.
    * Use o método `.send_keys()` no objeto do elemento, passando a string que você deseja digitar.
* **Enviando Teclas Especiais:** Para enviar teclas como `Enter` ou `Return`, importe a classe `Keys` de `selenium.webdriver.common.keys`.


---

## 📝 Desafio: Raspar os Próximos Eventos do Python <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

- Use o Selenium para abrir [python.org](https://www.python.org/)
- Extraia a data e o nome dos próximos 5 eventos
- Armazene-os em um dicionário como:

```python
events = {
    0: {"time": "2025-06-11", "name": "PyCon"},
    1: {"time": "2025-06-18", "name": "DjangoCon"},
    # ...
}
```

---

## 🚀 Resumo <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

- Use o Beautiful Soup para raspagem de HTML estático
- Use o Selenium para sites dinâmicos e interativos
- Sempre respeite as regras e a ética do site

Agora você tem as ferramentas para coletar dados de quase qualquer site. Boa raspagem!
