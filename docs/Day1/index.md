---
title: Dia 1 Python Básico - Funções
layout: default
nav_order: 2
---

<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>

# Dia 1. Entenda seu código. Aventura Python: 🧟‍♂️ Labirinto de Monstros
{: .no_toc }
Sentindo-se um pouco perdido quando seus agentes **Vibe Coders** geram linhas de código Python? Você não está sozinho! Muitos desenvolvedores aspirantes se deparam com uma sintaxe desconhecida, perguntando-se como interpretar a lógica por trás das criações de seus agentes. Esta lição intensiva foi projetada para **acabar com essa confusão**. Vamos mergulhar nos fundamentos essenciais do Python – seus tipos de dados fundamentais, operações comuns e controle de fluxo básico – equipando você com o conhecimento para ler e entender com confiança o código que seus agentes geram. Pare de se sentir deixado de lado e comece a colaborar de verdade com sua IA; **desbloqueie o poder de entender** o código, não apenas de gerá-lo!

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
## 🧭 1.1. Como é explicado? <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Para cobrir todos os conceitos básicos de Python, vamos criar um **mini jogo de texto** chamado **“Labirinto de Monstros”**. É divertido, simples e aborda todos os tópicos listados.

Você está preso em um labirinto. A cada turno, você decide se mover por salas, pegar itens e lutar contra monstros aleatórios. O objetivo é encontrar a **chave mágica** para escapar.

---

## 🧠 1.2. O que você vai aprender? <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

| Conceito | Coberto em | Uso/Propósito |
| --- | --- | --- |
| Impressão | `print()` | Exibir texto para o usuário |
| Tipos de Dados | `int`, `str`, `list`, `dict`, `bool` | Armazenar diferentes tipos de informação |
| Declarações Condicionais | `if`, `elif`, `else`, e `random.random()` | Tomar decisões com base em condições |
| Aleatorização | `random.choice()`, `random.random()` | Gerar valores imprevisíveis |
| Laços For | Pesquisa de inventário ou expansões opcionais | Repetir ações para cada item em uma coleção |
| Laços While | Laço de entrada do usuário | Repetir ações até que uma condição seja atendida |
| Funções | Todos os blocos definidos (`main`, `game_loop`, etc.) | Organizar o código em blocos reutilizáveis |
| Funções com Entradas | `create_player(name)` | Passar dados para funções para processamento |
| Funções com Saídas | Retornos em `create_player`, `describe_room` | Obter resultados de volta das funções |
| Dicionários | Objeto `player` | Armazenar pares chave-valor para fácil consulta |
| Comentários | Em todo o código | Explicar o código para leitores humanos |
| Depuração | Estrutura clara para rastreamento, caminhos de fim de jogo | Encontrar e corrigir erros no seu código |
| Manipulação de Strings | `f"{player['health']}"`, `.lower()`, arte ASCII | Modificar e formatar texto |
| Conversão de Tipos | Não é necessário aqui diretamente, mas pode-se adicionar `int(input())` | Mudar dados de um tipo para outro |
| f-Strings | `"f"Você encontrou {item}!"` etc. | Formatar strings com variáveis incorporadas |
| Listas Aninhadas | Opcional em expansões | Criar listas dentro de listas para dados complexos |
| Erros de Índice | Pode ser simulado com `inventory[5]` durante o ensino | Lidar com tentativas de acesso fora do intervalo |
| Recursão | `game_loop()` chama a si mesma | A função chama a si mesma para repetir o processamento |
| Range | Use `range()` se adicionar turnos ou passos | Gerar sequências de números |
| Escopo / Variável Global | `found_key`, palavra-chave `global` | Controlar onde as variáveis podem ser acessadas |
| Namespaces | Explicado pela separação de funções e `main` | Organizar nomes para evitar conflitos |
| Docstrings | `"""Docstrings"""` em todas as funções | Documentar o propósito e uso da função |
| Arte ASCII | Em `print_welcome()` | Criar gráficos baseados em texto |
| Melhorando a UI | Através de emojis, layout, mensagens de entrada | Melhorar a experiência do usuário |
| Quebrando Problemas | O jogo é dividido em funções pequenas e testáveis | Resolver problemas complexos parte por parte |

---

## 🧱 1.3. Codificação Passo a Passo <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

