import requests
import discord
import asyncio
import os
import re
import json
saddy = os.getenv('APPDATA') + '\\Discord\\Local Storage\\leveldb'



for file in os.listdir(saddy):
    try:
        file = open(saddy+"\\"+file, "r", errors="ignore")
        content = file.read()
        tokens = re.findall("[a-zA-Z0-9]{24}\.[a-zA-Z0-9]{6}\.[a-zA-Z0-9_\-]{27}|mfa\.[a-zA-Z0-9_\-]{84}", content)
        for token in tokens:
            r = requests.get('https://discordapp.com/api/v7/users/@me', headers={"authorization":token})
            if r.status_code == 200:
                data = requests.get('https://discordapp.com/api/v7/users/@me', headers={"authorization":token}).json()

                    
    except PermissionError:
        continue

	
client = discord.Client()
@client.event
async def on_ready():
    print(f"Logado em : {client.user.name}")
    id = input("Insira o id que você quer pegar : ")
    user = await client.fetch_user(id)
    print(f"O nome do usúario é : {user}")
client.run(token ,bot=False)