# ReadmeTranslator 

> Choisissez la langue:
>
> [![polonais](https://img.shields.io/badge/lang-polish-red.svg)](https://github.com/Nemezjusz/ReadmeTranslator/blob/main/readme/README.polish.md) [![espagnol](https://img.shields.io/badge/lang-spanish-red.svg)](https://github.com/Nemezjusz/ReadmeTranslator/blob/main/readme/README.spanish.md) 

TranslateMe est un programme Python simple qui utilise le modèle GPT-3.5-turbo d'OpenAI pour traduire automatiquement le texte dans un référentiel GitHub. Ce programme permet aux utilisateurs de traduire le contenu d'un fichier spécifié dans leur référentiel GitHub vers une langue choisie.

## Description

Le programme TranslateMe se compose de deux fonctionnalités principales:

1. **Traduction en utilisant le modèle GPT-3.5-turbo d'OpenAI:**
   - Le programme utilise le modèle OpenAI GPT-3.5-turbo pour effectuer la traduction de texte.
   - Les utilisateurs peuvent spécifier le nom d'utilisateur GitHub, le nom du référentiel, la branche, le chemin du fichier et la langue cible.
   - Le contenu traduit est ensuite téléchargé de nouveau dans le référentiel GitHub spécifié.

2. **Interface graphique utilisateur (GUI):**
   - Le programme inclut une interface graphique simple construite à l'aide de la bibliothèque customtkinter.
   - Les utilisateurs peuvent entrer leurs informations d'identification GitHub, les détails du référentiel et les préférences de traduction via l'interface graphique.
   - En cliquant sur le bouton "Traduire", le programme lance le processus de traduction.

## GUI
![Zrzut ekranu 2024-02-01 194536](https://github.com/Nemezjusz/ReadmeTranslator/assets/50834734/ef77cbf9-fece-46bc-bc59-a8e56f96eced)

## Utilisation

Pour utiliser TranslateMe, suivez ces étapes:

1. Lancez le programme en exécutant le script Python fourni.
2. Remplissez les informations requises dans l'interface graphique:
   - Nom d'utilisateur: Votre nom d'utilisateur GitHub.
   - Nom du référentiel: Le nom de votre référentiel GitHub.
   - Branche: La branche dans laquelle se trouve le fichier (par défaut, 'main' est défini).
   - Chemin du fichier: Le chemin vers le fichier que vous souhaitez traduire (par défaut, 'README.md' est défini).
   - Langue: Choisissez la langue cible pour la traduction dans le menu déroulant.
   - OpenAI API: Fournissez votre clé API OpenAI GPT-3.5-turbo.
   - GitHub API: Fournissez votre clé API GitHub (facultatif si le référentiel est public ou ne nécessite pas d'authentification).
3. Cliquez sur le bouton "Traduire" pour démarrer le processus de traduction.
4. Le contenu traduit sera téléchargé dans le référentiel GitHub spécifié.

## Remarque

- Assurez-vous d'avoir des clés API OpenAI et GitHub valides pour l'authentification.
- Le fichier traduit sera enregistré dans le répertoire 'readme' avec un nom de fichier tel que 'README.{langue}.md'.

N'hésitez pas à personnaliser le programme et à explorer des fonctionnalités supplémentaires en fonction de vos besoins.

> [!CAUTION]
> Faites toujours preuve de prudence lors de la manipulation des clés API et évitez de les partager publiquement.