# ReadmeTranslator 

> Elige idioma: 
>
> [![polish](https://img.shields.io/badge/lang-polish-red.svg)](https://github.com/Nemezjusz/ReadmeTranslator/blob/main/readme/README.polish.md) 


TranslateMe es un programa simple en Python que utiliza el modelo GPT-3.5-turbo de OpenAI para traducir automáticamente texto en un repositorio de GitHub. Este programa permite a los usuarios traducir el contenido de un archivo especificado en su repositorio de GitHub a un idioma elegido.

## Descripción

El programa TranslateMe consta de dos funcionalidades principales:

1. **Traducción utilizando el modelo GPT-3.5-turbo de OpenAI:**
   - El programa utiliza el modelo GPT-3.5-turbo de OpenAI para realizar traducciones de texto.
   - Los usuarios pueden especificar el nombre de usuario de GitHub, el nombre del repositorio, la rama, la ruta del archivo y el idioma de destino.
   - El contenido traducido se sube de nuevo al repositorio de GitHub especificado.

2. **Interfaz de usuario gráfica (GUI):**
   - El programa incluye una interfaz gráfica simple construida con la biblioteca customtkinter.
   - Los usuarios pueden ingresar sus credenciales de GitHub, detalles del repositorio y preferencias de traducción utilizando la GUI.
   - Al hacer clic en el botón "Traducir", el programa inicia el proceso de traducción.

## GUI
![Zrzut ekranu 2024-02-01 194536](https://github.com/Nemezjusz/ReadmeTranslator/assets/50834734/ef77cbf9-fece-46bc-bc59-a8e56f96eced)

## Uso

Para usar TranslateMe, siga estos pasos:

1. Ejecute el programa ejecutando el script de Python proporcionado.
2. Complete la información requerida en la GUI:
   - Usuario: tu nombre de usuario de GitHub.
   - Nombre del Repositorio: el nombre de tu repositorio de GitHub.
   - Rama: la rama en la que se encuentra el archivo (por defecto está configurada en 'main').
   - Ruta del Archivo: la ruta del archivo que deseas traducir (por defecto está configurada en 'README.md').
   - Idioma: elige el idioma de destino para la traducción desde el menú desplegable.
   - OpenAI API: proporciona tu clave de API de OpenAI GPT-3.5-turbo.
   - GitHub API: proporciona tu clave de API de GitHub (opcional si el repositorio es público o no requiere autenticación).
3. Haz clic en el botón "Traducir" para iniciar el proceso de traducción.
4. El contenido traducido se subirá al repositorio de GitHub especificado.

## Nota

- Asegúrate de tener claves de API válidas de OpenAI y GitHub para la autenticación.
- El archivo traducido se guardará en el directorio 'readme' con un nombre de archivo como 'README.{idioma}.md'.

Siéntete libre de personalizar el programa y explorar características adicionales según tus necesidades.

> [!CAUTION]
> Siempre ten cuidado al manejar claves de API y evita compartirlas públicamente.