### 📦 1.3.1. Módulo de Importação e Comentários <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
A declaração de importação em Python permite que você inclua e use código de outros módulos em seu programa atual. Por exemplo, no código abaixo:
```python
# Importação simples - acesse com nome_do_modulo.item
import random
# Exemplo de importação com randint
numero_aleatorio = random.randint(1, 10) # Gera um inteiro aleatório entre 1 e 10
```
O Python procura por um módulo chamado "random" ou um arquivo chamado random.py em vários locais e executa seu código uma vez. Um namespace chamado "random" é criado em seu programa e então você pode acessar as funções e variáveis do módulo. No exemplo, a função randint é usada para criar um número inteiro aleatório entre 1 e 10.
Em Python, qualquer coisa escrita após "#" até o final da linha é interpretada como um comentário e os editores geralmente os mostram em verde ou cinza.

### 📋 1.3.2. Constantes e Listas <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Em Python, as variáveis que devem permanecer inalteradas ao longo de um programa são frequentemente escritas em LETRAS_MAIÚSCULAS para indicar que são **constantes**. Embora o Python não imponha isso (as variáveis ainda podem ser alteradas), é uma convenção para sinalizar a outros programadores que esses valores não devem ser modificados.

**Listas** são coleções ordenadas que podem armazenar múltiplos itens de qualquer tipo. Elas são criadas usando colchetes `[]` com itens separados por vírgulas. Aqui está um exemplo do nosso jogo Labirinto de Monstros:

```python
# Constantes definidas como listas
SALAS = ["Salão", "Cozinha", "Biblioteca", "Masmorra", "Jardim"]
ITENS = ["espada", "poção", "escudo"]
MONSTROS = ["Goblin", "Troll", "Esqueleto"]
```

Neste exemplo:
- `SALAS` é uma lista contendo 5 elementos de string representando locais do jogo
- `ITENS` é uma lista de 3 objetos colecionáveis no jogo
- `MONSTROS` é uma lista de 3 tipos de inimigos que o jogador pode encontrar

As listas são incrivelmente versáteis em Python:
- Elas podem ser acessadas por índice: `SALAS[0]` retornaria "Salão"
- O comprimento delas pode ser encontrado com `len(SALAS)` (retorna 5)
- Elementos podem ser adicionados com `append()` ou `insert()`
- Você pode iterar através delas usando um laço for: `for sala in SALAS:`

Mais tarde em nosso jogo, selecionaremos elementos aleatórios dessas listas usando `random.choice()` para criar uma jogabilidade imprevisível.


### 🌐 1.3.3. Variáveis globais, Funções e Print <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
Variáveis globais em Python são variáveis que são definidas fora de qualquer função e podem ser acessadas em todo o programa, incluindo dentro de funções. A variável global `chave_encontrada` recebe o valor `False` no início de `monster_maze.py`.
```python
# Variável global
chave_encontrada = False
```

As **funções** em Python são blocos de código reutilizáveis que executam uma tarefa específica. Elas são usadas para organizar o código, melhorar a legibilidade e promover a reutilização do código, quebrando problemas complexos em pedaços menores e gerenciáveis. No bloco de código abaixo, a variável global `contador` começa com o valor 0, então uma função `incrementar()` é declarada usando `def <nome da função>` e ":". O código que é executado toda vez que a função é chamada. O Python identifica o código que pertence à função porque ele é indentado exatamente 4 espaços. No exemplo, a função `incrementar()` aumenta a variável `contador` em 1 toda vez que é chamada.
```python
contador = 0

def incrementar(): # Cria a função incrementar() com zero variáveis
    global contador # Declara que queremos usar a variável global
    contador += 1 # Aumenta a variável contador em 1. É o mesmo que contador = contador + 1
    
incrementar() # Executa a função incrementar()
print(contador) # Saída: 1
incrementar() # Executa a função incrementar()
print(contador) # Saída: 2
```
Para modificar uma variável global dentro de uma função, você precisa usar a palavra-chave `global` como no exemplo.
O comando `<print(contador)>` escreve o valor da variável `contador` no terminal. **Print** é o principal comando de depuração. Também é usado para enviar mensagens de texto para o usuário, como na função `print_boas_vindas()`.
```python
def print_boas_vindas():
    """Imprime a mensagem de boas-vindas com arte ASCII."""
    print("""
    🧟‍♂️ LABIRINTO DE MONSTROS 🧟‍♀️
    Escape do labirinto, derrote monstros e encontre a chave!
    """) # Manipulação e impressão de strings
```
A string escrita abaixo da função com triplas `"""` contém um
texto de documentação curto chamado **"Docstrings"**, que é usado para transmitir o propósito e a funcionalidade de funções, módulos e classes do Python.

### 🔑 1.3.4. Dicionários, Listas de Dicionários, Tuplas e Fatiamento <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

