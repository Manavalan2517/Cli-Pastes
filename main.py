import json  
import platform
import os  
from rich.console import Console  
from rich.syntax import Syntax  
import questionary  
import pyperclip  
import random  
import string 

idCreate = False
console = Console()

try:
    # Check JSON File Exist or not
    uf = open("UserData.json", "r+")
    ufData = json.load(uf)
    uf.close()
except:
    
    # If not exist create a new one
    create = open("UserData.json", "x")
    create.close()
    uf = open("UserData.json", "w")
    osdata = {"OS": platform.system()}
    json.dump(osdata, uf, indent=3)
    uf.close()

    # Storing user data in a variable
    uf = open("UserData.json", "r")
    ufData = json.load(uf)
    uf.close()

# Update user data
def update_json(_name, _id, _paste):
    f1 = open("data.json", "r+")
    fdata = json.load(f1)
    data = {_id: {"name": _name, "paste": _paste}}
    fdata["pastes"].update(data)
    f2 = open("data.json", "w")
    json.dump(fdata, f2, indent=4)
    f2.close()

print(
    """

              $$\ $$\                                         $$\               
              $$ |\__|                                        $$ |              
     $$$$$$$\ $$ |$$\          $$$$$$\   $$$$$$\   $$$$$$$\ $$$$$$\    $$$$$$\  
    $$  _____|$$ |$$ |$$$$$$\ $$  __$$\  \____$$\ $$  _____|\_$$  _|  $$  __$$\ 
    $$ /      $$ |$$ |\______|$$ /  $$ | $$$$$$$ |\$$$$$$\    $$ |    $$$$$$$$ |
    $$ |      $$ |$$ |        $$ |  $$ |$$  __$$ | \____$$\   $$ |$$\ $$   ____|
    \$$$$$$$\ $$ |$$ |        $$$$$$$  |\$$$$$$$ |$$$$$$$  |  \$$$$  |\$$$$$$$\ 
     \_______|\__|\__|        $$  ____/  \_______|\_______/    \____/  \_______|
                              $$ |                                              
                              $$ |                                              
                              \__|                                              
                                                                           """
)

while True:
    osname = ufData
    
    cmd = questionary.select(
        "What do you want to do?",
        choices=["create", "view", "exit"],
    ).ask()

    match cmd:
        case "create" | "C":

            confirm = questionary.confirm("Are you sure?").ask()
            name = questionary.text("Paste name").ask()
            
            # Checking User's OS
            if ufData["OS"] == "Windows":
                txtfile = 'notepad'
            if ufData["OS"] == "Linux":
                txtfile = 'gedit'
                
            txtfile = 'notepad'
            pd = open("paste-" + name + ".txt", "x") # Create an empty text file
            pd.close()
            file = f"{txtfile} paste-" + name + ".txt"
            os.system(file) # Open Notepad
            pd = open("paste-" + name + ".txt", "r") # Read the Entered Data in the text file
            pdData = pd.read()
            pd.close()

            idCreate = True

            # Create a unique id to access user's data
            while idCreate:
                letters = string.ascii_letters
                randomchoice = random.choices(letters, k=5)
                id = "".join(randomchoice)
                f1 = open("data.json", "r")
                fdata = json.load(f1)

                # Checks if unique id already exists in the 'data.json'
                if id not in fdata["pastes"]:
                    print("Created a new paste!\nID(Share id to others to view your content) -> " + id)
                    update_json(name, id, pdData)
                    idCreate = False
                    os.remove("paste-" + name + ".txt") # removes the temporary text file.
                else:
                    break

        case "view" | "V":
            vID = questionary.text("Enter ID:").ask() 
            vf = open("data.json", "r")
            vfData = json.load(vf)
            for i in vfData["pastes"]:
            
                if i == vID:  # Checks if Unique id exists in the 'data.json' file.
                    print("\n")
                    printPaste = Syntax(
                        vfData["pastes"][i]["paste"], "python", theme="ansi_dark" # prints the paste content
                    )
                    console.print(printPaste)
                    print("\n")

                    copy = questionary.select(  # prompts the user to copy the content to the clipboard
                        "Copy to clipboard?",
                        choices=["Yes", "No"],
                    ).ask()

                    if copy == "Yes":
                        pyperclip.copy(vfData["pastes"][i]["paste"]) # copy the content to the clipboard
                    else:
                        break

        case "exit": # breaks out of the while loop
            break
        case _:
            print("Unknown command try again.")