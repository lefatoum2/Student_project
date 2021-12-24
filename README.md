# Student_project

## Sommaire 

* [1. Installation](#Section_1)
* [2. Les Routes](#Section_2)
* [3. Les Templates](#Section_3)


## 1. Installation<a class="anchor" id="section_1"></a>  


```
pip install django==3.0.2
```
Création d'un projet :
```
django-admin startproject Student_project
```
Création d'une application (compte, CRUD) :

```
django-admin startapp compte
```
```
django-admin startapp CRUD
```

projet/settings.py :

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compte',
    'CRUD',
]
```