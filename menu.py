import json
import sys
import os

# Turn on to see extraDetails messages in console
extraDetails = True

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
# Turn on to see Extra Details  in console
extraDetails = data["extraDetails"]
# import the key button binding from map.json
key_dict = json.load(open('map.json'))

# List of all valid key presses from pyKey
validKeyPresses = [
    "`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "-",
    "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+",
    "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "\\",
    "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "{", "}", "|",
    "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'",
    "A", "S", "D", "F", "G", "H", "J", "K", "L", ":", "\"",
    "z", "x", "c", "v", "b", "n", "m", ",", ".", "/",
    "Z", "X", "C", "V", "B", "N", "M", "<", ">", "?",
    "UP", "DOWN", "LEFT", "RIGHT",
    "NUM1", "NUM2", "NUM3", "NUM4", "NUM5", "NUM6", "NUM7", "NUM8", "NUM9", "NUM0", "NUM-", "NUM+",
    "INS", "HOME", "PGUP", "DEL", "END", "PGDN", "PRTSC", "SCROLL_LOCK",
    "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12",
    "CTRL", "LSHIFT", "RSHIFT", "BSLASH", "BKSP", "ENTER", "TAB", "TILDE", "BACKTICK", "ALT", "SPACEBAR", "CAPSLOCK",
    "NUMLOCK"
]


def clear():
    os.system('cls')


def pause():
    input("Press Enter to Continue.")


# import global flags from config.json
def loadConfig():
    global data
    global token
    global caseSensitive
    global pressTime
    global skipMenu
    global usePrefixes
    global prefix
    global extraDetails
    token = data["token"]
    caseSensitive = data["caseSensitive"]
    pressTime = data["pressTime"]
    skipMenu = data["skipMenu"]
    usePrefixes = data["usePrefixes"]
    prefix = data["prefix"]
    extraDetails = data["extraDetails"]


# update config.json with the current configuration
def saveConfig():
    config = {
        "token": token,
        "caseSensitive": caseSensitive,
        "pressTime": pressTime,
        "skipMenu": skipMenu,
        "usePrefixes": usePrefixes,
        "prefix": prefix,
        "extraDetails": extraDetails
    }
    with open('config.json', 'w') as outfile:
        json.dump(config, outfile, indent=4)
    # if extraDetails:
    #     print()
    #     print("DEBUG:SAVING CONFIG")
    #     print(json.dumps(config, indent=1))
    print()


# Search the dictionary for a given Key Press. If found, return all alias assigned with it, otherwise return "".
def getAliasFromKey(key_press):
    temp_dict = {}
    for alias in key_dict:
        if key_dict[alias] == key_press:
            temp_dict[alias] = key_press
    return temp_dict


def saveMapping():
    with open('map.json', 'w') as outfile:
        json.dump(key_dict, outfile, indent=4)
    # if extraDetails:
    #     print()
    #     print("DEBUG:SAVING CONFIG")
    #     print(json.dumps(key_dict, indent=1))


def printMapping():
    print()
    print("Key\t\tAlias")
    print("_____________________")
    for key in key_dict:
        print(key_dict[key] + "\t\t" + key)
    print("_____________________")
    print()


