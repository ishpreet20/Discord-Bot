import discord
from discord.ext import commands
from discord.utils import get

import random

intents = discord.Intents.all() #important for **1** part ALSO NECESSARY FOR OTHERS USERS TO CALL ASSIST COMMAND
client = commands.Bot(command_prefix=">>",activity=discord.Game(name='>>assist'))#,intents=intents) add this for **1** part

f=open("help.txt","r")
#help_text=f.readlines() #to make it read it as a list

@client.command()
async def assist(ctx):
    #setting EMBED MESSAGE
    myembed=discord.Embed(title="BOT INFO",description="The bot is ALIVE",color=0x00FF00)
    myembed.add_field(name="Version Code",value="2.0",inline=False)
    myembed.add_field(name="Bot Commands",value=f.read(),inline=False)
    myembed.set_footer(text="As on June 2021")
    #myembed.set_author(name="Ishpreet")

    await ctx.send(embed=myembed)
    #await ctx.send(f.read()) #this works read() is very important

@client.command(aliases=['hello','hemlo'])
async def hey(ctx):
    await ctx.send("https://tenor.com/view/animate-me-app-animate-me-simpsons-ralph-wiggum-gif-20970911")


@client.command(aliases=['cheats_on','cheatson'])
async def cheatsON(ctx):
    await ctx.send("Cheating Mode status: ACTIVE\nGet Ready, Be Focused, 10CGPA")

@client.command(aliases=['cheats_off','cheatsoff'])
async def cheatsOFF(ctx):
    await ctx.send("Cheating Mode status: INACTIVE\nGOOD ONE, Keep up the good work")

@client.command()
async def teamcsgo(ctx):

    '''  **1**  admin=get(ctx.guild.roles, name='Brother Supreme')
    ish=client.get_user(783603068607528991)
    await ctx.send(f"{ish.mention}")
    await ctx.send(f"{admin.mention}")'''

    await ctx.send("Calling CS:GO Players........\nThe Carry <@412128765485907979>\nThe Sniper <@760565120782303283>\nThe Assassin <@783603068607528991>\nThe Moral Support <@765836545499332629>\nThe Koder <@759798524560539649>")

@client.command(aliases=['teambalo'])
async def teamvalo(ctx):
    await ctx.send("Calling Balorant Players........\nAlmost Silver <@412128765485907979>\nRaze Main <@765836545499332629>\nJust Happy To Be Here <@783603068607528991>")

@client.command()
async def teamcod(ctx):
    await ctx.send("Calling COD Players........\nThe Pro CODer <@759798524560539649>\nThe Always ready <@412128765485907979>\nThe Former CS:GO player <@760565120782303283>")
    await ctx.send("https://tenor.com/view/call-of-duty-gif-20020144")

@client.event
async def on_message(message):
    if message.author==client.user:
        return

    for word in message.content.split():
        if word =='good' or word== 'gud' or word== 'nice':
            await message.reply("https://cdn.discordapp.com/emojis/837587359830638632.png?v=1")

        if word == 'loda' or word=='lauda' or word=='laude' or word=='lode':
            await message.reply("https://tenor.com/view/doge-meme-deal-with-it-cool-gif-15101750")

        if word == 'game' or word== 'csgo' or word== 'balorant' or word== 'balo' or word== 'valo' or word=='cod':
            await message.reply("https://tenor.com/view/abe-lvde-apna-kam-kr-gif-18170896")

        if word == 'bolna':
            await message.reply("https://tenor.com/view/ab-bolna-mc-gif-18648572")


    '''if message.content.endswith("lode"):
        await message.reply("https://tenor.com/view/abe-lvde-apna-kam-kr-gif-18170896")'''

    '''if message.content.endswith("bot"):
        await message.reply("https://tenor.com/view/doge-meme-deal-with-it-cool-gif-15101750")

    if message.content.startswith("nice"):
        await message.reply("https://cdn.discordapp.com/emojis/837587359830638632.png?v=1")

    if message.content.startswith("game"):
        await message.channel.send("Padhai Kar Lode")

    if message.content.startswith("ab bolna"):
        await message.channel.send("https://tenor.com/view/ab-bolna-mc-gif-18648572")'''

    if message.author.id==760565120782303283:
        if random.random()>0.45:
            await message.reply("https://tenor.com/view/abe-lvde-apna-kam-kr-gif-18170896")
    if message.author.id==765836545499332629:
        if random.random()>0.35:
            await message.reply("https://tenor.com/view/mere-pyare-foji-bhaiyo-ye-diwali-aapke-naam-gifkaro-festival-diwali-gif-20911905")

    if message.author.id==759798524560539649:
        if random.random()>0.45:
            await message.reply("https://cdn.discordapp.com/emojis/837195560762736642.png?v=1")

    await client.process_commands(message)

@client.event
async def on_message_delete(message):
    await message.channel.send("Commander Cheems just saw the message that you deleted!!! \n https://tenor.com/view/shiba-inu-wink-gif-11153954")

# running the client
client.run('ODQ3MDc3MDc0NTI3MTkxMDQy.YK40AA.hsNG0ivTx9GeJnQAqtshEc_F_B8') #the token has expired. hehe bro. let me see how to make it private.
