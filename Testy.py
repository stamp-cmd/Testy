import random
import os

list = []

print("******-----------------------******")
print("*-----|         Testy       |-----*")
print("******-----------------------******")
print("          List Playground          ")

print("Commands:")
print(" \Add to Add object in list")
print(" \Remove to Remove object in list")
print(" \Reset to Reset list")
print(" \Help to Show Command")
print(" \Show to Show list")
print(" \Quit to Quit Program")
print(" \Clear to clear terminal")
print(" \Detect to count Element is list")

while True:
    Command = input(">>> ")
    if Command == "\Add":
        print(list)
        Aobject = input("Object to Add: ")
        list.insert(0, Aobject)
        print("Added Successfully")
    elif Command == "\Remove":
        print(list)
        Robject = input("Object to remove: ")
        try:
            list.remove(Robject)
            print("Remove Successfully")
        except ValueError:
            print("Warning: Does not found: " + Robject)
    elif Command == "\Reset":
        list.clear()
        print("Reset Successfully")
    elif Command == "\Rand":
        Tries = input("Times: ")
        if Tries.isnumeric():
            Tries = int(Tries)
            if Tries > 1000:
                print("Warning: Value Overload")
            else:
                Dpattern = ""
                try:
                    for i in range(Tries):
                        Dpattern = Dpattern + random.choice(list)
                        Rpattern = ""
                        Rpattern = random.choice(list)
                        print("Attempt " + str(i) + ": " + Rpattern)
                except ValueError:
                    print("Warning: List Empty")
        else:
            print("Warning: Not a number")
    elif Command == "\Detect":
        Dobject = input("Object to Detect: ")
        print("Detect: " + str(Dpattern.count(Dobject)))
    elif Command == "\Clear":
        os.system("cls||clear")
    elif Command == "\Show":
        print(list)
    elif Command == "\Quit":
        quit()
    elif Command == "\Help":
        print("Commands:")
        print(" \Add to Add object in list")
        print(" \Remove to Remove object in list")
        print(" \Reset to Reset list")
        print(" \Help to Show Command")
        print(" \Show to Show list")
        print(" \Quit to Quit Program")
        print(" \Clear to clear terminal")
        print(" \Detect to count Element is list")
    else:
        print("Warning: Command not found")
