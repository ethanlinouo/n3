import discord
import random
from discord.ext import commands
import time

from discord.ext.commands import bot

client = discord.Client()

bot = commands.Bot(command_prefix='')


@client.event
async def on_ready():
    print('目前登入身份：', client.user)



@client.event
async def on_message(message):
    if message.author == client.user:
        return    
    if message.content.finishswith('?'):   
      tmp = message.content.split(2," ")  
      if len(tmp) == 1:
        await message.channel.send("你說什麼啦？")
      else:
        await message.channel.send("不知道")





@client.event
async def on_message(msg):
    if msg.content.startswith('打@{menber} '):
        await msg.channel.send('@{menber}爽死了...')



@client.event
async def on_message(msg):
    if msg.content == '救命':
        await msg.channel.send('乾我屁事')



client.run('ODcyNzcyNTgxMTk4MDE2NTQy.YQuuzg.DvC0QSYUfEure_5p0ckOZoKDKe4') #TOKEN在剛剛Discord Developer那邊「BOT」頁面裡面




