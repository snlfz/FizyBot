import random
import asyncio
import os
import discord
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot


#----------------NOTES----------------#

#dont forget to change help

#change version in info each time
#serverinfo(WIP)
#userinfo (whois)
#Embeds
#whois
#slots

#info (heart)

#help emojified

#add new commands to help

#ping posn change

#------------------VARIABLES--------------#


BOT_PREFIX = (",","$","<@472615266103328778> ","<@472615266103328778>")

TOKEN =os.environ.get(Token) 


COLOUR=0x0



bot =commands.Bot(command_prefix=BOT_PREFIX)
bot.remove_command('help')





#----------------NEW COMMANDS------------------#

	



#-----------------EVENTS-----------------#

    #Playing Status
    

PLAYING="in a super secret garden"

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
       
        
											

#----------------INFO COMMANDS----------------#



#HELP#
@bot.command(pass_context=True, aliases=['h'])
async def help(ctx,arg1= None ):
	
	embed=discord.Embed(
	title="FizyBot to Your Rescue!",
	description="<a:attention:475307661395623936> *Invite me!* [➡️Tap here](https://discordapp.com/oauth2/authorize?client_id=472615266103328778&scope=bot) \n<a:owo:475305390247247873> *Visit me!* [➡️Doorbell](https://discord.gg/JaTEP56)" ,
	colour=discord.Colour(COLOUR))


	dict= {}
	
	dict['invite']= dict['links']= f'*Gives important Invite Links for the Bot* \n▫️**Aliases:** `invite` `links` \n▫️**Usage:** ```>>>,{arg1}```'
	
	dict['info']= dict['about']= f'*Gives a Brief Info about the Bot* \n▫️**Aliases:** `info` `about` \n▫️**Usage:** ```>>>,{arg1}```'
	
	dict['ping']= dict['pong']= f'*Pong! Displays the Bot\'s Latency.* \n▫️**Aliases:** `ping` `pong` `latency` \n▫️**Usage:** ```>>>,{arg1}```'

	dict['purge']= dict['delete']= f'*Deletes chats from the Channel where it\'s used in.* \n▫️**Parameters:** [`number of messages`] \n▫️**Aliases:** `purge` `delete` \n▫️**Usage:** ```>>>,{arg1} 3```*3 messages deleted from* ***#channel***'
	
	dict['greet']= dict['hi']= f'*Simply Greets You!* \n▫️**Aliases:** `greet` `hi` \n▫️**Usage:** ```>>>,{arg1}```'

	dict['8ball']= dict['8-ball']= dict['eightball']= f'*Ask me anything and get an answer!* \n▫️**Aliases:** `8ball` `8-ball` `eightball` \n▫️**Parameters:** [`question`] \n▫️**Usage:** ```>>>,{arg1} Do You Like Pizza??```*Yeah sure but no Pineapples Please.*'
	
	dict['cointoss']= dict['coin']= dict['coinflip']= f'*Can\'t decide on something? Flip a Coin!* \n▫️**Aliases:** `cointoss` `coin` `coinflip` \n▫️**Usage:** ```>>>,{arg1}```'
	
	dict['slots']= dict['jackpot']= f'*Win the JACKPOT!* \n▫️**Aliases:** `slots` `jackpot` \n▫️**Usage:* ```>>>,{arg1}```*Did You Win?*'
	
	dict['embed']= f'*Create a custom Embed of Your Own!* \n▫️**Aliases:** `embed` \n▫️**Parameters:** [`#channel`] [`Title!`] [`Description!`] <`Hex color Code`> <`Thumbnail url`> \n▫️**Usage:** ```>>>,{arg1} #general "Hello World!" "This is my First embed!" ffffff https://i.imgur.com/5mCccjN.gif```[Tap here to see the result](https://i.imgur.com/8Ld1Lxq.mp4) ```,{arg1} #gamers WhoLetTheDogsOut! \"Who Who Who Who. Just Tell me Who :dog:\" 51ff00```[Tap here to see the result!](https://i.imgur.com/9AqMl5I.jpg)'
	
	dict['whois']= dict['userinfo']= f'*Get Info about a specific user.* \n**Aliases:** `whois` `userinfo` \n▫️**Parameters:** [`@user`] \n▫️**Usage:** ```>>>,{arg1} @Somebody#6969```'
	
	dict['avatar']= f'*Get the Avatar for any user!* \n▫️**Aliases:* `avatar` \n▫️**Parameters:** [`@user`] \n▫️**Usage:** ```>>>,{arg1} @ARandomGuy#0911```'

	dict['serverinfo']= dict['server']= f'*Fetches Information about the Server.* \n▫️**Aliases:** `serverinfo` `server` \n▫️**Usage:** ```>>>,{arg1}```'
	
	dict['echo']= dict['say']= f'*Makes the Bot repeat What you say!* \n▫️**Aliases:** `echo` `say` \n▫️**Parameters:** [`whatever you want to say`] \n▫️**Usage:** ```>>>,{arg1} Hey Morty Ssup!```*Hey Morty Ssup!*'
	
	dict['add']= dict['sum']= f'*Adds any Two Numbers.* \n▫️**Aliases:** `add` `sum` \n▫️**Parameters:** [`number1`] [`number2`] ▫️**Usage:** ```>>>,{arg1} 13 7.98```*Is it 20.98?*'
	
	dict['subtract']= dict['sub']= f'*Subtracts any Two Numbers.* \n▫️**Aliases:** `subtract` `sub` \n▫️**Parameters:** [`number1`] [`number2`] ▫️**Usage:** ```>>>,{arg1} 13 7.98```*°.°*'
	
	dict['multiply']= dict['mult']= f'*Multiplies any Two Numbers.* \n▫️**Aliases:** `multiply` `mult` \n▫️**Parameters:** [`number1`] [`number2`] ▫️**Usage:** ```>>>,{arg1} 13 7.685```*Whoa dude*'
	
	dict['divide']= dict['div']= f'*Divides any Two Numbers.* \n▫️**Aliases:** `add` `sum` \n▫️**Parameters:** [`number1`] [`number2`] ▫️**Usage:** ```>>>,{arg1} 153 7.98```*I can\'t. I just can\'t*'
	
	dict['square']= dict['sq']= f'*Finds the Square of a Number. Because Why not!* \n▫️**Aliases:** `square` `sq` \n▫️**Parameters:** [`number`] ▫️**Usage:** ```>>>,{arg1} 296.207```*answer is CH₃COONa*'
	
	

	blank="<:blank:476086983614136330>"
	
	
	if (arg1 is None):
		embed.add_field(
		name="OwO" ,
		value=f"__**Essential**__     \n▫️`,invite` *Fetches important links.*     \n▫️`,info` *Gives a Brief Info of the Bot.*\n▫️`,ping` *Pong!*     \n {blank} \n__**Moderation**__     \n▫️`,purge` *Purges Stuff from the Chat.*     \n {blank} \n__**Pointless & Fun**__     \n▫️`,greet` *Greets You!*     \n▫️`,8ball` *Get Answers to Almost any Question!*     \n▫️`,cointoss` *Heads/Tails?*     \n▫️`,slots` *Win the Jackpot!*    \n {blank} \n__**Utility**__     \n▫️`,embed` *Create a Custom Embed of your Own!*     \n▫️`,whois` *Info about Users*     \n▫️`,avatar` *Get someone's Avatar.*     \n▫️`,serverinfo` *Get Information about the Server.*     \n▫️`,echo` *Make the Bot say Anything!*     \n {blank} \n__**Math**__     \n▫️`,add` *Adds any 2 Numbers.*     \n▫️`,subtract` *Subtracts any 2 Numbers.*     \n▫️`,multiply` *Multiplies any 2 Numbers.*     \n▫️`,divide` *Divides any 2 Numbers.*\n {blank} ")
		
		embed.set_footer(text="To see detailed Info and Aliases of a command, Type `,help <command>`. To see that for all commands, Type `,help all`")
	
	
	elif (arg1 is not None ):
		
		if ( arg1 in dict ) : embed.add_field( name=","+arg1, value =dict[arg1])
		
