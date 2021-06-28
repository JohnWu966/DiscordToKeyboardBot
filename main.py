import discord
import json
import sys
from pyKey import press
from menu import startUp, validKeyPresses, printMapping, printBotSettings
client = discord.Client()


# remove the prefix from a message
def skimMessage(message):
    return message[len(prefix)+1:len(message)].strip()


def initDict():
    # initialize keyMapping from map.json
    temp_dict = json.load(open('map.json'))
    keyboard_dict = {}
    # if caseSensitive is turned on, just create a dictionary matching the one in map.json
    if caseSensitive:
        keyboard_dict = temp_dict
    # if caseSensitive is turned off, create a new dictionary that is identical to the one found in map.json,
    # except all keys are lowercase
    else:
        for dictKey in temp_dict:
            keyboard_dict[dictKey.lower()] = temp_dict[dictKey]

    # check the resulting dictionary to make sure that all keyboard presses are valid.
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
    print()
    print("Here's a list of the bot's settings.")
    printBotSettings()
    print()
    print("Here's a list of the key mappings.")
    printMapping()
    print()
    print("You can turn off the bot by pressing Ctrl + C")


# runs every time the bot sees anyone enter a message
@client.event
async def on_message(message):
    # If this is the bot's message, skip the message.
    if message.author == client.user:
        return

    messageText = message.content

    # if the bot is not in case sensitive mode, convert the message text into lowercase for processing
    if not caseSensitive:
        messageText = messageText.lower()

    # if the bot is using prefixes, then check if the message starts with the prefix.
        # if it does not, then skip the message.
        # if it does, then extract the actual message content.
    if usePrefixes:
        if not messageText.startswith(prefix):
            if extraDetails:
                print("Message: " + messageText + " does not start with prefix: " + prefix)
            return
        else:
            messageText = skimMessage(messageText)

    # test message to check if the bot is online
    if messageText == 'status':
        await message.channel.send("Online.")
        return

    if messageText == 'help':
        await message.channel.send("Here is a list of current key bindings.")
        text = "```\n{} \t {}".format("Alias".ljust(20), "Keyboard Press")
        text = text + "\n________________________________________________"
        for alias in keyMapping:
            text = text + "\n" + '{} \t {}'.format(alias.ljust(20),keyMapping[alias])
        text = text + "```"
        await message.channel.send(text)

        if usePrefixes:
            await message.channel.send("The bot is currently using a prefix to filter out messages. The current prefix is " + prefix)
            await message.channel.send("Please begin your commands with " + prefix + " if you would like to make a key press.")
        return

    # search the list of alias / key mapping for the alias.
    # if a valid alias is found, press the key associated with the alias.
    try:
        key = keyMapping[messageText]
        print("User " + message.author.display_name + " has pressed:" + key)
        press(key, 0.05)
        return
    except KeyError:
        if extraDetails:
            print(message.author.display_name + " has entered an invalid input. " + messageText +
                  " is not a valid keyboard press.")

# run the startup menu, unless the user has explicitly turned it off.
if not json.load(open('config.json'))["skipMenu"]:
    startUp()

# load the global flags from config.json
with open('config.json') as file:
    data = json.load(file)
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
# Turn on to see extra details in console
extraDetails = data["extraDetails"]

# import the keyboard mapping from map.json
keyMapping = initDict()

# start running the bot
try:
    client.run(data["token"])
except Exception as e:
    print("Error:")
    print(e)
    print("You've probably entered an invalid Bot Token")
    print("Please re-enter the bot Token")
