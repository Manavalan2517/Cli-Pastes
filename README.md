# CLI - Paste



https://github.com/Manavalan2517/Cli-Pastes/assets/112639423/92b48edd-201c-415b-a7a0-195db9281a30



> ` It is Inspired from ( https://github.com/codemyst/pastemyst )`

# A simple Python script to create and manage text pastes.

## Introduction
This script allows users to create, view, and manage text pastes. It provides a simple command-line interface for creating new pastes and viewing existing ones.

### Commands Used:

- `create`: Create a new paste.
- `view`: View an existing paste.
- `exit`: Exit the script.


## Modules Used:
The script imports several modules including 
1. `json` -----------> `for parsing and generating JSON data`
2. `platform` ------> `to access underlying platform’s identifying data`
3. `os` --------------> `for a portable way of using operating system dependent functionality`
4. `rich.console`-> `enables rich text and beautiful formatting in the terminal`
5. `rich.syntax`--> `allows syntax highlighting of code snippets`
6. `questionary`--> `for creating interactive prompts and questionnaires`
7. `pyperclip`----> `access to the clipboard for copying and pasting`
8. `random`-------> `used for generating random numbers and selecting random elements`
9. `string`-------> `provides a collection of string constants, useful for generating random strings`

## Working
1. The script checks if a `JSON` file named 'UserData.json' exists. 
>
2. If it doesn't exist, it creates a new one and stores the user's operating system information in it. 
>
3. The script also defines a function 'update_json' that updates the user's data in a JSON file named 'data.json'.
>
4. The script then enters a while loop that prompts the user to select an action: create, view, or exit. 
>
5. If the user selects 'create', the script prompts for confirmation, paste name, and checks the user's operating system. 
>
6. If the operating system is Windows, it creates an empty text file, opens it with notepad, reads the entered data, and stores it in a variable 'pdData'. 
>
7. The script then generates a unique ID and checks if it already exists in the 'data.json' file. 
>
8. If it doesn't exist, it updates the JSON file with the paste name, ID, and data, and removes the temporary text file.
>
9.  If the user selects 'view', the script prompts for an ID and checks if it exists in the 'data.json' file. 
>
10. If it exists, it prints the paste content using the rich.syntax module, prompts the user to copy the content to the clipboard, and copies it if requested.
>
11. If the user selects 'exit', the script breaks out of the while loop and terminates.
>
12. If an unknown command is entered, the script prints a message to try again.