#		elif ( arg1 == "all") :
#			for key in sorted(dict.keys()):
#				embed.add_field(name=f",{key}" , value=dict[key])
		
		else : embed.add_field( name=f"Command `,{arg1}` not found." ,value="Type `,help` to get a List of All Commands.")


 
#	yee=
	await bot.say(embed=embed)
#	await asyncio.sleep(60)
#	await bot.delete_message(yee)   
    
    
    
#Invite
@bot.command(pass_context=True,aliases=["links"])
async def invite(ctx):
    embed=discord.Embed(
    colour=discord.Colour(COLOUR)
    )
    embed.set_author(name='Links!')

    embed.add_field(name='<a:attention:475307661395623936> *Invite me!*' , value=" [➡️Tap here](https://discordapp.com/oauth2/authorize?client_id=472615266103328778&scope=bot)")
    embed.add_field(name='<a:owo:475305390247247873> *Visit me!* ', value='[➡️Doorbell](https://discord.gg/JaTEP56)')
           
           
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
    embed.set_author(name='FizyBot v0.0.7 alpha - in vigorous development!')
    embed.add_field(name="*Made with Python* <a:heart:475305073262592010>", value="by *fizy#9347*")
 
           
  #  yee=
    await bot.say(embed=embed)
  #  await asyncio.sleep(60)
  #  await bot.delete_message(yee)
 
    
    #ping