def addMapping():
    loop1 = True
    while loop1:
        clear()
        print("Which button would you like to press?")
        print("If you would like a list of all valid keyboard buttons, type \"/list\"")
        print()
        print("Type \"__exit\" to exit")
        print()
        button = input("What keyboard button would you like to press? ").strip()
        if button == "/list":
            print()
            printValidPresses()
            print()
            pause()
        elif button.strip().lower() == "__exit":
            print("Exiting")
            pause()
            return
        else:
            if button in validKeyPresses:
                alias_list = getAliasFromKey(button)
                if alias_list:
                    loop2 = True
                    while loop2:
                        print()
                        print("A mapping for the button [" + button + "] already exists.")
                        print()
                        print("Key\tAlias")
                        print("_____________________")
                        for alias in alias_list:
                            print(alias_list[alias] + "\t" + alias)
                        print()
                        print("Are you sure that you would like to add another alias to [" + button + "]?")
                        print("Adding multiple alias' to a single button will not cause any issues.")
                        answer = input("Please enter [y] or [n]. ").strip().lower()
                        if answer == "y":
                            loop1 = False
                            loop2 = False
                        elif answer == "n":
                            loop2 = False

                        else:
                            print("Invalid Input")
                            clear()
                else:
                    loop1 = False
            else:
                print("Error: " + button + " is not a valid key press")
                print("Please type \"/list\" to get a list of all valid key presses. Take note that the keypresses "
                      "are case sensitive")
                print()
                pause()
    print()
    loop1 = True
    while loop1:
        conflict = False
        clear()
        print("What alias would you like to use?")
        print("An alias is the message that a user has to type to press a button.")
        print()
        print("For example typing \"start\" on Discord to make the bot press \"ENTER\" on the host's keyboard")
        print()
        print("You can type \"__exit\" to exit.")
        print()
        alias = input("Please type the alias you would to use to press [" + button + "]. ").strip()
        if alias.strip().lower() == "__exit":
            print()
            print("Exiting")
            print()
            pause()
            return
        for dict_alias in key_dict:
            if alias == dict_alias:
                print("Error: " + alias + " is already associated in an existing key binding")
                print("Key:\t\tAlias")
                print("_____________________")
                print(key_dict[alias] + "\t\t" + alias)
                print("_____________________")
                print()
                print("Please choose another alias.")
                pause()
                conflict = True
                break
        if not conflict:
            print()
            print("Adding new key binding.")
            print("_____________________")
            print("Key: " + button + "\t Alias: " + alias )
            print("_____________________")
            print()
            key_dict[alias] = button
            pause()
            saveMapping()
            return


def editMapping():
    clear()
    loop1 = True
    while loop1:
        print("Here are the current Key Bindings.")
        printMapping()
        print()
        print("Which button would you like to edit the mapping for?")
        print()
        print("Type \"__exit\" to exit")
        print()
        button = input("What keyboard button would you like to edit? ").strip()
        if button.strip().lower() == "__exit":
            print()
            print("Exiting")
            print()
            pause()
            return
        else:
            alias_list = getAliasFromKey(button)
            if alias_list:
                print()
                if len(alias_list.keys()) == 1:
                    conflict = True
                    while conflict:
                        conflict = False
                        new_alias = input("What would you like to change the alias for ["+button+"] to? ")
                        for dict_alias in key_dict:
                            if new_alias == dict_alias:
                                print("Error: " + new_alias + " is already associated in an existing key binding")
                                print("Key:\t\tAlias")
                                print("_____________________")
                                print(key_dict[new_alias] + "\t\t" + new_alias)
                                print("_____________________")
                                print()
                                print("Please choose another alias.")
                                pause()
                                conflict = True

                    # remove the old binding from the dict and add the new one
                    for alias in key_dict:
                        if key_dict[alias] == button:
                            print("Key:\t\tAlias")
                            print("_____________________")
                            print("BEFORE:")
                            print(key_dict[alias] + "\t\t" + alias)
                            del key_dict[alias]
                            break
                    key_dict[new_alias] = button

                    print("AFTER:")
                    print(key_dict[new_alias] + "\t\t" + new_alias)

                else:
                    loop2 = True
                    while loop2:
                        clear()
                        print("Multiple bindings for [" + button + "] found.")
                        print()
                        print("Key\tAlias")
                        print("_____________________")
                        for alias in alias_list:
                            print(alias_list[alias] + "\t" + alias)
                        print()
                        temp_alias = input("Which alias would you like to replace? ")

                        for alias in alias_list:
                            if temp_alias == alias:
                                loop2 = False

                        if loop2:
                            print("Invalid alias. Please pick a valid alias from the list")
                            pause()

                    conflict = True
                    while conflict:
                        conflict = False
                        new_alias = input("What would you like to change [" + temp_alias + "] to? ")
                        for dict_alias in key_dict:
                            if new_alias == dict_alias:
                                print("Error: " + new_alias + " is already associated in an existing key binding")
                                print()
                                print("Key:\t\tAlias")
                                print("_____________________")
                                print(key_dict[new_alias] + "\t\t" + new_alias)
                                print("_____________________")
                                print()
                                print("Please choose another alias.")
                                print()
                                pause()
                                print()
                                conflict = True

                    print("Key:\t\tAlias")
                    print("_____________________")
                    print("BEFORE:")
                    print(key_dict[temp_alias] + "\t\t" + temp_alias)
                    # remove the old binding from the dict and add the new one
                    del key_dict[temp_alias]
                    key_dict[new_alias] = button

                    print("AFTER:")
                    print(key_dict[new_alias] + "\t\t" + new_alias)


                loop1 = False
                print()
                saveMapping()
                pause()

            else:
                print("Error: " + button + " is not in the key mapping.")
                print("Take note that the button names are case sensitive")
                print("Please try again.")
                print()
                pause()
                clear()


