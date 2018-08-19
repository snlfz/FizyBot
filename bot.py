import os
import asyncio
import discord
from discord.ext import commands
import psutil


description = '''Hey! FizyBot in here!'''

# this specifies what extensions to load when the bot starts up
startup_extensions = [
	"cogs.general",
	"cogs.utils", 
	"cogs.embed", 
	"cogs.fun",
	"cogs.eval",
	"cogs.embed2"
	]

bot = commands.Bot(command_prefix='..', description=description)
#bot.remove_command('help')



COLOUR=0X0

DEV_ID='463754565771329536'

#idk what this does :/

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----------')

    PLAYING="in a secret garden."
    await bot.change_presence(game=discord.Game(name=PLAYING),status=discord.Status.idle)
  

#doesnt let bots use the bot c:

@bot.event
async def on_message(message):
	if not (message.author.bot):
		await bot.process_commands(message)




#change the playing status anytime

@bot.command(pass_context=True , hidden = True )
async def playing(ctx,*args):
	if (ctx.message.author.id == DEV_ID):
		output=''
		for word in args:
			output+= word
			output+= ' '
		await bot.change_presence( game=discord.Game(name=output), status= discord.Status.idle)
		await bot.add_reaction(ctx.message, "a:Tick:464851815435993108")
		


#Load cogs

@bot.command( pass_context=True, hidden = True )
async def load(ctx, extension_name : str):
    """Loads an extension."""
    if (ctx.message.author.id == DEV_ID):
        try:
            bot.load_extension(extension_name)
        except (AttributeError, ImportError) as e:
            await bot.say("```py\n{}: {}\n```".format( type(e).__name__, str(e)))
            return
        await bot.say("<a:cogs:479264957318430722> {} loaded.".format(extension_name))



#Unload cogs

@bot.command( pass_context=True ,hidden = True )
async def unload(ctx, extension_name : str):
    """Unloads an extension."""
    if (ctx.message.author.id == DEV_ID):
        bot.unload_extension(extension_name)
        await bot.say("<a:cogs:479264957318430722> {} unloaded.".format(extension_name))


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))











bot.run(os.environ.get('Token'))





