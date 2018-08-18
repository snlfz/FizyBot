import discord
from discord.ext import commands
import random
import asyncio
import aiohttp


COLOUR = 0x0

class Fun():
	def __init__(self, bot):
		self.bot = bot
		
	####################
	"FUNFUNFUNFUNFUN"
	####################
		
	
	
 
    #8ball
    
	@commands.command( name = '8ball',aliases = ['eightball', '8-ball'], pass_context=True)
	async def eight_ball(self, context):
		possible_responses = [
		'That is a resounding no',
		'It is not looking likely',
		'Too hard to tell',
		'It is quite possible',
		'Definitely',
		'Probably? Idk',
		'Well i\'m not sure this time'
		]
		await self.bot.say( embed = discord.Embed(description= random.choice( possible_responses) + ", " + context.message.author.mention))


	#cointoss

	@commands.command(aliases = ['cointoss', 'coinflip'], pass_context=True )
	async def coin(self, ctx):
		choice=random.randint(1,2)
		if choice == 1:
			await self.bot.add_reaction(ctx.message,"🌑")
		if choice == 2:
			await self.bot.add_reaction(ctx.message,"🌕")
	

	#slotmachine!

	@commands.command( pass_context = True, aliases = ['slots', 'jackpot'])
	async def slot(self, ctx):
		emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
		a = random.choice(emojis)
		b = random.choice(emojis)
		c = random.choice(emojis)
		user=ctx.message.author.mention
        
		embed=discord.Embed(colour=COLOUR)
		slot=f"**[ {a} {b} {c} ]**"
		
		
		if (a == b == c):
			embed.add_field( name=slot, value= f"**{user}**, All matching, Jackpot! <a:shake:475305983195742211> ")
		elif (a == b) or (a == c) or (b == c):
			embed.add_field( name= slot, value= f"**{user}**, 2 in a row, you won! <a:grin:475304794958069760> ")
		else:
			embed.add_field( name= slot, value= f"**{user}**, No match, you lost <a:triggered:475838149692751873> ")
        
		await self.bot.say(embed=embed)



	@commands.command()
	async def diceroll(self):
		die_faces = [
		'https://cdn.discordapp.com/attachments/478623413032976386/480018302568103946/1.png',
		'https://cdn.discordapp.com/attachments/478623413032976386/480018301926506505/2.png',
		'https://cdn.discordapp.com/attachments/478623413032976386/480018301926506506/3.png',
		'https://cdn.discordapp.com/attachments/478623413032976386/480018302568103948/4.png',
		'https://cdn.discordapp.com/attachments/478623413032976386/480018303314558977/5.png',
		'https://cdn.discordapp.com/attachments/478623413032976386/480018302568103947/6.png'
		]
		
		init = discord.Embed(description= "Rolling it ... <a:loading:479264910744748054> ", colour=COLOUR)
		init.set_thumbnail(url = "https://cdn.discordapp.com/attachments/478623413032976386/480005385252503562/lg.gambling-rotating-dice.gif")
		
		send= await self.bot.say(embed=init)
		await asyncio.sleep(3)
		
		resp = discord.Embed(description= "Rolled the Die! <a:cyclone:475304980132397066>  ", colour=COLOUR)
		resp.set_thumbnail(url = random.choice(die_faces))

		await self.bot.edit_message(send, embed=resp)
		
		


		
			
#CAT
					
	@commands.command(pass_context=True, name="cat")
	async def _cat(self, ctx: commands.Context):
		"""Shows a random cat."""

		user= ctx.message.author
		await self.bot.type()
		url = "http://shibe.online/api/cats?count=1"
		async with aiohttp.get(url) as response:
			img_url = (await response.json())[0]
			
			embed=discord.Embed( description ="<a:cat:479266953077456926> ", color=0x0 )
			embed.set_image(url= img_url)
			embed.set_footer( text= f"Requested by {user.name}#{user.discriminator}", icon_url= user.avatar_url)
		
			await self.bot.say(embed=embed)




#DOG

	@commands.command(pass_context=True, name="dog")
	async def _dog(self, ctx: commands.Context):
		"""Shows a random dog."""

		user= ctx.message.author
		await self.bot.type()
		
		url = "http://random.dog/"
		async with aiohttp.get(url +"woof.json") as response:
			
			filename = (await response.json())["url"]
			async with aiohttp.get(filename) as image:
				
				
				embed=discord.Embed( description = "<a:aww:479266711145545730>",color=0x0 )
				embed.set_image(url= (filename))
				embed.set_footer( text= f"Requested by {user.name}#{user.discriminator}", icon_url= user.avatar_url)
				
				await self.bot.say(embed=embed)

			



#FOX
	@commands.command(pass_context=True, name="fox")
	async def _fox(self, ctx: commands.Context):
		"""Shows a random fox."""

		user= ctx.message.author
		await self.bot.type()
		rand=random.randint(1,121)
		img_url = f"https://randomfox.ca/images/{str(rand)}.jpg"
		
		embed=discord.Embed(description="<a:hungry:479279786741727233> " ,color=0x0)
		embed.set_image(url=img_url)
		embed.set_footer( text= f"Requested by {user.name}#{user.discriminator}", icon_url= user.avatar_url)
		
		await self.bot.say(embed=embed)




#BIRB
	@commands.command(pass_context=True, name="bird")
	async def _bird(self, ctx: commands.Context):
		"""Shows a random bird."""

		user= ctx.message.author
		await self.bot.type()
		url = "http://shibe.online/api/birds?count=1"
		async with aiohttp.get(url) as response:
			img_url = (await response.json())[0]
			
			embed=discord.Embed( description="<a:ablobpopcorn:477886186850091038> " ,color=0x0)
			embed.set_image(url= img_url)
			embed.set_footer( text= f"Requested by {user.name}#{user.discriminator}", icon_url= user.avatar_url)
			
			await self.bot.say(embed=embed)




		
def setup(bot):
	bot.add_cog(Fun(bot))