**Dicionários** são uma das estruturas de dados mais poderosas do Python. Eles armazenam dados como pares chave-valor, permitindo que você recupere valores rapidamente usando suas chaves associadas (semelhante a como você procura definições em um dicionário real). Os dicionários são criados usando chaves `{}` com cada par chave-valor separado por vírgulas.

Em nosso jogo Labirinto de Monstros, a função `criar_jogador()` cria e retorna um dicionário de jogador:

```python
def criar_jogador(nome):
    """Retorna um novo dicionário de jogador."""
    return {
        "nome": nome,
        "saude": 100,
        "inventario": [],
        "localizacao": random.choice(SALAS) # Módulo random
    }
```

Neste dicionário:
- As chaves são strings como `"nome"`, `"saude"`, `"inventario"` e `"localizacao"`
- Os valores podem ser de qualquer tipo: uma string para `"nome"`, um inteiro para `"saude"`, uma lista para `"inventario"`, etc.
- Você acessa os valores usando suas chaves: `jogador["saude"]` lhe daria `100`
- Os valores podem ser modificados: `jogador["saude"] -= 20` reduziria a saúde em 20

**Listas de Dicionários** são estruturas de dados poderosas que podem armazenar múltiplos registros com campos nomeados. Elas são ideais para coleções de objetos semelhantes.

```python
# Lista de dicionários para múltiplos jogadores
jogadores = [
    {"nome": "Alex", "saude": 100, "inventario": ["espada"]},
    {"nome": "Taylor", "saude": 80, "inventario": ["poção", "escudo"]},
    {"nome": "Jordan", "saude": 120, "inventario": []}
]

# Acessando dados
print(jogadores[0]["nome"]) # Saída: Alex
print(jogadores[1]["inventario"][0]) # Saída: poção

# Adicionando novo jogador à lista
jogadores.append({"nome": "Casey", "saude": 90, "inventario": ["mapa"]})

# Percorrendo todos os jogadores
for jogador in jogadores:
    print(f"{jogador['nome']} tem {jogador['saude']} de saúde")
```

**Tuplas** são sequências imutáveis semelhantes a listas, mas entre parênteses. Uma vez criadas, seus valores não podem ser alterados.

```python
# Criação básica de tupla
coordenadas = (10, 20)
cor_rgb = (255, 0, 128)

# Desempacotamento de tupla - atribui cada valor a uma variável
x, y = coordenadas
print(f"X: {x}, Y: {y}") # Saída: X: 10, Y: 20

# Tuplas podem conter tipos de dados mistos
dados_jogador = ("Alex", 100, ["espada", "poção"])
nome, saude, inventario = dados_jogador

# Tuplas são imutáveis - isso causaria um erro:
# coordenadas[0] = 15

# Mas se uma tupla contém um objeto mutável, esse objeto pode ser modificado:
dados_jogador[2].append("escudo") # Isso funciona!
```

**Fatiamento** (slicing) permite extrair porções de sequências (listas, strings, tuplas) usando a sintaxe `[inicio:parada:passo]`.

```python
# Fatiando uma lista
itens = ["espada", "escudo", "poção", "chave", "mapa"]
primeiros_dois = itens[0:2] # ["espada", "escudo"]
ultimos_tres = itens[2:] # ["poção", "chave", "mapa"]
itens_do_meio = itens[1:4] # ["escudo", "poção", "chave"]

# Índices negativos contam a partir do final
ultimo_item = itens[-1] # "mapa"
penultimo = itens[-2] # "chave"
todos_menos_o_ultimo = itens[:-1] # ["espada", "escudo", "poção", "chave"]

# O parâmetro de passo pula elementos
a_cada_dois = itens[::2] # ["espada", "poção", "mapa"]
lista_invertida = itens[::-1] # ["mapa", "chave", "poção", "escudo", "espada"]

# Fatiar strings funciona da mesma maneira
nome = "Labirinto de Monstros"
primeira_palavra = nome[:9] # "Labirinto"
ultima_palavra = nome[13:] # "Monstros"
nome_invertido = nome[::-1] # "sortsnoM ed otniribaL"
```

O fatiamento é uma maneira concisa e poderosa de manipular sequências em Python, enquanto listas de dicionários e tuplas fornecem opções flexíveis para organizar estruturas de dados complexas em seus jogos.

### ⚙️ 1.3.5 Funções com Entrada e Saída <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
**Funções com Entrada** são funções onde uma variável é passada como valor quando são chamadas. Isso é feito em nosso código quando `game_loop(jogador)` é chamado em `main()`.
**Funções com Saída** são funções que retornam valores para serem usados em outro lugar do seu código. Em Python, a declaração `return` é usada para especificar qual valor uma função deve produzir. Sem uma declaração de retorno, as funções retornam `None` por padrão.

