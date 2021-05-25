import discord
import json
import sys
from pyKey import press
from menu import startUp, validKeyPresses
client = discord.Client()

# Turn on to see debug messages in console
debugMode = True


# remove the prefix from a message
def skimMessage(message):
    return message[len(prefix)+1:len(message)].strip()


def initDict():
    # initialize keyMapping from map.json
    temp_dict = json.load(open('map.json'))
    keyboard_dict = {}
    # if caseSensitive is turned on, create a dictionary matching the one in map.json
    if caseSensitive:
        keyboard_dict = temp_dict
    # if caseSensitive is turned off, create a new dictionary that is identical to the one found in map.json,
    # except all keys are lowercase
    else:
        for dictKey in temp_dict:
            keyboard_dict[dictKey.lower()] = temp_dict[dictKey]
    checkDict(keyboard_dict)
    return keyboard_dict


# given a key mapping dictionary, check to see if it only contains valid keyboard presses.
# crash the program if there's an invalid keyboard press.
def checkDict(keyboard_dict):
    for dict_key in keyboard_dict:
        if keyboard_dict[dict_key] not in validKeyPresses:
            print("Error when reading the button mapping.")
            print()
            print("Error in: ")
            print("Alias: " + dict_key)
            print("Key: " + keyboard_dict[dict_key])
            print(keyboard_dict[dict_key] + "is not a valid key.")
            print("Please refer to validkeys.md for a list of valid keys.")
            print("If you cannot resolve the issue, then please delete the problematic alias-key pair from map.json")
            input("Press ENTER to continue")
            sys.exit(0)


@client.event
async def on_ready():
    print('Successfully logged in as {0.user}'.format(client))
    print("You can turn off the bot by pressing Ctrl + C")


# runs everytime the bot sees anyone enter a message
@client.event
async def on_message(message):
    # If this is the bot's message, return.
    if message.author == client.user:
        return

    messageText = message.content

    # if the bot is not case sensitive, convert the message text into lowercase
    if not caseSensitive:
        messageText = messageText.lower()

    # if the bot is using prefixes, then check if the message starts with the prefix.
    # if it does not, then return
    # if it does, then take out the prefix from the actual message content.
    if usePrefixes:
        if not messageText.startswith(prefix):
            if debugMode:
                print("DEBUG: Message: " + messageText + " does not start with prefix: " + prefix)
            return
        else:
            messageText = skimMessage(messageText)

    # test message to check if the bot is online
    if messageText == 'status':
        await message.channel.send("Online.")
        return

    # search the dictionary for the alias.
    # if a valid alias is found, press the key associated with the alias.
    try:
        key = keyMapping[messageText]
        print("User " + message.author.display_name + " has pressed:" + key)
        press(key, 0.05)
        return
    except KeyError:
        if debugMode:
            print("DEBUG: Invalid Input:" + messageText)


# todo:
# add initial setup wizard thing
#   customizable keyboard setup
# rewrite readme
    # add readme disclaimer about 'sticky shift'
# add option for multicharacter presses.
#   use a prefix like \ to tell the bot that its a multi charactered input
# add mimic functionality
# add a !bot help thing to have the bot print out the mapping

# notes
# every time you add a flag:
#       add a menu for it in the list of bot Settings in the start menu
#       add a line for it in "list of current settings"
#       fix the else statement to account for the extra menu
#       add global variables for it in both main.py and menu.py
#       add those global variables to the json and the saveConfig and loadConfig


if not json.load(open('config.json'))["skipMenu"]:
    startUp()

# load the global flags from config.json
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
if not caseSensitive:
    prefix = prefix.lower()

# import the keyboard mapping from map.json
keyMapping = initDict()

# chunk of code for debugging stuff
# testString = "!bot      hi friends"
# newString = skimMessage(testString)
# print(testString)
# print(newString)
# sys.exit(0)

client.run(data["token"])
