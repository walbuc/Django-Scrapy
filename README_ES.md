# Django y Scrapy

Un ejemplo de como usar el Django para guardar datos obtenidos mediante un Spider de Scrapy en una base de datos y exponerlos via REST

## Requerimientos no instalables por pip

+ Python 2.7
+ pip
+ virtualenv
+ Un broker compatible con celery, este proyecto asume [redis](http://redis.io) 
+ Una [motor de base de datos](https://docs.djangoproject.com/en/1.3/ref/databases/) compatible con django 

## Instalación


```bash
# instalar fabric en ambiente global
pip install fabric
# clonar repositorio
git clone git://github.com/gcba/Scrapy-Django.git
cd rScrapy-Django
# correr setup
fab DEV setup
```

### Para usuarios de OSX solamente

Reemplazar el último comando por la siguiente secuencia

```bash
fab DEV setup_virtualenv
# activar virtualenv
source bin/activate
# instalar lxml con dependencias estáticas
STATIC_DEPS=true pip install lxml
# continuar instalación
fab DEV update

```

### Customización de Settings 

Cualquier customización de settings necesaria hacerla sobre **settings_local.py**. Copiar archivo demo:

```bash
cp settings_local_demo.py settings_local.py
```
y modificarlo a gusto

## Correr redis-server y celery deamon

```bash
redis-server
```

```bash
python manage.py celeryd
```

## Correr spider

```bash
scrapy runspider scrap.py
```

## Correr server de prueba para ver resultados 
```bash
python manage.py runserver
```