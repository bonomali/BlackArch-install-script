import subprocess
print("--------------------------------------")
print("            BlackArch     By:KattStof")
print("            Install       v:1.0.0    ")
print("            Script                ")
print("--------------------------------------")
print(" ")
print (" ")
print ("[1] Install All Blackarch *This will take a while go drink some coffee*")
print("[2] Install certain Blackarch Tool")
print ("[0] Exit")
chce = input(":")
if chce == '1':
        subprocess.call("curl -O https://blackarch.org/strap.sh", shell=True)
        subprocess.call("sudo chmod +x strap.sh", shell=True)
        subprocess.call("sudo ./strap.sh", shell=True)
        subprocess.call("sudo pacman -S blackarch", shell=True)
        subprocess.call("enter", shell=True)
if chce== '2':
        print("-------")
        print("PLEASE")
        print("WAIT")
        print("------")
        subprocess.call("curl -O https://blackarch.org/strap.sh", shell=True)
        subprocess.call("sudo chmod +x strap.sh", shell=True)
        subprocess.call("sudo ./strap.sh", shell=True)
        choice = input("Which tool would you like to install?:")
        subprocess.call("sudo pacman -S "  + choice, shell=True)
if chce == '0':
        print("Okay Scipt kiddie, Go back to HackForums")
        exit()
