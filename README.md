# ReadmeTranslator 


TranslateMe is a simple Python program that utilizes OpenAI's GPT-3.5-turbo model to automatically translate text in a GitHub repository. This program allows users to translate the content of a specified file in their GitHub repository into a chosen language.

## Description

The TranslateMe program consists of two main functionalities:

1. **Translation using OpenAI's GPT-3.5-turbo:**
   - The program uses the OpenAI GPT-3.5-turbo model to perform text translation.
   - Users can specify the GitHub username, repository name, branch, file path, and target language.
   - The translated content is then uploaded back to the specified GitHub repository.

2. **Graphical User Interface (GUI):**
   - The program includes a simple GUI built using the customtkinter library.
   - Users can input their GitHub credentials, repository details, and translation preferences using the GUI.
   - Upon clicking the "Translate" button, the program initiates the translation process.

## GUI
![Zrzut ekranu 2024-02-01 194536](https://github.com/Nemezjusz/ReadmeTranslator/assets/50834734/ef77cbf9-fece-46bc-bc59-a8e56f96eced)

## Usage

To use TranslateMe, follow these steps:

1. Launch the program by running the provided Python script.
2. Fill in the required information in the GUI:
   - Username: Your GitHub username.
   - Repo Name: The name of your GitHub repository.
   - Branch: The branch in which the file is located (default is set to 'main').
   - File Path: The path to the file you want to translate (default is set to 'README.md').
   - Language: Choose the target language for translation from the dropdown menu.
   - OpenAI API: Provide your OpenAI GPT-3.5-turbo API key.
   - GitHub API: Provide your GitHub API key (optional if the repository is public or doesn't require authentication).
3. Click the "Translate" button to start the translation process.
4. The translated content will be uploaded to the specified GitHub repository.

## Note

- Ensure that you have valid OpenAI API and GitHub API keys for authentication.
- The translated file will be saved in the 'readme' directory with a filename like 'README.{language}.md'.

Feel free to customize the program and explore additional features based on your requirements.

> [!CAUTION]
> Always exercise caution when handling API keys and avoid sharing them publicly.




