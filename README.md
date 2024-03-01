# Taskmaster

O Taskmaster é um website que permite o usuário criar tarefas para que ele possa se organizar melhor no seu dia a dia. A aplicação possui aparencia minimalista e busca ajudar o usuário a ter um lugar simples e sem distrações para se organizar.

# Objetivo

O objetivo do projeto é a prática do desenvolvimento web backend utilizando o framework Flask e o banco de dados MySQL. Além disso, aprender quais bibliotecas que o ambiente possui para tornar esse projeto possível.

# Funcionalidades

- [x] Cadastro do Usuário
- [x] Autenticação do Usuário
- [x] Sistema de Gerenciamento de Tarefas (Adicionar e Remover Tarefas) 
- [x] Feedback de Erros para diversas operações
- [ ] Ordenar as Tarefas por Status
- [ ] Exclusão da Conta

# Demonstração
## Cadastrando

## Login
![login](https://github.com/DeividSouSan/Taskmaster/assets/49818020/1292ad3a-cfae-4c4a-bf7d-1b59e30f777c)

## Adicionando Tarefa
![adicionando_tarefa](https://github.com/DeividSouSan/Taskmaster/assets/49818020/ae8f377c-62e4-4548-a9c8-f841359504fa)

## Removendo Tarefa
![excluindo_tarefa](https://github.com/DeividSouSan/Taskmaster/assets/49818020/190fcb2f-a2b2-4bc0-aa30-c50c9ad7aff9)

## Deslogando
![deslogando](https://github.com/DeividSouSan/Taskmaster/assets/49818020/fbecb0b3-88bd-4200-9114-71d9cc5d8456)

# Como Rodar o Projeto?

## Clonando

Clone o repositório utilizando:

```
git clone git@github.com:DeividSouSan/Taskmaster.git
```

Acesse o diretório do projeto com:

```
cd taskmaster
```

## Ambiente Virtual

Recomendo instalar as bibliotecas em um ambiente virtual para evitar conflitos de versões com os pacotes instalados globalmente. Para criar um ambiente virtual rode os comandos abaixo:

```
python3 -m venv <nome_do_ambiente_virtual>
```

Comumento o nome utilizado é .venv, mas isso é de sua escolha.

Para ativar o ambiente virutal:

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

Notas: o ambiente vitural é criado na mesma pasta do projeto.

## Bibliotecas

Algumas biblittecas e framework foram utilizadas para realização do projeto:

- Flask (Servidor e Rotas)
- Python Dotenv (Variáveis de Ambiente)
- PyMySQL
- Flask-SQLAlchemy e SQLAlchemy(Object Relational Mapper)
- Flask-WTF e WTForms (Formulários)
- Bcrypt (Hash da Senha)
- Unittest (built-in do Python para testes)

Para baixa-las basta você utilizar o seguinte comando:

```bash
pip install requirements.txt
```

Assim todas as dependencias serão baixadas para o seu computador ou ambiente virutal.

## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

```
USER = nome_usuario

PASSWORD = senha_perfil

DATABASE = nome_banco_de_dados
```

Os valores à direita são ficticios e devem ser susbstituidos pela informações da sua configuração. Elas serão importadas para dentro de `server.py` e serão utilizadas para acessar, criar e modificar o banco de dados.

**Nota**: Antes de iniciar a aplicação, certifique-se de criar manualmente o banco de dados no seu Sistema Gerenciador de Banco de Dados MySQL. Consulte a [documentação](https://dev.mysql.com/doc/) do MySQL para obter instruções sobre como criar um novo banco de dados. Além disso, é necessário que o perfil fornecido tenha acesso ao banco de dados para criar e modificar as tabelas.

Se estiver usando o MySQL pelo terminal, você pode acessa-lo e criar o banco de dados assim:

```mysql
mysql> CREATE DATABASE nome_do_seu_banco_de_dados;
```

## Finalmente Rodando a Aplicação

Para rodar a aplicação rode o arquivo nomeado como `wsgi.py`.
```
