import random as ran
import string as string

password = {}

try:
    with open("passwords.txt","r") as file:
      for line in file:
        website,pwd = line.strip().split(":")
        password[website] = pwd
except:
    pass

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*+=-"
    password = "".join(ran.choice(chars) for _ in range (8))
    return password

while True:
    print("_______Personal Password Manager__________")
    print("1.Save Password")
    print("2.View Password")
    print("3.Generate Password")
    print("4.Exit")

    choice = input("Enter your Choice: ")

    if choice == "1":
        site = input("Enter Website: ")
        pwd = input("Enter Password: ")
        
        password[site] = pwd

        with open("passwords.txt","a") as file:
            file.write(f"{site}:{pwd}\n")
        
        print("Saved!!!")
    elif choice == "2":
        if not password:
            print("No data")
        else:
            for site,pwd in password.items():
                print(site, ":" , pwd)
    elif choice == "3":
        print("Generated Password", generate_password())
    elif choice == "4":
        print("End")
        break
    else:
        print("Invalid Choice")





