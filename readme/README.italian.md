# ReadmeTranslator 

> Scegli la lingua: 
>
> [![francese](https://img.shields.io/badge/lang-francese-red.svg)](https://github.com/Nemezjusz/ReadmeTranslator/blob/main/readme/README.french.md) [![tedesco](https://img.shields.io/badge/lang-tedesco-red.svg)](https://github.com/Nemezjusz/ReadmeTranslator/blob/main/readme/README.german.md) [![polacco](https://img.shields.io/badge/lang-polacco-red.svg)](https://github.com/Nemezjusz/ReadmeTranslator/blob/main/readme/README.polish.md) [![spagnolo](https://img.shields.io/badge/lang-spagnolo-red.svg)](https://github.com/Nemezjusz/ReadmeTranslator/blob/main/readme/README.spanish.md) 


TranslateMe è un semplice programma Python che utilizza il modello GPT-3.5-turbo di OpenAI per tradurre automaticamente il testo in un repository di GitHub. Questo programma consente agli utenti di tradurre il contenuto di un file specificato nel loro repository di GitHub in una lingua scelta.

## Descrizione

Il programma TranslateMe è composto da due principali funzionalità:

1. **Traduzione utilizzando il modello GPT-3.5-turbo di OpenAI:**
   - Il programma utilizza il modello GPT-3.5-turbo di OpenAI per eseguire la traduzione del testo.
   - Gli utenti possono specificare il nome utente di GitHub, il nome del repository, il branch, il percorso del file e la lingua di destinazione.
   - Il contenuto tradotto viene quindi caricato nuovamente nel repository di GitHub specificato.

2. **Interfaccia grafica (GUI):**
   - Il programma include una semplice interfaccia grafica creata utilizzando la libreria customtkinter.
   - Gli utenti possono inserire le proprie credenziali di GitHub, i dettagli del repository e le preferenze di traduzione utilizzando la GUI.
   - Cliccando il pulsante "Traduci", il programma avvia il processo di traduzione.

## GUI
![Zrzut ekranu 2024-02-01 194536](https://github.com/Nemezjusz/ReadmeTranslator/assets/50834734/ef77cbf9-fece-46bc-bc59-a8e56f96eced)

## Utilizzo

Per utilizzare TranslateMe, seguire questi passaggi:

1. Avviare il programma eseguendo lo script Python fornito.
2. Compilare le informazioni richieste nella GUI:
   - Username: Il tuo nome utente di GitHub.
   - Nome Repo: Il nome del tuo repository di GitHub.
   - Branch: Il branch in cui si trova il file (è impostato per default su 'main').
   - Percorso File: Il percorso del file che si desidera tradurre (è impostato per default su 'README.md').
   - Lingua: Scegliere la lingua di destinazione per la traduzione dal menu a tendina.
   - OpenAI API: Fornire la propria chiave API di OpenAI GPT-3.5-turbo.
   - GitHub API: Fornire la propria chiave API di GitHub (opzionale se il repository è pubblico o non richiede autenticazione).
3. Fare clic sul pulsante "Traduci" per avviare il processo di traduzione.
4. Il contenuto tradotto verrà caricato nel repository di GitHub specificato.

## Nota

- Assicurarsi di avere chiavi API valide di OpenAI e GitHub per l'autenticazione.
- Il file tradotto verrà salvato nella directory 'readme' con un nome di file come 'README.{lingua}.md'.

Sentitevi liberi di personalizzare il programma e esplorare funzionalità aggiuntive in base alle vostre esigenze.

> [!CAUTION]
> Fate sempre attenzione quando gestite le chiavi API e evitate di condividerle pubblicamente.