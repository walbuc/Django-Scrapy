# An example of how to use Django ORM to store in a db obtained data by a Scrapy Spider an then exopse the data through an REST API

As an example, i set up this project to scrap all over rolling stone lists/rankings and store them in a relational db with proper data models
 
## Non pip requirements

+ Python 2.7
+ pip
+ virtualenv
+ Some broker compatible with celery, i use [redis](http://redis.io)
+ a db compatible with django, i use sqlite 3 in dev, postgres or mongodb in prod. If you are not familiar how django manages dbs go [here](https://docs.djangoproject.com/en/1.3/ref/databases/)

## Installation

Clone project and install requirements in virtualenv

```bash
# install fabric in python global enviroment
pip install fabric
# clone repo
git clone git://github.com/drkloc/rstone_scrapper.git
cd rstone_scrapper
# setup app
fab DEV setup
```

### For OSX users only

You need to install lxml with static deps **before** runing pip against requirements file:

```bash
STATIC_DEPS=true pip install lxml
```

### Settings override

Any settings override (Database config, broker config, etc) are conveniently made inside **settings_local.py**. Just copy the demo file:

```bash
cp settings_local_demo.py settings_local.py
```

and start customizing whatever you want/need.

## Start redis-server and celery deamon

```bash
redis-server
```

```bash
python manage.py celeryd
```

## Initialization

```bash
scrapy runspider scrap.py
```

## Running server
```bash
python manage.py runserver
```