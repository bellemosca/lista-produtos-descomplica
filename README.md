# Lista de Produtos - Descomplica

Quis adipisicing pariatur adipisicing Lorem aliqua velit id.

## Como rodar o projeto

1. Realize as migrações do banco de dados:
	```bash
	uv run python manage.py makemigrations
	uv run python manage.py migrate
	```

2. Popule o banco com dados de exemplo:
	```bash
	uv run python manage.py shell < seed/seed.py
	```

3. Inicie o servidor de desenvolvimento:
	```bash
	uv run python manage.py runserver
	```
