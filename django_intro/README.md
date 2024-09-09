# Prérequis

### Environnement

Création de l'environnement virtuel
`python -m venv .env`

Installation des librairies
`pip install -r requirements.txt`  


### Commandes Django

Pour créer l'architecture d'un projet Django :
`django-admin startproject MyDjangoProject`

Pour avoir la doc de la commande 
`django-admin help startproject`

Lancer le serveur en local (terminal ouvert à la racine de src)
`py manage.py runserver`

Pour créer une application
`py manage.py startapp WelcomeApp`

### Architecture Projet Django 

```MyDjangoProject/
    app1/
        static/
            app1/
                css/
                js/
                images/
        templates/
        views.py
        models.py
        ...
    app2/
        static/
            app2/
                css/
                js/
                images/
        templates/
        views.py
        models.py
        ...
    MyDjangoProject/
        settings.py
        urls.py
        ...
    static/
        css/
        js/
        images/
    templates/
        index.html
    ...
```