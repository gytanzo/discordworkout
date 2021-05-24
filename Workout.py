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
    role = discord.utils.get(member.guild.roles, name='Not Registered')
    await member.add_roles(role)
    await member.send(f'Hi {member.name}, welcome to the Discord Workout server! This is a work in progress, check back later.')

@bot.command(name="join")
async def join(ctx):
    # This should check for what channel the user is in, we don't want them to be able to register inside the #help channel.
    # For now, I want to be able to use this inside of #deleteme, so I'll move on.
    member = ctx.message.author
    await ctx.message.delete()

    role = discord.utils.get(member.guild.roles, name='Not Registered')
    await member.remove_roles(role)

    role = discord.utils.get(member.guild.roles, name='Registered')
    await member.add_roles(role)

    await member.send("You have been registered. The rest of the registration process will take place through DMs.")
    await member.send("If you have any questions, either now or in the future, please ask them in #help.")
    await member.send("To begin... PLACEHOLDER TEXT")


bot.run(TOKEN)