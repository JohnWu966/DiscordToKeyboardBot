import discord
import json
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
from map import buttonDict

client = discord.Client()

with open('config.json') as file:
    data = json.load(file)

# options:

# Setting this flag to True will require that the message match the key word's case sensitivity.
caseSensitive = False

# Length of time to keep the key pressed. Default time is 0.05
pressTime = 0.05


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if not caseSensitive:
        messageText = message.content.lower()

    if messageText == 'status':
        await message.channel.send("Online.")
        return

    try:
        key = buttonDict[messageText]
        print("Key Press:" + key)
        press(key, 0.05)
        return
    except:
        print("Invalid Input:" + messageText)

#todo:
# add prefix functionality
#   ie. !bot Alias
# add initial setup wizard thing
#   customizable keyboard setup
#   takes in discord token
# add flags for
#   lowercase
#   prefixs
# add readme disclaimer about 'sticky shift'
# sanitate json file of the discord token.
# add option for multicharacter presses.
#   use a prefix like _ to tell the bot that its a multi charactered input
client.run(data["token"])