---
title: Dia 2 Python Intermediário - Objetos
layout: default
nav_order: 3
---

# Dia 2. Python Intermediário. 🏋️ Rastreador de Fitness e Dieta
{: .no_toc }
No Dia 1, aprendemos as funções básicas do Python que nos permitem processar tarefas repetitivas e escolhas. Hoje, avançaremos um pouco mais e aprenderemos modos mais poderosos de gerenciar informações, aprendendo a manipular outros arquivos, trabalhando com objetos e classes e plotando dados.

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
## 🧭 Como é explicado? <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Desta vez, vamos construir um rastreador de fitness e dieta que calculará as calorias líquidas todos os dias e plotará o histórico em um gráfico. Esta ferramenta de linha de comando:
- Registra treinos e refeições
- Lê e limpa dados de CSV
- Realiza análise de dados
- Visualiza tendências usando gráficos
- Usa POO para código estruturado

## 📦 Pré-requisitos, instalação de módulos e ambiente.<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
Você precisará de:
- Python 3.x
- pandas e matplotlib
que você pode instalar executando o comando abaixo no bash:
```bash
pip install pandas matplotlib
```

## 🗂 **Passo 1**: Prepare Seus Dados. <a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

### 👉 Entendendo a Estrutura de Arquivos 📁 e Caminhos em Python<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Uma **estrutura de arquivos** (também conhecida como **estrutura de diretórios**) refere-se a como arquivos e pastas são organizados em seu computador. É como uma árvore:
- No topo está a **raiz** (por exemplo, C:\ no Windows ou / no Unix/Linux).
- Dentro dela estão **pastas/diretórios** (por exemplo, Documentos, Área de Trabalho, etc.)
- As pastas podem conter **arquivos** (como .txt, .csv, .py) ou **outras pastas** (subdiretórios).

### 👉 Precisamos de estruturas de arquivos para **organizar dados, localizar arquivos** e **construir aplicações escaláveis**.<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Um caminho de arquivo é o endereço para um arquivo ou pasta no computador. Existem dois tipos:
1. Caminho Absoluto que aponta para a localização exata a partir da raiz e sempre começa da unidade ou diretório raiz.
```python
"C:/Users/Alberto/Desktop/meu_arquivo.txt" # Windows
"/home/alberto/documents/meu_arquivo.txt" # Linux/macOS
```
1. Caminho Relativo que aponta para uma localização relativa ao diretório de trabalho atual.
```python
"dados/meu_arquivo.txt" # Significa dentro da pasta 'dados'
"./meu_arquivo.txt" # Diretório atual
"../meu_arquivo.txt" # Uma pasta acima
```

