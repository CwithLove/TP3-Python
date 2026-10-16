# Conception — TP3 Python

## Partie I — Dog Guesser

J'ai choisi de développer une application simple avec Tkinter pour respecter la contrainte Python et éviter une architecture trop complexe.

Le jeu contient 10 questions avec 4 réponses possibles. Chaque bonne réponse rapporte 100 points.

Pour améliorer l'expérience utilisateur, j'ai choisi :
- Un retour visuel sur les réponses : vert pour la bonne réponse et rouge pour la mauvaise.
- Une validation au relâchement du clic pour permettre au joueur d'annuler son choix.
- Un classement final avec des commentaires aléatoires selon le score.
- Une sauvegarde des scores et des records dans un fichier JSON.

L'application utilise `requests` pour récupérer les données de Dog CEO et Pillow pour afficher les images.

## Partie II — Tableau interactif

J'ai utilisé une architecture client/serveur avec une API HTTP et une communication WebSocket.

Le client Python utilise `requests` pour envoyer les formes au serveur. Le serveur utilise FastAPI pour recevoir les requêtes et transmettre les formes aux tableaux connectés.

Les formes sont affichées avec HTML Canvas. J'ai testé les cinq types de formes et la synchronisation entre deux tableaux connectés simultanément.

## Utilisation de l'IA

J'ai utilisé ChatGPT pour m'aider dans la rédaction du README et du document de conception, notamment pour la formulation en français, la grammaire et l'orthographe.

ChatGPT m'a également accompagné dans le développement du projet, notamment pour la compréhension du code, la résolution des erreurs rencontrées et l'amélioration des interactions du jeu.

Les fonctionnalités et les choix d'interface ont été discutés et ajustés au fur et à mesure des tests.