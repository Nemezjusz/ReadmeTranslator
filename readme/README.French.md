> Traduisez-moi

> Choisissez la langue :

> [![pl](https://img.shields.io/badge/lang-polski-red.svg)](https://github.com/Nemezjusz/ReadmeTranslator/blob/main/readme/README.Polish.md) [![es](https://img.shields.io/badge/lang-espanol-orange.svg)]() [![de](https://img.shields.io/badge/lang-deutsch-yellow.svg)]() [![fr](https://img.shields.io/badge/lang-français-blue.svg)]()
[![it](https://img.shields.io/badge/lang-italiano-grren.svg)]()


TranslateMe est un programme Python simple qui utilise le modèle GPT-3.5-turbo d'OpenAI pour traduire automatiquement le texte dans un dépôt GitHub. Ce programme permet aux utilisateurs de traduire le contenu d'un fichier spécifié dans leur dépôt GitHub dans une langue choisie.

## Description

Le programme TranslateMe se compose de deux fonctionnalités principales :

1. **Traduction à l'aide du modèle GPT-3.5-turbo d'OpenAI :**
   - Le programme utilise le modèle GPT-3.5-turbo d'OpenAI pour effectuer la traduction de texte.
   - Les utilisateurs peuvent spécifier le nom d'utilisateur GitHub, le nom du dépôt, la branche, le chemin du fichier et la langue cible.
   - Le contenu traduit est ensuite téléchargé à nouveau dans le dépôt GitHub spécifié.

2. **Interface Graphique Utilisateur (GUI) :**
   - Le programme comprend une interface graphique simple construite à l'aide de la bibliothèque customtkinter.
   - Les utilisateurs peuvent saisir leurs identifiants GitHub, les détails du dépôt et les préférences de traduction à l'aide de l'interface graphique.
   - En cliquant sur le bouton "Traduire", le programme lance le processus de traduction.

## GUI
![Zrzut ekranu 2024-02-01 194536](https://github.com/Nemezjusz/ReadmeTranslator/assets/50834734/ef77cbf9-fece-46bc-bc59-a8e56f96eced)

## Utilisation

Pour utiliser TranslateMe, suivez ces étapes :

1. Lancez le programme en exécutant le script Python fourni.
2. Remplissez les informations requises dans l'interface graphique :
   - Nom d'utilisateur : Votre nom d'utilisateur GitHub.
   - Nom du dépôt : Le nom de votre dépôt GitHub.
   - Branche : La branche dans laquelle se trouve le fichier (par défaut, il est configuré sur 'main').
   - Chemin du fichier : Le chemin vers le fichier que vous souhaitez traduire (par défaut, il est configuré sur 'README.md').
   - Langue : Choisissez la langue cible pour la traduction dans le menu déroulant.
   - OpenAI API : Indiquez votre clé OpenAI GPT-3.5-turbo API.
   - GitHub API : Indiquez votre clé GitHub API (facultatif si le dépôt est public ou ne nécessite pas d'authentification).
3. Cliquez sur le bouton "Traduire" pour lancer le processus de traduction.
4. Le contenu traduit sera téléchargé dans le dépôt GitHub spécifié.

## Remarque

- Assurez-vous d'avoir des clés API valides pour OpenAI et GitHub pour l'authentification.
- Le fichier traduit sera enregistré dans le répertoire 'readme' avec un nom de fichier du type 'README.{langue}.md'.

N'hésitez pas à personnaliser le programme et à explorer des fonctionnalités supplémentaires en fonction de vos besoins.

> [!ATTENTION]
> Faites toujours preuve de prudence lors de la manipulation des clés API et évitez de les partager publiquement.