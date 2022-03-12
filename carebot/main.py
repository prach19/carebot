import os
import nextcord
import requests
import json
from nextcord.ext import commands
from nextcord.utils import get
from asyncio import sleep as s
from alive import alive

client = commands.Bot(command_prefix = '~')

@client.event
async def on_ready():
  print('running')


@client.command()
##embed for help##
async def helper(ctx):
  embed = nextcord.Embed(
    title = 'help',
    description = 'this is a list of my commands!'
  )
  embed.add_field(name = 'wanna create a reminder?', value = 'use ~remind @username time units (choose from s, m, h, d) message', inline = False)
  embed.add_field(name = 'want a bob ross quote?', value = 'use ~bob', inline = False)
  embed.add_field(name = 'bored? get an activity to do', value = 'use ~bored', inline = False)
  
  await ctx.send(embed=embed)

@client.command()
async def bored(ctx):
    r = requests.get('http://www.boredapi.com/api/activity/').json()
    task = r['activity']
    await ctx.send(task)

@client.command()
async def bob(ctx):
    g = requests.get('https://api.bobross.dev/api').json()
    quote = g['response'][0]['quote']
    await ctx.send(quote)

@client.command()
async def remind(ctx, person: nextcord.Member, time: float, units, *, msg):
  
  if True:
    if (units == 's'):
      await s(time)
    elif (units == 'm'):
      await s(time*60)
    elif (units == 'h'):
      await s(time*3600)
    elif (units == 'd'):
      await s(time*86400)

  await ctx.send(f'{person.mention}, {ctx.author.mention} is reminding you: {msg}')


alive()
client.run(os.getenv('TOKEN'))
