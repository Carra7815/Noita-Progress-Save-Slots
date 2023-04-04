import os

def func():
  selection = int()
  if selection == 0:
    os.rename("../save00.py", "Save_Slots/save00_main.py")
    os.rename("Save_Slots/save00_cheat.py", "../save00.py")
    active = open("save00.py", "r")
    print(active.read(0))
    selection = 1
  elif selection == 1:
    os.rename("../save00.py", "Save_Slots/save00_cheat.py")
    os.rename("Save_Slots/save00_main.py", "../save00.py")
    active = open("save00.py", "r")
    print(active.read(0))
    selection = 0

func()