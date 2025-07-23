# 10 Dias de Código com IA

Este repositório contém as notas do curso e exemplos de código do curso [10 Dias de Python com IA]. O curso é voltado para programadores curiosos do Vibe Coding, sem experiência em programação, que desejam ter uma visão holística da codificação e das tecnologias de IA e as habilidades para depurar, especificar e examinar o código que é produzido principalmente com IA.

O curso foi criado em [Inglês] e traduzido para [Espanhol] e [Português].

O curso é produzido principalmente para usar o [Visual Studio Code] e o [Github Copilot]; e grande parte dele usa python para automação, chamadas de API, programação web, programação de IA e muito mais.

As notas do curso podem ser encontradas em [notas do curso 10 Dias de Código com IA] e os exemplos de código em [exemplos de código do git hub]. Uma vez que o [Visual Studio Code] e o [python] estejam instalados em sua máquina, você pode executar os exemplos simplesmente digitando em seu terminal:

```python
python <nome_do_arquivo>.py
```

## Clonando o Repositório

Se desejar, você pode instalar o git no seu vs code e clonar este repositório em sua máquina local.

### Instalando o Bash no Visual Studio Code

Se você estiver no Windows e quiser usar o Bash no VS Code, pode instalar o [Git para Windows](https://git-scm.com/download/win), que inclui o Git Bash.

1. Baixe e instale o Git para Windows.
2. Após a instalação, abra o VS Code.
3. Pressione <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> e digite `Terminal: Select Default Profile`.
4. Escolha `Git Bash` na lista.

Agora, quando você abrir um novo terminal no VS Code, ele usará o Bash.

> **Nota:** A instalação do Git para Windows também instalará o Git Bash. Você não precisa instalar o Git separadamente. O Git Bash está incluído como parte do pacote de instalação do Git.

### Crie um ambiente virtual e ative-o
Um **ambiente virtual** em Python é um espaço de trabalho isolado que permite instalar e gerenciar pacotes separadamente da sua instalação global do Python. Isso significa que cada projeto pode ter suas próprias dependências, versões e configurações sem interferir em outros projetos ou no Python do sistema.

**Por que usar um ambiente virtual?**

- Isolamento: Mantém as dependências do projeto separadas, evitando conflitos entre pacotes exigidos por diferentes projetos.
- Reprodutibilidade: Facilita o compartilhamento do seu projeto com outras pessoas, pois você pode especificar exatamente quais pacotes e versões são necessários.
- Segurança: Evita alterações acidentais nos pacotes Python de todo o sistema.

Fluxo de trabalho típico:
- Crie um ambiente virtual para o seu projeto.
- Ative-o antes de trabalhar.
- Instale pacotes usando o pip—estes vão apenas para o ambiente virtual.
- Desative quando terminar.

Essa abordagem é especialmente útil em ambientes colaborativos ou de produção, garantindo consistência e minimizando problemas de dependência.

Para criar um ambiente virtual Python, execute o seguinte comando em seu terminal:

```bash
python -m venv venv
```

Isso criará um novo diretório chamado `venv` contendo o ambiente virtual.

Para ativar o ambiente virtual:

- No Windows:
  ```bash
  .\venv\Scripts\activate
  ```
- No macOS/Linux/terminal bash:
  ```bash
  source .venv/bin/activate
  ```

Uma vez ativado, você pode instalar pacotes usando o `pip` e eles ficarão isolados neste ambiente.

Para desativar o ambiente virtual Python, simplesmente execute:

```bash
deactivate
```

Isso retornará seu terminal ao ambiente Python global.


### Clone este repositório

Para clonar este repositório para sua máquina local, abra seu terminal e execute:

```bash
git clone https://github.com/StructuralWizard/10DiasDePython_pt.github.io.git
```

Isso criará uma cópia local do repositório em seu diretório atual.

### Instale as dependências deste repositório
Para instalar as dependências listadas em `requirements.txt`, certifique-se de que seu ambiente virtual esteja ativado e, em seguida, execute:

```bash
pip install -r requirements.txt
```

Isso instalará todos os pacotes Python necessários para o projeto.

### Execute o site no servidor local
Este site foi criado usando o tema [Just the Docs] e hospedado no [GitHub Pages]. Você pode [Navegar em nossa documentação] para mais informações.

Para visualizar o site do github no navegador em vez de editar seu markdown, você pode executar `bundle exec jekyll serve` na pasta principal 10DaysOfCode, onde você tem o arquivo _config.yml.

Assumindo que [Jekyll] e [Bundler] estão instalados em seu computador:

1. Mude seu diretório de trabalho para o diretório raiz do seu site.

2. Execute `bundle install`.

3. Execute `bundle exec jekyll serve` para construir seu site e visualizá-lo em `localhost:4000`.

    O site construído é armazenado no diretório `_site`.


Nota: Se você estiver usando uma versão do Jekyll inferior a 3.5.0, use a chave `gems` em vez de `plugins`.

----

[Visual Studio Code]: https://code.visualstudio.com/
[Github Copilot]: https://code.visualstudio.com/docs/copilot/overview
[python]: https://www.python.org/downloads/
[Jekyll]: https://jekyllrb.com
[Just the Docs]: https://just-the-docs.github.io/just-the-docs/
[GitHub Pages]: https://docs.github.com/en/pages
[Bundler]: https://bundler.io
[10 Dias de Python com IA]: https://youtube.com/@10diasdepythoncomia?si=xGA44ST0Adad9umr
[Structural Wizard]: https://github.com/StructuralWizard/
[notas do curso 10 Dias de Código com IA]: https://structuralwizard.github.io/10DiasDePython_pt.github.io/
[exemplos de código do git hub]: https://github.com/StructuralWizard/10DiasDePython_pt.github.io/tree/main/_python_code
[Inglês]: https://structuralwizard.github.io/10DaysOfCode.github.io/
[Espanhol]: https://structuralwizard.github.io/10DiasDePython_es.github.io/
[Português]: https://structuralwizard.github.io/10DiasDePython_pt.github.io/