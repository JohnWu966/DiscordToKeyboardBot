import discord
import json
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
from menu import startUp, validKeyPresses
client = discord.Client()
import sys

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    messageText = message.content

    if not caseSensitive:
        messageText = messageText.lower()

    if messageText == 'status':
        await message.channel.send("Online.")
        return

    try:
        key = buttonDict[messageText]
        print("Key Press:" + key)
        press(key, 0.05)
        return
    except KeyError:
        print("Invalid Input:" + messageText)


# todo:
# add prefix functionality
#   ie. !bot Alias
# add initial setup wizard thing
#   customizable keyboard setup
#   takes in discord token
# add readme disclaimer about 'sticky shift'
# sanitate json file of the discord token.
# add option for multicharacter presses.
#   use a prefix like \ to tell the bot that its a multi charactered input
# rewrite map in JSON
# add mimic functionality

# If usePrefixes is on, then given a message with a prefix,
# skimMessage() will return the message, with the prefix cut out.

# import map
    # if not caseSensitive, convert all keys into lowercase after importing.

# notes
# every time you add a flag:
#       add a menu for it in the list of bot Settings in the start menu
#       add a line for it in "list of current settings"
#       fix the else statement to account for the extra menu
#       add global variables for it in both main.py and menu.py
#       add those global variables to the json and the saveConfig and loadConfig

# remove the prefix from a message
def skimMessage(message):
    return message[len(prefix)+1:len(message)].strip()


if not json.load(open('config.json'))["skipMenu"]:
    startUp()

# reload the configuration in case changes were made in the startup menu.
with open('config.json') as file:
    data = json.load(file)

# load configuration
# _______________________________
# The token for the Discord Bot
token = data["token"]
# Setting this flag to True will require that the message match the key word's case sensitivity.
caseSensitive = data["caseSensitive"]
# Length of time to keep the key pressed. Default time is 0.05
pressTime = data["pressTime"]
# Setting this flag to True will skip the initial menu and immediately run the bot.
skipMenu = data["skipMenu"]
# Setting this flag to True will have the bot ignore any inputs that don't start with a prefix, i.e (~bot A).
usePrefixes = data["usePrefixes"]
# If usePrefixes is true, the bot will only look at messages that start with the specified prefix.
# It will ignore the prefix and scan the message starting from after the prefix.
prefix = data["prefix"]

# initialize buttonDict from map.json
with open('map.json') as map_json:
    tempDict = json.load(map_json)
    buttonDict = {}

    # if caseSensitive is turned on, create a dictionary matching the one in map.json
    if caseSensitive:
        buttonDict = tempDict
    # if caseSensitive is turned off, create a new dictionary that is identical to the one found in map.json,
    # except all keys are lowercase
    else:
        for dictKey in tempDict:
            buttonDict[dictKey.lower()] = tempDict[dictKey]
    for dictKey in buttonDict:
        if buttonDict[dictKey] not in validKeyPresses:
            print("Error when reading the button mapping.")
            print()
            print("Error in: ")
            print("Alias: " + dictKey)
            print("Key: " + buttonDict[dictKey])
            print(buttonDict[dictKey] + "is not a valid key.")
            print("Please refer to validkeys.md for a list of valid keys.")
            print("If you cannot resolve the issue, then please delete the problematic alias-key pair from map.json")
            sys.exit(0)

print("DEBUG:")
print("BUTTON DICT")
print(buttonDict)
client.run(data["token"])
