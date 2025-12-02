# Lista de Produtos - Descomplica

Aplicação web Django para exibição de uma lista de produtos com paginação. O projeto exibe produtos (nome, descrição e preço) em uma interface web com 5 produtos por página.

## Como rodar o projeto

1. Instale o uv (gerenciador de pacotes Python):

   Siga as instruções de instalação na [documentação oficial do uv](https://docs.astral.sh/uv/).

2. Instale o Python 3.12:

   ```bash
   uv python install 3.12
   ```

3. Realize as migrações do banco de dados:

   ```bash
   uv run python manage.py makemigrations
   uv run python manage.py migrate
   ```

4. Popule o banco com dados de exemplo:

   ```bash
   uv run python manage.py shell < seed/seed.py
   ```

5. Inicie o servidor de desenvolvimento:
   ```bash
   uv run python manage.py runserver
   ```