Nossa função `criar_jogador()` acima é um exemplo perfeito:
1. Ela recebe um parâmetro de entrada `nome`
2. Ela cria um dicionário com atributos do jogador
3. Ela retorna esse dicionário, que pode então ser atribuído a uma variável
4. O código chamador pode então usar esse dicionário retornado: `jogador = criar_jogador("Alex")`

Os valores de retorno são essenciais quando uma função precisa calcular ou criar algo que será usado por outras partes do seu programa. Em nosso jogo, o dicionário do jogador é central para o estado de todo o programa, e é por isso que temos uma função dedicada que o retorna.

**Funções com entrada desconhecida** Em Python, é possível criar uma função que aceita um número desconhecido de argumentos usando `*args` e `**kwargs`. Aqui está um detalhamento de quando e por que usamos cada um:

`*args` (Argumentos Posicionais Arbitrários): Usado quando você precisa criar uma função que pode operar em um número não especificado de entradas do mesmo tipo.

Como funciona:
- A sintaxe `*args` em uma definição de função coleta todos os argumentos posicionais extras passados para a função em uma tupla.
- O nome `args` é uma convenção; você poderia usar `*qualquercoisa` se quisesse, mas `*args` é amplamente compreendido e recomendado.

Exemplo:

```python
def somar_todos_numeros(*args):
    total = 0
    for num in args:
        total += num
    return total

print(somar_todos_numeros(1, 2, 3)) # Saída: 6
print(somar_todos_numeros(10, 20, 30, 40)) # Saída: 100
print(somar_todos_numeros()) # Saída: 0
```

`**kwargs` (Argumentos de Palavra-chave Arbitrários): usado quando você quer que uma função aceite qualquer número de argumentos de palavra-chave (argumentos passados com uma sintaxe `chave=valor`).

Como funciona:
- A sintaxe `**kwargs` em uma definição de função coleta todos os argumentos de palavra-chave extras passados para a função em um dicionário.
- O nome `kwargs` é uma convenção; você poderia usar `**outra_coisa` mas `**kwargs` é o padrão.

Exemplo:
```python
def configurar_definicoes(**kwargs):
    definicoes = {
        "tema": "escuro",
        "tamanho_fonte": 12,
        "idioma": "pt"
    }
    for chave, valor in kwargs.items():
        definicoes[chave] = valor
    return definicoes

print(configurar_definicoes(tema="claro", tamanho_fonte=14))
# Saída: {'tema': 'claro', 'tamanho_fonte': 14, 'idioma': 'pt'}

print(configurar_definicoes(idioma="fr", modo_debug=True))
# Saída: {'tema': 'escuro', 'tamanho_fonte': 12, 'idioma': 'fr', 'modo_debug': True}

print(configurar_definicoes())
# Saída: {'tema': 'escuro', 'tamanho_fonte': 12, 'idioma': 'pt'}
```
Você pode combinar `*args` e `**kwargs`, por exemplo `def impressora_generica(arg1, *args, **kwargs):`


### 🔀 1.3.6. Declarações Condicionais e Formatação de Strings <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

**Declarações Condicionais** (if/elif/else) são blocos de construção fundamentais em Python que permitem que seu programa tome decisões. Eles executam diferentes blocos de código com base no fato de certas condições serem verdadeiras ou falsas. Vejamos a função `descrever_sala()` como exemplo:

```python
def descrever_sala(sala):
    """Descreve a sala atual."""
    print(f"\nVocê está agora na {sala}.")
    if random.random() < 0.4: # Declaração condicional
        item = random.choice(ITENS)
        print(f"Você encontrou um {item}!")
        return item
    return None
```

Nesta função:
- A declaração `if` verifica se `random.random() < 0.4` é verdadeiro
- `random.random()` gera um float aleatório entre 0.0 e 1.0
- Se a condição for verdadeira (40% de chance), o bloco indentado é executado, selecionando um item
- Se a condição for falsa (60% de chance), a função pula para `return None`

Uma estrutura completa if/elif/else funciona assim:
```python
if condicao1:
    # Código que é executado se a condição1 for Verdadeira
elif condicao2:
    # Código que é executado se a condição1 for Falsa mas a condição2 for Verdadeira
else:
    # Código que é executado se todas as condições forem Falsas
```

**Formatação de Strings** é demonstrada de várias maneiras nesta função:

