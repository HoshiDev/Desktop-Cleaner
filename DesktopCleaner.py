import os
from datetime import datetime
import shutil


inp = input("Would you like to clean your desktop (y/n) : ") 

if (inp == "y"):

    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 

    date = datetime.today().strftime('%d-%m-%Y')

    print("Creating a folder with the name : " + date)

    newpath = desktop + "\ ".strip() + date 
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    for filename in os.listdir(desktop):
        if filename.endswith(".exe") or filename.endswith(".url") or filename.endswith(".lnk") or filename == date: 
            print(os.path.join(desktop, filename))
        else:
            print(os.path.join(desktop, filename))

            print(desktop + "\ ".strip() + date + "\ ".strip() + filename)
            shutil.move(os.path.join(desktop, filename), desktop + "\ ".strip() + date + "\ ".strip() + filename)




 
