from discord_webhook import DiscordWebhook


webzn = input("Url da webhook que você irá floodar : ")
msg = input("Insira uma mensagem para floodar : ")
username = input("Insira o nome da webhook : ")
webhook = DiscordWebhook(url=webzn, content=msg ,username = username, avatar_url="https://cdn.discordapp.com/embed/avatars/0.png")
while True:
    response = webhook.execute()
    time.sleep(0.5)
    print(f"+ Mensagens enviada")