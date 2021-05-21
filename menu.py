import json
import sys

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


def loadConfig():
    global data
    global token
    global caseSensitive
    global pressTime
    global skipMenu
    global usePrefixes
    global prefix
    token = data["token"]
    caseSensitive = data["caseSensitive"]
    pressTime = data["pressTime"]
    skipMenu = data["skipMenu"]
    usePrefixes = data["usePrefixes"]
    prefix = data["prefix"]


# update config.json with the current configuration
def saveConfig():
    config = {
        "token": token,
        "caseSensitive": caseSensitive,
        "pressTime": pressTime,
        "skipMenu": skipMenu,
        "usePrefixes": usePrefixes,
        "prefix": prefix
    }
    with open('config.json', 'w') as outfile:
        json.dump(config, outfile)
    print("DEBUG:SAVING CONFIG")
    print(config)
    print()


def printBotSettings():
    print()
    print()
    print("Bot Settings:")
    print("_______________")
    if caseSensitive:
        print("Case Sensitive: Yes")
    else:
        print("Case Sensitive: No")
    print("Press Time: " + str(pressTime))
    if usePrefixes:
        print("Prefixes: On")
        print("Prefix: " + prefix)
    else:
        print("Prefixes: Off")
    print()
    print()
    input("Press ENTER to continue.")


def setPrefixStuff():
    global prefix
    global usePrefixes
    loop1 = True
    while loop1:
        print()
        print()
        print("The bot can filter inputs so that it will only take in messages that begin with a certain string.")
        print("For example, you set it such that the message \"!bot A\" will press the A key, you can also set it such "
              "that just \"A\" will press the A Key ")
        if usePrefixes:
            print("You are currently using a prefix.")
            print("The current prefix is:" + prefix)
            print()
            print("1. Stop using prefixes")
        if not usePrefixes:
            print("You are currently not using a prefix.")
            print()
            print("1. Start using prefixes")
        print("2. Change prefix")
        print("3. Back")
        print("Please enter '1','2',or '3'")
        userInput = input().lower()
        if userInput == '1':
            if usePrefixes:
                print("You are no longer using prefixes.")
                print("The bot will now interpret every message it sees as a potential call for a keyboard press")
                usePrefixes = False
            else:
                print("You are now using prefixes.")
                print("The current prefix is: " + prefix)
                print()
                print("The bot will now only consider messages that start with " + prefix + "as potential calls for a "
                                                                                            "keyboard press.")
                usePrefixes = True
            print()
            input("Please press ENTER to continue")
        elif userInput == '2':
            print("The current prefix is: " + prefix)
            if not usePrefixes:
                print("You are currently not using prefixes, but you can still change the prefix in case you would "
                      "like to use prefixes in the future.")
            loop2 = True
            while loop2:
                print()
                print("Would you like to change the prefix? Please enter 'y' or 'n'")
                userInput = input().lower()
                if userInput == 'y':
                    print()
                    newPrefix = input("Please enter the new Prefix:").strip()
                    prefix = newPrefix
                    print()
                    print("The current Prefix is: " + prefix)
                    print()
                    loop2 = False
                elif userInput == 'n':
                    loop2 = False
                else:
                    print("Invalid Input")
            input("Please press ENTER to continue")
        elif userInput == '3':
            loop1 = False
        else:
            print("Invalid Input")
    saveConfig()


def setCaseSensitive():
    global caseSensitive
    loop1 = True
    while loop1:
        print()
        print()
        print("The bot can be set to be case sensitive when matching a message to keys.")
        print("It is recommended to keep case sensitivity off.")
        print()
        if caseSensitive:
            print("The Bot is currently case sensitive.")
        else:
            print("The Bot is currently NOT case sensitive.")
        print()
        print("Would you like to switch the case sensitivity? ")
        print("Please enter either 'y' or 'n'")
        userInput = input().lower()
        if userInput == 'y':
            print()
            if caseSensitive:
                print("Case Sensitivity has been turned off")
                caseSensitive = False
            else:
                print("Case Sensitivity has been turned on")
                caseSensitive = True
            print("")
            loop1 = False
        elif userInput == 'n':
            loop1 = False
        else:
            print("Invalid Input")
    saveConfig()
    input("Press ENTER to continue.")


def setPressTime():
    global pressTime
    loop1 = True
    while loop1:
        print()
        print()
        print("The bot can be set to hold keypresses for a set amount of time.")
        print("By default, the bot presses keys down for 0.05 seconds.")
        print()
        print("The current press time is " + str(pressTime) + " seconds")
        print()
        print("Would you like to change the press time? ")
        print("Please enter either 'y' or 'n'")
        userInput = input().lower()
        if userInput == 'y':
            loop2 = True
            while loop2:
                print()
                newPressTime = input("How many seconds would you like one key press to last? ")
                try:
                    pressTime = float(newPressTime)
                    loop2 = False
                except ValueError:
                    print("Invalid input. Please enter a number")
            print("Press time has been changed to " + str(pressTime) + " seconds")
            print("")
            loop1 = False
        elif userInput == 'n':
            loop1 = False
        else:
            print("Invalid Input")
    saveConfig()
    input("Press ENTER to continue.")


