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
