import discord
import json
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys

client = discord.Client()

with open('config.json') as file:
    data = json.load(file)

# options:
# True requires that the full text of the message match with an option.
# False only requires that only the first word of the message match with an option.
fullText = False
# True will require that the message match the key word's case sensitivity.
caseSensitive = False




@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    messageText = message.content.lower()
    if messageText.startswith('down'):
        press('DOWN', 0.01)
        print("DOWN")
        return
    if messageText.startswith('up'):
        press('UP', 0.01)
        print("UP")
        return
    if messageText.startswith('left'):
        press('LEFT', 0.01)
        print("LEFT")
        return
    if messageText.startswith('right'):
        press('RIGHT', 0.01)
        print("RIGHT")
        return
    if messageText.startswith('a'):
        press('Z', 0.01)
        print("z")
        return
    if messageText.startswith('b'):
        press('X', 0.01)
        print("x")
        return
    if messageText.startswith('start'):
        press('ENTER', 0.01)
        print("Enter")
        return
    if messageText.startswith('select'):
        press('BKSP', 0.01)
        print("Backspace")
        return


# #todo:
# #implement using map
# #   |   Alias  |     Key     |   Duration    |
# # add prefix functionality
# #   ie. !bot Alias
# #add initial setup wizard thing
# #   customizable keyboard setup
# #   takes in discord token
# #add flags for
# #   lowercase
# #   startswith vs exact matching
# #   prefixs
# # add readme disclaimer about 'sticky shift'
# # sanitate json file of the discord token.
#
#

client.run(data["token"])