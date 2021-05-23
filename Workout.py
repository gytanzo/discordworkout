import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
    # DM the user when they join the server. Expand on this functionality later. 
    await member.send(f'Hi {member.name}, welcome to the Discord Workout server! This is a work in progress, check back later.')

@client.event
async def on_message(message):
    # Check to make sure that this isn't the bot itself sending a message. 
    if message.author == client.user:
        return

    # This should check for what channel the user is in, we don't want them to be able to register inside the #help channel.
    # For now, I want to be able to use this inside of #deleteme, so I'll move on. 
    registration_message = "In the future, this will make the bot give a user the \"Registered\" role and then DM the user additional instructions. For now, it is defunct."

    # Send the message. 
    if message.content.lower() in ("register".lower(), "register ".lower()): # Ignore capitalization, some users may be on mobile where it would capitalize the word for them. Also account for a space. 
        response = registration_message
        await message.channel.send(response)
   
client.run(TOKEN)