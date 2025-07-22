# Folha de Dicas do BeautifulSoup
O BeautifulSoup é uma biblioteca Python para analisar documentos HTML e XML. Ele cria uma árvore de análise para páginas analisadas que pode ser usada para extrair dados de HTML, o que é útil para web scraping.

## 1. Instalação
Se você não tiver o BeautifulSoup instalado, pode instalá-lo usando o pip:

```bash
pip install beautifulsoup4
pip install lxml # Opcional, mas recomendado para uma análise mais rápida
```

## 2. Análise Básica
Para começar, você precisa importar o BeautifulSoup e fornecer a ele o conteúdo HTML/XML.

```python
from bs4 import BeautifulSoup

# Conteúdo HTML de exemplo
html_doc = """
<html><head><title>Meu Documento</title></head>
<body>
    <p class="title"><b>O Título do Documento</b></p>

    <a href="http://example.com/one" class="external-link" id="link1">Link Um</a>
    <a href="http://example.com/two" class="external-link" id="link2">Link Dois</a>
    <p>Este é outro conteúdo.</p>
    <div class="container">
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
        </ul>
    </div>
</body>
</html>
"""

# Cria um objeto BeautifulSoup
# 'lxml' é um analisador comum e rápido; 'html.parser' é integrado
soup = BeautifulSoup(html_doc, 'lxml')

# Imprime o HTML analisado de forma bonita
print(soup.prettify())
```

## 3. Navegando na Árvore de Análise
O BeautifulSoup permite que você navegue no documento analisado usando acesso orientado a objetos.

### Acessando Tags
Você pode acessar as tags diretamente como atributos do objeto BeautifulSoup ou de outras tags.

```python
# Obtém a primeira tag <head>
head_tag = soup.head
print(f"Tag Head: {head_tag}")

# Obtém a primeira tag <title> dentro de <head>
title_tag = soup.title
print(f"Tag Title: {title_tag}")

# Obtém o nome da tag
print(f"Nome da Tag Title: {title_tag.name}")

# Obtém o conteúdo de string da tag
print(f"Conteúdo da Tag Title: {title_tag.string}")

# Acessando atributos de uma tag
link_one = soup.a
print(f"href do Link Um: {link_one['href']}")
print(f"class do Link Um: {link_one['class']}")

# Obtém todos os atributos como um dicionário
print(f"Atributos do Link Um: {link_one.attrs}")
```

### Navegando para Baixo
- `.contents`: Uma lista dos filhos diretos da tag.
- `.children`: Um iterador dos filhos diretos da tag.
- `.descendants`: Um iterador de todos os filhos, netos, etc.

```python
body_tag = soup.body
print("\nConteúdo da Tag Body:")
for child in body_tag.contents:
    if child.name: # Imprime apenas tags reais
        print(child.name)

print("\nDescendentes da Tag Body (Exemplos):")
for descendant in body_tag.descendants:
    if descendant.name:
        print(descendant.name, end=" ")
        if descendant.name == 'li': break # Para após alguns exemplos
```

### Navegando para Cima
- `.parent`: O pai direto de uma tag.
- `.parents`: Um iterador de todos os ancestrais.

```python
# Encontra o pai da tag de título
p_tag = soup.p
print(f"\nPai de <p>: {p_tag.parent.name}")

# Itera através dos pais de um link específico
link2 = soup.find(id="link2")
print(f"Pais de <a id='link2'>:")
for parent in link2.parents:
    if parent is None:
        continue
    if parent.name:
        print(parent.name)
```

### Navegando Lateralmente
- `.next_sibling`: O próximo irmão após a tag atual.
- `.previous_sibling`: O irmão anterior antes da tag atual.
- `.next_siblings`: Um iterador de todos os irmãos seguintes.
- `.previous_siblings`: Um iterador de todos os irmãos anteriores.

```python
first_p_tag = soup.p
print(f"\nPróximo irmão do primeiro <p>: {first_p_tag.next_sibling.next_sibling.name}") # Pula a nova linha
print(f"Irmão anterior do primeiro <p>: {first_p_tag.previous_sibling.previous_sibling.name}") # Pula a nova linha

print("\nPróximos irmãos do primeiro <p> (exemplos):")
for sibling in first_p_tag.next_siblings:
    if sibling.name:
        print(sibling.name)
```

## 4. Pesquisando na Árvore (`find()` e `find_all()`)
Estes são os métodos mais poderosos para localizar elementos específicos.

### `find_all(name, attrs, recursive, string, limit)`
Encontra todas as ocorrências de uma tag que correspondem aos critérios. Retorna uma lista de tags.

- `name`: Nome da tag (por exemplo, 'a', 'p'). Pode ser uma string, lista, expressão regular ou função.
- `attrs`: Um dicionário de valores de atributos (por exemplo, `{'class': 'external-link'}`).
- `recursive`: Se `False`, examina apenas os filhos diretos. O padrão é `True`.
- `string`: Procura por strings em vez de tags.
- `limit`: Para de pesquisar após um certo número de correspondências.

