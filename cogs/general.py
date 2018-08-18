import discord
from discord.ext import commands
import psutil
import datetime


COLOUR = 0X0

class General():
	def __init__(self, bot):
		self.bot = bot
    





		
	#Invite
	@commands.command( pass_context=True,aliases=["links"])
	async def invite(self, ctx):
		embed=discord.Embed( colour=discord.Colour(COLOUR))
		embed.set_author(name='Links!')
		
		embed.add_field( name='<a:attention:475307661395623936> *Invite me!*' , value=" [➡️Tap here](https://discordapp.com/oauth2/authorize?client_id=472615266103328778&scope=bot)")
		embed.add_field( name='<a:owo:475305390247247873> *Visit me!* ', value='[➡️Doorbell](https://discord.gg/JaTEP56)')
           
		await self.bot.say(embed=embed)

    


 
     
	#info
	@commands.command( aliases=['about'],pass_context=True)
	async def info(self, ctx):
		
		cpu = psutil.cpu_percent()
		ram = psutil.virtual_memory().percent
    
		servers =0
		channels =0
		members = 0
		for server in self.bot.servers:
			servers+= 1
			for channel in server.channels:
				channels+=1
			for member in server.members:
				members+=1
	


		embed=discord.Embed( description = "**CPU :** *{:0.2f}%* \n**RAM :** *{:0.2f}%* \n**Users :** *{}* \n**Servers :** *{}* \n**Channels :** *{}* \n ​ ​ ​ ​ ​ ​ ​ \nMade with Python <a:heart:475305073262592010> by *fizy#9347*".format(cpu,ram,members,servers,channels) , colour = discord.Colour(COLOUR))
		embed.set_author(name='FizyBot in here!', icon_url="https://cdn.discordapp.com/attachments/478623413032976386/479721191779729408/20180810_235146_0001.png")
    
		await self.bot.say(embed=embed)

 



	#ping
	@commands.command( pass_context=True, aliases=['pong','latency'])
	async def ping(self, ctx):
		embed1=discord.Embed( description='<a:loading:474402569544925205>  Pong! Loading...' ,colour=COLOUR)
		resp = await self.bot.say(embed=embed1)
		diff = resp.timestamp - ctx.message.timestamp
		embed2=discord.Embed( description=f'<a:ablobthinkingfast:474762165325135882> Pong! That took {1000*diff.total_seconds():.1f}ms.',colour=COLOUR)
		await self.bot.edit_message(resp, embed=embed2)
    	



def setup(bot):
	bot.add_cog(General(bot))
		
		