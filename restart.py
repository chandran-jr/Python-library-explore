import os

choice = input("Restart your computer? y/n")

if choice == 'y':
    os.system("shutdown /r")
 else:
    print("Operation cancelled")
