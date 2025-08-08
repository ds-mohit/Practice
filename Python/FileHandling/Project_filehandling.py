from pathlib import Path

# This is the base path where the script is located
BASE_PATH = Path(__file__).parent

def readfileandfolder():
    path = BASE_PATH
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")

def createfile():
    try:
        readfileandfolder()
        name = input("Please enter your file name: ")
        p = BASE_PATH / name

        if not p.exists():
            with open(p, 'w') as fs:
                data = input("What do you want to write in this file: ")
                fs.write(data)
            print("File created successfully")
        else:
            print("File already exists")
    except Exception as e:
        print(f"An error occurred: {e}")

def readfile():
    try:
        readfileandfolder()
        name = input("Which file do you want to read: ")
        p = BASE_PATH / name

        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)
            print("File read successfully")
        else:
            print("File does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")

def updatefile():
    try:
        readfileandfolder()
        name = input("Which file do you want to update: ")
        p = BASE_PATH / name

        if p.exists() and p.is_file():
            print("Press 1 to change the name of the file")
            print("Press 2 to overwrite the data in the file")
            print("Press 3 to append data to the file")

            res = int(input("Please enter your choice: "))

            if res == 1:
                name2 = input("Enter your new file name: ")
                p2 = BASE_PATH / name2
                p.rename(p2)
                print("File name updated successfully")

            elif res == 2:
                with open(p, 'w') as fs:
                    data = input("Enter new data to write into the file: ")
                    fs.write(data)
                print("File updated successfully")

            elif res == 3:
                with open(p, 'a') as fs:
                    data = input("Enter data to append into the file: ")
                    fs.write(" " + data)
                print("Data appended successfully")

            else:
                print("Invalid option selected.")
        else:
            print("File does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")

def deletefile():
    try:
        readfileandfolder()
        name = input("Which file do you want to delete: ")
        p = BASE_PATH / name

        if p.exists() and p.is_file():
            p.unlink()
            print("File deleted successfully")
        else:
            print("File does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main menu
print("Press 1 to create a file")
print("Press 2 to read a file")
print("Press 3 to update a file")
print("Press 4 to delete a file")

try:
    check = int(input("Please enter your choice: "))

    if check == 1:
        createfile()
    elif check == 2:
        readfile()
    elif check == 3:
        updatefile()
    elif check == 4:
        deletefile()
    else:
        print("Invalid option selected.")

except ValueError:
    print("Please enter a valid number.")
