import discord, asyncio, time
client = discord.Client()
import requests
token = input("Consulte token : ")
@client.event
async def on_ready():
    print(f"""
    Username : {client.user}
    ID : {client.user.id}
    Email : {client.user.email}
    URL de avatar : {client.user.avatar_url}
    Quantidade de amigos : {len(client.user.friends)}
    Quantidade de servidores {len(client.guilds)}""")

client.run(token, bot=False)