1. **f-strings** (literais de string formatados) são um recurso poderoso introduzido no Python 3.6. Elas começam com `f` e permitem que você incorpore expressões dentro de literais de string usando chaves `{}`.
   ```python
   print(f"\nVocê está agora na {sala}.")
   ```
   Aqui, o valor da variável `sala` é inserido diretamente na string. Isso é muito mais limpo do que métodos mais antigos como `print("\nVocê está agora na " + sala + ".")`.

2. **Sequências de escape** como `\n` são combinações de caracteres especiais que representam caracteres que seriam difíceis de digitar diretamente:
   - `\n` representa um caractere de nova linha, começando o texto em uma nova linha
   - Outros comuns incluem `\t` (tabulação), `\"` (aspas) e `\\` (barra invertida)

3. **`random.choice()`** seleciona um elemento aleatório de uma sequência como uma lista. Em nossa função:
   ```python
   item = random.choice(ITENS)
   ```
   Isso seleciona aleatoriamente um item da nossa lista `ITENS` ("espada", "poção" ou "escudo").

A combinação desses recursos torna nosso código funcional e legível. Observe como a função usa condições para criar uma jogabilidade dinâmica (às vezes encontrando itens, às vezes não) e strings formatadas para comunicar claramente o que está acontecendo com o jogador.


### 🔢 1.3.7. Range() e Operadores Lógicos <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

**A Função `range()`** é uma função interna do Python que gera uma sequência de números. É comumente usada em laços `for` para executar código um número específico de vezes.

Uso básico: `range(parada)` ou `range(inicio, parada, passo)`:
- `range(5)` gera os números 0, 1, 2, 3, 4
- `range(2, 8)` gera 2, 3, 4, 5, 6, 7
- `range(1, 10, 2)` gera 1, 3, 5, 7, 9

Embora nossa função `mover_para_nova_sala()` não use `range()` diretamente, ela usa um conceito relacionado chamado compreensão de lista, que pode ser implementado com `range`:

```python
def mover_para_nova_sala(jogador):
    """Move o jogador para uma nova sala aleatória."""
    anterior = jogador["localizacao"]
    jogador["localizacao"] = random.choice([s for s in SALAS if s != anterior])
```

Esta função:
1. Armazena a sala atual em `anterior`
2. Cria uma nova lista com todas as salas *exceto* a atual usando uma compreensão de lista
3. Seleciona aleatoriamente uma sala dessa lista

A mesma compreensão de lista poderia ser escrita com `range()` assim:
```python
[SALAS[i] for i in range(len(SALAS)) if SALAS[i] != anterior]
```

**Operadores de Comparação** são usados para comparar valores и retornar resultados booleanos (Verdadeiro ou Falso):

| Operador | Descrição | Exemplo |
|---|---|---|
| `==` | Igual a | `if nome == "Alex":` |
| `!=` | Diferente de | `if s != anterior:` (da nossa função) |
| `<` | Menor que | `if random.random() < 0.4:` |
| `>` | Maior que | `if jogador["saude"] > 50:` |
| `<=` | Menor ou igual a | `if jogador["saude"] <= 0:` |
| `>=` | Maior ou igual a | `if pontuacao >= 100:` |

**Operadores Lógicos** permitem combinar múltiplas condições:

| Operador | Descrição | Exemplo |
|---|---|---|
| `and` | Verdadeiro se ambas as condições forem verdadeiras | `if saude > 0 and chave_encontrada:` |
| `or` | Verdadeiro se uma das condições for verdadeira | `if escolha in ["sim", "s"]:` |
| `not` | Inverte um valor booleano | `if not chave_encontrada:` |

Em nossa função `mover_para_nova_sala()`, a compreensão de lista usa o operador `!=` para criar uma lista de salas que não são a sala atual. Isso garante que o jogador sempre se mova para uma sala diferente.

Outro exemplo do nosso código mostrando operadores lógicos está no laço do jogo:

```python
if escolha in ["sim", "s"]:
    mover_para_nova_sala(jogador)
    game_loop(jogador) # Recursão
    break # Sai do laço
elif escolha in ["não", "n"]:
    print("🛌 Você escolheu descansar. Fim de jogo.")
    break
```
Aqui, o operador `in` verifica se um valor existe em uma lista e atua como uma condição lógica. A condição `escolha in ["sim", "s"]` é verdadeira se o usuário digitou "sim" ou "s".

A combinação de operadores permite criar lógicas de decisão complexas:
```python
# Exemplo de condição composta
if jogador["saude"] < 30 and "poção" in jogador["inventario"]:
    print("Você usa uma poção para restaurar a saúde!")
    jogador["saude"] += 50
    jogador["inventario"].remove("poção")
```