@bot.command(pass_context=True, aliases=['pong','latency'])
async def ping(ctx):
	embed1=discord.Embed( description='<a:loading:474402569544925205>  Pong! Loading...' ,colour=COLOUR)
	resp = await bot.say(embed=embed1)
	diff = resp.timestamp - ctx.message.timestamp
	embed2=discord.Embed( description=f'<a:ablobthinkingfast:474762165325135882> Pong! That took {1000*diff.total_seconds():.1f}ms.',colour=COLOUR)
	await bot.edit_message(resp, embed=embed2)
    	





#----------------FUN-----------------#




    #greet
@bot.command(pass_context=True) 
async def greet(ctx): 
    await bot.say("<a:ablobwave:474874458780205066>  Hello, there!\n "+ ctx.message.author.mention ) 



    	
 
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


	#cointoss

@bot.command(aliases=['cointoss','coinflip'],pass_context=True)
async def coin(ctx):
    choice=random.randint(1,2)
    if choice == 1:
	    await bot.add_reaction(ctx.message,"🌑")
    if choice == 2:
        await bot.add_reaction(ctx.message,"🌕")
	

	#slotmachine!

@bot.command(pass_context=True,aliases=['slots','jackpot'])
async def slot(ctx):
        
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)
        user=ctx.message.author.mention
        
        embed=discord.Embed(colour=COLOUR)
        slot=f"**[ {a} {b} {c} ]**"
        if (a == b == c):
            embed.add_field(name=slot,value=f"**{user}**, All matching, Jackpot! <a:shake:475305983195742211> ")
        elif (a == b) or (a == c) or (b == c):
            embed.add_field(name=slot,value=f"**{user}**, 2 in a row, you won! <a:grin:475304794958069760> ")
        else:
            embed.add_field(name=slot,value=f"**{user}**, No match, you lost <a:triggered:475838149692751873> ")
        
        await bot.say(embed=embed)






#----------------MODERATION COMMANDS----------------#


 
    


    #Purge
@bot.command(pass_context=True, aliases=['delete'])
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
 

#----------------UTILITY COMMANDS----------------#



    # Embeds 
