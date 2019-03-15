# Mordor

Proyecto de ejemplo

### Requisitos

Python +3.7

### Instalación

Primero tienen que crear su enviroment con el siguiente commando:

```
py -m venv {nombre del enviroment}
```

A veces puede py o py3 depende de la variable de entorno.
Después activan su enviroment:

```
Mac o linux: source /{nombre del enviroment}/bin/activate
Windows: ./{nombre del enviroment}/Scripts/activate
```

Installan las dependecias para su enviroment:

```
pip install -r requirements (instala todos los paquetes dentro del archivo requirements.txt)
pip install {paquete} (por paquetes individuales)
```

Aplican migraciones:

```
python manage.py migrate
```

Y corren el servidor local

```
python manage.py runserver 8000 (puerto 8000)
python manage.py runserver 0.0.0.0:8000 (puerto 8000 compartido por IP)
```
