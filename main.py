import csv
from datetime import datetime

def GetID():
    sID = ""
    id = -1
    while id == -1:
        while sID == "":
            sID = input("Enter id: ")
        id = int(sID)

        with open('tasks.csv', "r") as reader:
            line = reader.readline()
            while (line != ""):
                if id == int(line.split(';')[0]):
                    return id
                line = reader.readline()
        id = -1
        sID = ""
    return id
    
def GetNow():
    now = datetime.now()
    return now.strftime('%H:%M:%S %d.%m.%Y')

def GenerateID():
    id = 0
    with open('tasks.csv', "r") as reader:
        line = reader.readline()
        while (line != ""):
            id = int(line.split(';')[0])
            line = reader.readline()
    return id + 1

def AddNote():
    name = ""
    while name == "":
        name = input("Enter name: ")
    desc = ""
    while desc == "":
        desc = input("Enter description: ")
    id = GenerateID()

    nowFormated = GetNow()
    
    with open('tasks.csv', "a") as csv_file:
        csv_file.write(str(id)
        + ";" + name
        + ";" + desc
        + ";" + nowFormated
        + ";" + nowFormated
        + "\n")
    
    print("Note is added!")

def EditNote(id):
    task = ""
    desc = ""
    create = ""
    edit = ""
    with open('tasks.csv', "r") as reader:
        line = reader.readline()
        while (line != ""):
            if id == int(line.split(';')[0]):
                task = line.split(';')[1]
                desc = line.split(';')[2]
                create = line.split(';')[3]
                edit = line.split(';')[4]
                break
            line = reader.readline()
    
    newtask = input("Enter new task name (old: " + task + "): ") or task
    newdesc = input("Enter new description (old: " + desc + "): ") or desc

    f = open('tasks.csv', "r")
    data = f.read()
    f.close()

    newdata = data.replace(
        str(id) + ";"+ task + ";" + desc + ";" + create + ";" + edit,
        str(id) + ";"+ newtask + ";" + newdesc + ";" + create + ";" + GetNow() + "\n")
    f = open('tasks.csv', "w")
    f.write(newdata)
    f.close()

    print("Note #" + str(id) + " was edited!")
    
def DeleteNote(id):
    with open('tasks.csv', "r") as reader:
        line = reader.readline()
        while (line != ""):
            if id == int(line.split(';')[0]):
                break
            line = reader.readline()
    

    f = open('tasks.csv', "r")
    data = f.read()
    f.close()

    newdata = data.replace(line, "")
    f = open('tasks.csv', "w")
    f.write(newdata)
    f.close()
    
    print("Note #" + str(id) + " was deleted!")

def PrintNote(id):
    task = ""
    desc = ""
    create = ""
    edit = ""
    with open('tasks.csv', "r") as reader:
        line = reader.readline()
        while (line != ""):
            if id == int(line.split(';')[0]):
                task = line.split(';')[1]
                desc = line.split(';')[2]
                create = line.split(';')[3]
                edit = line.split(';')[4].split('\n')[0]
                break
            line = reader.readline()
    print("")
    print("Note #" + str(id) + ": " + task)
    print("Created: " + create)
    print("Edited: " + edit)
    print("Description: " + desc)
    print("")
    
def PrintNotes():
    task = ""
    desc = ""
    create = ""
    edit = ""
    with open('tasks.csv', "r") as reader:
        line = reader.readline()
        while (line != ""):
            id = int(line.split(';')[0])
            task = line.split(';')[1]
            desc = line.split(';')[2]
            create = line.split(';')[3]
            edit = line.split(';')[4].split('\n')[0]

            print("")
            print("Note #" + str(id) + ": " + task)
            print("Created: " + create)
            print("Edited: " + edit)
            print("Description: " + desc)

            line = reader.readline()
        print("")

loop = bool(True)
while (loop):
    print("""Command keys:
    Add note
    Edit note (id)
    Delete note (id)
    Print note (id)
    Print all
    Exit""")

    question = "Enter command: "
    query = input(question)

    if (query == "Add note"):
        AddNote()
    elif(query == "Edit note"):
        id = GetID()
        EditNote(id)
    elif(query == "Delete note"):
        id = GetID()
        DeleteNote(id)
    elif(query == "Print note"):
        id = GetID()
        PrintNote(id)
    elif(query == "Print all"):
        PrintNotes()

    elif (query == "Exit"):
        loop = False
        print("Exit program")
    else:
        print("Incorrect input, try again")