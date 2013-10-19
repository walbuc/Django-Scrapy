from fabric.api import * 
import os
FAB_ROOT = os.path.dirname(os.path.realpath(__file__))

def virtualenv(command):
    if env.host_string is 'localhost':
        with lcd(env.directory):
            local("/bin/bash -l -c '%s && %s'"%(env.activate,command))
    else:
        with cd(env.directory):
            run("%s && %s"%(env.activate,command))

def git_pull():
    if env.host_string is 'localhost':
        with lcd(env.directory):
            local('git pull')
    else:
        with cd(env.directory):
            run('git pull')

def setup_virtualenv():
    if env.host_string is 'localhost':
        with lcd(env.directory):
            local('virtualenv . --distribute')
    else:
        run('mkvirtualenv --no-site-packages --distribute coras')

def install_requirements():
    virtualenv('pip install -U -r %s'%(os.path.join(env.directory,'requirements.txt')))

def collect_static():
    if env.host_string is not None and env.host_string is not 'localhost':
        virtualenv('cd %s && python manage.py collectstatic --noinput'%env.project_directory)

def setup_app():
    virtualenv('cd %s && python manage.py syncdb --noinput --all'%env.project_directory)
    virtualenv('cd %s && python manage.py migrate --fake'%env.project_directory)
    virtualenv('cd %s && python manage.py createsuperuser'%env.project_directory)

# Workflow
def data_backup():
    # virtualenv('cd %s && python manage.py dumpdata cms text filer.image cmsplugin_filer_image.filerimage --indent 2 > core/fixtures/data.json'%env.project_directory)
    pass

def pip_freeze():
    virtualenv('pip freeze | grep -v distribute > requirements.txt')
# / Workflow

def push_changes(message):
    local('git add . -A')
    local('git commit -m "%s"'%message)
    local('git push')

# Enviroments
def DEV():
    env.hosts=['localhost']
    env.directory=FAB_ROOT
    env.activate='source %s'%os.path.join(FAB_ROOT,'bin/activate')
    env.project_directory='rstone'

# / Enviroments

# Deploys
def setup():
    setup_virtualenv()
    update()    

def update():
    install_requirements()
    setup_app()

def freeze():
    data_backup()
    pip_freeze()
    push_changes('Freezing before deploy')
# / Deploys
