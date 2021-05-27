from helpers import convert

async def monday(ctx):
    # Gather all of the information we'll need.
    message = ctx.message
    channel = ctx.channel
    member = message.author
    channel_id = channel.id

    # Open and read the file. 
    filename = "Users/" + str(channel_id) + ".txt"
    f = open(filename, "r")
    lines = f.readlines()

    # Depending on the day, grab the lifts. For Monday, that's bench and OHP. 
    bench = int(lines[4])
    press = int(lines[2])

    # Calculate the different sets for the workout. 
    warmup_1 = convert(bench, 40, 5)
    warmup_2 = convert(bench, 50, 5)
    warmup_3 = convert(bench, 60, 5)
    t1_1 = convert(bench, 65, 8)
    t1_2 = convert(bench, 75, 6)
    t1_3 = convert(bench, 85, 4)
    t1_4 = convert(bench, 85, 4) 
    t1_5 = convert(bench, 85, 4)
    t1_6 = convert(bench, 80, 5)
    t1_7 = convert(bench, 75, 6)
    t1_8 = convert(bench, 70, 7)
    t1_9 = convert(bench, 65, 8)
    t2_1 = convert(press, 50, 6)
    t2_2 = convert(press, 60, 5)
    t2_3 = convert(press, 70, 3)
    t2_4 = convert(press, 70, 5)
    t2_5 = convert(press, 70, 7)
    t2_6 = convert(press, 70, 4)
    t2_7 = convert(press, 70, 6)
    t2_8 = convert(press, 70, 8)

    # Combine it all into a string. 
    workout = """\
    ***WARMUP - BENCH PRESS***\n\
    {warmup1}\n\
    {warmup2}\n\
    {warmup3}\n\n***T1 - BENCH PRESS***\n\
    {t1_1}\n\
    {t1_2}\n\
    {t1_3}\n\
    {t1_4}\n\
    {t1_5}\n\
    {t1_6}\n\
    {t1_7}\n\
    {t1_8}\n\
    {t1_9}+\n\n***T2 - OVERHEAD PRESS***\n\
    {t2_1}\n\
    {t2_2}\n\
    {t2_3}\n\
    {t2_4}\n\
    {t2_5}\n\
    {t2_6}\n\
    {t2_7}\n\
    {t2_8}\n\nRecommended accessory work: Chest, arms, and back.\
    """.format(warmup1=warmup_1, warmup2=warmup_2, warmup3=warmup_3, t1_1=t1_1, t1_2=t1_2, t1_3=t1_3, t1_4=t1_4, t1_5=t1_5, t1_6=t1_6, t1_7=t1_7, t1_8=t1_8, t1_9=t1_9, t2_1=t2_1, t2_2=t2_2, t2_3=t2_3, t2_4=t2_4, t2_5=t2_5, t2_6=t2_6, t2_7=t2_7, t2_8=t2_8)

    # Send the user their workout. 
    await member.send(workout)

    f.close()

async def tuesday(ctx):
    message = ctx.message
    channel = ctx.channel
    member = message.author
    channel_id = channel.id

    filename = "Users/" + str(channel_id) + ".txt"
    f = open(filename, "r")
    lines = f.readlines()

    squat = int(lines[3])
    deadlift = int(lines[1])

    warmup_1 = convert(squat, 40, 5)
    warmup_2 = convert(squat, 50, 5)
    warmup_3 = convert(squat, 60, 5)
    t1_1 = convert(squat, 75, 5)
    t1_2 = convert(squat, 85, 3)
    t1_3 = convert(squat, 95, 1)
    t1_4 = convert(squat, 90, 3) 
    t1_5 = convert(squat, 85, 3)
    t1_6 = convert(squat, 80, 3)
    t1_7 = convert(squat, 75, 5)
    t1_8 = convert(squat, 70, 5)
    t1_9 = convert(squat, 65, 5)
    t2_1 = convert(deadlift, 50, 5)
    t2_2 = convert(deadlift, 60, 5)
    t2_3 = convert(deadlift, 70, 3)
    t2_4 = convert(deadlift, 70, 5)
    t2_5 = convert(deadlift, 70, 7)
    t2_6 = convert(deadlift, 70, 4)
    t2_7 = convert(deadlift, 70, 6)
    t2_8 = convert(deadlift, 70, 8)

    workout = """\
    ***WARMUP - SQUAT***\n\
    {warmup1}\n\
    {warmup2}\n\
    {warmup3}\n\n***T1 - SQUAT***\n\
    {t1_1}\n\
    {t1_2}\n\
    {t1_3}+\n\
    {t1_4}\n\
    {t1_5}\n\
    {t1_6}\n\
    {t1_7}\n\
    {t1_8}\n\
    {t1_9}\n\n***T2 - SUMO DEADLIFT***\n\
    {t2_1}\n\
    {t2_2}\n\
    {t2_3}\n\
    {t2_4}\n\
    {t2_5}\n\
    {t2_6}\n\
    {t2_7}\n\
    {t2_8}\n\nRecommended accessory work: Legs and abs.\
    """.format(warmup1=warmup_1, warmup2=warmup_2, warmup3=warmup_3, t1_1=t1_1, t1_2=t1_2, t1_3=t1_3, t1_4=t1_4, t1_5=t1_5, t1_6=t1_6, t1_7=t1_7, t1_8=t1_8, t1_9=t1_9, t2_1=t2_1, t2_2=t2_2, t2_3=t2_3, t2_4=t2_4, t2_5=t2_5, t2_6=t2_6, t2_7=t2_7, t2_8=t2_8)

    await member.send(workout)

    f.close()

