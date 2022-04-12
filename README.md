# ECF - Groupe Hôtelier Hypnos

## Description
Dans le cadre de ma formation, j'ai réalisé l'application d'un groupe hôtelier. Elle permet de se renseigner sur les suites, de les réserver à l'aide de votre compte client. Cette application permet au gérant d'un établissement de maintenir les données de son établissement et au client de gérer ses réservations, ou de contacter le support.

## Le Projet Hypnos
Le projet est actuellement déployé avec Heroku, vous pouvez le retrouver à cette URL : https://hypnos-ecf.herokuapp.com/ 

## En local
Cette application est codée en python avec le framework Flask. Vous pouvez le déployer en local en effectuant les commandes suivantes:

```
  - Placez-vous dans un nouveau dossier
  - Lancer un terminal powershell
  - git clone git@github.com:mayyyyyl/ECF.git
  - python -m -venv -venv
  - pip install -r requirements.txt
  - flask init_db (permet d'initialiser la base de données et de créer un administrateur)
  - $env:FLASK_ENV = "development"
  - flask run
 ```
Vous pouvez actuellement naviguer en mode développement sûr : http://localhost:5000/

## Pour déployer le projet
Une fois sur votre machine en local, vous pouvez être à même de vouloir déployer le projet avec Heroku.
Il vous faudra être connecté sur un compte Heroku (https://id.heroku.com/login)
Après veuillez effectuer les commandes suivantes :
```
- heroku apps:create nom_de_votre_application
- git push heroku main
```
