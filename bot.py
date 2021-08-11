import discord
from discord.ext import tasks
import random
client = discord.Client()
num = 0

@tasks.loop(minutes=40)
async def sendone():
    channel = client.get_channel(614877948679553032)
    channel2 = client.get_channel(665397604728832002)
    await channel.send(random.choice(open('migmsg.txt').readlines()))
    await channel2.send(random.choice(open('migmsg.txt').readlines()))

@tasks.loop(minutes=40)
async def sendtwo():
    channel = client.get_channel(614877948679553032)
    await channel.send(random.choice(open('migmsg.txt').readlines()))
    await channel.send(random.choice(open('migmsg.txt').readlines()))

@tasks.loop(minutes=40)
async def sendthree():
    channel = client.get_channel(614877948679553032)
    await channel.send(random.choice(open('migmsg.txt').readlines()))
    await channel.send(random.choice(open('migmsg.txt').readlines()))
    await channel.send(random.choice(open('migmsg.txt').readlines()))

@tasks.loop(minutes=40)
async def sendfour():
    channel = client.get_channel(665397604728832002)
    await channel.send(random.choice(open('migmsg.txt').readlines()))
    await channel.send(random.choice(open('migmsg.txt').readlines()))
    await channel.send(random.choice(open('migmsg.txt').readlines()))
    await channel.send(random.choice(open('migmsg.txt').readlines()))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "MIGUEL" in message.content:
       await message.channel.send(random.choice(open('migmsg.txt').readlines()))
       num = random.choice(range(10, 101))

    if "mig" in message.content:
       await message.channel.send(random.choice(open('migmsg.txt').readlines()))
       num = random.choice(range(10, 101))

    if "miggy" in message.content:
       await message.channel.send(random.choice(open('migmsg.txt').readlines()))
       num = random.choice(range(10, 101))

    if "kirinvision" in message.content:
       await message.channel.send(random.choice(open('migmsg.txt').readlines()))
       num = random.choice(range(10, 101))

    if "lasvegas63" in message.content:
       await message.channel.send(random.choice(open('migmsg.txt').readlines()))
       num = random.choice(range(10, 101))

if num < 85:
    @client.event
    async def on_ready():
        sendone.start()
if num < 95 and num > 85:
    @client.event
    async def on_ready():
        sendtwo.start()
        print(num)
if num < 96 and num > 99:
    @client.event
    async def on_ready():
        sendthree.start()
if num == 100:
    @client.event
    async def on_ready():
        sendfour.start()

client.run('Token')