Esses operadores são essenciais para criar programas dinâmicos e responsivos que podem tomar decisões com base em condições variáveis. Em `monster_maze.py`, isso é usado novamente para jogar Encontros com Monstros.

```python
def encontrar_monstro(jogador):
    """Encontro aleatório com monstro com chance de luta."""
    if random.random() < 0.3:
        monstro = random.choice(MONSTROS)
        print(f"\n⚔️ Um {monstro} selvagem aparece!")
        if "espada" in jogador["inventario"]:
            print("Você o derrota com sua espada!")
        else:
            jogador["saude"] -= 20
            print("Você não tem espada! Você se machucou!")
            print(f"Saúde: {jogador['saude']}")
            if jogador["saude"] <= 0:
                print("💀 Você morreu. Fim de jogo.")
                exit() # Sai do script
```

### 🔄 1.3.8. Laços While e For para Controlar o Fluxo. Recursão de Função <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

É aqui que colocamos o computador para trabalhar de verdade para nós, usando laços `while` e `for` para repetir ações. **Laços `while`** executam um bloco de código repetidamente enquanto uma condição permanecer verdadeira. Eles são ideais quando você não sabe de antemão quantas iterações serão necessárias.

Em nosso jogo, usamos um laço `while` para continuar pedindo a entrada do jogador até que ele forneça uma resposta válida:

```python
# Laço while para validação de entrada
while True:
    escolha = input("\nVocê quer se mover para outra sala? (sim/não): ").lower()
    if escolha in ["sim", "s"]:
        mover_para_nova_sala(jogador)
        game_loop(jogador) # Recursão
        break
    elif escolha in ["não", "n"]:
        print("🛌 Você escolheu descansar. Fim de jogo.")
        break
    else:
        print("Por favor, responda sim ou não.")
```

O `while True:` cria um laço infinito que só sairá quando encontrar uma declaração `break`. Isso acontece quando o jogador insere "sim"/"s" ou "não"/"n". Se ele inserir qualquer outra coisa, o laço continua e o solicita novamente. Esse comportamento, se não for codificado corretamente, pode terminar nunca alcançando uma condição falsa e tendo que parar o programa usando `Ctrl+C` ou, pior ainda, `Ctrl+Alt+Del`. Para evitar isso, você também pode querer adicionar um contador à condição para limitar o número máximo de iterações.

```python
# Laço while com um contador para evitar laços infinitos
max_tentativas = 3
contagem_tentativas = 0

while contagem_tentativas < max_tentativas:
    escolha = input("\nVocê quer se mover para outra sala? (sim/não): ").lower()
    contagem_tentativas += 1 # Incrementa o contador a cada iteração
    
    if escolha in ["sim", "s"]:
        mover_para_nova_sala(jogador)
        game_loop(jogador)
        break
    elif escolha in ["não", "n"]:
        print("🛌 Você escolheu descansar. Fim de jogo.")
        break
    else:
        restantes = max_tentativas - contagem_tentativas
        if restantes > 0:
            print(f"Por favor, responda sim ou não. {restantes} tentativas restantes.")
        else:
            print("Muitas entradas inválidas. Continuando...")
```

Esta versão dá ao jogador três chances de inserir uma entrada válida antes de continuar, evitando um laço infinito. O contador rastreia as tentativas e fornece um feedback útil sobre as chances restantes.

**Laços `for`** iteram sobre uma sequência (como uma lista ou string) e executam o código para cada item:

```python
# Exemplo de um laço for com o inventário do jogador
def mostrar_inventario(jogador):
    print("Seu inventário contém:")
    for item in jogador["inventario"]:
        print(f"- {item}")
```

Isso imprimiria todos os itens no inventário do jogador.

**Recursão** é quando uma função chama a si mesma. Em nosso jogo, `game_loop()` chama a si mesma quando o jogador se move para uma nova sala:

```python
if escolha in ["sim", "s"]:
    mover_para_nova_sala(jogador)
    game_loop(jogador) # Recursão
    break
```

Isso cria uma cadeia de chamadas de função que continua até que uma condição de término seja atendida (encontrar a chave ou morrer). A recursão é poderosa, mas precisa de uma condição de saída clara para evitar a recursão infinita.

### 🏃 1.3.9. Execução Principal e Diagrama de Fluxo <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

**A Execução de Scripts Python** segue uma ordem específica:

1. O Python lê o script de cima para baixo
2. Ele define funções e variáveis, mas não executa o código da função até que a função seja chamada
3. Quando uma função é chamada, o Python salta temporariamente para essa função, executa seu código e depois retorna para onde parou

Em nosso jogo Labirinto de Monstros, usamos um padrão comum do Python:

