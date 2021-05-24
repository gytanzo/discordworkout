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
    # When the user joins, give them a "Not Registered" role to limit their access to the first channel. 
    role = discord.utils.get(member.guild.roles, name='Not Registered')
    await member.add_roles(role)

@bot.command(name="join")
async def join(ctx):
    # If someone is trying to do this in the wrong channel, don't do anything. 
    if (ctx.message.channel.id != 844327265533165590):
        return

    # Delete the message. 

    # Find the member that sent it for registration purposes. 
    member = ctx.message.author

    # Remove their "Not Registered" role.
    role = discord.utils.get(member.guild.roles, name='Not Registered')
    await member.remove_roles(role)

    # Add a "Registered" role. 
    role = discord.utils.get(member.guild.roles, name='Registered')
    await member.add_roles(role)

    # DM the user the next steps. 
    await member.send("You have been registered. The rest of the registration process will take place through DMs.")
    await member.send("If you have any questions, either now or in the future, please ask them in #help.")
    await member.send("To begin... PLACEHOLDER TEXT")


bot.run(TOKEN)