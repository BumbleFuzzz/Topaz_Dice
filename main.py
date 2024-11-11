import discord
from discord.ext import commands, tasks
import random
import re
import testing as tes
import dice as d
import ops as o
from flask import Flask
from threading import Thread
import itertools as it

app = Flask(__name__)

@app.route('/')
def main():
  return "Your Bot Is Ready"

def run():
  app.run(host="0.0.0.0", port=8000)

def keep_alive():
  server = Thread(target=run)
  server.start()


description = '''A Dice-Rolling bot that has just a few other functionalities.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix = '~', description = description, intents = intents)

status = it.cycle(['with Python','JetHub'])

@bot.event
async def on_ready():
  change_status.start()
  print("Your bot is ready")

@tasks.loop(seconds=10)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))

def helpEmbed():
		embed = discord.Embed(
						color = discord.Colour.orange(),
						title='Help'
		)
		embed.add_field(name='~cmdhelp', value='This message',inline=False)
		embed.add_field(name='~ping', value='Returns Pong!',inline=False)
		embed.add_field(name='~roll', value='Rolls a dice in a NdN format. dN is accepted as well.',inline=False)
		embed.add_field(name='~slap', value='The DM can slap stupid players',inline=False)
		
		return embed

def checkRole(ctx,desiredRole):
		ans = False
		for role in ctx.author.roles:
				if str(role) == desiredRole:
						ans = True
		return ans

@bot.event
async def on_ready():
		print(f'Logged in as {bot.user} (ID: {bot.user.id})')
		print('------')

@bot.command()
async def slap(ctx, slapped: discord.User, *message: str):
		if(checkRole(ctx, 'DM')):
				message = ' '.join(message)
				send = discord.Embed(title = None, description = f"{ctx.author.mention} slapped {slapped.mention} for {message}")
				await ctx.send(embed = send)
		else:
			send = discord.Embed(title = None, description = 'This fun command is only for DMs sorry :(')
			await ctx.send(embed = send)

@bot.command()
async def spray(ctx, spray: discord.User):
		liquids = ["water", "juice", "soda", "milk", "bleach", "chloroform", "nitroglycerin", "Raid Multi Insect Spray", "mayonnaise", "... something .."]
		liquid = random.choice(liquids)
		send = discord.Embed(title = None, description = f"{spray.mention} has been sprayed with {liquid}.")
		await ctx.send(embed = send)

@bot.command()
async def roll(ctx, *message: str):
	message = ' '.join(message)
	message = re.split("([+|×|÷|/|<|>|%|*|-|' '|~])", message)
	for x in range(0,10000):
		for a in message:
			if (str.isspace(a)) or (a == ''):
				message.remove(a)
	theChaos = message
	a = 0
	while (len(theChaos) >= 1) or (tes.checkInt(theChaos[0]) == False):
		
		if (tes.checkIndex(theChaos, a) == False):
			break
			
		if (tes.checkIndex(theChaos, a + 1)) and ((theChaos[a+1] == "<") or (theChaos[a+1] == ">")):
			if tes.checkIndex(theChaos, a + 2) == False:
				if theChaos[a+1] == "<":
					list = d.rollADice(theChaos[a])
					list.sort()
					for l in list:
						x = list.index(l)
						e = list.pop(x)
						e = str(e)
						list.insert(x,e)
					list = ', '.join(list)
					answer = list
					break
				if theChaos[a+1] == ">":
					list = d.rollADice(theChaos[a])
					list.sort(reverse = True)
					for l in list:
						x = list.index(l)
						e = list.pop(x)
						e = str(e)
						list.insert(x,e)
					list = ', '.join(list)
					answer = list
					break
			if theChaos[a+2] == "ml":
				if theChaos[a+1] == "<":
					list = d.rollADice(theChaos[a])
					list.sort()
					list.pop(0)
					for l in list:
						x = list.index(l)
						e = list.pop(x)
						e = str(e)
						list.insert(x,e)
					list = ', '.join(list)
					answer = list
					break
				if theChaos[a+1] == ">":
					list = d.rollADice(theChaos[a])
					if theChaos[a+1] == ">":
						list.sort(reverse = True)
						list.pop(-1)
					for l in list:
						x = list.index(l)
						e=list.pop(x)
						e = str(e)
						list.insert(x,e)
					list = ', '.join(list)
					answer = list
					break
				
			if theChaos[a+2] == "mg":
				if theChaos[a+1] == "<":
					list = d.rollADice(theChaos[a])
					list.sort()
					list.pop(-1)
					for l in list:
						x = list.index(l)
						e = list.pop(x)
						e = str(e)
						list.insert(x,e)
					list = ', '.join(list)
					answer = list
					break
				if theChaos[a+1] == ">":
					list = d.rollADice(theChaos[a])
					list.sort(reverse = True)
					list.pop(0)
					for l in list:
						x = list.index(l)
						e = list.pop(x)
						e = str(e)
						list.insert(x,e)
					list = ', '.join(list)
					answer = list
					break
		
		if (theChaos[a] == "×") or (theChaos[a] == "+") or (theChaos[a] == "÷") or (theChaos[a] == "/") or (theChaos[a] == "%") or (theChaos[a] == "*") or (theChaos[a] == "-"):
			
			if theChaos[a] == theChaos[0]:
				print("invalid")
				return 1
		
			elif (tes.checkInt(theChaos[a - 1]) == False) and (tes.checkInt(theChaos[a + 1]) == False):
				answer = o.Op(theChaos[a],sum(d.rollADice(theChaos[a - 1])),sum(d.rollADice(theChaos[a + 1])))
			
			elif (tes.checkInt(theChaos[a - 1]) == True) and (tes.checkInt(theChaos[a + 1]) == False):
				answer = o.Op(theChaos[a],int(theChaos[a - 1]),sum(d.rollADice(theChaos[a + 1])))
			
			elif (tes.checkInt(theChaos[a - 1]) == False) and (tes.checkInt(theChaos[a + 1]) == True):
				answer = o.Op(theChaos[a],sum(d.rollADice(theChaos[a - 1])),int(theChaos[a + 1]))
		
			elif (tes.checkInt(theChaos[a - 1]) == True) and (tes.checkInt(theChaos[a + 1]) == True):
				answer = o.Op(theChaos[a],int(theChaos[a - 1]),int(theChaos[a + 1]))
			
			for c in range(1, 4):
				theChaos.pop(a - 1)
			
			theChaos.insert(a - 1, answer)
				
			a -= 1
		
		else:
			if (tes.checkIndex(theChaos, a + 1) == True) and (theChaos[a+1] == "~"):
				list = d.rollADice(theChaos[a])
				for l in list:
					x = list.index(l)
					e = list.pop(x)
					e = str(e)
					list.insert(x,e)
				list = ', '.join(list)
				answer = list
				break
			else:
				theChaos.insert(a,sum(d.rollADice(theChaos.pop(a))))
				answer = theChaos[a]
				
		a += 1

	answer = discord.Embed(title = f"{ctx.author.display_name}'s Roll", description = f'{answer}')
	await ctx.send(embed = answer)

@bot.command()
async def ping(ctx):
    print(f'{ctx.channel.id}')
    await ctx.send(f'Pong!')

@bot.command()
async def cmdhelp(ctx):
  await ctx.channel.send(embed=helpEmbed())



bot.run('BOT_TOKEN')