def setBotToken():
    global token
    loop1 = True
    while loop1:
        print()
        print()
        print("A Bot Token is a long randomized string of characters that is unique to your specific bot account.")
        print("By providing your bot account's token, you allow this program to control your bot account.")
        print("If you don't know how to find your bot token, you can google how to find it.")
        print()
        print("The Current Bot Token is: " + token)
        print()
        print("Would you like to change the Bot Token? ")
        print("Please enter either 'y' or 'n'")
        userInput = input().lower()
        if userInput == 'y':
            print()
            newToken = input("Please enter your new Bot Token:")
            token = newToken
            print()
            print("Your new Bot Token is: " + token)
            print()
            loop1 = False
        elif userInput == 'n':
            loop1 = False
        else:
            print("Invalid Input")
    saveConfig()
    input("Press ENTER to continue.")


def setSkipMenu():
    global skipMenu
    loop1 = True
    while loop1:
        print()
        print()
        print("Are you sure you want to turn off the startup menu?")
        print(
            "If you turn this off, then running run.bat will immediately start up the bot, but you'll no longer be "
            "able to change any settings without manually editing the configuration file yourself.")
        print(
            "Type (y) to confirm that you would like to turn off the startup menu. Type (n) to go back to the main "
            "menu.")
        userInput = input().lower()

        if userInput == "y":
            skipMenu = True
            print()
            print()
            print("You have turned off the startup menu.")
            print(
                "If you would like to turn the startup menu back on, you can edit config.json using a text editor and "
                "set \"skipMenu\" from true to false")
            input("Please press ENTER to continue")
            loop1 = False
        elif userInput == "n":
            print("Returning to Main Menu.")
            loop1 = False
        if userInput != "y" and userInput != "n":
            print("Please type either (y) or (n)")
    input("Press ENTER to continue.")


def startUp():
    loadConfig()
    global token
    global caseSensitive
    global pressTime
    global skipMenu
    global usePrefixes
    global prefix

    if not skipMenu:
        loop1 = True
        while loop1:
            # startup menu
            print("")
            print("")
            print("Discord to Keyboard Bot")
            print("________________________")
            print("1. Start Bot")
            print("2. Change Keyboard Bindings")
            print("3. Bot Settings")
            print("4. Help.")
            print("5. Stop showing Startup Menu")
            print("6. Exit")
            print("")
            userInput = input("Which menu would you like to go to? ")
            if userInput.startswith("1"):
                if len(data["token"]) <= 30:
                    print("Hi, it looks like this is your first time running this bot.")
                    print("Lets quickly go through some initial set up.")
                    print("To be implemented later.")
                loop1 = False
            elif userInput.startswith("2"):
                loop2 = True
                while loop2:
                    print()
                    print()
                    print("Keyboard Bindings")
                    print("________________________")
                    print("1. See Current Key Bindings")
                    print("2. Set New Key Bindings")
                    print("3. Learn how to manually adjust Key Bindings")
                    print("4. Back")
                    print("")
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
                loop2 = True
                while loop2:
                    print()
                    print()
                    print("Bot Settings")
                    print("________________________")
                    print("1. See Current List of Settings")
                    print("2. Prefix")
                    print("3. Case Sensitivity")
                    print("4. Press Time")
                    print("5. Change Bot Token")
                    print("6. Save and Return to Main Menu")
                    print("...")
                    userInput = input("Which menu would you like to go to? ")
                    if userInput.startswith("1"):
                        printBotSettings()
                    elif userInput.startswith("2"):
                        setPrefixStuff()
                    elif userInput.startswith("3"):
                        setCaseSensitive()
                    elif userInput.startswith("4"):
                        setPressTime()
                    elif userInput.startswith("5"):
                        setBotToken()
                    elif userInput.startswith("6"):
                        print("Saving")
                        print("Returning to Main Menu.")
                        saveConfig()
                        loop2 = False
                    else:
                        print("Please enter a proper input.")
                        print("Options are '1', '2', '3', '4', '5', or '6'.")
            elif userInput.startswith("4"):
                print()
                print()
                print("Description stuff")
            elif userInput.startswith("5"):
                setSkipMenu()
                if skipMenu:
                    loop1 = False
            elif userInput.startswith("6"):
                print("Press ENTER to exit.")
                input("")
                sys.exit(0)
            else:
                print("Please enter a proper input.")
                print("Options are '1', '2', '3', '4', '5', '6'.")
        print("Starting up the bot...")
        saveConfig()
