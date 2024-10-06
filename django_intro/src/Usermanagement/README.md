# Prérequis

### Différentes méthodes d'authentification pour utiliser son API :

#### Avec les cookies
Sur Postman on récupère le CSRF token dans les cookies   
Puis on ajoute celui-ci dans les headers (X-CSRFToken)

- **Ce qui est en dessous n'est pas forcément vrai.**   


Basic Auth
Juste besoin de renseigner le user et le password


Bearer Token

Un `POST http://127.0.0.1:8000/dj-rest-auth/login/` avec en body : 
```json
{"username": "username",
 "password": "password"}
```
va renvoyer un access token lié au user (qui doit avoir été créé au préalable). Ce token est utilisable en Bearer Token.