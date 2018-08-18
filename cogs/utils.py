import discord
from discord.ext import commands



COLOUR =0x0


class Info():
	def __init__(self, bot):
		self.bot = bot
		
	######################
	"INFORMATION COMMANDS"
	######################
	




	
####    1----AVATAR


	@commands.command(pass_context=True)
	async def avatar(self, ctx, user: discord.Member = None):
		"""Simply fetches the avatar for any use="""
        
		if user is None:
			user = ctx.message.author
			
		embed = discord.Embed(description=f"It's {user.mention}, everyone! <a:shades:475306116839112705> ", colour=COLOUR)
		embed.set_image(url=user.avatar_url)
		
        
        
		await self.bot.say(embed=embed)





####    2----WHOIS

	@commands.command(pass_context=True, aliases =['whois']) 
	async def userinfo(self, ctx, member: discord.Member =None):
		"""Gives important info about any user"""
	
	
		if member is None:
			member = ctx.message.author
		time = f"{member.joined_at.date():%a, %b %d %Y}"
		embed=discord.Embed(title=f"{member.name} ? Lemme check", description ="Here's what I Found <a:think2:475306370661351424> ",color =COLOUR)
	
	
		embed.add_field(name="Username", value=f"{member}", inline=True )
		embed.add_field(name="Nickname", value=member.nick if hasattr(member, "nick") else "None", inline=True)
		embed.add_field(name="Account created", value=(f"{member.created_at:%a, %b %d %Y}"), inline=True)
		embed.add_field(name="Status", value=f"{member.status}".capitalize(), inline=True)
		embed.add_field(name="Member since", value=time, inline=True)
		embed.add_field(name="Roles",value=', '.join([f"<@&{x.id}>" for x in reversed(member.roles) if x is not ctx.message.server.default_role]) if len(member.roles) > 1 else 'None', inline=False
        )
		embed.set_thumbnail(url=member.avatar_url)
	
		embed.set_footer(text = f"[ID: {str(member.id)}]")
		await self.bot.say(embed=embed)





####    3----SERVER

	@commands.command(pass_context=True, aliases=["server"])
	async def serverinfo(self, ctx):
		"""Fetches info about the server"""
		
		embed = discord.Embed(title="{}'s info".format(ctx.message.server.name), description="Here's what I could find <a:whee:475307014675890216> ", color=COLOUR)
    
		findbots = sum(1 for member in ctx.message.server.members if member.bot)
		roles=ctx.message.server.roles 
    
    
		embed.set_footer(text= f" [ID: {str(ctx.message.server.id)}]")
		embed.add_field(name="Owner", value=ctx.message.server.owner.mention)
		embed.add_field(name="Region", value=ctx.message.server.region, inline=True)
		embed.add_field(name="Created At", value=(f"{ctx.message.server.created_at:%a, %b %d %Y}"), inline=True)
    
  
		embed.add_field(name='Roles', value=', '.join([f"<@&{x.id}>" for x in (ctx.message.server.role_hierarchy) if x is not ctx.message.server.default_role]) if len(ctx.message.server.roles) > 1 else 'None',inline=True)
    
    
		embed.add_field(name="Members", value=f"**Total** : {ctx.message.server.member_count}\n**Bots** : {str(findbots)}\n**Humans** :{str(ctx.message.server.member_count - findbots)}" , inline=True)
    
    
		embed.set_thumbnail(url = ctx.message.server.icon_url)
		await self.bot.say(embed=embed)





####    4----ROLEINFO

	@commands.command(pass_context=True,aliases=['role'])
	async def roleinfo(self, ctx, rolename):
		'''Get information about a role. Case Sensitive!'''
		
		rolen=0
		for memb in ctx.message.server.members:
			for mrole in memb.roles:
				
				if mrole.name.lower() == rolename.lower():
					rolen += 1
					break
		
		
		for arole in ctx.message.server.roles:
			if rolename.lower() == arole.name.lower():
				role=arole
				break
			

		"""try:
			role = discord.utils.get(ctx.message.server.roles, name=rolename)
		except:
			await self.bot.say(f"Role could not be found. The system IS case sensitive!")
"""
		em = discord.Embed( color=role.color or discord.Color.green())
		em.title = role.name
		em.set_footer(text = f"[ID: {str(role.id)}]")
		perms = ""
		if role.permissions.administrator:
			perms += "Administrator, "
		if role.permissions.create_instant_invite:
			perms += "Create Instant Invite, "
		if role.permissions.kick_members:
			perms += "Kick Members, "
		if role.permissions.ban_members:
			perms += "Ban Members, "
		if role.permissions.manage_channels:
			perms += "Manage Channels, "
		if role.permissions.manage_server:
			perms += "Manage Server, "
		if role.permissions.add_reactions:
			perms += "Add Reactions, "
		if role.permissions.view_audit_logs:
			perms += "View Audit Log, "
		if role.permissions.read_messages:
			perms += "Read Messages, "
		if role.permissions.send_messages:
			perms += "Send Messages, "
		if role.permissions.send_tts_messages:
			perms += "Send TTS Messages, "
		if role.permissions.manage_messages:
			perms += "Manage Messages, "
		if role.permissions.embed_links:
			perms += "Embed Links, "
		if role.permissions.attach_files:
			perms += "Attach Files, "
		if role.permissions.read_message_history:
			perms += "Read Message History, "
		if role.permissions.mention_everyone:
			perms += "Mention Everyone, "
		if role.permissions.external_emojis:
			perms += "Use External Emojis, "
		if role.permissions.connect:
			perms += "Connect to Voice, "
		if role.permissions.speak:
			perms += "Speak, "
		if role.permissions.mute_members:
			perms += "Mute Members, "
		if role.permissions.deafen_members:
			perms += "Deafen Members, "
		if role.permissions.move_members:
			perms += "Move Members, "
		if role.permissions.use_voice_activation:
			perms += "Use Voice Activation, "
		if role.permissions.change_nickname:
			perms += "Change Nickname, "
		if role.permissions.manage_nicknames:
			perms += "Manage Nicknames, "
		if role.permissions.manage_roles:
			perms += "Manage Roles, "
		if role.permissions.manage_webhooks:
			perms += "Manage Webhooks, "
		if role.permissions.manage_emojis:
			perms += "Manage Emojis, "
			
		if perms is None:
			perms = "None"
		else:perms = perms.strip(", ")

		em.add_field(name='Hoisted', value=str(role.hoist))
		em.add_field(name='Position from bottom', value=str(role.position))
		em.add_field(name='Managed by Integration', value=str(role.managed))
		em.add_field(name='Mentionable', value=str(role.mentionable))
		
		em.add_field(name='People in this role', value=str(rolen))

 
		em.add_field(name='Permissions', value=perms)


		await self.bot.say(embed= em)
		


def setup(bot):
	bot.add_cog(Info(bot))