import os
import os.path
from os import path

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

    message = ctx.message
    member = message.author
    id = message.channel.id

    # Checks if the user sent a valid unit of measurement.
    def check_unit(m):
        if m.content.lower() in ("kg", "lb"):
            return True

    # Checks for a yes or a no. 
    def check_confirmation(m):
        if m.content.lower() in ("yes", "no"):
            return True

    # Checks if the user sent a valid number. 
    def check_number(m):
        return m.content.isnumeric()

    # Checks what kind of workout the user wants. 
    def check_day(m):
        if m.content.lower() in ("four", "five", "six", "4", "5", "6"):
            return True

    def check_setting(m):
        if m.content.lower() in ("manual", "automatic"):
            return True

    def check_time(m):
        time = m.content
        bool = True
        if (len(time) == 4):
            if time[0].isnumeric() == False:
                bool = False
            if time[1] != ":":
                bool = False
            if time[2].isnumeric() == False:
                bool = False
            if time[3].isnumeric() == False:
                bool = False
        elif (len(time) == 5):
            if time[0].isnumeric() == False:
                bool = False
            if time[1].isnumeric() == False:
                bool = False
            if time[2] != ":":
                bool = False
            if time[3].isnumeric() == False:
                bool = False
            if time[4].isnumeric() == False:
                bool = False
        else:
            bool = False
        return bool

    def convert_day_to_int(val):
        if val == "4":
            return "four"
        elif val == "5":
            return "five"
        elif val == "6":
            return "six"
        return val

    # Create a text file using the channel ID. In other words, the channel ID is the users account number!
    filename = "Users/" + str(id) + ".txt"

    # Open the file that will store the information provided by the user.
    f = open(filename, "w")

       # DM the user the next steps. 
    await member.send("You have been registered. The rest of the registration process will take place through DMs.")
    await member.send("If you have any questions, either now or in the future, please ask them in #help.")
    await member.send("DISCLAIMER: As of right now, this bot only sends you plans for nSuns 5/3/1 workout. In the future, I may add more programs, but for now this is all I've got.") 
    await member.send("ANOTHER DISCLAIMER: I'm going to be asking you for a lot of information to set up your account. Please respond in exactly the format I ask, I won't recognize it otherwise.")

    response = ""

    # Find their unit of measurement.
    await member.send("First things first. What unit of weight do you want to use? Respond kg or lb.")
    msg = await bot.wait_for('message', check=check_unit)
    while(msg.content.lower() != "yes"):
        response = msg.content
        await member.send("You answered \"" + msg.content + "\". Is this correct? Please respond yes or no.")
        msg = await bot.wait_for('message', check=check_confirmation)
        if (msg.content.lower() == "no"):
            await member.send("You responded no. Please respond with the unit of weight you wish to use.")
            msg = await bot.wait_for('message', check=check_unit)

    f.write(response + "\n")

    # The next step is finding the 1RMs for each of the four big lifts: deadlift, overhead press, squat, and bench press. 

    deadlift = ""
    press = ""
    squat = ""
    bench = ""

    # First one is the deadlift. 
    await member.send("Got it. Now I need to start jotting down your lifts. This program uses 1RMs, or one rep maxes, to calculate your workout each day. If you need help finding your 1RMs, go to #help.")
    await member.send("To begin, what is your deadlift 1RM?")
    msg = await bot.wait_for('message', check=check_number)
    while(msg.content.lower() != "yes"):
        response = msg.content
        await member.send("You answered \"" + msg.content + "\". Is this correct?")
        msg = await bot.wait_for('message', check=check_confirmation)
        if (msg.content.lower() == "no"):
            await member.send("You responded no. Please respond with your deadlift 1RM.")
            msg = await bot.wait_for('message', check=check_number)

    deadlift = response
    f.write(response + "\n")

    # Next is overhead press. 
    await member.send("Cool, thanks. Next, mind telling me your overhead press 1RM?")
    msg = await bot.wait_for('message', check=check_number)
    while(msg.content.lower() != "yes"):
        response = msg.content
        await member.send("You answered \"" + msg.content + "\". Is this correct?")
        msg = await bot.wait_for('message', check=check_confirmation)
        if (msg.content.lower() == "no"):
            await member.send("You responded no. Please respond with your overhead press 1RM.")
            msg = await bot.wait_for('message', check=check_number)

    press = response
    f.write(response + "\n")

    # Then is squat. 
    await member.send("Recorded. Up next is your squat 1RM.")
    msg = await bot.wait_for('message', check=check_number)
    while(msg.content.lower() != "yes"):
        response = msg.content
        await member.send("You answered \"" + msg.content + "\". Is this correct?")
        msg = await bot.wait_for('message', check=check_confirmation)
        if (msg.content.lower() == "no"):
            await member.send("You responded no. Please respond with your squat 1RM.")
            msg = await bot.wait_for('message', check=check_number)

    squat = response
    f.write(response + "\n")

    # Finally is bench press. 
    await member.send("Jotted that one down too. One more, what's your bench press 1RM?")
    msg = await bot.wait_for('message', check=check_number)
    while(msg.content.lower() != "yes"):
        response = msg.content
        await member.send("You answered \"" + msg.content + "\". Is this correct?")
        msg = await bot.wait_for('message', check=check_confirmation)
        if (msg.content.lower() == "no"):
            await member.send("You responded no. Please respond with your bench press 1RM.")
            msg = await bot.wait_for('message', check=check_number)

    bench = response
    f.write(response + "\n")

	# Move on to some more logistical questions. 
    await member.send("Time to move on to some more logistical questions.")

    # Find how many days the users wants to work out. 
    await member.send("This program has three \"versions\" - a four day, five day, and a six day regimen. Which one of these do you want to do?")
    msg = await bot.wait_for('message', check=check_day)
    while(msg.content.lower() != "yes"):
        response = convert_day_to_int(msg.content)
        await member.send("You answered \"" + msg.content + "\", meaning you will work out " + msg.content + " days a week. Is this correct?")
        msg = await bot.wait_for('message', check=check_confirmation)
        if (msg.content.lower() == "no"):
            await member.send("You responded no. Please respond with the number of days you wish to work out.")
            msg = await bot.wait_for('message', check=check_day)

    f.write(response + "\n")

    # Used to store whether they pick automatic or manual. 
    setting = ""
			
	# Ask them if they want the workout to be automatically sent or not. 
    await member.send("I can send you your program automatically every day at a specified time or you can manually activate the workout. Which do you prefer? Respond \"manual\" or \"automatic\".")
    msg = await bot.wait_for('message', check=check_setting)
    while(msg.content.lower() != "yes"):
        setting = msg.content
        await member.send("You chose the \"" + msg.content + "\" setting. Is this correct?")
        msg = await bot.wait_for('message', check=check_confirmation)
        if (msg.content.lower() == "no"):
            await member.send("You responded no. Please let me know whether you want me to automatically or manually send you your workout.")
            msg = await bot.wait_for('message', check=check_setting)

    f.write(setting + "\n")

    # They don't need to do anything if they chose it to be manual. 
    if (setting.lower() == "manual"):
        await member.send("Since you chose the manual setting, no further action is required.")

    # If it was automatic, they need to specify a time and whether or not they are working out today (since you can't manually ask for the plan).
    elif (setting.lower() == "automatic"):
        await member.send("You chose to have me automatically send you your workout every day. Please provide a time, such as 23:59, for me to so.")
        msg = await bot.wait_for('message', check=check_time)
        while(msg.content.lower() != "yes"):
            response = msg.content
            await member.send("You chose to workout at " + msg.content + ". Is this correct?")
            msg = await bot.wait_for('message', check=check_confirmation)
            if (msg.content.lower() == "no"):
                await member.send("You responded no. Please tell me what time of the day you want to have your workout sent.")
                msg = await bot.wait_for('message', check=check_time)
        f.write(response)
				
    await member.send("And we're all set! I'm going to send a couple messages and pin them, but your work here is done. I hope to see you for a workout soon!")

    # Send the user's initial (and in the future current) lifts.
    lifts = """\
    Your current lifts are...\n\
    DEADLIFT - {deadlift}\n\
    OVERHEAD PRESS - {press}\n\
    SQUAT - {squat}\n\
    BENCH PRESS -{bench}\n\
    """.format(deadlift=deadlift, press=press, squat=squat, bench=bench)
    msg = await member.send(lifts)
    await msg.pin()

    f.close()


bot.run(TOKEN)