async def wednesday(ctx):
    message = ctx.message
    channel = ctx.channel
    member = message.author
    channel_id = channel.id

    filename = "Users/" + str(channel_id) + ".txt"
    f = open(filename, "r")
    lines = f.readlines()

    press = int(lines[2])
    bench = int(lines[4])
 
    warmup_1 = convert(press, 40, 5)
    warmup_2 = convert(press, 50, 5)
    warmup_3 = convert(press, 60, 5)
    t1_1 = convert(press, 75, 5)
    t1_2 = convert(press, 85, 3)
    t1_3 = convert(press, 95, 1)
    t1_4 = convert(press, 90, 3) 
    t1_5 = convert(press, 85, 3)
    t1_6 = convert(press, 80, 3)
    t1_7 = convert(press, 75, 5)
    t1_8 = convert(press, 70, 5)
    t1_9 = convert(press, 65, 5)
    t2_1 = convert(bench, 40, 6)
    t2_2 = convert(bench, 50, 5)
    t2_3 = convert(bench, 60, 3)
    t2_4 = convert(bench, 60, 5)
    t2_5 = convert(bench, 60, 7)
    t2_6 = convert(bench, 60, 4)
    t2_7 = convert(bench, 60, 6)
    t2_8 = convert(bench, 60, 8)

    workout = """\
    ***WARMUP - OVERHEAD PRESS***\n\
    {warmup1}\n\
    {warmup2}\n\
    {warmup3}\n\n***T1 - OVERHEAD PRESS***\n\
    {t1_1}\n\
    {t1_2}\n\
    {t1_3}+\n\
    {t1_4}\n\
    {t1_5}\n\
    {t1_6}\n\
    {t1_7}\n\
    {t1_8}\n\
    {t1_9}\n\n***T2 - INCLINE BENCH PRESS***\n\
    {t2_1}\n\
    {t2_2}\n\
    {t2_3}\n\
    {t2_4}\n\
    {t2_5}\n\
    {t2_6}\n\
    {t2_7}\n\
    {t2_8}\n\nRecommended accessory work: Shoulders and chest.\
    """.format(warmup1=warmup_1, warmup2=warmup_2, warmup3=warmup_3, t1_1=t1_1, t1_2=t1_2, t1_3=t1_3, t1_4=t1_4, t1_5=t1_5, t1_6=t1_6, t1_7=t1_7, t1_8=t1_8, t1_9=t1_9, t2_1=t2_1, t2_2=t2_2, t2_3=t2_3, t2_4=t2_4, t2_5=t2_5, t2_6=t2_6, t2_7=t2_7, t2_8=t2_8)
 
    await member.send(workout)

    f.close()