A barra (`/`) é usada em Unix/macOS/Linux, e também em Python em todas as plataformas. A barra invertida (`\`) é usada no Windows.

{: .note }
>Melhor prática: Use barras (`/`) em Python ou use o módulo `os.path` para compatibilidade.

### 👉Python e o **Módulo OS**<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

O módulo `os` ajuda a interagir com o sistema de arquivos, reduzindo erros de sintaxe e executando certas funções básicas.

```python
import os

print(os.getcwd()) # Obtém o diretório atual

print(os.listdir(".")) # Lista arquivos e pastas em um diretório

caminho_arquivo = os.path.join("dados", "arquivo.csv") # Junta caminhos de forma segura
print(caminho_arquivo)

print(os.path.exists(caminho_arquivo))# Verifica se o caminho existe
```

No rastreador de fitness, `os` é usado para criar o caminho para os arquivos de entrada:
```python
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
WORKOUTS_FILE = os.path.join(DATA_DIR, 'workouts.csv')
MEALS_FILE = os.path.join(DATA_DIR, 'meals.csv')
```


### 👉 **Estrutura de arquivos** e arquivos **csv**<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Para este exemplo, armazenaremos os registros de nossos treinos и refeições nos arquivos csv na subpasta `data`.


```kotlin
rastreador_fitness/
├── dados/
│   ├── treinos.csv
│   └── refeicoes.csv
└── rastreador_fitness.py
```
CSV significa Valores Separados por Vírgula. É um arquivo de texto simples usado para armazenar dados tabulares (como uma planilha ou banco de dados) em um formato simples.

Cada linha é uma linha no arquivo, e cada valor de coluna é separado por uma vírgula (,).

🔹 Regras Chave de Formatação

| Elemento | Descrição |
| --- | --- |
| **Vírgula (,)** | Separador padrão entre valores |
| **Nova Linha** | Separa linhas |
| **Primeira linha** | Frequentemente usada como **cabeçalho** (nomes das colunas) |
| **Aspas ("")** | Usadas em torno de campos que contêm vírgulas ou quebras de linha |
| **.csv** | Extensão de arquivo para arquivos CSV |

Para este exemplo, os arquivos csv são:

<details markdown="block">
  <summary>
    `dados/treinos.csv`
  </summary>
```csv
data,tipo,duracao_minutos,calorias_queimadas
2025-06-01,Corrida,30,300
2025-06-02,Ciclismo,45,400
2025-06-03,Yoga,60,200
2025-06-04,Natação,30,350
2025-06-05,Corrida,40,350
```
</details>
<details markdown="block">
  <summary>
    `dados/refeicoes.csv`
  </summary>
```csv
data,tipo_refeicao,comida,calorias
2025-06-01,Café da Manhã,Aveia,250
2025-06-01,Almoço,Salada de Frango,500
2025-06-01,Jantar,Massa,600
2025-06-02,Café da Manhã,Ovos,300
2025-06-02,Almoço,Sanduíche,450
2025-06-02,Jantar,Bife,700
2025-06-03,Café da Manhã,Smoothie,200
2025-06-03,Almoço,Arroz e Feijão,550
2025-06-03,Jantar,Peixe Grelhado,500
2025-06-04,Café da Manhã,Iogurte com Granola,320
2025-06-04,Almoço,Sopa de Legumes,380
2025-06-04,Jantar,Frango ao Curry,650
2025-06-05,Café da Manhã,Torrada com Abacate,400
2025-06-05,Almoço,Salada Caesar,420
2025-06-05,Jantar,Salmão com Legumes,580
```
</details>

## 🐍 **Passo 2**: Crie `rastreador_fitness.py`. **Classes** e **Programação Orientada a Objetos**<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>


Vamos mergulhar na **Programação Orientada a Objetos (POO)** com uma analogia simples!

### 👉 O que é **Programação Orientada a Objetos** (POO)?<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Imagine que você quer construir uma frota de diferentes tipos de veículos: carros, motocicletas e caminhões. Em vez de listar cada detalhe para cada veículo que você constrói (por exemplo, "Este carro tem 4 rodas, cor vermelha, pode acelerar, pode frear. Este outro carro tem 4 rodas, cor azul, pode acelerar, pode frear..."), a POO ajuda você a organizar seu design.

**POO é uma maneira de organizar seu código em torno de "objetos" em vez de apenas funções e dados**. Pense nisso como um sistema de projetos para criar coisas.

### 👉 O que são **Classes**?<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Vamos continuar com a analogia da "Fábrica de Veículos":

**Classes** são como Projetos: Antes de construir qualquer veículo, você precisa de um design. Você teria um Projeto de Carro, um Projeto de Motocicleta e um Projeto de Caminhão. Esses projetos definem quais características (como número de rodas, cor) e comportamentos (como acelerar, frear) todos os carros, motocicletas ou caminhões terão.
**Objetos** são como os Veículos Reais: Uma vez que você tem um projeto, você pode construir veículos reais a partir dele. Então, um carro vermelho específico que você acabou de construir, uma motocicleta azul ou um caminhão verde são todos objetos. Cada um é uma **instância** única criada a partir de seu respectivo projeto.

### 👉 **Por que** a POO é Útil e Quando?<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

A POO é útil para:
- *Organização e Modularidade*: Ajuda a quebrar problemas complexos em pedaços menores e gerenciáveis (objetos). Isso torna seu código mais fácil de entender, manter e depurar. Em vez de um manual de instruções gigante para tudo, você tem projetos separados para carros, motocicletas, etc.
- *Reutilização*: Você pode reutilizar seus projetos (classes) para criar muitos objetos semelhantes. Você não precisa redesenhar o projeto do carro toda vez que quiser construir um novo carro. Você apenas usa o existente.
- *Flexibilidade e Manutenibilidade*: Se você precisar mudar como todos os carros aceleram, você apenas modifica o "Projeto do Carro". Todos os carros construídos a partir desse projeto terão então o comportamento de aceleração atualizado. Se você decidir que todos os carros agora devem ter capacidade de direção autônoma, você atualiza o Projeto do Carro, e todos os novos carros que você construir a partir dele terão esse recurso.
- *Lidar com a Complexidade*: À medida que seus programas crescem, a POO ajuda a gerenciar a complexidade, encapsulando dados e comportamentos relacionados juntos.

### 👉 **Quando** é útil?<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

A POO brilha quando você está lidando com:
- *Sistemas complexos*: Jogos, simulações, grandes aplicações de negócios.
- *Programas com muitas "coisas" semelhantes*: Pense em um sistema de gerenciamento de usuários (muitos objetos "usuário"), um site de comércio eletrônico (muitos objetos "produto") ou uma interface gráfica de usuário (muitos objetos "botão", "campo de texto", "janela").
- *Quando você quer colaborar no código*: Diferentes desenvolvedores podem trabalhar em diferentes partes do sistema (diferentes classes) mais facilmente.

### 👉 O que são **Métodos** e **Atributos**?<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Vamos voltar à nossa analogia de veículos:
- *Objetos*: Como explicado, são as "coisas" reais criadas a partir de um projeto (classe). Por exemplo, `meu_carro_vermelho`, `moto_do_joao`.
- *Atributos* (Propriedades/Dados): São as características ou dados associados a um objeto. São como os detalhes no projeto que descrevem o que o veículo é. Para um objeto Carro, os atributos podem ser `cor` (por exemplo, "vermelho"), `numero_de_rodas` (por exemplo, 4), `marca` (por exemplo, "Toyota").
- *Métodos* (Comportamentos/Funções): São as ações que um objeto pode realizar. São como as instruções no projeto que descrevem o que o veículo pode fazer. Para um objeto Carro, os métodos podem ser `acelerar()`, `frear()`, `acender_farois()`.

Como você cria um objeto a partir de uma classe em Python?

Primeiro, você define uma classe (nosso projeto):
```python
class Carro:
    # Este é o projeto para um Carro

    def __init__(self, cor, marca, num_rodas=4):
        # Este é um método especial chamado "construtor".
        # É como a linha de montagem inicial para um novo carro.
        # 'self' refere-se ao objeto carro específico que está sendo criado.
        self.cor = cor # Define o atributo cor para este carro
        self.marca = marca # Define o atributo marca para este carro
        self.num_rodas = num_rodas # Define o número de rodas (padrão para 4)

    def acelerar(self):
        # Este é um método (comportamento) para um objeto Carro
        print(f"O carro {self.cor} {self.marca} está acelerando!")

    def frear(self):
        # Outro método
        print(f"O carro {self.cor} {self.marca} está freando.")
```

Agora, para criar um objeto (um carro específico) a partir desta classe `Carro`:

```python
# Criando um objeto (um carro específico) a partir da classe Carro
meu_carro_vermelho = Carro("vermelho", "Toyota")
carro_azul_do_joao = Carro("azul", "Honda")
meu_carro_vermelho.acelerar()
meu_carro_vermelho.frear()
```
o que retornará
```bash
$ python fabrica_de_carros.py
O carro vermelho Toyota está acelerando!
O carro vermelho Toyota está freando.
```

Para acessar ou definir atributos, você usa a notação de ponto (`.`) para acessar ou definir atributos:
```python
# Acessando atributos
print(f"A cor do meu carro: {meu_carro_vermelho.cor}")
print(f"A marca do carro do João: {carro_azul_do_joao.marca}")

# Definindo (modificando) um atributo
meu_carro_vermelho.cor = "amarelo"
print(f"A nova cor do meu carro: {meu_carro_vermelho.cor}")
```

### 👉 O que é **Herança de Classe**?<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

A herança é um conceito poderoso da POO que permite criar novas classes com base nas existentes. Pense nisso como criar projetos mais especializados a partir de projetos gerais.

Você tem um "Projeto de Veículo" geral. A partir deste, você pode criar um "Projeto de Carro", um "Projeto de Motocicleta" e um "Projeto de Caminhão". Um Carro é um Veículo, uma Motocicleta é um Veículo. O projeto do Carro herda automaticamente todas as características e comportamentos gerais de um Veículo (como ter rodas, poder se mover) e depois adiciona os seus próprios específicos (como ter portas, assentos específicos).

A herança promove a reutilização de código e ajuda a modelar relacionamentos do mundo real.

Em Python:

```python
class Veiculo: # Projeto geral
    def __init__(self, num_rodas, velocidade_maxima):
        self.num_rodas = num_rodas
        self.velocidade_maxima = velocidade_maxima

    def mover(self):
        print("O veículo está se movendo.")

class Carro(Veiculo): # Carro herda de Veiculo
    def __init__(self, cor, marca):
        super().__init__(4, 200) # Chama o construtor do pai (Veiculo)
        self.cor = cor
        self.marca = marca

    def acelerar(self): # Carro tem seu próprio método específico
        print(f"O carro {self.cor} {self.marca} está acelerando!")

class Motocicleta(Veiculo): # Motocicleta também herda de Veiculo
    def __init__(self, tamanho_motor):
        super().__init__(2, 180) # Chama o construtor do pai (Veiculo)
        self.tamanho_motor = tamanho_motor

    def empinar(self):
        print(f"A motocicleta está empinando!")

meu_carro = Carro("verde", "BMW")
meu_carro.mover() # Carro pode usar o método mover do Veiculo
meu_carro.acelerar()

minha_moto = Motocicleta("1000cc")
minha_moto.mover()
minha_moto.empinar()
```

### 👉 **Criando** as classes Refeições, Treinos e Datas<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Em nosso rastreador de fitness, usaremos três classes, uma para as datas, outra para os treinos e outra para as refeições. Cada uma das colunas em treinos e refeições será um atributo diferente.

```python
class EntradaLog:
    def __init__(self, data):
        self.data = data

class Treino(EntradaLog): # Treino herda de EntradaLog
    def __init__(self, data, tipo_treino, duracao, calorias):
        super().__init__(data) # Chama o pai (EntradaLog)
        self.tipo_treino = tipo_treino
        self.duracao = duracao
        self.calorias = calorias

class Refeicao(EntradaLog): # Refeicao herda de EntradaLog
    def __init__(self, data, tipo_refeicao, comida, calorias):
        super().__init__(data) # Chama o pai (EntradaLog)
        self.tipo_refeicao = tipo_refeicao
        self.comida = comida
        self.calorias = calorias
```

## 📄 **Passo 3**: Ler e Limpar **Arquivos CSV**<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
### 👉 Leitura Manual com o Módulo CSV<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Existem duas rotas principais para carregar o arquivo csv. A primeira é usando o módulo `csv` e carregá-lo em uma lista. Ao fazer isso, usamos os métodos `strip()` e `int()`.
O método `strip()` é usado para remover espaços em branco no início e no final (espaços, tabulações, novas linhas) de uma string. Isso ajuda a prevenir Problemas Comuns de Entrada de Dados causados por entrada de dados humana ou automatizada, Comparações/Buscas Precisas e Erros ao aplicar a outra conversão de tipo, por exemplo, com `int()`.
A função `int()` é usada para converter uma string ou um float em um inteiro para que possamos fazer operações numéricas com ele.

```python
import csv

def ler_treinos_manual(caminho_arquivo):
    treinos = []
    with open(caminho_arquivo, newline='') as csvfile: # Abre e fecha automaticamente quando terminar
        leitor = csv.reader(csvfile) # Cria um objeto que pode iterar sobre as linhas
        next(leitor) # Pula o cabeçalho
        for linha in leitor:
            # Cria um objeto Treino para cada linha e adiciona à lista de treinos
            data = linha[0].strip()
            tipo_treino = linha[1].strip()
            duracao = int(linha[2].strip())
            calorias = int(linha[3].strip())
            treinos.append(Treino(data, tipo_treino, duracao, calorias))
    return treinos

```

### 👉 Usando Pandas<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

O segundo módulo que é usado para carregar arquivos csv e trabalhar com suas informações é o `pandas`. O Pandas carrega as informações do arquivo csv em um dataframe do pandas. Um **Dataframe** é uma estrutura de dados rotulada bidimensional com colunas de tipos potencialmente diferentes. Esta é a principal estrutura de dados do Pandas e é essencialmente uma tabela ou planilha.

Você pode acessar uma célula do dataframe fazendo `df.loc[rotulo_linha, rotulo_coluna]` e uma coluna referindo-se ao seu cabeçalho como abaixo.
```python
import pandas as pd
dados = {'Nome': ['Alice', 'Bob', 'Charlie','Andres'],
        'Idade': [25, 30, 35, 45],
        'Cidade': ['Nova York', 'Londres', 'Paris','Madri']}
df = pd.DataFrame(dados)

valor_celula_padrao = df.loc[0, 'Nome'] # Acessando a linha 0, coluna 'Nome'
print(f"Célula no índice 0, coluna 'Nome' (índice padrão): {valor_celula_padrao}")

coluna_nomes = df['Nome'] # Acessa a coluna 'Nome'
print("A coluna 'Nome':")
print(coluna_nomes)

```

Abaixo, um exemplo de como acessar as linhas.

```python
# Acessa a linha na posição inteira 1 (a segunda linha)
linha_pos_1 = df.iloc[1]
print("Linha na posição inteira 1:")
print(linha_pos_1)
print("-" * 40)

# Acessa múltiplas linhas usando uma lista de posições inteiras
multiplas_linhas_pos = df.iloc[[0, 2]] # Primeira e terceira linhas
print("Linhas nas posições inteiras 0 e 2:")
print(multiplas_linhas_pos)
print("-" * 40)

# Acessa uma fatia de linhas usando posições inteiras (exclusivo do final)
fatia_de_linhas_pos = df.iloc[1:4] # Da posição 1 até (mas não incluindo) 4
print("Fatia de linhas da posição 1 a 3:")
print(fatia_de_linhas_pos)
print("-" * 40)
```

Em nosso rastreador de fitness, a biblioteca pandas é usada na função `carregar_e_limpar_dados()`. O método `.fillna` é usado para substituir as células com dados `NaN` (Não é um Número).

```python
import pandas as pd

def carregar_e_limpar_dados():
    df_treinos = pd.read_csv('dados/treinos.csv')
    df_refeicoes = pd.read_csv('dados/refeicoes.csv')

    df_treinos['data'] = pd.to_datetime(df_treinos['data'])
    df_refeicoes['data'] = pd.to_datetime(df_refeicoes['data'])

    # Preenche quaisquer valores ausentes nos dados de treino com zeros (por exemplo, durações ou calorias ausentes)
    df_treinos.fillna(0, inplace=True)
    # Preenche quaisquer valores ausentes nos dados de refeição com "Desconhecido" (por exemplo, descrições de alimentos ausentes)
    df_refeicoes.fillna("Desconhecido", inplace=True)

    return df_treinos, df_refeicoes
```

## 📊 **Passo 4**: **Resumir** e **Mesclar Dados**<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Agora é hora de combinar os treinos e refeições usando a biblioteca pandas para obter as calorias líquidas. Para fazer isso, seguimos esta sequência:

### 👉 **Agrupar linhas** `df_refeicoes.groupby('data')`:<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Esta é a primeira e mais crucial parte. O método `groupby()` é usado para agrupar linhas com base em valores únicos em uma ou mais colunas.
Neste caso, `df_refeicoes` será agrupado pelos valores únicos na coluna 'data'. Conceitualmente, o pandas criará "grupos" separados para cada data única. Para o nosso exemplo, haveria um grupo para '2025-06-01', um para '2025-06-02' e um para '2025-06-03'.

### 👉 **Selecionar uma coluna** `['calorias']`:<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Após agrupar, você normalmente deseja realizar uma operação em uma coluna específica dentro de cada grupo. `['calorias']` seleciona a coluna 'calorias' de cada um desses grupos criados. Isso significa que, para cada grupo de data, estamos interessados apenas nos valores de calorias.

### 👉 Calcular **subtotais** `.sum()`:<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Esta é uma função de agregação. Após selecionar a coluna 'calorias_queimadas' para cada grupo, `.sum()` calcula a soma total de 'calorias' para cada respectivo grupo (ou seja, para cada data única).

Neste ponto, a saída seria uma Série pandas com a 'data' como índice e a soma de 'calorias' como os valores. Ficaria algo assim:

```bash
data
2025-06-01    1350  (250 + 500 + 600)
2025-06-02    1450  (300 + 450 + 700)
2025-06-03    1250  (200 + 550 + 500)
Nome: calorias_queimadas, dtype: int64
```

### 👉 **Re-Numerar** as linhas da seleção `.reset_index()`:<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Como você pode ver na etapa anterior, após `sum()`, 'data' é o índice da Série resultante.

`.reset_index()` converte o índice de volta em uma coluna regular. Isso é frequentemente desejado para dataframes mais limpos, onde você quer que a coluna agrupada ('data' neste caso) seja uma coluna apropriada em vez do índice do DataFrame.

Após `reset_index()`, a saída será um novo DataFrame:

| data | calorias |
|:---|:---|
| 2025-06-01 | 1350 |
| 2025-06-02 | 1450 |
| 2025-06-03 | 1250 |


Depois disso, os dois dataframes do pandas para treinos e refeições são mesclados e uma nova coluna com as `'calorias_liquidas'` é criada.

A função real que resume os dados em nosso rastreador de fitness é:

```python
def resumir_dados(df_treinos, df_refeicoes):
    resumo_treino = df_treinos.groupby('data')['calorias_queimadas'].sum().reset_index()
    resumo_refeicao = df_refeicoes.groupby('data')['calorias'].sum().reset_index()

    combinado = pd.merge(resumo_treino, resumo_refeicao, on='data', how='outer').fillna(0)
    combinado['calorias_liquidas'] = combinado['calorias'] - combinado['calorias_queimadas']
    return combinado
```


## 📈 **Passo 5**: Visualizar com **matplotlib**<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

A última função que vamos escrever é a que cria o gráfico das calorias de treino, refeição e líquidas para cada dia registrado. Para fazer isso, simplesmente carregamos a biblioteca `matplotlib` e criamos um gráfico montando cada parte como mostrado no código abaixo.

```python
import matplotlib.pyplot as plt

def plotar_tendencias_fitness(df_combinado):
    # Cria uma nova figura com tamanho especificado (largura: 16 polegadas, altura: 10 polegadas)
    # Isso cria um gráfico maior que é mais fácil de ler e analisar
    plt.figure(figsize=(16, 10)) 
    
    # Plota as calorias consumidas com marcadores circulares
    plt.plot(df_combinado['data'], df_combinado['calorias'], label="Calorias Consumidas", marker='o')
    
    # Plota as calorias queimadas com marcadores x para distinção visual
    plt.plot(df_combinado['data'], df_combinado['calorias_queimadas'], label="Calorias Queimadas", marker='x')
    
    # Plota as calorias líquidas (consumidas - queimadas) com estilo de linha tracejada
    # Isso mostra o balanço calórico para cada dia
    plt.plot(df_combinado['data'], df_combinado['calorias_liquidas'], label="Calorias Líquidas", linestyle='--')

    # Calcula e plota uma média móvel de 2 dias das calorias líquidas
    # Isso suaviza as flutuações diárias e mostra a tendência geral
    rolagem = df_combinado['calorias_liquidas'].rolling(window=2).mean()
    plt.plot(df_combinado['data'], rolagem, label="Média Móvel (Líquida)", linestyle='dotted')

    # Adiciona rótulos aos eixos com tamanho de fonte aumentado para melhor legibilidade
    plt.xlabel('Data', fontsize=14)
    plt.ylabel('Calorias', fontsize=14)
    
    # Formata o eixo x para exibir as datas no formato AAAA-MM-DD
    # Isso garante uma representação de data consistente no gráfico
    formato_data = DateFormatter('%Y-%m-%d')
    plt.gca().xaxis.set_major_formatter(formato_data)
    
    # Rotaciona os rótulos do eixo x em 45 graus para evitar sobreposição e aumenta o tamanho da fonte
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    
    plt.title('Resumo do Rastreador de Fitness', fontsize=16) # Adiciona um título descritivo ao gráfico com fonte maior
    
    plt.legend() # Adiciona uma legenda para identificar cada linha no gráfico
    
    plt.grid(True) # Adiciona uma grade para facilitar a leitura de valores do gráfico
    
    plt.tight_layout() # Ajusta o layout para garantir que todos os elementos se encaixem sem sobreposição
    
    plt.show() # Exibe o gráfico concluído
```

O gráfico resultante com as calorias Consumidas e Queimadas, bem como as Líquidas, se parece com:

![Histórico de Calorias Consumidas e Queimadas](Matplotlib_calories_figure.png)

## ▶️ **Passo 6**: Programa Principal<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>

Seguindo as melhores práticas, deixamos a função principal para especificar o fluxo do programa. Isso torna mais fácil revisar e atualizar o código.

```python
def main():
    df_treinos, df_refeicoes = carregar_e_limpar_dados()
    combinado = resumir_dados(df_treinos, df_refeicoes)
    print(combinado)
    plotar_tendencias_fitness(combinado)

if __name__ == "__main__":
    main()
```


## 🧪 Desafios Práticos<a href="#top" class="back-to-top-link" aria-label="Back to Top">↑</a>
Tente modificar ou estender o projeto:
- Adicione o rastreamento de peso.
- Categorize os tipos de refeição (por exemplo, “Alta Proteína”).
- Exporte os resultados para um novo arquivo CSV.
- Destaque os dias com superávit calórico.
