import random
import discord
from discord.ext import commands


COLOUR = 0X0



class Embed():
	def __init__(self, bot):
		self.bot = bot
		
	####################
	"EMBED MAKER"
	####################
	
	
	
	
	
#make embed!

	@commands.command(pass_context=True)
	async def embed(self, ctx):
	
	# First message
	
		embed = discord.Embed(
		title="Welcome to FizyBot Embed Wizard!",
		description="**Here are the Parts of an Embed** <a:shake:475305983195742211>", colour=COLOUR)
		embed.set_image( url="https://cdn.discordapp.com/attachments/478623413032976386/479009792057278473/embedinfo.png")
	
		
		final = await self.bot.say(embed=embed)
	


		#Funcs!
		
			#displays bot output and takes input. then deletes both
		async def work(outp):
			a = await self.bot.say( embed= discord.Embed( description = "<a:ablobpopcorn:477886186850091038> " +outp))
			b = await self.bot.wait_for_message(author = ctx.message.author ,timeout=90)
		
		
			if ctx.message.server.me.permissions_in(ctx.message.channel).manage_messages:
				await self.bot.delete_messages([a,b])
			else:
				await self.bot.delete_message(a)
			return b.content




			#displays bot output for confirmation . takes confirmation and returns 1 if yes and 0 if anything else
		async def conf(outp):
			a = await self.bot.say(embed=discord.Embed(description="<a:think2:475306370661351424> "+outp))
			b = await self.bot.wait_for_message(author = ctx.message.author, timeout=90)
			c = b.clean_content.lower()
			okay_values=["yes","y"]
		
		
			if ctx.message.server.me.permissions_in(ctx.message.channel).manage_messages:
				await self.bot.delete_messages([a,b])
			else:
				await self.bot.delete_message(a)
		
			if c in okay_values:
				return 1
			else:
				return 0



		#--title
		title= await work("Enter **Title**")
		

		#--description
		description = await work("Enter **Description**")
		ch = await conf("Do you want to set the Embed **Colour**?")
		if ch:
			colour= await work("Enter Embed **Color**\n *Examples:* `7289da` `5c1ebf` `000000`\n"+"[Tap Here](https://htmlcolorcodes.com/color-picker/)"+" to get a Hex code for your Color!")
		


			embed = discord.Embed(title=title, description=description , colour = int(f"{colour}",16))
		else:
			embed = discord.Embed(title=title, description=description)
	
	
	
		#--author
		ch= await conf("Do you want to set **Author Name**?")
		if ch:
			auth_name = await work("Enter **Author Name**")
		
		
			ch = await conf("Do you want your **Author Name** to point out to an URL?")

			if ch:
				auth_url = await work("Enter **Author URL**")
			else:
				auth_url = ""
			
			ch = await conf("Do you want to set an **Author Avatar**?")
		
			if ch: 
				auth_avt = await work("Enter **Author Avatar** URL")
			else:
				auth_avt= ""

		
			embed.set_author(name=auth_name, url=auth_url, icon_url=auth_avt)



		#--image
		ch = await conf("Do you want to put an **Image** (Centered below) in your Embed?")

		if ch:
			image = await work("Enter **Image URL**")
		
			embed.set_image(url=image)
	

		#--thumbnail
		ch = await conf("Do you want to put a **Thumbnail**?")

		if ch:
			thumbnail = await work("Enter the URL of the **Thumbnail**")
		
			embed.set_thumbnail(url=thumbnail)


		#--field(s)
		ch = await conf("Do you want to add **Fields** in your Embed? Yes/No")
	
		if ch:
			ch = 1
			while ch:
				field_name = await work("Enter **Field Name** (the heading that appear in bold)")
			
				field_val = await work("Enter the **Field Description/Value** (the one that appears under Field Heading)")
			
			
				embed.add_field(name = field_name, value = field_val)
				ch = await conf("Do you want to add more Fields? Yes/No")
			
			
	
		#--footer
		ch = await conf("Do you want to add a **Footer** to your Embed? Yes/No")
	
		if ch:
			footer_text = await work("Enter **Footer** Text")

			ch= await conf("Do you want to add **Footer Icon** (which is placed before the Footer) Yes/No")
		
			if ch:
				footer_icon = await work("Enter **Footer Icon** URL")
			else:
				footer_icon = ''
		
			embed.set_footer(text = footer_text, icon_url = footer_icon)
	
		await self.bot.delete_message(final)	
	
		#-say
	
		await self.bot.say(embed=embed)
	


		
		



def setup(bot):
	bot.add_cog(Embed(bot))