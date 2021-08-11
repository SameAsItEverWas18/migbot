import discord
from discord.ext import tasks
import random
import fnmatch
import asyncio
import tokenext
client = discord.Client()
num = 0

@tasks.loop(minutes=20)
async def sendone():
    channel = client.get_channel(614877948679553032)
    channel2 = client.get_channel(665397604728832002)
    async with message.channel.typing():
        await asyncio.sleep(5)
        await channel.send(random.choice(open('migmsg.txt').readlines()))
        await channel2.send(random.choice(open('migmsg.txt').readlines()))

@tasks.loop(minutes=20)
async def sendtwo():
    channel = client.get_channel(614877948679553032)
    async with message.channel.typing():
        await asyncio.sleep(5)
        await channel.send(random.choice(open('migmsg.txt').readlines()))
        await channel.send(random.choice(open('migmsg.txt').readlines()))

@tasks.loop(minutes=20)
async def sendthree():
    channel = client.get_channel(614877948679553032)
    async with message.channel.typing():
        await asyncio.sleep(5)
        await channel.send(random.choice(open('migmsg.txt').readlines()))
        await channel.send(random.choice(open('migmsg.txt').readlines()))
        await channel.send(random.choice(open('migmsg.txt').readlines()))

@tasks.loop(minutes=20)
async def sendfour():
    channel = client.get_channel(665397604728832002)
    async with message.channel.typing():
        await asyncio.sleep(5)
        await channel.send(random.choice(open('migmsg.txt').readlines()))
        await channel.send(random.choice(open('migmsg.txt').readlines()))
        await channel.send(random.choice(open('migmsg.txt').readlines()))
        await channel.send(random.choice(open('migmsg.txt').readlines()))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "MIGUEL" in message.content:
        async with message.channel.typing():
            await asyncio.sleep(5)
            await message.channel.send(random.choice(open('migmsg.txt').readlines()))
            num = random.choice(range(10, 101))

    if "mig" in message.content:
       async with message.channel.typing():
            await asyncio.sleep(5)
            await message.channel.send(random.choice(open('migmsg.txt').readlines()))
            num = random.choice(range(10, 101))

    if "miggy" in message.content:
       async with message.channel.typing():
            await asyncio.sleep(5)
            await message.channel.send(random.choice(open('migmsg.txt').readlines()))
            num = random.choice(range(10, 101))

    if "kirinvision" in message.content:
       async with message.channel.typing():
            await asyncio.sleep(5)
            await message.channel.send(random.choice(open('migmsg.txt').readlines()))
            num = random.choice(range(10, 101))

    if "lasvegas63" in message.content:
       async with message.channel.typing():
            await asyncio.sleep(5)
            await message.channel.send(random.choice(open('migmsg.txt').readlines()))
            num = random.choice(range(10, 101))

if num < 85:
    @client.event
    async def on_ready():
        async with message.channel.typing():
            await asyncio.sleep(5)
            sendone.start()
if num < 95 and num > 85:
    @client.event
    async def on_ready():
        async with message.channel.typing():
            await asyncio.sleep(5)
            sendtwo.start()
            print(num)
if num < 96 and num > 99:
    @client.event
    async def on_ready():
        async with message.channel.typing():
            await asyncio.sleep(5)
            sendthree.start()
if num == 100:
    @client.event
    async def on_ready():
        async with message.channel.typing():
            await asyncio.sleep(5)
            sendfour.start()

client.run(token)
