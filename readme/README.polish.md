# ReadmeTranslator 


TranslateMe to prosty program w języku Python, który wykorzystuje model GPT-3.5-turbo firmy OpenAI do automatycznego tłumaczenia tekstu w repozytorium GitHub. Ten program umożliwia użytkownikom przetłumaczenie zawartości określonego pliku w ich repozytorium GitHub na wybrany język.

## Opis

Program TranslateMe składa się z dwóch głównych funkcjonalności:

1. **Tłumaczenie za pomocą modelu GPT-3.5-turbo firmy OpenAI:**
   - Program używa modelu OpenAI GPT-3.5-turbo do wykonywania tłumaczeń tekstowych.
   - Użytkownicy mogą podać nazwę użytkownika GitHub, nazwę repozytorium, gałąź, ścieżkę pliku i docelowy język.
   - Przetłumaczona zawartość jest następnie przesyłana z powrotem do określonego repozytorium GitHub.

2. **Interfejs graficzny (GUI):**
   - Program zawiera prosty interfejs graficzny zbudowany przy użyciu biblioteki customtkinter.
   - Użytkownicy mogą wprowadzać swoje dane uwierzytelniające GitHub, szczegóły repozytorium i preferencje tłumaczenia za pomocą interfejsu GUI.
   - Po kliknięciu przycisku "Translate" program rozpoczyna proces tłumaczenia.

## GUI
![Zrzut ekranu 2024-02-01 194536](https://github.com/Nemezjusz/ReadmeTranslator/assets/50834734/ef77cbf9-fece-46bc-bc59-a8e56f96eced)

## Użycie

Aby korzystać z programu TranslateMe, wykonaj następujące kroki:

1. Uruchom program, uruchamiając dostarczony skrypt Python.
2. Wypełnij wymagane informacje w interfejsie GUI:
   - Nazwa użytkownika: Twój użytkownik GitHub.
   - Nazwa repozytorium: Nazwa Twojego repozytorium GitHub.
   - Gałąź: Gałąź, w której znajduje się plik (domyślnie ustawiona na "main").
   - Ścieżka pliku: Ścieżka do pliku, który chcesz przetłumaczyć (domyślnie ustawiona na "README.md").
   - Język: Wybierz docelowy język tłumaczenia z menu rozwijanego.
   - OpenAI API: Podaj klucz API OpenAI GPT-3.5-turbo.
   - GitHub API: Podaj klucz API GitHub (opcjonalnie, jeśli repozytorium jest publiczne lub nie wymaga uwierzytelnienia).
3. Kliknij przycisk "Translate", aby rozpocząć proces tłumaczenia.
4. Przetłumaczona zawartość zostanie przesłana do określonego repozytorium GitHub.

## Uwaga

- Upewnij się, że masz ważne klucze API OpenAI i GitHub do uwierzytelniania.
- Przetłumaczony plik zostanie zapisany w katalogu 'readme' pod nazwą pliku 'README.{język}.md'.

Modyfikuj program według własnych potrzeb i eksploruj dodatkowe funkcje.

> [!OSTRZEŻENIE]
> Zawsze postępuj ostrożnie przy obsłudze kluczy API i unikaj ich udostępniania publicznie.