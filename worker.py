import discord
import asyncio
        
client = discord.Client()
        
@client.event
async def on_ready():
    print('Logged in as')
	print(client.user.name)
    print(client.user.id)
    print('------')
        
@client.event
async def on_message(message):
    if message.content == "Hello":
        await client.send_message(message.channel, "World")
        
client.run(https://discordapp.com/api/oauth2/authorize?client_id=469248346574422026&permissions=603049168&scope=bot)