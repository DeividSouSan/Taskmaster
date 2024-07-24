# Taskmaster

O Taskmaster é um website que permite o usuário criar tarefas para que ele possa se organizar melhor no seu dia a dia. A aplicação possui aparencia minimalista e busca ajudar o usuário a ter um lugar simples e sem distrações para se organizar.

## Objetivo

O objetivo do projeto foi aprender mais sobre o desenvolvimento backend utilizando o Python e o micro-framework Flask. Além disso, desenvolver minhas habilidades de solução de problemas e de escrita de código. Como consequência acabei descobrindo algumas bibliotecas que forem facilitadores chave para que o projeto pudesse ser concluído.

## Funcionalidades

- [x] Cadastro de Usuários no Banco de Dados
- [x] Autenticação de Usuários (Login)
- [x] Sistema de Gerenciamento de Tarefas (CRUD)
- [x] Feedback de Operações (foco em UX)

## Demonstração
### Tela Inicial
![Taskmaster - Home](https://github.com/user-attachments/assets/78f7325c-2ec2-4fed-87cd-ffdedcadc854)

### Tela de Cadastro
![Taskmaster - Cadastro 1](https://github.com/user-attachments/assets/9a3031fe-667b-478d-adea-ae18320d47be)
![Taskmaster - Cadastro 2](https://github.com/user-attachments/assets/0ceec80a-9ca5-414c-8f87-8ac2fa05c24f)

### Tela de Login
![Taskmaster - Login 1](https://github.com/user-attachments/assets/9b70764d-e46a-401a-b40d-e3bb3a81b97b)
![Taskmaster - Login 2](https://github.com/user-attachments/assets/1268259c-eb32-4a1f-ad92-88664cce74ba)

### Quadro de Tarefas
![Taskmaster - Board](https://github.com/user-attachments/assets/5591d5a4-37fe-48e8-b018-8c9e26840409)
![Taskmaster - Board 2](https://github.com/user-attachments/assets/5fe7492c-7b83-4752-af81-b652a7d9a24f)
![Taskmaster - Board 3](https://github.com/user-attachments/assets/9351ad58-eb83-4e68-b318-9cbbd197a2e2)

## Como Rodar o Projeto?

### Clonando

Primeiro clone o repositório. Isso pode ser feito baixando-o ou utilizando o comando:

```
git clone git@github.com:DeividSouSan/Taskmaster.git
```

Utilizando sua IDE ou Editor de Texto abra o projeto. Se estiver pelo terminal acesse a pasta onde baixou/clonou o projeto e escreva: 

```
cd taskmaster
```

### Ambiente Virtual

Dentro da pasta do projeto, inicie um ambiente virtual. Eu recomendo instalar as bibliotecas em um ambiente virtual para evitar conflitos de versões com os pacotes instalados globalmente. Pelo terminal, crie um ambiente virtual utilizando:
```
python3 -m venv <nome_do_ambiente_virtual>
```

Comumento o nome utilizado é .venv, mas isso é de sua escolha.

Para ativar o ambiente virutal no linux:

```
source .venv/bin/activate
```

Ou

```
. .venv/bin/activate
```

Para desativa-lo:

```
deactivate
```

No windows:
```
.venv/Scripts/activate
```

Para desativa-lo:

```
.venv/Scripts/deactivate
```

### Bibliotecas

Utilizei as seguintes bibliotecas para realização do projeto:

- Flask (Servidor e Rotas)
- Python Dotenv (Variáveis de Ambiente)
- PyMySQL (Driver de Conexão para o MySQL)
- Flask-SQLAlchemy e SQLAlchemy(Object Relational Mapper)
- Flask-WTF e WTForms (Formulários)
- Bcrypt (Hash da Senha)
- Unittest (built-in do Python para testes)
- HTMX (requisições HTTP direto dos elementos HTML)
- SQLite3 (built-in do Python)

Para baixar as bibliotecas do Python escreva no terminal (antes verifique se o ambiente virtual está ativado):

```bash
pip install requirements.txt
```

Assim todas as dependencias que estão dentro do arquivo `requirements.txt` serão baixadas para o seu ambiente virtual.

### Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

```
APP_CONFIG = "ProductionConfig"

SECRET_KEY = <uma_string_difícil>
```

Os valores à direita são ficticios e devem ser susbstituidos pela informações da sua configuração. Elas serão importadas para dentro de `server.py` e serão utilizadas para acessar, criar e modificar o banco de dados.

O `APP_CONFIG` é onde você define qual configurações do Flask serão utilizadas. Utilize `ProductionConfig` para testar o aplicativa da maneira que ele iria para produção. As outras configurações podem ser vistas em `config.py`.

### Banco de Dados

O banco de dados utilizado para essa aplicação foi o SQLite por motivos de praticidade. Nenhuma configuração adicional é necessária. Basta rodar a aplicação normalmente. Se tudo ocorrer bem ao rodar pela primeira vez, um arquivo chamado `taskmaste.db` surgirá dentro do diretório `instance/`.

### Finalmente Rodando a Aplicação

Para rodar a aplicação rode o arquivo nomeado como `wsgi.py`.

```
python wsgi.py
```

##3 Ferramentas e Tecnologias
![HTMX](https://img.shields.io/badge/%3C/%3E%20htmx-3D72D7?style=for-the-badge&logo=mysl&logoColor=white)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![VSCode](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