```python
# Encontra todas as tags <a>
all_links = soup.find_all('a')
print(f"\nTodos os links: {all_links}")

# Encontra todas as tags <p> com a classe 'title'
title_p = soup.find_all('p', class_='title') # 'class_' porque 'class' é uma palavra-chave do Python
print(f"Parágrafos com a classe 'title': {title_p}")

# Encontra todas as tags que têm um atributo 'id'
tags_with_id = soup.find_all(id=True)
print(f"Tags com um atributo 'id': {tags_with_id}")

# Encontra todas as tags <li>
list_items = soup.find_all('li')
for item in list_items:
    print(f"Item da Lista: {item.string}")

# Encontra tags contendo texto específico (usando 'string')
p_with_content = soup.find_all(string="Este é outro conteúdo.")
print(f"Tags com conteúdo de string específico: {p_with_content}")
```

### `find(name, attrs, recursive, string)`
Semelhante a `find_all()`, mas retorna apenas a primeira correspondência.

```python
# Encontra a primeira tag <a>
first_link = soup.find('a')
print(f"\nPrimeiro link encontrado: {first_link}")

# Encontra a primeira tag <p> com a classe 'title'
first_title_p = soup.find('p', class_='title')
print(f"Primeiro parágrafo com a classe 'title': {first_title_p}")
```

### Padrões de Pesquisa Comuns
```python
# Por nome da tag
print(f"\nEncontra todas as tags 'p': {soup.find_all('p')}")

# Por classe CSS (note o sublinhado!)
print(f"Encontra todas as tags 'a' com a classe 'external-link': {soup.find_all('a', class_='external-link')}")

# Por ID
print(f"Encontra a tag com id 'link1': {soup.find(id='link1')}")

# Por valor de atributo (qualquer atributo)
print(f"Encontra todas as tags com href='http://example.com/one': {soup.find_all(href='http://example.com/one')}")

# Usando uma lista de nomes de tags
print(f"Encontra todas as tags 'p' ou 'a': {soup.find_all(['p', 'a'])}")

# Usando expressões regulares
import re
print(f"Encontra todas as tags cujo nome começa com 'b': {soup.find_all(re.compile('^b'))}") # ex., <body>, <b>
print(f"Encontra todas as tags com 'link' em seu ID: {soup.find_all(id=re.compile('link'))}")
```

## 5. Modificando a Árvore
O BeautifulSoup permite que você modifique a árvore de análise.

```python
# HTML de exemplo para modificação
html_mod = """
<html>
<body>
    <p>Texto original.</p>
    <div id="target">Conteúdo aqui</div>
</body>
</html>
"""
soup_mod = BeautifulSoup(html_mod, 'lxml')

# Altera o nome da tag
p_tag_mod = soup_mod.p
p_tag_mod.name = "div"
print(f"\nApós alterar p para div: {soup_mod.prettify()}")

# Modifica os atributos da tag
div_tag_mod = soup_mod.find(id="target")
div_tag_mod['class'] = 'new-class'
div_tag_mod['data-type'] = 'example'
print(f"Após modificar os atributos: {soup_mod.prettify()}")

# Adiciona novo conteúdo
new_tag = soup_mod.new_tag("span")
new_tag.string = "Texto do span adicionado."
div_tag_mod.append(new_tag) # Adiciona dentro da div
print(f"Após anexar uma nova tag: {soup_mod.prettify()}")

# Substitui o conteúdo
div_tag_mod.string = "Novo conteúdo substituído."
print(f"Após substituir o conteúdo da div: {soup_mod.prettify()}")

# Remove o conteúdo
span_to_remove = soup_mod.find('span')
if span_to_remove:
    span_to_remove.decompose() # Remove a tag e seu conteúdo
print(f"Após remover o span: {soup_mod.prettify()}")
```

## 6. Seletores CSS (`select()` e `select_one()`)
O BeautifulSoup também suporta seletores CSS usando o método `select()` (retorna uma lista) e `select_one()` (retorna a primeira correspondência).

```python
# Seleciona todas as tags <p>
print(f"\nSeleciona todas as tags 'p': {soup.select('p')}")

# Seleciona tags por classe
print(f"Seleciona todos os elementos com a classe 'external-link': {soup.select('.external-link')}")

# Seleciona a tag por ID
print(f"Seleciona o elemento com id 'link2': {soup.select('#link2')}")

# Seleciona filhos diretos
print(f"Seleciona filhos diretos <li> de .container: {soup.select('div.container > ul > li')}")

# Seleciona descendentes
print(f"Seleciona todos os descendentes <li> de .container: {soup.select('div.container li')}")

# Seleciona seletores combinados
print(f"Seleciona tags 'p' ou 'a': {soup.select('p, a')}")

# Seleciona tags com valores de atributos específicos
print(f"Seleciona tags 'a' com href começando com 'http://example.com': {soup.select('a[href^=\"http://example.com\"]')}")

# Seleciona o primeiro elemento correspondente
print(f"Seleciona o primeiro link: {soup.select_one('a')}")
```
