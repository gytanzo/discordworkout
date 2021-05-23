import os
import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_member_join(member):
    # DM the user when they join the server. Expand on this functionality later. 
    await member.send(f'Hi {member.name}, welcome to the Discord Workout server! This is a work in progress, check back later.')

@bot.command(name="register")
async def register(ctx):
    # This should check for what channel the user is in, we don't want them to be able to register inside the #help channel.
    # For now, I want to be able to use this inside of #deleteme, so I'll move on. 
    response = "In the future, this will make the bot give a user the \"Registered\" role and then DM the user additional instructions. For now, it is defunct."
    await ctx.send(response)

bot.run(TOKEN)