import discord
import datetime
import random
import os
import json
import requests
from discord.ext import commands


def get_prefix(client, message):
    with open('C:/Users/olafm/OneDrive/Desktop/mathify/MATH-BOT/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix=get_prefix)
client.remove_command('help')
token = os.environ.get("DISCORD_BOT_SECRET")


@client.event
async def on_guild_join(guild):
    with open('C:/Users/olafm/OneDrive/Desktop/mathify/MATH-BOT/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = 'm!'

    with open('C:/Users/olafm/OneDrive/Desktop/mathify/MATH-BOT/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=2)


@client.event
async def on_guild_remove(guild):
    with open('C:/Users/olafm/OneDrive/Desktop/mathify/MATH-BOT/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('C:/Users/olafm/OneDrive/Desktop/mathify/MATH-BOT/prefixes.json', 'w') as f:
        json.dump(prefixes, f)


@client.event
async def on_ready():
    print('bot is online')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{str(len(set(client.get_all_members())))} users do math! m!help for commands'))


@client.command()
@commands.has_permissions(administrator=True)
async def prefix(ctx, *, prefix):
    with open('C:/Users/olafm/OneDrive/Desktop/mathify/MATH-BOT/prefixes.json', 'r') as f:
        prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] =  prefix
  
    with open('C:/Users/olafm/OneDrive/Desktop/mathify/MATH-BOT/prefixes.json', 'w') as f:
        json.dump(prefixes, f)

    await ctx.send(f'Prefix is now **{prefix}**')

@client.command()
async def add(ctx, arg1, arg2):
    equationAnswer = int(arg1)++int(arg2)
    embed = discord.Embed(title="Addition", color=0xff0000, timestamp=datetime.datetime.utcnow())
    embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
    embed.add_field(name=f"Equation: {arg1} + {arg2}", value=f"Answer: {equationAnswer}", inline=False)
    await ctx.send(embed=embed)


@client.command()
async def subtract(ctx, arg1, arg2):
    equationAnswer = int(arg1) - int(arg2)
    embed = discord.Embed(title="Subtraction", color=0xff0000, timestamp=datetime.datetime.utcnow())
    embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
    embed.add_field(name=f"Equation: {arg1} - {arg2}", value=f"Answer: {equationAnswer}", inline=False)
    await ctx.send(embed=embed)


@client.command()
async def multiply(ctx, arg1, arg2):
    equationAnswer = int(arg1) * int(arg2)
    embed = discord.Embed(title="Multiplication", color=0xff0000, timestamp=datetime.datetime.utcnow())
    embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
    embed.add_field(name=f"Equation: {arg1} x {arg2}", value=f"Answer: {equationAnswer}", inline=False)
    await ctx.send(embed=embed)


@client.command()
async def divide(ctx, arg1, arg2):
    equationAnswer = int(arg1) / int(arg2)
    embed = discord.Embed(title="Division", color=0xff0000, timestamp=datetime.datetime.utcnow())
    embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
    embed.add_field(name=f"Equation: {arg1} / {arg2}", value=f"Answer: {equationAnswer}", inline=False)
    await ctx.send(embed=embed)


@client.command()
async def power(ctx, arg1, arg2):
    equationAnswer = int(arg1) ** int(arg2)
    embed = discord.Embed(title="Powers", color=0xff0000, timestamp=datetime.datetime.utcnow())
    embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
    embed.add_field(name=f"Equation: {arg1} to the {arg2}", value=f"Answer: {equationAnswer}", inline=False)
    await ctx.send(embed=embed)


@client.command()
async def factorial(ctx, arg):
    num = int(arg)
    factorial = 1
    if num < 0:
        embed = discord.Embed(title="ERROR :x:", color=0xff0000, timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
        embed.add_field(name=("There was an error!"), value="You Cannot Factorial Numbers\nThat Are Less Than 0!", inline=False)
        await ctx.send(embed=embed)
    elif num == 0:
        embed = discord.Embed(title="Factorial", color=0xff0000, timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
        embed.add_field(name="Factorial Calculator", value="The factorial of 0 is 1.", inline=False)
        await ctx.send(embed=embed)
    else:
        for i in range(1, num + 1):
            factorial = factorial*i
            embed = discord.Embed(title="Factorial", color=0xff0000, timestamp=datetime.datetime.utcnow())
            embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
            embed.add_field(name="Factorial Calculator", value=f"The factorial\nof {num} is {factorial}!", inline=False)
        await ctx.send(embed=embed)


@client.command()
async def help(ctx, category='0'):
    if category == 'basic':
        embed = discord.Embed(title=":baby: Basic Help", color=0xff0000, timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
        embed.add_field(name="Addition", value="`m!add [num1] [num2]`", inline=False)
        embed.add_field(name="Subtraction", value="`m!subtract [num1] [num2]`", inline=False)
        embed.add_field(name="Multiplication", value="`m!multiply [num1] [num2]`", inline=False)
        embed.add_field(name="Division", value="`m!divide [num1] [num2]`", inline=False)
    elif category == 'advanced':
        embed = discord.Embed(title="<:hmmm:738990399489835039> Advanced (not rlly) Help", color=0xff0000, timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
        embed.add_field(name="Powers", value="`m!power [num1] [num2]`", inline=False)
        embed.add_field(name="Factorial", value="`m!factorial [num]`", inline=False)
        embed.add_field(name="Square Root", value="`m!sqrt [num]`", inline=False)
        embed.add_field(name="Percent", value="`m!percent [num1] [num2]`", inline=False)
    elif category == 'misc':
        embed = discord.Embed(title=":newspaper: Miscellaneous Help", color=0xff0000, timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
        embed.add_field(name="Random Number Generator", value="`m!randomnum [num1] [num2]`", inline=False)
        embed.add_field(name="Invite Link", value="`m!invite`", inline=False)
        embed.add_field(name="Change Prefix", value="`m!prefix [new prefix]`", inline=False)
        embed.add_field(name="Dev Server", value="`devserver`", inline=False)
    elif category == 'comparisons':
        embed = discord.Embed(title="<:idk:739165262036729856> Comparisons", color=0xff0000, timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
        embed.add_field(name='Greater Than', value='`greaterthan [num1] [num2]`', inline=False)
        embed.add_field(name='Less Than', value='`lessthan [num1] [num2]`', inline=False)
        embed.add_field(name='Equal To', value='`equalto [num1] [num2]`', inline=False)
    elif category == 'shapes':
        embed = discord.Embed(title="<:shapes:739327930513227776> Shapes", color=0xff0000, timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
        embed.add_field(name='Circumference', value='`circumference [radius]`', inline=False)
        embed.add_field(name='Square Area', value='`area [side1] [side2] square`', inline=False)
        embed.add_field(name='Rectangle Area', value='`area [side1] [side2] rectangle`', inline=False)
        embed.add_field(name='Triangle Area', value='`area [base] [height] triangle`', inline=False)
    else:
        embed = discord.Embed(title="Help", color=0xff0000, timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
        embed.add_field(name=":baby: **Basic Math**", value="`help basic`", inline=True)
        embed.add_field(name="<:hmmm:738990399489835039> **Advanced Math**", value="`help advanced`", inline=True)
        embed.add_field(name="<:idk:739165262036729856> **Comparisons**", value="`help comparisons`", inline=True)
        embed.add_field(name="<:shapes:739327930513227776> **Shapes**", value=f"`help shapes`", inline=True)
        embed.add_field(name=":newspaper: **Miscellaneous**", value=f"`help misc`", inline=True)

    await ctx.send(embed=embed)


@client.command()
async def randomnum(ctx, arg: int, arg2: int):
    randomNumber = random.randint(arg, arg2)
    embed = discord.Embed(title="Random Number Generator", color=0xff0000, timestamp=datetime.datetime.utcnow())
    embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
    embed.add_field(name=f"The numbers you\ninputted were: {arg}, {arg2}", value=f"The random number is {randomNumber}!", inline=False)
    await ctx.send(embed=embed)


@client.command()
async def invite(ctx):
    embed = discord.Embed(title="Click on this text to invite Mathify!", url="https://tinyurl.com/Mathifybot", color=0xff0000, timestamp=datetime.datetime.utcnow())
    embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
    await ctx.send(embed=embed)


@client.command()
async def sqrt(ctx, arg: int):
    sqrt = arg**(1/2)
    embed = discord.Embed(title='Square Root', timestamp=datetime.datetime.utcnow(), color=0xff0000)
    embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
    embed.add_field(name=f'The square root of {arg} is...', value=f'Around {round(sqrt)}!')
    await ctx.send(embed=embed)


@client.command()
async def percent(ctx, arg1: int, arg2: int):
    decimalAnswer = arg1 / 100
    finalAnswer = decimalAnswer * arg2
    embed = discord.Embed(title='Percentage', timestamp=datetime.datetime.utcnow(), color=0xff0000)
    embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
    embed.add_field(name=f'{arg1}% of {arg2} is...', value=f'{finalAnswer}!')
    await ctx.send(embed=embed)



@client.command()
async def devserver(ctx):
    embed = discord.Embed(title="Click on this text\nto join my dev server!'", url="https://discord.gg/MCUwqVT", color=0xff0000, timestamp=datetime.datetime.utcnow())
    embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
    await ctx.send(embed=embed)


@client.command()
async def greaterthan(ctx, arg1: int, arg2: int):
    if arg2 > arg1:
        notequal = arg2 - arg1
    else:
        notequal = arg1 - arg2
    answer = arg1 > arg2
    embed = discord.Embed(title='Comparison', timestamp=datetime.datetime.utcnow(), color=0xff0000)
    embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
    embed.add_field(name=f'Comparison: {arg1} > {arg2}', value=f'Answer: **{answer}**!')
    embed.add_field(name='Difference:', value=f'**{notequal}**!', inline=False)
    await ctx.send(embed=embed)

@client.command()
async def lessthan(ctx, arg1: int, arg2: int):
    if arg2 > arg1:
        notequal = arg2 - arg1
    else:
        notequal = arg1 - arg2
    answer = arg1 < arg2
    embed = discord.Embed(title='Comparison', timestamp=datetime.datetime.utcnow(), color=0xff0000)
    embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
    embed.add_field(name=f'Comparison: {arg1} < {arg2}', value=f'Answer: **{answer}**!')
    embed.add_field(name='Difference:', value=f'**{notequal}**!', inline=False)
    await ctx.send(embed=embed)
    
@client.command()
async def equalto(ctx, arg1: int, arg2: int):
    if arg2 > arg1:
        notequal = arg2 - arg1
    else:
        notequal = arg1 - arg2

    if arg1 == arg2:
        embed = discord.Embed(title='Comparison', timestamp=datetime.datetime.utcnow(), color=0xff0000)
        embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
        embed.add_field(name='Equal To', value=f'**{arg1}** is equal to **{arg2}**!')
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title='Comparison', timestamp=datetime.datetime.utcnow(), color=0xff0000)
        embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
        embed.add_field(name='Equal To', value=f'**{arg1}** is not equal to **{arg2}**!')
        embed.add_field(name='Difference:', value=f'**{notequal}**!', inline=False)
        await ctx.send(embed=embed)

@client.command()
async def circumference(ctx, arg: int):
    circum = 2*3.14*arg
    embed = discord.Embed(title='Circumference', timestamp=datetime.datetime.utcnow(), color=0xff0000)
    embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
    embed.add_field(name=f'The circumference of a circle\nwith a radius of {arg} is...', value=f'Around **{round(circum)}**!')
    await ctx.send(embed=embed)

@client.command()
async def area(ctx, arg1: int, arg2: int, shape='0'):
    if shape == 'square':
        if arg1 != arg2:
            embed = discord.Embed(title="ERROR :x:", color=0xff0000, timestamp=datetime.datetime.utcnow())
            embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
            embed.add_field(name=("There was an error!"), value="This is a rectangle!\nNot a square!\nDo `area [num1] [num2] rectangle`\n for the area of a rectangle!", inline=False)
            await ctx.send(embed=embed)
        else:
            squarea = arg1 * arg2
            embed = discord.Embed(title='Area', timestamp=datetime.datetime.utcnow(), color=0xff0000)
            embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
            embed.add_field(name=f'Area of a {arg1} x {arg2} square', value=f'Area = {squarea}')
            await ctx.send(embed=embed)
    elif shape == 'rectangle':
        if arg1 == arg2:
            embed = discord.Embed(title="ERROR :x:", color=0xff0000, timestamp=datetime.datetime.utcnow())
            embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
            embed.add_field(name=("There was an error!"), value="This is a square!\nNot a rectangle!\nDo `area [num1] [num2] square`\n for the area of a square!", inline=False)
            await ctx.send(embed=embed)
        else:
            rectanglearea = arg1 * arg2
            embed = discord.Embed(title='Area', timestamp=datetime.datetime.utcnow(), color=0xff0000)
            embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
            embed.add_field(name=f'Area of a {arg1} x {arg2} rectangle', value=f'Area = {rectanglearea}')
            await ctx.send(embed=embed)
    elif shape == 'triangle':
        if arg1 == arg2:
            embed = discord.Embed(title="ERROR :x:", color=0xff0000, timestamp=datetime.datetime.utcnow())
            embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
            embed.add_field(name=("There was an error!"), value="This is not a trangle!", inline=False)
            await ctx.send(embed=embed)
        else:
            trianglearea = (1/2) * arg1 * arg2
            embed = discord.Embed(title='Area', timestamp=datetime.datetime.utcnow(), color=0xff0000)
            embed.set_author(name="Mathify", icon_url="https://cdn.discordapp.com/avatars/738971491286384670/c4d9ebeda2bc6129c862983ed1b13ec6.webp?size=1024")
            embed.add_field(name=f'Area of a triangle\nBase: {arg1}\nHeight: {arg2}', value=f'Area: {trianglearea}')
            await ctx.send(embed=embed)
    

client.run('NzM4OTcxNDkxMjg2Mzg0Njcw.XyTq1A.qyq7oYWDP9HSlgVnUT-fUdZeHUQ')