async def thursday(ctx):
    message = ctx.message
    channel = ctx.channel
    member = message.author
    channel_id = channel.id

    filename = "Users/" + str(channel_id) + ".txt"
    f = open(filename, "r")
    lines = f.readlines()

    deadlift = int(lines[1])
    squat = int(lines[3])
 
    warmup_1 = convert(deadlift, 40, 5)
    warmup_2 = convert(deadlift, 50, 5)
    warmup_3 = convert(deadlift, 60, 5)
    t1_1 = convert(deadlift, 75, 5)
    t1_2 = convert(deadlift, 85, 3)
    t1_3 = convert(deadlift, 95, 1)
    t1_4 = convert(deadlift, 90, 3) 
    t1_5 = convert(deadlift, 85, 3)
    t1_6 = convert(deadlift, 80, 3)
    t1_7 = convert(deadlift, 75, 3)
    t1_8 = convert(deadlift, 70, 3)
    t1_9 = convert(deadlift, 65, 3)
    t2_1 = convert(squat, 35, 5)
    t2_2 = convert(squat, 45, 5)
    t2_3 = convert(squat, 55, 3)
    t2_4 = convert(squat, 55, 5)
    t2_5 = convert(squat, 55, 7)
    t2_6 = convert(squat, 55, 4)
    t2_7 = convert(squat, 55, 6)
    t2_8 = convert(squat, 55, 8)

    workout = """\
    ***WARMUP - DEADLIFT***\n\
    {warmup1}\n\
    {warmup2}\n\
    {warmup3}\n\n***T1 - DEADLIFT***\n\
    {t1_1}\n\
    {t1_2}\n\
    {t1_3}+\n\
    {t1_4}\n\
    {t1_5}\n\
    {t1_6}\n\
    {t1_7}\n\
    {t1_8}\n\
    {t1_9}\n\n***T2 - FRONT SQUAT***\n\
    {t2_1}\n\
    {t2_2}\n\
    {t2_3}\n\
    {t2_4}\n\
    {t2_5}\n\
    {t2_6}\n\
    {t2_7}\n\
    {t2_8}\n\nRecommended accessory work: Back and abs.\
    """.format(warmup1=warmup_1, warmup2=warmup_2, warmup3=warmup_3, t1_1=t1_1, t1_2=t1_2, t1_3=t1_3, t1_4=t1_4, t1_5=t1_5, t1_6=t1_6, t1_7=t1_7, t1_8=t1_8, t1_9=t1_9, t2_1=t2_1, t2_2=t2_2, t2_3=t2_3, t2_4=t2_4, t2_5=t2_5, t2_6=t2_6, t2_7=t2_7, t2_8=t2_8)
 
    await member.send(workout)

    f.close()
    
async def friday(ctx):
    message = ctx.message
    channel = ctx.channel
    member = message.author
    channel_id = channel.id

    filename = "Users/" + str(channel_id) + ".txt"
    f = open(filename, "r")
    lines = f.readlines()

    bench = int(lines[4])

    warmup_1 = convert(bench, 40, 5)
    warmup_2 = convert(bench, 50, 5)
    warmup_3 = convert(bench, 60, 5)
    t1_1 = convert(bench, 75, 5)
    t1_2 = convert(bench, 85, 3)
    t1_3 = convert(bench, 95, 1)
    t1_4 = convert(bench, 90, 3) 
    t1_5 = convert(bench, 85, 3)
    t1_6 = convert(bench, 80, 3)
    t1_7 = convert(bench, 75, 5)
    t1_8 = convert(bench, 70, 5)
    t1_9 = convert(bench, 65, 5)
    t2_1 = convert(bench, 40, 6)
    t2_2 = convert(bench, 50, 5)
    t2_3 = convert(bench, 60, 3)
    t2_4 = convert(bench, 60, 5)
    t2_5 = convert(bench, 60, 7)
    t2_6 = convert(bench, 60, 4)
    t2_7 = convert(bench, 60, 6)
    t2_8 = convert(bench, 60, 8)

    workout = """\
    ***WARMUP - BENCH PRESS***\n\
    {warmup1}\n\
    {warmup2}\n\
    {warmup3}\n\n***T1 - BENCH PRESS***\n\
    {t1_1}\n\
    {t1_2}\n\
    {t1_3}+\n\
    {t1_4}\n\
    {t1_5}\n\
    {t1_6}\n\
    {t1_7}\n\
    {t1_8}\n\
    {t1_9}\n\n***T2 - CLOSE GRIP BENCH PRESS***\n\
    {t2_1}\n\
    {t2_2}\n\
    {t2_3}\n\
    {t2_4}\n\
    {t2_5}\n\
    {t2_6}\n\
    {t2_7}\n\
    {t2_8}\n\nRecommended accessory work: Arms and any other areas you think need work..\
    """.format(warmup1=warmup_1, warmup2=warmup_2, warmup3=warmup_3, t1_1=t1_1, t1_2=t1_2, t1_3=t1_3, t1_4=t1_4, t1_5=t1_5, t1_6=t1_6, t1_7=t1_7, t1_8=t1_8, t1_9=t1_9, t2_1=t2_1, t2_2=t2_2, t2_3=t2_3, t2_4=t2_4, t2_5=t2_5, t2_6=t2_6, t2_7=t2_7, t2_8=t2_8)

    await member.send(workout)

    f.close()




# Choose the high level function depending on what program they chose. 
async def workout(ctx, dow):
    message = ctx.message
    member = message.author
    
    # Day is Monday:
    if dow == 0:
        await monday(ctx)

    # Day is Tuesday:
    elif dow == 1:
        await tuesday(ctx)
        
    # Day is Wednesday:
    elif dow == 2:
        await wednesday(ctx)

    # Day is Thursday:
    elif dow == 3:
        await thursday(ctx)

    # Day is Friday:
    elif dow == 4:
        await friday(ctx)

    else:
        await member.send("You aren't working out today.")