import os
import os.path
from os import path

import discord
from dotenv import load_dotenv
from discord.ext import commands

from datetime import datetime
from helpers import get_change, check_unit, check_confirmation, check_number, check_day, convert_day_to_int
import day4 as four
import day5 as five
import day6 as six

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

# Register sender with the program. 
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

    # Store the users ORIGINAL lifts. These never get updated, they are here to stay!
    f.write(deadlift + "\n")
    f.write(press + "\n")
    f.write(squat + "\n")
    f.write(bench + "\n")

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
        new_val = press
    elif selected_lift == "squat":
        squat = squat + int(arg2)
        lines[3] = str(squat) + "\n"
        new_val = squat
    elif selected_lift == "bench":
        bench = bench + int(arg2)
        lines[4] = str(bench)
        new_val = bench

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
        new_val = press
    elif selected_lift == "squat":
        squat = squat - int(arg2)
        lines[3] = str(squat) + "\n"
        new_val = squat
    elif selected_lift == "bench":
        bench = bench - int(arg2)
        lines[4] = str(bench)
        new_val = bench

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

# Informs the user how much they've improved since they started using the program.
@bot.command(name="improved")
async def improved(ctx):
    # First, this command can't be run in either #server-access or #help. I want it to only be usable in DMs, prevents server clog.
    if (ctx.message.channel.id == 844327265533165590) or (ctx.message.channel.id == 844328208350707712):
        return

    message = ctx.message
    channel = ctx.channel
    member = message.author
    channel_id = channel.id

    # Find the users ID and open their file. 
    filename = "Users/" + str(channel_id) + ".txt"
    f = open(filename, "r")

    # Read the lines and find their lifts. 
    lines = f.readlines()
    cur_deadlift = int(lines[1])
    og_deadlift = int(lines[5])
    pc_dead = str(get_change(cur_deadlift, og_deadlift)) + "%"
    cur_press = int(lines[2])
    og_press = int(lines[6])
    pc_press = str(get_change(cur_press, og_press)) + "%"
    cur_squat = int(lines[3])
    og_squat = int(lines[7])
    pc_squat = str(get_change(cur_squat, og_squat)) + "%"
    cur_bench = int(lines[4])
    og_bench = int(lines[8])
    pc_bench = str(get_change(cur_bench, og_bench)) + "%"

    change = """\
    Here's how much you've improved since you began using me.\n\
    DEADLIFT - Originally {og_dead}, now {cur_dead}. That's a {pc_dead} increase!\n\
    OVERHEAD PRESS - Originally {og_press}, now {cur_press}. That's a {pc_press} increase!\n\
    SQUAT - Originally {og_squat}, now {cur_squat}. That's a {pc_squat} increase!\n\
    BENCH PRESS - Originally {og_bench}, now {cur_bench}. That's a {pc_bench} increase!\n\
    """.format(og_dead=og_deadlift, cur_dead=cur_deadlift, pc_dead=pc_dead, og_press = og_press, cur_press=cur_press, pc_press=pc_press, og_squat=og_squat, cur_squat=cur_squat, pc_squat=pc_squat, og_bench=og_bench, cur_bench=cur_bench, pc_bench=pc_bench)

    await member.send(change)

# Start today's workout. 
@bot.command(name="start")
async def start(ctx):
    # First, this command can't be run in either #server-access or #help. I want it to only be usable in DMs, prevents server clog.
    if (ctx.message.channel.id == 844327265533165590) or (ctx.message.channel.id == 844328208350707712):
        return

    channel = ctx.channel
    channel_id = channel.id

    # Find the users ID and open their file. 
    filename = "Users/" + str(channel_id) + ".txt"
    f = open(filename, "r")

    # Read the lines. We need to know everything for this command. 
    lines = f.readlines()
    user_plan = lines[9] # This represents whether they picked a four, five, or six day plan. 

    dayofweek = datetime.today().weekday()
    
    # Working out four days a week. 
    if (user_plan == "four\n"):
        await four.workout(ctx, dayofweek)

    # Working out five days a week. 
    elif (user_plan == "five\n"):
        await five.workout(ctx, dayofweek)
    
    # Working out six days a week. 
    elif (user_plan == "six\n"):
        await six.workout(ctx, dayofweek)

# Simply sends the user a link to the public GitHub repository.
@bot.command(name="source")
async def source(ctx):
    # First, this command can't be run in either #server-access or #help. I want it to only be usable in DMs, prevents server clog.
    if (ctx.message.channel.id == 844327265533165590) or (ctx.message.channel.id == 844328208350707712):
        return

    message = ctx.message
    channel = ctx.channel
    member = message.author
    channel_id = channel.id

    await member.send("Link to the GitHub repository: https://github.com/gytanzo/discordworkout")
    

bot.run(TOKEN)
