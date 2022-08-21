import random
import discord
import traceback
import os

from time import sleep
from discord.ext import commands
from colorama import Fore
from pystyle import *

config = {
    # If set to True there will be a 5 second delay between sending pings. This makes it less likely that discord will terminate your account. If set to False then there will be no delay.
    'ratelimit' : False
}

banner1 ='''
                        ▄▄▄▄███▄▄▄▄      ▄████████    ▄████████    ▄████████        
                      ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███   ███    ███        
                      ███   ███   ███   ███    ███   ███    █▀    ███    █▀         
                      ███   ███   ███   ███    ███   ███          ███               
                      ███   ███   ███ ▀███████████ ▀███████████ ▀███████████        
                      ███   ███   ███   ███    ███          ███          ███        
                      ███   ███   ███   ███    ███    ▄█    ███    ▄█    ███        
                       ▀█   ███   █▀    ███    █▀   ▄████████▀   ▄████████▀         
                                                                   
                  ▄███████▄  ▄█  ███▄▄▄▄      ▄██████▄     ▄████████   ▄████████▄                  
                  ███    ███ ███  ███▀▀▀██▄   ███    ███   ███    ███   ███    ███ 
                  ███    ███ ███▌ ███   ███   ███    █▀    ███    █▀    ███    ███ 
                  ███    ███ ███▌ ███   ███  ▄███         ▄███▄▄▄       ███▄▄▄▄██▀ 
                ▀█████████▀  ███▌ ███   ███ ▀▀███ ████▄  ▀▀███▀▀▀       █████████▄   
                  ███        ███  ███   ███   ███    ███   ███    █▄    ███▀▀▀▀███
                  ███        ███  ███   ███   ███    ███   ███    ███   ███     ██ 
                 ▄████▀      █▀    ▀█   █▀    ████████▀    ██████████   ███     ██'''          

dark = Col.gray
purple = Colors.StaticMIX((Col.purple, Col.blue))

System.Size(100, 25)
System.Title("Mass Pinger - Made By Smug")
Cursor.HideCursor()
print(Colorate.Diagonal(Colors.DynamicMIX((purple, dark)), Center.XCenter(banner1)))
print()

token = input(f'{purple}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{purple}]{Fore.RESET} Enter your token: ')

def fetch_conf(e: str) -> str or bool | None:
        return config.get(e)

def banner2():
    print(Colorate.Diagonal(Colors.DynamicMIX((purple, dark)), Center.XCenter(banner1)))
    print('\n')

def slowtype(text: str, speed: float, newLine=True):
        for i in text: 
            print(i, end="", flush=True)
            sleep(speed)  
        if newLine:  
            print()

intents = discord.Intents().all()
Luna = discord.Client()
Luna = commands.Bot(description="Luna Selfbot", command_prefix="$", self_bot=True, intents=intents, case_insensitive=True, guild_subscriptions=True)

def Main():
    try:
        Luna.run(token, bot=False)
    except discord.errors.LoginFailure:
        print(f'{purple}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{purple}]{Fore.RESET} Invalid Token')
        print(f'{purple}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{purple}]{Fore.RESET} Press Enter To Exit . . .')
        input()
        exit()
    except Exception as e:
        print(f'{purple}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{purple}]{Fore.RESET}\nAn error occured while logging in:\n{"".join(traceback.format_exception(type(e), e, e.__traceback__))}\n')
        print(f'{purple}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{purple}]{Fore.RESET} Press Enter To Exit . . .')
        input()
        exit()

@Luna.event
async def on_ready():
    os.system('cls')
    banner2()
    slowtype(f'\n{purple}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{purple}]{Fore.RESET} SelfBot is online!', .02)

@Luna.event
async def on_command_error(self, error):
    self.errors = commands.errors
    if (isinstance(error, self.errors.BadArgument) or isinstance(error, commands.MissingRequiredArgument)
            or isinstance(error, self.errors.PrivateMessageOnly) or isinstance(error, self.errors.CheckFailure)
            or isinstance(error, self.errors.CommandNotFound)):
        return
    elif isinstance(error, self.errors.MissingPermissions):
        print(f"{Fore.RED}Missing permissions {Fore.RESET}")
        print(f'{purple}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{purple}]{Fore.RESET} Press Enter To Exit . . .')
        input()
        exit()
    else:
        print(f'{Fore.RED}\n\n{"".join(traceback.format_exception(type(error), error, error.__traceback__))}{Fore.RESET}')
        print(f'{purple}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{purple}]{Fore.RESET} Press Enter To Exit . . .')
        input()
        exit()

@Luna.command(aliases=["mp"])
async def massping(ctx, amount: int):
    await ctx.message.delete()
    members = [m.mention for m in ctx.guild.members]

    for _ in range(amount):
        users = random.sample(members, len(ctx.guild.members))
        await ctx.send(" ".join(users))
        if fetch_conf('ratelimit'):
            sleep(5)
        else:
            pass
    print(f'{purple}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{purple}]{Fore.RESET} Pinged {len(users)} Members!')

@Luna.command(aliases=["stop", "st", "shutdown"])
async def restart(ctx):
    os.system("main.py")

if __name__ == '__main__':
    Main()
