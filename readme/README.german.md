# ReadmeTranslator 

> Sprache auswählen: 
>
> [![french](https://img.shields.io/badge/lang-französisch-red.svg)](https://github.com/Nemezjusz/ReadmeTranslator/blob/main/readme/README.french.md) [![polish](https://img.shields.io/badge/lang-polnisch-red.svg)](https://github.com/Nemezjusz/ReadmeTranslator/blob/main/readme/README.polish.md) [![spanish](https://img.shields.io/badge/lang-spanisch-red.svg)](https://github.com/Nemezjusz/ReadmeTranslator/blob/main/readme/README.spanish.md) 


TranslateMe ist ein einfaches Python-Programm, das das GPT-3.5-turbo-Modell von OpenAI verwendet, um Text automatisch in einem GitHub-Repository zu übersetzen. Dieses Programm ermöglicht es Benutzern, den Inhalt einer angegebenen Datei in ihrem GitHub-Repository in eine ausgewählte Sprache zu übersetzen.

## Beschreibung

Das TranslateMe-Programm besteht aus zwei Hauptfunktionen:

1. **Übersetzung mit OpenAI's GPT-3.5-turbo:**
   - Das Programm verwendet das OpenAI GPT-3.5-turbo-Modell zur Durchführung von Textübersetzungen.
   - Benutzer können den GitHub-Benutzernamen, den Repository-Namen, den Branch, den Dateipfad und die Zielsprache angeben.
   - Der übersetzte Inhalt wird dann zurück in das angegebene GitHub-Repository hochgeladen.

2. **Grafische Benutzeroberfläche (GUI):**
   - Das Programm enthält eine einfache GUI, die mit der Bibliothek customtkinter erstellt wurde.
   - Benutzer können ihre GitHub-Anmeldeinformationen, Repository-Details und Übersetzungseinstellungen über die GUI eingeben.
   - Nach dem Klicken auf die Schaltfläche "Übersetzen" startet das Programm den Übersetzungsprozess.

## GUI
![Zrzut ekranu 2024-02-01 194536](https://github.com/Nemezjusz/ReadmeTranslator/assets/50834734/ef77cbf9-fece-46bc-bc59-a8e56f96eced)

## Verwendung

Um TranslateMe zu verwenden, befolgen Sie diese Schritte:

1. Starten Sie das Programm, indem Sie das bereitgestellte Python-Skript ausführen.
2. Füllen Sie die erforderlichen Informationen in der GUI aus:
   - Benutzername: Ihr GitHub-Benutzername.
   - Repo-Name: Der Name Ihres GitHub-Repositorys.
   - Branch: Der Branch, in dem sich die Datei befindet (standardmäßig auf 'main' eingestellt).
   - Dateipfad: Der Pfad zur Datei, die Sie übersetzen möchten (standardmäßig auf 'README.md' eingestellt).
   - Sprache: Wählen Sie die Zielsprache für die Übersetzung aus dem Dropdown-Menü aus.
   - OpenAI-API: Geben Sie Ihren OpenAI GPT-3.5-turbo-API-Schlüssel ein.
   - GitHub-API: Geben Sie Ihren GitHub-API-Schlüssel ein (optional, wenn das Repository öffentlich ist oder keine Authentifizierung erfordert).
3. Klicken Sie auf die Schaltfläche "Übersetzen", um den Übersetzungsprozess zu starten.
4. Der übersetzte Inhalt wird in das angegebene GitHub-Repository hochgeladen.

## Hinweis

- Stellen Sie sicher, dass Sie gültige OpenAI-API- und GitHub-API-Schlüssel für die Authentifizierung haben.
- Die übersetzte Datei wird im 'readme'-Verzeichnis mit einem Dateinamen wie 'README.{Sprache}.md' gespeichert.

Fühlen Sie sich frei, das Programm anzupassen und zusätzliche Funktionen entsprechend Ihren Anforderungen zu erkunden.

> [!ACHTUNG]
> Gehen Sie beim Umgang mit API-Schlüsseln immer vorsichtig vor und vermeiden Sie es, sie öffentlich zu teilen.