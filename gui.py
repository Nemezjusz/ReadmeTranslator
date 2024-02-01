
import customtkinter
from translate import execute

def start_function():
    # Retrieve values from the text boxes
    username = username_entry.get()
    repo_name = repo_name_entry.get()
    branch = branch_entry.get()
    file_path = file_path_entry.get()
    language = language_entry.get()
    openai_api_key = openai_api_entry.get()
    github_api_key = github_api_entry.get()

    # Perform the desired action with the retrieved values
    execute(username, repo_name, file_path, branch, language, openai_api_key, github_api_key)
    print("Done!")

# Create the main window

#make window not resizable
window = customtkinter.CTk()
window.title("TranslateMe")
window.configure(bg="#333333")  # Set background color
window.resizable(False, False)

# Create the text box labels
username_label = customtkinter.CTkLabel(master=window, text="Username")
repo_name_label = customtkinter.CTkLabel(master=window, text="Repo Name")
branch_label = customtkinter.CTkLabel(master=window, text="Branch")
file_path_label = customtkinter.CTkLabel(master=window, text="File Path")
language_label = customtkinter.CTkLabel(master=window, text="Language")
openai_api_label = customtkinter.CTkLabel(master=window, text="OpenAI API")
github_api_label = customtkinter.CTkLabel(master=window, text="GitHub API")


# Create the text boxes
username_entry = customtkinter.CTkEntry(master=window)
repo_name_entry = customtkinter.CTkEntry(master=window)
branch_entry = customtkinter.CTkEntry(master=window, textvariable = customtkinter.StringVar(value="main"))
file_path_entry = customtkinter.CTkEntry(master=window, textvariable = customtkinter.StringVar(value="README.md"))
#language_entry = customtkinter.CTkEntry(master=window)

combobox_var = customtkinter.StringVar(value="English")  # set initial value
def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)
language_entry = customtkinter.CTkComboBox(master=window,
                                     values=["English","Polish" ,"Spanish", "French", "German", "Italian"],
                                     command=combobox_callback,
                                     variable=combobox_var)

openai_api_entry = customtkinter.CTkEntry(master=window, show="*")
github_api_entry = customtkinter.CTkEntry(master=window, show="*")

# Create the start button
start_button = customtkinter.CTkButton(master=window, text="Translate", command=start_function)

# Place the elements in the window using a grid layout
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry.grid(row=0, column=1, padx=10, pady=10)
repo_name_label.grid(row=1, column=0, padx=10, pady=10)
repo_name_entry.grid(row=1, column=1, padx=10, pady=10)
branch_label.grid(row=2, column=0, padx=10, pady=10)
branch_entry.grid(row=2, column=1, padx=10, pady=10)
file_path_label.grid(row=3, column=0, padx=10, pady=10)
file_path_entry.grid(row=3, column=1, padx=10, pady=10)
language_label.grid(row=4, column=0, padx=10, pady=10)
language_entry.grid(row=4, column=1, padx=10, pady=10)
openai_api_label.grid(row=5, column=0, padx=10, pady=10)
openai_api_entry.grid(row=5, column=1, padx=10, pady=10)
github_api_label.grid(row=6, column=0, padx=10, pady=10)
github_api_entry.grid(row=6, column=1, padx=10, pady=10)
start_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()