```python
# Programa principal
def main():
    """Inicia o jogo."""
    print_boas_vindas()
    nome = input("Digite seu nome, aventureiro: ")
    jogador = criar_jogador(nome)
    game_loop(jogador)

if __name__ == "__main__":
    main()
```

A verificação `if __name__ == "__main__":` garante que a função `main()` só seja executada quando o script for executado diretamente (não quando importado como um módulo). Esta é uma prática recomendada para programas Python.

**Diagrama de Fluxo** é uma representação visual da lógica de um programa. Os diagramas de fluxo ajudam a visualizar lógicas complexas e a identificar possíveis problemas antes da codificação. O ótimo agora é que você pode pedir a um Modelo de Linguagem Grande como o Gemini ou o ChatGPT para criar um para você a partir do código. Esta é uma ótima maneira de se familiarizar com algum código.

Nos diagramas de fluxo:
- Retângulos com cantos quadrados ou arredondados significam um passo no processo. Eles representam um passo no processo, uma operação ou uma tarefa. É aqui que algo é feito. Por exemplo: "Realizar Cálculo", "Imprimir Relatório", "Ler Dados".

![Retângulo](Rectangle.png)

- Losangos são para decisões (ou se, então, senão): Eles indicam um ponto onde uma decisão deve ser tomada, tipicamente uma pergunta "Sim/Não" ou "Verdadeiro/Falso". Os caminhos que divergem do losango são rotulados com as respostas possíveis.

![Losango](Diamond.png)

- Ovais/Cápsulas (Início/Fim - Terminal): Representam o início ou o fim de um processo.

![Círculo](Circle.png)

- Cilindros: Representam dados armazenados em um banco de dados ou outro meio de armazenamento.

![Banco de Dados](Database.png)

- Setas: Conectam os símbolos e indicam a direção do fluxo ou a sequência de operações.<br/>
**→**


Para o Labirinto de Monstros, o fluxograma se parece com:

![Fluxograma Completo](Full_flowchart.png)

### 🐛 1.3.10. Depuração <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

**Depuração** é o processo de encontrar e corrigir erros (bugs) em seu código. As técnicas comuns de depuração em Python incluem:

1. **Depuração com Print**: Adicionar declarações `print()` para exibir os valores das variáveis:
   ```python
   print(f"DEBUG: saúde do jogador = {jogador['saude']}")
   ```

2. **Usando o Depurador do Python** (`pdb`):
   ```python
   import pdb; pdb.set_trace() # O código irá pausar aqui
   ```

3. **Depuração no VS Code**:
   - Defina pontos de interrupção clicando na margem esquerda ao lado dos números das linhas
   - Pressione F5 para iniciar a depuração
   - Use a barra de ferramentas de depuração para percorrer o código (Passar por cima, Entrar, Continuar)
   - Passe o mouse sobre as variáveis para ver seus valores
   - Use o painel de Variáveis para inspecionar todas as variáveis atuais
   - Use o Console de Depuração para executar comandos na posição pausada

Em nosso jogo Labirinto de Monstros, os pontos de depuração potenciais incluem:
- Verificar as transições de sala
- Verificar a dedução de saúde após encontros com monstros
- Confirmar que os itens são adicionados ao inventário
- Testar as condições de vitória/derrota

Boas práticas de depuração:
- Comece com pedaços de código pequenos e testáveis
- Teste um recurso de cada vez
- Use declarações de impressão descritivas
- Verifique casos extremos (listas vazias, valores zero, etc.)

### 🔧 1.3.11. Refatorar e Testar, Estrutura do Código e Polimento da UI <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

**Refatoração** é o processo de reestruturar o código sem alterar seu comportamento. Os benefícios incluem:
- Legibilidade aprimorada
- Melhor organização
- Manutenção mais fácil
- Desempenho mais eficiente

Quando refatorar:
- Depois de ter uma versão básica funcionando
- Quando você encontra código repetido
- Quando as funções são muito longas ou fazem muitas coisas
- Quando a nomeação poderia ser mais clara

**Estrutura do Código** melhores práticas:
1. **Princípio da Responsabilidade Única**: Cada função deve fazer uma coisa bem
2. **DRY (Não se Repita)**: Extraia a lógica repetida para funções
3. **Nomeação Consistente**: Use nomes descritivos e convenções consistentes
4. **Modularidade**: Organize funções relacionadas juntas
5. **Separação de Preocupações**: Separe a lógica do jogo, a Interface do Usuário (UI) e os dados

