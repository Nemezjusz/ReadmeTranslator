> Wybierz język:
> 
> [![pl](https://img.shields.io/badge/lang-polski-red.svg)](https://github.com/Nemezjusz/ReadmeTranslator/blob/main/readme/README.Polish.md) [![es](https://img.shields.io/badge/lang-espanol-orange.svg)]() [![de](https://img.shields.io/badge/lang-deutsch-yellow.svg)]() [![fr](https://img.shields.io/badge/lang-français-blue.svg)]()
[![it](https://img.shields.io/badge/lang-italiano-grren.svg)]()


TranslateMe to prosty program napisany w języku Python, który wykorzystuje model OpenAI GPT-3.5-turbo do automatycznego tłumaczenia tekstu w repozytorium GitHub. Ten program pozwala użytkownikom przetłumaczyć zawartość określonego pliku w repozytorium GitHub na wybrany język.

## Opis

Program TranslateMe składa się z dwóch głównych funkcji:

1. **Tłumaczenie za pomocą modelu OpenAI GPT-3.5-turbo:**
   - Program wykorzystuje model OpenAI GPT-3.5-turbo do przeprowadzania tłumaczenia tekstu.
   - Użytkownicy mogą podać nazwę użytkownika GitHub, nazwę repozytorium, gałąź, ścieżkę do pliku i język docelowy.
   - Przetłumaczona zawartość jest następnie wysyłana z powrotem do określonego repozytorium GitHub.

2. **Interfejs graficzny (GUI):**
   - Program zawiera prosty interfejs graficzny zbudowany przy użyciu biblioteki customtkinter.
   - Użytkownicy mogą wprowadzać swoje dane uwierzytelniające do GitHub, szczegóły repozytorium i preferencje tłumaczenia przy użyciu interfejsu graficznego.
   - Po kliknięciu przycisku "Translate" program rozpoczyna proces tłumaczenia.

## GUI
![Zrzut ekranu 2024-02-01 194536](https://github.com/Nemezjusz/ReadmeTranslator/assets/50834734/ef77cbf9-fece-46bc-bc59-a8e56f96eced)

## Użycie

Aby korzystać z programu TranslateMe, wykonaj następujące kroki:

1. Uruchom program, uruchamiając dostarczony skrypt Python.
2. Wypełnij wymagane informacje w interfejsie graficznym:
   - Nazwa użytkownika: Twoja nazwa użytkownika GitHub.
   - Nazwa repozytorium: Nazwa Twojego repozytorium GitHub.
   - Gałąź: Gałąź, w której znajduje się plik (domyślnie ustawiona na "main").
   - Ścieżka pliku: Ścieżka do pliku, który chcesz przetłumaczyć (domyślnie ustawiona na "README.md").
   - Język: Wybierz język docelowy tłumaczenia z listy rozwijanej.
   - Klucz API OpenAI: Podaj swój klucz API do OpenAI GPT-3.5-turbo.
   - Klucz API GitHub: Podaj swój klucz API do GitHub (opcjonalne, jeśli repozytorium jest publiczne lub nie wymaga uwierzytelnienia).
3. Kliknij przycisk "Translate", aby rozpocząć proces tłumaczenia.
4. Przetłumaczona zawartość zostanie wysłana do określonego repozytorium GitHub.

## Uwaga

- Upewnij się, że masz poprawne klucze API OpenAI i GitHub do uwierzytelniania.
- Przetłumaczony plik zostanie zapisany w katalogu "readme" pod nazwą pliku "README.{język}.md".

Swobodnie dostosuj program i eksploruj dodatkowe funkcje zgodnie z Twoimi wymaganiami.

> [!CAUTION]
> Zawsze zachowuj ostrożność podczas obsługi kluczy API i unikaj ich udostępniania publicznie.