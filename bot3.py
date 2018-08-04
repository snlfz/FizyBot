import random
import asyncio
import json
import os
import discord
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot



BOT_PREFIX = (",","$","<@472615266103328778> ","<@472615266103328778>")

TOKEN = os.environ.get(Token)

COLOUR=0xfbb716

bot =commands.Bot(command_prefix=BOT_PREFIX)
bot.remove_command('help')


#EVENTS#

    #Playing Status
    
PLAYING="in a secret garden"
@bot.event
async def on_ready():
    await bot.change_presence(game=Game(name=PLAYING),status=discord.Status.idle)
    print("Logged in as " + bot.user.name)


@bot.command(pass_context=True)
async def playing(ctx,*args):
        output=''
        for word in args:
            output+= word
            output+= ' '
        yeep=await bot.change_presence(game=Game(name=output))
        await bot.add_reaction(ctx.message, "a:Tick:464851815435993108")
        await asyncio.sleep(20)
        await bot.change_presence(game=Game(name=PLAYING),status=discord.Status.idle)
       
        

#############################


#HELP#
@bot.command(pass_context=True)
async def help(ctx):
    embed=discord.Embed(
    colour=discord.Colour(COLOUR)
    )
    embed.set_author(name='Need Help? FizyBot to your Rescue!')
    embed.add_field(name="__**Utility**__", value="🔸`help` : *Opens up this Page*\n🔸`echo [...]` : *Repeats after you*\n🔸`purge [number]` : *clean chat*")
    embed.add_field(name='__**Fun**__', value="🔸`playing [...]` : *Changes bot playing status for 20 seconds!*\n🔸`8ball [question]` : *Oldschool 8 ball responses*")
    embed.add_field(name='__**Math**__', value="🔸`add [] []` : *does something*\n🔸`subtract [] []` : *does something else*\n🔸`multiply [] []` : *more stuff*\n🔸`divide [] []` : *and more.*\n🔸`square []` : *What even is my life*",)
    embed.add_field(name='__**Pointless**__', value="🔸`ping` : *Pong!*\n🔸`greet` : *Heya!*" )
 
           
 #   yee=
    await bot.say(embed=embed)
 #   await asyncio.sleep(60)
 #   await bot.delete_message(yee)   
    
    
    
#Invite
@bot.command(pass_context=True)
async def invite(ctx):
    embed=discord.Embed(
    colour=discord.Colour(COLOUR)
    )
    embed.set_author(name='Links!')

    embed.add_field(name='*Invite me!*', value=" [➡️Tap heppre](https://discordapp.com/oauth2/authorize?client_id=472615266103328778&scope=bot)")
    embed.add_field(name='*Visit my abode!*', value='[➡️Doorbell](https://discord.gg/JaTEP56)')
           
           
 #   yee=
    await bot.say(embed=embed)
 #   await asyncio.sleep(60)
 #   await bot.delete_message(yee)   
    
    
#info
@bot.command(aliases=['about'],pass_context=True)
async def info(ctx):
    embed=discord.Embed(
    colour=discord.Colour(COLOUR)
    )
    embed.set_author(name='FizyBot v0.4 alpha - in vigorous development!')
    embed.add_field(name="*Made with a Secret potion of Python & 💛*", value="by *fizy#9347*")
 
           
  #  yee=
    await bot.say(embed=embed)
  #  await asyncio.sleep(60)
  #  await bot.delete_message(yee)   
    


#USELESS BUT FUN#




    #greet
@bot.command(pass_context=True) 
async def greet(ctx): 
    await bot.say("<a:ablobwave:474874458780205066>  Hello, there!\n "+ ctx.message.author.mention ) 


    #ping
@bot.command(pass_context=True)
async def ping(ctx):
	embed1=discord.Embed( description='<a:loading:474402569544925205>  Pong! Loading...' ,colour=COLOUR)
	resp = await bot.say(embed=embed1)
	diff = resp.timestamp - ctx.message.timestamp
	embed2=discord.Embed( description=f'<a:ablobthinkingfast:474762165325135882> Pong! That took {1000*diff.total_seconds():.1f}ms.',colour=COLOUR)
	await bot.edit_message(resp, embed=embed2)
    	
    	
    	
    #	<a:ablobthinkingfast:474762165325135882> Pong! That took {1000*diff.total_seconds():.1f}ms.
    	
    #8ball
@bot.command(name='8ball',aliases=['eightball', '8-ball'],pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await bot.say(random.choice(possible_responses) + ", " + context.message.author.mention)



#UTILITY COMMANDS#

    #Purge
@bot.command(pass_context=True)
async def purge(ctx, which : int=None):
    if ctx.message.author.server_permissions.manage_messages:
        if which is None:
            await bot.say("Please enter the amount of messages to purge")
        else:
            try:
                await bot.purge_from(ctx.message.channel, check=None, limit = which+1)
                yee = await bot.say(f"**{str(ctx.message.author)}** purged `{which}` messages successfully.")
                await asyncio.sleep(2)
                await bot.delete_message(yee)
            except discord.Forbidden:
                await bot.say("I don't have permission to purge messages")
    else:
        embed = discord.Embed(description="You do not have permission to use the `purge` command.")
        embed.set_author(name="Access denied",icon_url=bot.user.avatar_url)
        await bot.say(embed=embed)
 


    #echo
@bot.command()
async def echo(*args):
        output=''
        for word in args:
          	output+= word
          	output+= ' '
        await bot.say(output)
        



#MATH COMMANDS#

    #add
@bot.command(pass_context=True)
async def add(ctx, a:float, b:float):
    await bot.say(a+b)
    
    

    #subtract
@bot.command(pass_context=True)
async def subtract(ctx, a:float, b:float):
    await bot.say(a-b)


    #multiply
@bot.command(pass_context=True)
async def multiply(ctx, a: float, b: float):
    await bot.say(a*b)


    #divide
@bot.command(pass_context=True)
async def divide(ctx, a:float, b:float):
    await bot.say(a/b)
    


    #Square
@bot.command()
async def square(number):
    squared_value = float(number) * float(number)
    await bot.say(str(number) + " squared is " + str(squared_value))


bot.run(TOKEN)