@bot.command()
async def embed(arg1:discord.Channel, arg2, arg3, arg4= "0", arg5= None ):

	eChannel =arg1
	eTitle =arg2		
	eDescription = arg3
	eColour = arg4
	eThumbnail = arg5

	
	
	embed = discord.Embed(title = eTitle, description = eDescription , colour = int(f"0x{eColour}",16))

	if (arg5 !=None):
		embed.set_thumbnail(url=arg5)
	
	await bot.send_message( arg1,embed =embed)

    #echo
@bot.command(aliases=['say'])
async def echo(*args):
        output=''
        for word in args:
          	output+= word
          	output+= ' '
        await bot.say(output)
        

	#avatar(done)
@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member = None):
        
        if user is None:
            user = ctx.message.author
        embed = discord.Embed(description=f"It's {user.mention}, everyone! <a:shades:475306116839112705> ", colour=COLOUR)
        embed.set_image(url=user.avatar_url)
        
        await bot.say(embed=embed)




	#whois
@bot.command(pass_context=True, aliases =['userinfo']) 
async def whois(ctx, member: discord.Member =None):
	
	if member is None:
		member = ctx.message.author
	time = member.joined_at.date()
	embed=discord.Embed(title=f"{member.name} ? Lemme check", description ="Here's what I Found <a:think2:475306370661351424> ",color =COLOUR)
	
	
	embed.add_field(name="Username", value=f"{member}", inline=True )
	embed.add_field(name="Nickname", value=member.nick if hasattr(member, "nick") else "None", inline=True)
	embed.add_field(name="Account created", value=(member.created_at), inline=True)
	embed.add_field(name="Status", value=f"{member.status}".capitalize(), inline=True)
	embed.add_field(name="Member since", value=time, inline=True)
	embed.add_field(name="Roles",value=', '.join([f"<@&{x.id}>" for x in member.roles if x is not ctx.message.server.default_role]) if len(member.roles) > 1 else 'None',
            inline=False
        )
	embed.set_thumbnail(url=member.avatar_url)
	
	
	await bot.say(embed=embed)


	
	
		
	#serverinfo(done)



@bot.command(pass_context=True, aliases=["server"])
async def serverinfo(ctx):
    embed = discord.Embed(title="{}'s info".format(ctx.message.server.name), description="Here's what I could find <a:whee:475307014675890216> ", color=COLOUR)
    
    findbots = sum(1 for member in ctx.message.server.members if member.bot)
    roles=ctx.message.server.roles 
    
    embed.set_author(name="Server Info")
    embed.add_field(name="Name", value=str(ctx.message.server.name)+ f" [ID: {str(ctx.message.server.id)}]" , inline=True)
    embed.add_field(name="Owner", value=ctx.message.server.owner.mention)
    embed.add_field(name="Region", value=ctx.message.server.region, inline=True)
    embed.add_field(name="Created At", value=(ctx.message.server.created_at), inline=True)
    embed.add_field(name="Roles", value=', '.join([f"<@&{x.id}>" for x in ctx.message.server.roles]),inline=True)
    embed.add_field(name="Members", value=str(ctx.message.server.member_count)+f" ,of which \n**Bots** : {str(findbots)}\n**Humans** :{str(ctx.message.server.member_count - findbots)}" , inline=True)
    
    
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)




#-----------------MATH COMMANDS----------------#

    #add
@bot.command(pass_context=True, aliases=['sum'])
async def add(ctx, a:float, b:float):
    await bot.say(a+b)
    
    

    #subtract
@bot.command(pass_context=True, aliases=['sub'])
async def subtract(ctx, a:float, b:float):
    await bot.say(a-b)


    #multiply
@bot.command(pass_context=True, aliases=['mult'])
async def multiply(ctx, a: float, b: float):
    await bot.say(a*b)


    #divide
@bot.command(pass_context=True, aliases=['div'])
async def divide(ctx, a:float, b:float):
    await bot.say(a/b)
    


    #Square
@bot.command(aliases=['sq'])
async def square(number):
    squared_value = float(number) * float(number)
    await bot.say(str(number) + " squared is " + str(squared_value))





#-----------------RUN----------------#
bot.run(TOKEN)