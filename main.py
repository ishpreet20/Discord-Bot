import os
import discord
from discord.ext import commands
import random

#INITIALISING
intents = discord.Intents.all()
client = commands.Bot(command_prefix=">>",activity=discord.Game(name='testing 3.1.0'))

#RESOURCES
f=open("help.txt","r")
good=['good','gud','nice','op']
bad=['loda','lomdu','lodu','lode','bhsdk','fuddu','lauda','laude','saale','gamdu','gandu']
game=['game','balo','balo?','csgo','csgo?','csgo??','csgo','cod','cod?']
greet=['hello','hemlo','hey','oye']
bolna=['bolna','ruko','sorry','galti']
celeb=['party','yeah','nacho','moj']

#USE COMMAND
@client.command()
async def use(ctx):
    mbed=discord.Embed(title="COMMANDER CHEEMS",url="https://github.com/ishpreet20/Discord-Bot",description="A meme inspired bot.",color=0xFFFFFF)

    mbed.set_author(name="DOGE MEMES")

    mbed.set_thumbnail(url="https://i.pinimg.com/564x/1a/10/6f/1a106f30df65c6916dc99adbd6f9faec.jpg")

    # mbed.add_field(name="Bot Commands",value="hehe bro",inline=False)

    mbed.set_footer(text="Information requested by: {}".format(ctx.author.display_name))

    await ctx.send(embed=mbed)

#CHEAT MODE
@client.command(aliases=['cheats_on','cheatson'])
async def cheatsON(ctx):
    await ctx.send("Cheating Mode status: ACTIVE\nGet Ready, Be Focused, 10CGPA")

@client.command(aliases=['cheats_off','cheatsoff'])
async def cheatsOFF(ctx):
    await ctx.send("Cheating Mode status: INACTIVE\nGOOD ONE, Keep up the good work")

#CALLING GAMERS
@client.command()
async def teamcsgo(ctx):
    await ctx.send("Calling CS:GO Players........\nThe Carry <@412128765485907979>\nThe Sniper <@760565120782303283>\nThe Assassin <@783603068607528991>\nThe Moral Support <@765836545499332629>\nThe Koder <@759798524560539649>")

@client.command(aliases=['teambalo'])
async def teamvalo(ctx):
    await ctx.send("Calling Balorant Players........\nAlmost Silver <@412128765485907979>\nRaze Main <@765836545499332629>\nJust Happy To Be Here <@783603068607528991>")

@client.command()
async def teamcod(ctx):
    await ctx.send("Calling COD Players........\nThe Pro CODer <@759798524560539649>\nThe Always ready <@412128765485907979>\nThe Former CS:GO player <@760565120782303283>")
    await ctx.send("https://tenor.com/view/call-of-duty-gif-20020144")

#FOR EVERY MESSAGE SENT ON DISCORD
@client.event
async def on_message(message):
    if message.author==client.user:
        return

    note=message.content.lower()

    for word in note.split():
        if word in good:
            await message.reply("https://cdn.discordapp.com/emojis/837587359830638632.png?v=1")

        if word in bad:
            await message.reply("https://tenor.com/view/doge-meme-deal-with-it-cool-gif-15101750")

        if word in game:
            await message.reply("https://tenor.com/view/abe-lvde-apna-kam-kr-gif-18170896")

        if word in greet:
            await message.reply("https://tenor.com/view/animate-me-app-animate-me-simpsons-ralph-wiggum-gif-20970911")

        if word in bolna:
            await message.reply("https://tenor.com/view/ab-bolna-mc-gif-18648572")

        if word in celeb:
            await message.reply("https://media.discordapp.net/attachments/802114010441842699/853189105772920862/image0-5.gif")

    #F1
    if message.author.id == 760565120782303283:
        if random.random()>0.55:
            await message.reply("https://tenor.com/view/abe-lvde-apna-kam-kr-gif-18170896")

    #F2
    if message.author.id == 765836545499332629:
        if random.random() > 0.35:
            await message.reply("https://tenor.com/view/mere-pyare-foji-bhaiyo-ye-diwali-aapke-naam-gifkaro-festival-diwali-gif-20911905")

    #F3
    if message.author.id == 759798524560539649:
        if random.random() > 0.45:
            await message.reply("https://cdn.discordapp.com/emojis/837195560762736642.png?v=1")

    #F4
    if message.author.id == 412128765485907979:
        if random.random() > 0.6:
            await message.reply("https://tenor.com/view/jaspreet-singh-beta-tu-toh-chup-hi-raha-kr-beta-tu-toh-chup-hi-rha-kr-jaspreet-sigh-stand-up-comedy-gif-16842763")

    #PROCESSING COMMANDS AFTER EVENTS or something like that
    await client.process_commands(message)

#ON MESSAGE DELETION
@client.event
async def on_message_delete(message):
    await message.channel.send("Commander Cheems just saw the message that you deleted!!!")
    await message.channel.send("https://tenor.com/view/shiba-inu-wink-gif-11153954")

#RUNNING THE BOT
bot_code=os.environ['BOT_CODE']
client.run(bot_code)