def removeMapping():
    clear()
    loop1 = True
    while loop1:
        print("Here are the current Key Bindings.")
        printMapping()
        print()
        print("Which button would you like to remove? ")
        print()
        print("Type \"__exit\" to exit")
        print()
        button = input("What keyboard button would you like to remove? ").strip()
        if button.strip().lower() == "__exit":
            print()
            print("Exiting")
            print()
            pause()
            return
        else:
            alias_list = getAliasFromKey(button)
            if alias_list:
                print()
                if len(alias_list.keys()) == 1:
                    # remove the old binding from the dict and add the new one
                    for alias in key_dict:
                        if key_dict[alias] == button:
                            print("Removing the following binding:")
                            print(key_dict[alias] + "\t\t" + alias)
                            del key_dict[alias]
                            break
                else:
                    loop2 = True
                    while loop2:
                        clear()
                        print("Multiple bindings for [" + button + "] found.")
                        print()
                        print("Key\tAlias")
                        print("_____________________")
                        for alias in alias_list:
                            print(alias_list[alias] + "\t" + alias)
                        print()
                        print("Which alias would you like to remove?")
                        print("You can type __all to remove all associated bindings.")
                        print()
                        temp_alias = input("Which alias would you like to remove? ")

                        if temp_alias == "__all":
                            print("Deleting all alias' associated with [" + button + "].")
                            for alias in alias_list:
                                del key_dict[alias]
                            loop2 = False
                            break

                        for alias in alias_list:
                            if temp_alias == alias:
                                loop2 = False
                                print("Removing the following binding:")
                                print("Key\tAlias")
                                print("_____________________")
                                print(key_dict[temp_alias] + "\t" + temp_alias)
                                # remove the binding from the dict
                                del key_dict[temp_alias]
                                loop2 = False
                                break

                        if loop2:
                            print()
                            print("Invalid alias. Please pick a valid alias from the list")
                            pause()

                loop1 = False
                print()
                saveMapping()
                pause()

            else:
                print("Error: " + button + " is not in the key mapping.")
                print("Take note that the button names are case sensitive")
                print("Please try again.")
                print()
                pause()
                clear()


def printManuallyEditing():
    clear()
    print("Manually editing the key mapping can be done by opening the \"map.json\" file in a text editor.")
    print()
    print("Choosing to manually edit the mapping can be faster, but should only be done if you're not worried about "
          "messing up.")
    print()
    print("It is recommended that you save a copy of map.json before you manually edit the mapping so that you can "
          "revert to a working file in case you make a mistake.")
    print()
    print()
    pause()
    print("\033[A                             \033[A")
    print()
    print("When you open map.json, you'll see something similar to the following.")
    print('''
    {
        "down": "DOWN",
        "up": "UP",
        "left": "LEFT",
        "right": "RIGHT",
    }
    ''')
    print()
    print()
    print("The string before the colon is known as the 'alias', it is the keyword that the bot looks for to know "
          "which button it should press.")
    print()
    print("The string after the colon is the button code, every button on the keyboard has an associated code.")
    print("You can find a list of all keyboard codes in validkeys.md")
    print("Make sure that you only use valid keyboard codes.")
    print()
    pause()
    print("\033[A                             \033[A")
    print()
    print("The proper structure to add a new mapping is as follows:")
    print("\t\"[ALIAS]\": \"[KEYBOARD CODE]\",")
    print()
    print("Its important that you use double quotation marks [\"] and not single quotation marks [']")
    print("Don't forget to add a comma after you write a new mapping")
    print()
    print("After manually editing the keyboard mapping, you should go to the \"See Current Key Bindings\" menu to double check that everything is right.")
    print()
    pause()


