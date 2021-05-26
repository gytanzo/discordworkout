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

# Register with the program. Necessary to use the bot to begin with. 
@bot.command(name="join")
async def join(ctx):
    # If someone is trying to do this in the wrong channel, don't do anything. 
    if (ctx.message.channel.id != 844327265533165590):
        return

    message = ctx.message
    channel = ctx.channel
    member = message.author
    channel_id = channel.id

    # Delete the message. 
    await message.delete()

    # Remove their "Not Registered" role.
    role = discord.utils.get(member.guild.roles, name='Not Registered')
    await member.remove_roles(role)

    # Add a "Registered" role. 
    role = discord.utils.get(member.guild.roles, name='Registered')
    await member.add_roles(role)

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
    filename = "Users/" + str(channel_id) + ".txt"

    # Open the file that will store the information provided by the user.
    f = open(filename, "w")

       # DM the user the next steps. 
    await member.send("You have been registered. The rest of the registration process will take place through DMs.")
    await member.send("If you have any questions, either now or in the future, please ask them in #help.")
    await member.send("DISCLAIMER: As of right now, this bot only sends you plans for nSuns 5/3/1 workout. In the future, I may add more programs, but for now this is all I've got.") 
    await member.send("ANOTHER DISCLAIMER: I'm going to be asking you for a lot of information to set up your account. Please respond in exactly the format I ask, I won't recognize it otherwise.")
    await member.send("ONE LAST DISCLAIMER: I am **not** a licensed fitness trainer or instructor. Use this application at your own risk, I am not liable for any harm that may or may not come to any persons.")

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
        response = str(int(msg.content))
        await member.send("You answered \"" + response + "\". Is this correct?")
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
        response = str(int(msg.content))
        await member.send("You answered \"" + response + "\". Is this correct?")
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
        response = str(int(msg.content))
        await member.send("You answered \"" + response + "\". Is this correct?")
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
        response = str(int(msg.content))
        await member.send("You answered \"" + response + "\". Is this correct?")
        msg = await bot.wait_for('message', check=check_confirmation)
        if (msg.content.lower() == "no"):
            await member.send("You responded no. Please respond with your bench press 1RM.")
            msg = await bot.wait_for('message', check=check_number)

    bench = response
    f.write(response + "\n")

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
				
    await member.send("All set! I hope to see you for a workout soon!")

    # Send the user's initial (and in the future current) lifts.
    lifts = """\
    Your current lifts are...\n\
    DEADLIFT - {deadlift}\n\
    OVERHEAD PRESS - {press}\n\
    SQUAT - {squat}\n\
    BENCH PRESS - {bench}\
    """.format(deadlift=deadlift, press=press, squat=squat, bench=bench)
    msg = await member.send(lifts)
    await msg.pin()

    f.close()

# Start today's workout. 
@bot.command(name="start")
async def start(ctx):
    # First, this command can't be run in either #server-access or #help. I want it to only be usable in DMs, prevents server clog.
    if (ctx.message.channel.id == 844327265533165590) or (ctx.message.channel.id == 844328208350707712):
        return

    message = ctx.message
    channel = ctx.channel
    member = message.author

    await member.send("Right now, this functionality is missing. Work in progress!")

# Increases a lifts current training max (or TM). 
@bot.command(name="increase")
async def increase(ctx, arg1, arg2):
    # First, this command can't be run in either #server-access or #help. I want it to only be usable in DMs, prevents server clog.
    if (ctx.message.channel.id == 844327265533165590) or (ctx.message.channel.id == 844328208350707712):
        return

    message = ctx.message
    channel = ctx.channel
    member = message.author
    channel_id = channel.id

    # Check if the first argument is valid.
    if arg1 not in ("deadlift", "press", "squat", "bench"):
        await member.send("Your first argument was invalid. Please try again, using one of these four accepted values: \"deadlift\", \"press\", \"squat\", or \"bench\".")
        return

    # Find the users ID and open their file. 
    filename = "Users/" + str(channel_id) + ".txt"
    f = open(filename, "r")

    # Read the lines and find their lifts. 
    lines = f.readlines()
    deadlift = int(lines[1])
    press = int(lines[2])
    squat = int(lines[3])
    bench = int(lines[4])

    # Store the value of the current lift. 
    selected_lift = ""
    selected_val = 0
    if arg1.lower() == "deadlift":
        selected_lift = "deadlift"
        selected_val = deadlift
    elif arg1.lower() == "press":
        selected_lift = "press"
        selected_val = press
    elif arg1.lower() == "squat":
        selected_lift = "squat"
        selected_val = squat
    elif arg1.lower() == "bench":
        selected_lift = "bench"
        selected_val = bench

    # Check if the second argument is more valid. More can go wrong here, more complex error checking.
    if selected_val + int(arg2) > 1200:
        await member.send("You're either a world-class strongman, a superhero, or you're giving me an invalid number. First two are unlikely, last one is rude. Try again.")
        return

    elif int(arg2) == 0:
        await member.send("You're trying to increase your TM by... 0? That doesn't do anything.")
        return

    elif int(arg2) < 0:
        await member.send("You're trying to increase your TM by a negative number. Just use !decrease at that point.")
        return

    old_val = selected_val
    new_val = 0

    # Now we can modify the lift itself. 
    if selected_lift == "deadlift":
        deadlift = deadlift + int(arg2)
        lines[1] = str(deadlift) + "\n"
        new_val = deadlift
    elif selected_lift == "press":
        press = press + int(arg2)
        lines[2] = str(press) + "\n"
        new_val = deadlift
    elif selected_lift == "squat":
        squat = squat + int(arg2)
        lines[3] = str(squat) + "\n"
        new_val = deadlift
    elif selected_lift == "bench":
        bench = bench + int(arg2)
        lines[4] = str(bench)
        new_val = deadlift

    # Open the file again, this time to write. Re-make the file with the updated value. 
    f = open(filename, "w")
    f.writelines(lines)
    f.close()

    # Create the string. 
    lifts = """\
    Your current lifts are...\n\
    DEADLIFT - {deadlift}\n\
    OVERHEAD PRESS - {press}\n\
    SQUAT - {squat}\n\
    BENCH PRESS - {bench}\
    """.format(deadlift=deadlift, press=press, squat=squat, bench=bench)

    # Edit the message. 
    msg_to_edit = (await channel.pins())[0]
    await msg_to_edit.edit(content = lifts)

    # Inform the user their lifts have been changed. 
    updated = """\
        Updated your {selected_lift} value.\n\
        Was: {old_val}\n\
        Now: {new_val}\
    """.format(selected_lift=selected_lift, old_val=old_val, new_val=new_val)
    await member.send(updated)

