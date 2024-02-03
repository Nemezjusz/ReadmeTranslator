# TraduciMe

> Scegli lingua:
>
> [![francese](https://img.shields.io/badge/lang-francese-red.svg)](https://github.com/Nemezjusz/ReadmeTranslator/blob/main/readme/README.French.md) [![tedesco](https://img.shields.io/badge/lang-tedesco-red.svg)](https://github.com/Nemezjusz/ReadmeTranslator/blob/main/readme/README.German.md) [![polacco](https://img.shields.io/badge/lang-polacco-red.svg)](https://github.com/Nemezjusz/ReadmeTranslator/blob/main/readme/README.Polish.md) [![spagnolo](https://img.shields.io/badge/lang-spagnolo-red.svg)](https://github.com/Nemezjusz/ReadmeTranslator/blob/main/readme/README.Spanish.md)


TraduciMe è un semplice programma Python che utilizza il modello GPT-3.5-turbo di OpenAI per tradurre automaticamente il testo in un repository di GitHub. Questo programma consente agli utenti di tradurre il contenuto di un file specificato nel loro repository di GitHub in una lingua scelta.

## Descrizione

Il programma TraduciMe è composto da due funzionalità principali:

1. **Traduzione utilizzando il modello GPT-3.5-turbo di OpenAI:**
   - Il programma utilizza il modello GPT-3.5-turbo di OpenAI per eseguire la traduzione del testo.
   - Gli utenti possono specificare il nome utente di GitHub, il nome del repository, il ramo, il percorso del file e la lingua di destinazione.
   - Il contenuto tradotto viene quindi caricato nuovamente nel repository di GitHub specificato.

2. **Interfaccia utente grafica (GUI):**
   - Il programma include una semplice GUI creata utilizzando la libreria customtkinter.
   - Gli utenti possono inserire le proprie credenziali di GitHub, i dettagli del repository e le preferenze di traduzione utilizzando la GUI.
   - Cliccando il pulsante "Traduci", il programma avvia il processo di traduzione.

## GUI
![Zrzut ekranu 2024-02-01 194536](https://github.com/Nemezjusz/ReadmeTranslator/assets/50834734/ef77cbf9-fece-46bc-bc59-a8e56f96eced)

## Utilizzo

Per utilizzare TraduciMe, seguire questi passaggi:

1. Avviare il programma eseguendo lo script Python fornito.
2. Compilare le informazioni richieste nella GUI:
   - Nome utente: Il proprio nome utente di GitHub.
   - Nome repo: Il nome del proprio repository di GitHub.
   - Ramo: Il ramo in cui si trova il file (impostato per default su 'main').
   - Percorso file: Il percorso del file da tradurre (impostato per default su 'README.md').
   - Lingua: Scegliere la lingua di destinazione per la traduzione dal menu a tendina.
   - API OpenAI: Fornire la propria chiave API di OpenAI GPT-3.5-turbo.
   - API GitHub: Fornire la propria chiave API di GitHub (facoltativo se il repository è pubblico o non richiede l'autenticazione).
3. Cliccare il pulsante "Traduci" per avviare il processo di traduzione.
4. Il contenuto tradotto verrà caricato nel repository di GitHub specificato.

## Nota

- Assicurarsi di avere chiavi API valide di OpenAI e GitHub per l'autenticazione.
- Il file tradotto verrà salvato nella directory 'readme' con un nome come 'README.{lingua}.md'.

Sentiti libero di personalizzare il programma e esplorare funzionalità aggiuntive in base alle tue esigenze.

> [!CAUTION]
> Esercitare sempre cautela nell'uso delle chiavi API e evitare di condividerle pubblicamente.