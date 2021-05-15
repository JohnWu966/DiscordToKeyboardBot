import discord
import json
import sys
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
from map import buttonDict

client = discord.Client()

with open('config.json') as file:
    data = json.load(file)


# Setting this flag to True will require that the message match the key word's case sensitivity.
caseSensitive = data["caseSensitive"]
# Length of time to keep the key pressed. Default time is 0.05
pressTime = data["pressTime"]
# Setting this flag to True will skip the initial menu and immediately run the bot.
skipMenu = data["skipMenu"]
# Setting this flag to True will have the bot ignore any inputs that don't start with a prefix, i.e (~bot A).
usePrefixes = data["usePrefixes"]

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


if not skipMenu:
    #startup menu
    print("")
    print("")
    print("Discord to Keyboard Bot")
    print("________________________")
    print("1. Start Bot")
    print("2. Change Keyboard Bindings")
    print("3. Bot Settings")
    print("4. Help.")
    print("5. Exit")
    print("")
    #todo: Write something with better grammar
    loop1 = True
    while loop1:
        userInput = input("Which menu would you like to go to?")
        if userInput.startswith("1"):
            if len(data["token"]) <= 30:
                print("Hi, it looks like this is your first time running this bot.")
                print("Lets quickly go through some initial set up.")
                print("To be implemented later.")
            loop1 = False
            print("Starting up the bot...")
        elif userInput.startswith("2"):
            print()
            print()
            print("Keyboard Bindings")
            print("________________________")
            print("1. See Current Key Bindings")
            print("2. Set New Key Bindings")
            print("3. Learn how to manually adjust Key Bindings")
            print("4. Main Menu")
            print("")
            loop2 = True
            while loop2:
                userInput = input("Which menu would you like to go to?")
                if userInput.startswith("1"):
                    print("Here are the current Key Bindings:")
                    print("...")
                    print("To be implemented later")
                elif userInput.startswith("2"):
                    print("Here are the current Key Bindings.")
                    print("Which key would you like to add a binding for?")
                    print("If you would to remove a key binding, please type \"remove\"")
                    print("If you would like a list of all possible keys to bind, please type \"show all\"")
                    print("...")
                    print("To be implemented Later")
                elif userInput.startswith("3"):
                    print("Manually adjusting Key Bindings")
                    print("...")
                    print("To be implemented Later")
                elif userInput.startswith("4"):
                    print("Returning to Main Menu.")
                    loop2 = False
                else:
                    print("Please enter a proper input.")
                    print("Options are '1', '2', '3',or '4'.")

        elif userInput.startswith("3"):
            print()
            print()
            print("Bot Settings")
            print("________________________")
            print("1. Prefix")
            print("2. Case Sensitivity")
            print("3. Press Time")
            print("4. Save and Return to Main Menu")
            print("...")
            loop2 = True
            while loop2:
                userInput = input("Which menu would you like to go to?")
                if userInput.startswith("1"):
                    print("Prefixes")
                    print("")
                    print("Details about prefixes")
                    print("To be implemented later")
                elif userInput.startswith("2"):
                    print("Case Sensitivitiy.")
                    print("")
                    print("Details about Case Sensitivity")
                    print("To be implemented Later")
                elif userInput.startswith("3"):
                    print("Press Time Settings")
                    print("...")
                    print("To be implemented Later")
                elif userInput.startswith("4"):
                    print("Saving")
                    print("....")
                    print("To be implemented later")
                    print("Returning to Main Menu.")
                    loop2 = False
                else:
                    print("Please enter a proper input.")
                    print("Options are '1', '2', '3',or '4'.")
        elif userInput.startswith("4"):
            print("Description stuff")
        elif userInput.startswith("5"):
            print("Press any key to exit.")
            input("")
            sys.exit(0)
        else:
            print("Please enter a proper input.")
            print("Options are '1', '2', '3', '4', or '5'.")

client.run(data["token"])
