# TP3 — Programmation Python

Ce projet contient deux applications : **Dog Guesser** et **Tableau interactif**.

## Installation

Prérequis : Python 3 avec Tkinter.

Créer et activer un environnement virtuel :

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Installer les dépendances :

```bash
python3 -m pip install -r requirements.txt
```

## Partie I — Dog Guesser

Jeu de reconnaissance de races de chiens utilisant l'API Dog CEO.

- 10 questions avec 4 réponses possibles.
- 100 points par bonne réponse.
- Sauvegarde des scores et records dans un fichier JSON.
- Classement et commentaires selon le score final.

Lancement :

```bash
python3 partie1/main.py
```

## Partie II — Tableau interactif

Tableau de dessin partagé utilisant HTTP et WebSocket.

Lancer le serveur :

```bash
python3 partie2/server.py
```

Ouvrir `http://localhost:8080/` dans un navigateur.

Dans un autre terminal, lancer le client :

```bash
python3 partie2/client.py
```

Le client permet de dessiner cinq formes : point, ligne, cercle, rectangle et carré. Les dessins sont transmis en temps réel aux tableaux connectés.