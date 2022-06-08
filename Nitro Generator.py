import requests
import time
import random, string
import requests
from discord import Webhook, RequestsWebhookAdapter
import colorama
from colorama import Back, Fore, Style

print( """
██████╗░███████╗██╗░█████╗░██╗░░██╗███╗░░░███╗░█████╗░███╗░░██╗███╗░░██╗
██╔══██╗██╔════╝██║██╔══██╗██║░░██║████╗░████║██╔══██╗████╗░██║████╗░██║
██║░░██║█████╗░░██║██║░░╚═╝███████║██╔████╔██║███████║██╔██╗██║██╔██╗██║
██║░░██║██╔══╝░░██║██║░░██╗██╔══██║██║╚██╔╝██║██╔══██║██║╚████║██║╚████║
██████╔╝███████╗██║╚█████╔╝██║░░██║██║░╚═╝░██║██║░░██║██║░╚███║██║░╚███║
╚═════╝░╚══════╝╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝
  """)

colorama.init(autoreset=True)

print(Fore.CYAN + "Join Discord:https://discord.gg/sC3jzRkM9G")
print()

link = input("Webhook Link : ")
amount = int(input("How many codes to generate : "))
for i in range(amount):
    time.sleep(1)
    code = "https://discord.gift/" + "".join(random.choices(string.ascii_letters + string.digits, k=16))
    print(Fore.RED + "[GENERATED] " + code)
    webhook = Webhook.from_url(link, adapter=RequestsWebhookAdapter())
    webhook.send(code)