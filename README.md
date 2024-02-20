# Taskmaster

O Taskmaster é um website que permite o usuário criar tarefas para que ele possa se organizar melhor no seu dia a dia. A aplicação possui aparencia minimalista e busca ajudar o usuário a ter um lugar simples e sem distrações para se organizar.

# Objetivo

O objetivo do projeto é a prática do desenvolvimento web backend utilizando o framework Flask e o banco de dados MySQL. Além disso, aprender quais bibliotecas existem úteis e que permitem tornar esse projeto possível.

# Funcionalidades

- [ ] Landing Page de Apresentação  
- [ ] Cadastro do Usuário  
- [ ] Login do Usuário com Autenticação JWT  
- [ ] Board com as Tarefas  
- [ ] Gerenciamento das Tarefas   
- [ ] Gerencimaneto da Conta do Usuário 

Foram utilizados conceitos como Inversão de Dependencia durante o desenvolvimento de projeto e foram elaborados testes para todos os casos de uso.

# Demonstração

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

Geralemente, o nome colocado o .venv, mas isso é de sua escolha.

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

Notas: o ambiente vitural é criada na mesma pasta do projeto.

## Bibliotecas

Algumas biblittecas e framework foram utilizadas para realização do projeto:

- Flask (Servidor e Rotas)
- Python Dotenv
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

Crie a variável de ambiente FLASK_APP com o diretório da aplicação:

```
export FLASK_APP=src/server/server.py
```
Sem espaço antes de depois do sinal de igual.

Rode com o seguinte comando.

```
flask run --debug
```