# Decreases a lifts current TM.
@bot.command(name="decrease")
async def decrease(ctx, arg1, arg2):
    # First, this command can't be run in either #server-access or #help. I want it to only be usable in DMs, prevents server clog.
    if (ctx.message.channel.id == 844327265533165590) or (ctx.message.channel.id == 844328208350707712):
        return

    message = ctx.message
    channel = ctx.channel
    member = message.author
    channel_id = channel.id

    # Check if the first argument is valid.
    if arg1 not in ("deadlift", "press", "squat", "bench"):
        await member.send("Your first argument was invalid. Please try again, using one of these four accepted values: \"deadlift\", \"press\", \"squat\", or \"bench\".")
        return

    # Find the users ID and open their file. 
    filename = "Users/" + str(channel_id) + ".txt"
    f = open(filename, "r")

    # Read the lines and find their lifts. 
    lines = f.readlines()
    deadlift = int(lines[1])
    press = int(lines[2])
    squat = int(lines[3])
    bench = int(lines[4])

    # Store the value of the current lift. 
    selected_lift = ""
    selected_val = 0
    if arg1.lower() == "deadlift":
        selected_lift = "deadlift"
        selected_val = deadlift
    elif arg1.lower() == "press":
        selected_lift = "press"
        selected_val = press
    elif arg1.lower() == "squat":
        selected_lift = "squat"
        selected_val = squat
    elif arg1.lower() == "bench":
        selected_lift = "bench"
        selected_val = bench

    # Check if the second argument is more valid. More can go wrong here, more complex error checking.
    if selected_val - int(arg2) <= 0:
        await member.send("You're attempting to lower your lift below 0. Please try again.")
        return

    elif int(arg2) == 0:
        await member.send("You're trying to decrease your TM by... 0? That doesn't do anything.")
        return

    elif int(arg2) < 0:
        await member.send("You're trying to decrease your TM by a negative number. Just use !increase at that point.")
        return

    old_val = selected_val
    new_val = 0

    # Now we can modify the lift itself. 
    if selected_lift == "deadlift":
        deadlift = deadlift - int(arg2)
        lines[1] = str(deadlift) + "\n"
        new_val = deadlift
    elif selected_lift == "press":
        press = press - int(arg2)
        lines[2] = str(press) + "\n"
        new_val = deadlift
    elif selected_lift == "squat":
        squat = squat - int(arg2)
        lines[3] = str(squat) + "\n"
        new_val = deadlift
    elif selected_lift == "bench":
        bench = bench - int(arg2)
        lines[4] = str(bench)
        new_val = deadlift

    # Open the file again, this time to write. Re-make the file with the updated value. 
    f = open(filename, "w")
    f.writelines(lines)
    f.close()

    # Create the string. 
    lifts = """\
    Your current lifts are...\n\
    DEADLIFT - {deadlift}\n\
    OVERHEAD PRESS - {press}\n\
    SQUAT - {squat}\n\
    BENCH PRESS - {bench}\
    """.format(deadlift=deadlift, press=press, squat=squat, bench=bench)

    # Edit the message. 
    msg_to_edit = (await channel.pins())[0]
    await msg_to_edit.edit(content = lifts)

    # Inform the user their lifts have been changed. 
    updated = """\
        Updated your {selected_lift} value.\n\
        Was: {old_val}\n\
        Now: {new_val}\
    """.format(selected_lift=selected_lift, old_val=old_val, new_val=new_val)
    await member.send(updated)
    

bot.run(TOKEN)