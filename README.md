# Sprechen-youtube-automation
# 🎥 Robot de Création de Vidéos Automatisées

Ce projet a pour objectif de montrer comment automatiser la création de vidéos éducatives à l'aide de technologies modernes. En utilisant la génération de voix avec Text-to-Speech (TTS) et le montage vidéo avec MoviePy, ce robot prend en charge tout le processus de production de vidéos, depuis le texte brut jusqu'à la vidéo finale.

## 🧑‍🏫 Contexte

L'idée m'est venue lorsqu'un ami enseignant d'allemand m'a demandé de l'aider à créer des vidéos pour enseigner la langue à ses élèves. Plutôt que de produire chaque vidéo manuellement, j'ai développé un robot qui le fait automatiquement, économisant ainsi beaucoup de temps et d'effort.

## ⚙️ Fonctionnalités

- **Génération automatique de voix** : Utilise la bibliothèque Text-to-Speech (TTS) pour générer des voix off en français et en allemand à partir d'un texte.
- **Montage vidéo automatisé** : Assemble le fond, le texte et les voix off en une vidéo complète à l'aide de MoviePy.
- **Gestion dynamique du contenu** : Les phrases et traductions sont stockées dans un fichier CSV, ce qui permet de générer automatiquement plusieurs vidéos sans intervention manuelle.
- **Fond coloré dynamique** : Le fond de la vidéo change à chaque nouvelle phrase, offrant une variation visuelle subtile.

## 🛠️ Technologies Utilisées

- **Python** : Le langage principal utilisé pour automatiser la génération et le montage vidéo.
- **TTS (Text-to-Speech)** : Génération des voix à partir des phrases écrites en français et en allemand.
- **MoviePy** : Bibliothèque Python pour la création et l'édition de vidéos.
- **CSV** : Format de fichier utilisé pour stocker les phrases en français et en allemand.

## 📁 Structure du Projet
root
│── data/\
│   └── phrases.csv             # Contient les phrases en français et leurs traductions en allemand\
│── temps/\
│   └── audio1/                     # Dossier pour les fichiers audio en français\
│   └── audio2/                     # Dossier pour les fichiers audio en allemand\
│── videos/\
│   └── finale/                 # fichier où les vidéos générées seront enregistrées\
│── classes/\
│   └── main.py                 # Script principal pour générer les vidéos\
│   └── Audio.py                  # classe pour générer les voix off\
│   └── Sprechen.py         # classe pour assembler les éléments en vidéo avec MoviePy\
│   └── Clip.py         # classe pour la création des clips vidéo avec MoviePy\
│── README.md  


## 🚀 Comment Utiliser le Projet

### 1. Cloner le dépôt

```shell
git clone https://github.com/dekelshoot/Sprechen-youtube-automation-.git
```


### 2. Installer les dépendances

Assurez-vous d'avoir Python installé sur votre machine. Ensuite, installez les dépendances nécessaires avec la commande suivante :

```shell
pip install -r requirements.txt
```

### 3. Préparer les données

Dans le fichier `data/phrases.csv`, ajoutez les phrases en français et leurs traductions en allemand au format suivant :

```csv
phrase_fr,phrase_de
"Bonjour", "Guten Tag"
"Merci", "Danke"
```

### 4. Générer les vidéos
Exécutez le script principal pour générer les vidéos automatiquement :

```shell
python classes/main.py
```
Les vidéos générées seront disponibles dans le dossier videos/output.

## 📖 Explication du Code
main.py : Coordonne les différentes étapes, de la lecture du fichier CSV à la création finale de la vidéo.
Audio.py : Utilise TTS pour générer les fichiers audio des phrases en français et en allemand.
Clip.py : Utilise MoviePy pour assembler les vidéos avec le fond coloré, le texte et les voix off.

## 🤖 Améliorations Futures
Ajouter plus de personnalisation dans les couleurs et les polices.
Intégrer plus de langues et de voix.
Générer des sous-titres pour les vidéos.
Optimiser le traitement pour de plus grandes quantités de données.

## 📝 Licence
Ce projet est sous licence MIT. 

Profite bien du projet et n’hésite pas à contribuer ou à poser des questions si nécessaire ! 😊