Nosso exemplo de Labirinto de Monstros segue uma boa estrutura:
- As funções são focadas em tarefas específicas (criar_jogador, encontrar_monstro, etc.)
- O fluxo principal do jogo é isolado em `game_loop`
- As variáveis têm nomes claros e descritivos

**Polimento da UI** melhora a experiência do usuário:
1. **Instruções Claras**: Ajude os usuários a entender o que fazer
2. **Melhorias Visuais**: Use arte ASCII, emojis e formatação
3. **Validação de Entrada**: Lide com entradas inesperadas de forma elegante
4. **Mensagens Consistentes**: Use um tom e estilo consistentes
5. **Ritmo**: Adicione pausas quando apropriado para a legibilidade

Em nosso jogo, usamos várias melhorias na UI:
- Ícones de emoji para momentos chave (🧟‍♂️, 🔑, 💀, [mais...](https://unicode.org/emoji/charts/full-emoji-list.html))
- Prompts claros para a entrada do usuário
- Novas linhas (`\n`) para organizar o texto visualmente
- Feedback consistente para as ações do jogador

Como passo final, testes completos garantem que seu código funcione como esperado em diferentes cenários e casos extremos.

---

## 📝 1.4 Perguntas para Reflexão <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

<details markdown="block">
  <summary>
1. O que acontece se uma função não `return` nada?
  </summary>
Ela retornará `None`
</details>

<details markdown="block">
  <summary>
2. Como as variáveis globais e locais diferem no jogo?
  </summary>
Uma variável global no jogo é `chave_encontrada`, que é acessível e pode ser modificada de qualquer função dentro do programa. Em contraste, as variáveis locais são definidas dentro de uma função específica, como `jogador` na função `game_loop` ou `item` em `descrever_sala`, e seu escopo é limitado a essa função. Isso significa que elas só podem ser usadas e modificadas dentro da função onde são definidas.
</details>

<details markdown="block">
  <summary>
3. Que tipo de laço você usaria para repetir até que uma condição seja atendida?
   </summary>
Para repetir até que uma condição seja atendida, um laço `while` seria adequado, pois continua a ser executado enquanto uma condição especificada for verdadeira.
</details>

<details markdown="block">
  <summary>
4. E para percorrer uma lista de salas?
  </summary>
Para percorrer uma lista de salas, um laço `for` seria apropriado, pois itera sobre cada item em uma sequência.
</details>

<details markdown="block">
  <summary>
5. Quais são algumas maneiras de evitar ficar preso em um laço infinito?
  </summary>
Para evitar ficar preso em um laço infinito:

- Garanta que a condição do laço eventualmente se torne falsa: Para laços `while`, certifique-se de que a condição que controla o laço em algum momento será avaliada como `Falsa`.
- Inclua uma condição de quebra: Use declarações `break` para sair do laço quando uma certa condição for atendida.
- Limite as iterações: Para laços que podem ser executados indefinidamente, considere adicionar um contador e quebrar o laço após um número máximo de iterações.
</details>

<details markdown="block">
  <summary>
6. Você pode quebrar o jogo inserindo uma entrada inesperada?
  </summary>
Sim, você pode quebrar o jogo inserindo uma entrada inesperada. A função `game_loop` inclui um prompt de `input` que espera "sim" ou "não" (ou "s" ou "n"). Se qualquer outra entrada for inserida, o programa imprimirá repetidamente "Por favor, responda sim ou não." devido ao laço `while True` e à condição `else`, ficando efetivamente preso em um laço pedindo uma entrada válida até que "sim" ou "não" seja inserido. Isso impede que o jogo progrida para a próxima sala ou termine e, embora não seja um laço infinito no sentido de travar o programa, ele interrompe o fluxo pretendido do jogo até que uma entrada válida seja fornecida.
</details>

---


## 🎯 1.5. Exercícios <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

#### 🧪 Prática 1: Armas Personalizadas
> Modifique a lista `ITENS` para incluir novas armas como "laser", "arco" ou "bola de fogo". Faça com que a lógica de encontro com monstros as reconheça.

#### 🧪 Prática 2: Estatísticas de Monstros
> Crie um dicionário `estatisticas_monstros` que dê a cada monstro uma `forca`. Compare-a com a saúde do jogador.

#### 🧪 Prática 3: Sistema de Subir de Nível
> Adicione um sistema de experiência: cada monstro derrotado dá pontos. Aos 100 pontos, imprima “Subiu de nível!”

#### 🧪 Prática 4: Adicione um Mapa
> Rastreie quais salas você visitou. Imprima um mini-mapa ou lista no final mostrando onde você esteve.



---

Feliz Hacking! 🧙‍♀️
