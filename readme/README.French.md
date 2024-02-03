# ReadmeTranslator 

> Choisissez la langue : 
>
> [![german](https://img.shields.io/badge/lang-german-red.svg)](https://github.com/Nemezjusz/ReadmeTranslator/blob/main/readme/README.German.md) [![italian](https://img.shields.io/badge/lang-italian-red.svg)](https://github.com/Nemezjusz/ReadmeTranslator/blob/main/readme/README.Italian.md) [![polish](https://img.shields.io/badge/lang-polish-red.svg)](https://github.com/Nemezjusz/ReadmeTranslator/blob/main/readme/README.Polish.md) [![spanish](https://img.shields.io/badge/lang-spanish-red.svg)](https://github.com/Nemezjusz/ReadmeTranslator/blob/main/readme/README.Spanish.md) 

TranslateMe est un programme Python simple qui utilise le modèle GPT-3.5-turbo d'OpenAI pour traduire automatiquement du texte dans un dépôt GitHub. Ce programme permet aux utilisateurs de traduire le contenu d'un fichier spécifié dans leur dépôt GitHub vers une langue choisie.

## Description

Le programme TranslateMe se compose de deux fonctionnalités principales :

1. **Traduction à l'aide du modèle GPT-3.5-turbo d'OpenAI :**
   - Le programme utilise le modèle GPT-3.5-turbo d'OpenAI pour effectuer la traduction de texte.
   - Les utilisateurs peuvent spécifier le nom d'utilisateur GitHub, le nom du dépôt, la branche, le chemin du fichier et la langue cible.
   - Le contenu traduit est ensuite téléchargé de nouveau dans le dépôt GitHub spécifié.

2. **Interface graphique (GUI) :**
   - Le programme comprend une interface graphique simple construite à l'aide de la bibliothèque customtkinter.
   - Les utilisateurs peuvent saisir leurs informations d'identification GitHub, les détails du dépôt et les préférences de traduction à l'aide de l'interface graphique.
   - En cliquant sur le bouton "Traduire", le programme lance le processus de traduction.

## GUI
![Zrzut ekranu 2024-02-01 194536](https://github.com/Nemezjusz/ReadmeTranslator/assets/50834734/ef77cbf9-fece-46bc-bc59-a8e56f96eced)

## Utilisation

Pour utiliser TranslateMe, suivez ces étapes :

1. Lancez le programme en exécutant le script Python fourni.
2. Remplissez les informations requises dans l'interface graphique :
   - Nom d'utilisateur : Votre nom d'utilisateur GitHub.
   - Nom du dépôt : Le nom de votre dépôt GitHub.
   - Branche : La branche dans laquelle se trouve le fichier (par défaut, il est défini sur "main").
   - Chemin du fichier : Le chemin vers le fichier que vous souhaitez traduire (par défaut, il est défini sur "README.md").
   - Langue : Choisissez la langue cible pour la traduction dans le menu déroulant.
   - API OpenAI : Fournissez votre clé d'API OpenAI GPT-3.5-turbo.
   - API GitHub : Fournissez votre clé d'API GitHub (facultatif si le dépôt est public ou ne nécessite pas d'authentification).
3. Cliquez sur le bouton "Traduire" pour démarrer le processus de traduction.
4. Le contenu traduit sera téléchargé dans le dépôt GitHub spécifié.

## Note

- Assurez-vous d'avoir des clés d'API OpenAI et GitHub valides pour l'authentification.
- Le fichier traduit sera enregistré dans le répertoire "readme" avec un nom de fichier comme "README.{langue}.md".

N'hésitez pas à personnaliser le programme et à explorer des fonctionnalités supplémentaires en fonction de vos besoins.

> [!CAUTION]
> Faites toujours preuve de prudence lors de la manipulation des clés d'API et évitez de les partager publiquement.