def printValidPresses():
    print("Here's a list of all allowed key presses.")
    print("___________________________________________")
    print()
    print("`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "-", )
    print("~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", )
    print("q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "\\", )
    print("Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "{", "}", "|", )
    print("a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", )
    print("A", "S", "D", "F", "G", "H", "J", "K", "L", ":", "\"", )
    print("z", "x", "c", "v", "b", "n", "m", ",", ".", "/", )
    print("Z", "X", "C", "V", "B", "N", "M", "<", ">", "?", )
    print("UP", "DOWN", "LEFT", "RIGHT", )
    print("NUM1", "NUM2", "NUM3", "NUM4", "NUM5", "NUM6", "NUM7", "NUM8", "NUM9", "NUM0", "NUM-", "NUM+", )
    print("INS", "HOME", "PGUP", "DEL", "END", "PGDN", "PRTSC", "SCROLL_LOCK", )
    print("F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", )
    print("CTRL", "LSHIFT", "RSHIFT", "BSLASH", "BKSP", "ENTER", "TAB", "TILDE", "BACKTICK", "ALT", "SPACEBAR",
          "CAPSLOCK", "NUMLOCK")


def printBotSettings():
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
    if extraDetails:
        print("Extra Details: On")
    else:
        print("Extra Details:: Off")
    print()
    print()


def setPrefixStuff():
    global prefix
    global usePrefixes
    loop1 = True
    while loop1:
        clear()
        print("The bot can filter inputs so that it will only take in messages that begin with a certain string.")
        print("For example, you set it such that the message \"!bot A\" will press the A key, you can also set it such "
              "that just \"A\" will press the A Key ")
        print()
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
        print()
        print("Please enter '1','2', or '3'")
        userInput = input().lower()
        if userInput == '1':
            clear()
            if usePrefixes:
                print("You are no longer using prefixes.")
                print("The bot will now interpret every message it sees as a potential call for a keyboard press")
                usePrefixes = False
            else:
                print("You are now using prefixes.")
                print("The current prefix is: " + prefix)
                print()
                print("The bot will now only consider messages that start with " + prefix + " as potential calls for a "
                                                                                            "keyboard press.")
                usePrefixes = True
            print()
            pause()
        elif userInput == '2':
            clear()
            print("The current prefix is: " + prefix)
            if not usePrefixes:
                print()
                print("You are currently not using prefixes, but you can still change the prefix in case you would "
                      "like to use prefixes in the future.")
            loop2 = True
            while loop2:
                print()
                print("Would you like to change the prefix? Please enter 'y' or 'n'")
                userInput = input().lower()
                if userInput == 'y':
                    print()
                    newPrefix = input("Please enter the new Prefix: ").strip()
                    prefix = newPrefix
                    print()
                    print("The current Prefix is: " + prefix)
                    print()
                    loop2 = False
                elif userInput == 'n':
                    loop2 = False
                else:
                    print("Invalid Input")
        elif userInput == '3':
            print("Exiting")
            print()
            loop1 = False
        else:
            print("Invalid Input")
    saveConfig()
    pause()


def setCaseSensitive():
    global caseSensitive
    loop1 = True
    clear()
    while loop1:
        print("The bot can be set to be case sensitive when matching a message to keys.")
        print("It is recommended to keep case sensitivity off.")
        print()
        if caseSensitive:
            print("Case Sensitivity is currently ON.")
        else:
            print("Case Sensitivity is currently OFF.")
        print()
        print("Would you like to turn the case sensitivity on or off? ")
        print()
        print("Please enter either 'on' or 'off'")
        userInput = input().lower()
        if userInput == 'on':
            print()
            print("Case Sensitivity has been turned on")
            caseSensitive = True
            loop1 = False
        elif userInput == 'off':
            print()
            print("Case Sensitivity has been turned off")
            caseSensitive = False
            loop1 = False
        else:
            print("Invalid Input")
    saveConfig()
    pause()


def setPressTime():
    global pressTime
    loop1 = True
    while loop1:
        clear()
        print("The bot can be set to hold keypresses for a set amount of time.")
        print("By default, the bot presses keys down for 0.05 seconds.")
        print()
        print("The current press time is " + str(pressTime) + " seconds")
        print()
        print("Would you like to change the press time? ")
        print()
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
    pause()


def setextraDetails():
    global extraDetails
    loop1 = True
    while loop1:
        clear()
        print("The bot can be set to also report to console about any messages that fail to press a button.")
        print("Messages can fail to press a button in the following ways:")
        print("• Not using the prefix")
        print("• Trying to reference an alias that doesn't exist.")
        print("Extra Details mode will also tell you about details when editing settings.")
        print()
        print("It is recommended to keep the Extra Details menu off to avoid cluttering your console.")
        print()
        if extraDetails:
            print("The Bot is currently in Extra Details  mode")
        else:
            print("The Bot is currently NOT in Extra Details  mode")
        print()
        print("Would you like to turn Extra Details  mode on or off")
        print("Please enter either 'on' or 'off'")
        userInput = input().lower()
        if userInput == 'on':
            print()
            print("Extra Details Mode has been turned on")
            extraDetails = True
            loop1 = False
        elif userInput == 'off':
            print()
            print("Extra Details Mode has been turned off")
            extraDetails = False
            loop1 = False
        else:
            print("Invalid Input")
    saveConfig()
    pause()


def setBotToken():
    global token
    loop1 = True
    while loop1:
        clear()
        print("A Bot Token is a long randomized string of characters that is unique to your specific bot account.")
        print("By providing your bot account's token, you allow this program to control your bot account.")
        print("If you don't know how to find your bot token, you can google how to find it, or look at the "
              "\"How to setup a Discord Bot Account.pdf\" located in the docs folder.")
        print()
        print("The Current Bot Token is: " + token)
        print()
        print("Would you like to change the Bot Token? ")
        print()
        print("Please enter either 'y' or 'n'")
        userInput = input().lower()
        if userInput == 'y':
            print()
            newToken = input("Please enter your new Bot Token: ")
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
    pause()


def setSkipMenu():
    global skipMenu
    loop1 = True
    while loop1:
        clear()
        print("Are you sure you want to turn off the startup menu?")
        print()
        print(
            "If you turn this off, then using run.bat will immediately start up the bot, but you'll no longer be "
            "able to change any settings without manually editing the configuration file yourself.")
        print()
        print(
            "Type \"y\" to confirm that you would like to turn off the startup menu. Type \"n\" to go back to the main "
            "menu.")
        userInput = input().lower()

        if userInput == "y":
            skipMenu = True
            print()
            print("You have turned off the startup menu.")
            print(
                "If you would like to turn the startup menu back on, you can edit config.json using a text editor and "
                "set \"skipMenu\" from true to false")
            loop1 = False
        elif userInput == "n":
            print()
            print("Returning to Main Menu.")
            loop1 = False
        if userInput != "y" and userInput != "n":
            print("Please type either (y) or (n)")
    saveConfig()
    pause()


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
            clear()
            # startup menu
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
                clear()
                if len(data["token"]) <= 30:
                    print("Hi, it looks like this is your first time running this bot.")
                    print("Lets quickly go through some initial set up.")
                    print("")
                    print("First off, lets get your bot account's token.")
                    print()
                    print("Press ENTER to continue.")
                    input()
                    setBotToken()
                    clear()
                    print("Here is the current Keyboard Bindings")
                    printMapping()
                    print()
                    print("If you would like to customize these button mappings, "
                          "please restart the bot after finishing the initial setup and go into menu 2 in the Startup menu. "
                          "You can restart the bot by pressing Ctrl + C or by simply closing the window.")
                    print("Press ENTER to continue.")
                    input()
                    clear()

                    print("Here is the current list of bot settings")
                    printBotSettings()
                    print()
                    print("If you would like to customize these settings, "
                          "please restart the bot after finishing the initial setup and go into menu 3 in the Startup menu."
                          "You can restart the bot by pressing Ctrl + C or by simply closing the window.")
                    print("Press ENTER to continue.")
                    input()

                    print("Startup Complete.")


                loop1 = False
            elif userInput.startswith("2"):
                loop2 = True
                while loop2:
                    clear()
                    print("Keyboard Bindings")
                    print("________________________")
                    print("1. See Current Key Bindings")
                    print("2. Edit Key Bindings")
                    print("3. Learn how to manually adjust Key Bindings")
                    print("4. Back")
                    print("")
                    userInput = input("Which menu would you like to go to? ")
                    if userInput.startswith("1"):
                        clear()
                        print("Here are the current Key Bindings:")
                        printMapping()
                        pause()
                    elif userInput.startswith("2"):

                        loop3 = True
                        while loop3:
                            clear()
                            print("Here are the current Key Bindings.")
                            printMapping()
                            print("What would you like to do? ")
                            print()
                            print("1. Add a binding for a new key.")
                            print("2. Change a binding for a key.")
                            print("3. Remove a binding for a key.")
                            print("4. See a list of all valid key presses.")
                            print("5. Back")
                            print()
                            userInput2 = input("Please enter '1', '2', '3', '4', or '5'. ")
                            if userInput2.startswith("1"):
                                addMapping()
                            elif userInput2.startswith("2"):
                                editMapping()
                            elif userInput2.startswith("3"):
                                removeMapping()
                            elif userInput2.startswith("4"):
                                clear()
                                printValidPresses()
                                print()
                                pause()

                            elif userInput2.startswith("5"):
                                loop3 = False
                            else:
                                print("Please enter a proper input.")
                                print("Options are '1', '2', '3', '4', or '5'.")
                                pause()

                    elif userInput.startswith("3"):
                        printManuallyEditing()
                    elif userInput.startswith("4"):
                        loop2 = False
                    else:
                        print("Please enter a proper input.")
                        print("Options are '1', '2', '3',or '4'.")
                        pause()

            elif userInput.startswith("3"):
                loop2 = True
                while loop2:
                    clear()
                    print("Bot Settings")
                    print("________________________")
                    print("1. See Current List of Settings")
                    print("2. Prefix")
                    print("3. Case Sensitivity")
                    print("4. Press Time")
                    print("5. Extra Details Mode")
                    print("6. Change Bot Token")
                    print("7. Save and Return to Main Menu")
                    print()
                    userInput = input("Which menu would you like to go to? ")
                    if userInput.startswith("1"):
                        clear()
                        printBotSettings()
                        pause()
                    elif userInput.startswith("2"):
                        setPrefixStuff()
                    elif userInput.startswith("3"):
                        setCaseSensitive()
                    elif userInput.startswith("4"):
                        setPressTime()
                    elif userInput.startswith("5"):
                        setextraDetails()
                    elif userInput.startswith("6"):
                        setBotToken()
                    elif userInput.startswith("7"):
                        print("")
                        print("Saving")
                        saveConfig()
                        loop2 = False
                    else:
                        print("Please enter a proper input.")
                        print("Options are '1', '2', '3', '4', '5', '6' or '7'.")
                        pause()
                pause()

            elif userInput.startswith("4"):
                print()
                print()
                print("This bot is used to press buttons on a host's keyboard based on input provided through text messages sent on Discord.")
                print("By connecting this program with a discord bot account, the program will read every message "
                      "sent in a given server, and press a button if it sees an appropriate message.")
                print("For example, if the bot reads that a user has typed \"up\", the bot will press the up arrow on the host's keyboard.")
                print("")
                print("Press ENTER to exit.")
                input()
            elif userInput.startswith("5"):
                setSkipMenu()
                if skipMenu:
                    loop1 = False
            elif userInput.startswith("6"):
                print("Press ENTER to exit.")
                input()
                sys.exit(0)
            else:
                print("Please enter a proper input.")
                print("Options are '1', '2', '3', '4', '5', '6'.")
                pause()

        print("Starting up the bot...")
        saveConfig()

