# Como empezar un proyecto de Djnago desde 0 


1. Creamos un entorno virtual y lo inicializamos 

```zsh
  python3 -m venv .venv
  source .venv/bin/activate
```

2. Instalamos todas las dependencias y creamos el archivo para registrar todas las dependecias que suaremos 

```zsh
  pip install django
  pip freeze > requirements.txt
```

3. Creamos el proyecto 

```zsh
  django-admin startproject IspVisitManager .
  django-admin startapp customer
```