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

Faire les migrations (BDD)
`python manage.py makemigrations`
`python manage.py migrate`

Cibler une database lors de la migration
`python manage.py migrate --database {database_name}`

Revenir à la 1ere version d'une app avant les migrations
`python manage.py migrate {appName} zero

Pour créer une application
`py manage.py startapp WelcomeApp`

Créer un superuser pour se connecter à la page admin
`py manage.py createsuperuser`

Lancer les tests
`py manage.py test`

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