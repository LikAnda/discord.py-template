import os
import json
import time

print("\nMise en place de votre bot... - by LikAnda")
with open("config.json", "r") as f:
    data = json.load(f)
time.sleep(1)
print("\nInstallation des extensions nécessaires...")
time.sleep(1)
try:
    os.system("pip install -r requirments.txt")
except:
    input("\nErreur lors de l'installation des extensions...")
print("Installation réussie!")

bot_token = input("\nVeuillez entrer le token de votre bot: ")
bot_token = int(bot_token)
data["token"] = (bot_token)
bot_prefix = input("Entrer le préfixe du bot souhaité (exemple: !): ")
data["prefix"] = (bot_prefix)
owner_choice = input("Souhaitez vous ajouter l'ID discord d'un propriétaire du bot (y/n): ")
if owner_choice == "y" or owner_choice == "Y":
    owner_id = input("Entrer l'ID discord du propriétaire du bot: ")
    owner_id = int(owner_id)
    data["ownersID"].append(owner_id)
else:
    print("PS: vous pouvez toujours ajouter manuellement des propriétaires dans le fichier 'config.json'")

with open("config.json", "w") as f:
    json.dump(data, f, indent=4)
print("Configuration terminée!")
execute_bot = input("Executer le bot ? (y/n): ")
if execute_bot == "y" or execute_bot == "Y":
    os.system("python3 bot.py")