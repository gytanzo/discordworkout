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
    await ctx.message.delete()

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
    await member.send("As of right now, this bot only sends you plans for nSuns 5/3/1 workout. In the future, I may add more programs, but for now this is all I've got.")  

    # Begin registering the user. The first step is finding the 1RMs for each of the four big lifts: deadlift, overhead press, squat, and bench press. 

    await member.send("To start, what is your deadlift 1RM?")
    # Wait for response.
    await member.send("You answered {VALUE}. Is this correct? Please respond yes or no.")
    # Wait for response. If no, ask the original question again. 

    await member.send("Got it. I've recorded your deadlift 1RM as {VALUE}. Next, what is your overhead press 1RM?")
    # Wait for response.
    await member.send("You answered {VALUE}. Is this correct?")
    # Wait for response. If invalid response, redirect them to use yes/no. If no, ask the original question again.

    await member.send("Got it. I've recorded your overhead press 1RM as {VALUE}. Next, what is your squat 1RM?")
    # Wait for response.
    await member.send("You answered {VALUE}. Is this correct?")
    # Wait for response. If invalid response, redirect them to use yes/no. If no, ask the original question again.

    await member.send("Got it. I've recorded your squat 1RM as {VALUE}. Finally, what is your bench press 1RM?")
    # Wait for response.
    await member.send("You answered {VALUE}. Is this correct?")
    # Wait for response. If invalid response, redirect them to use yes/no. If no, ask the original question again.

    await member.send("Understood. I've recorded your bench press 1RM as {VALUE}. Now, let's move onto some logistical questions.")
    await member.send("This program has three variations: a four day, a five day, and a six day routine. Which one of these do you wish to do? This can be changed later.")
    # Wait for response. If invalid, redirect them to respond 4/5/6 or four/five/six. 
    await member.send("You answered {VALUE}. Is this correct?")
    # Wait for response. If invalid response, redirect them to use yes/no. 
    await member.send("You want to do the {VALUE} program. Please provide the {VALUE} days of the week you want to work out. These can be changed later. ")
    # Wait for response. If invalid (not a day of the week), redirect them to respond with a day of the week. 
    await member.send("You responded with {DAYS}. Are these days correct?")

    await member.send("Noted. Last question: I can have this program automatically send you the routine every day at a specific time or you can manually activate it. Which do you want? Answer \"manual\" or \"automatic\". This can be changed later.")
    # Wait for response. Correct if invalid. 
    await member.send("You answered {VALUE}. Is this correct?")
    # Wait for response. If invalid response, redirect them to use yes/no. 
    await member.send("Got it, I'll do that. You're all set, I'll see you soon for your first workout!")


bot.run(TOKEN)