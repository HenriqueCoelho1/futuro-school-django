# FUTURO ESCOLA

1. Certifique que há o pip instalado sem sua máquina:
   https://pypi.org/project/pip/

2. Na pasta raiz instale o venv e ative-o:

```sh
python -m venv venv
source venv/bin/activate
```

3. Instale as dependencias:

```sh
python > pip install -r requirements.txt
```

4. Execute a migração do banco de dados:

```sh
python manage.py makemigrations app_core
python manage.py migrate
```

5. Rode o servidor e access pela url http://127.0.0.1:8000/
