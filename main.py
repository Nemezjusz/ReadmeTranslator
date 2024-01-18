import requests
from requests.auth import HTTPBasicAuth
import base64
from API import TOKEN_GIT, TOKEN_OPENAI
from openai import OpenAI

client = OpenAI(api_key=TOKEN_OPENAI)
token = TOKEN_GIT

def translate(readme, language):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a translator"},
            {"role": "user", "content": f"Translate text to {language}, rest leave the same: {readme}"}
        ]
    )
    return completion.choices[0].message.content
def upload_to_github(username, repo_name, file_path, file_content, branch, token=TOKEN_GIT):
    # Set the GitHub API endpoint
    url = f"https://api.github.com/repos/{username}/{repo_name}/contents/{file_path}"

    # Encode the file content to base64
    encoded_content = base64.b64encode(file_content.encode()).decode()

    # Prepare the request payload
    payload = {
        "message": "Upload file",
        "content": encoded_content,
        "branch": branch
    }

    # If a token is provided, use it for authentication
    if token:
        headers = {"Authorization": f"token {token}"}
    else:
        # If no token is provided, you can use a username and password
        auth = HTTPBasicAuth(username, input("Enter your GitHub password: "))
        headers = {}

    # Make the request to upload the file
    response = requests.put(url, json=payload, headers=headers, auth=auth if not token else None)

def get_github_file_content(username, repo_name, file_path, branch, token=TOKEN_GIT):
    # Set the GitHub API endpoint
    url = f"https://api.github.com/repos/{username}/{repo_name}/contents/{file_path}?ref={branch}"

    # If a token is provided, use it for authentication
    if token:
        headers = {"Authorization": f"token {token}"}
    else:
        # If no token is provided, you can make unauthenticated requests, but this may be rate-limited
        headers = {}

    # Make the request to get the file content
    response = requests.get(url, headers=headers)

    # Check the response status
    if response.status_code == 200:
        content = response.json().get("content")
        # Decode the base64-encoded content
        decoded_content = base64.b64decode(content).decode("utf-8")
        return decoded_content
    else:
        print(f"Failed to fetch file content. Status code: {response.status_code}")
        print(response.text)
        return None


username = "Nemezjusz"
repo_name = "Chat-P2P"
file_path = "README.md"
branch = "master"
language = "english"

file_content = get_github_file_content(username, repo_name, file_path, branch)

file_content = translate(file_content, language)

file_path = "README.en.md"

upload_to_github(username, repo_name, file_path, file_content, branch)


