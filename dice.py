
import random
import re

# ----------------------------------------------------------------------------------------------------------------

# Displays log of dice rolls stored in rolls.md
def rolls(action='display'):
    if action == 'display':
        with open('rolls.md') as rollsLog:
            print(rollsLog.read())

    # Allows user to clear log of dice rolls after confirmation prompt
    elif action == 'delete':
        print('Confirm delete roll history: ')
        inputString = input()
        if inputString in ('y', 'yes', 'confirm'):
            open('rolls.md', 'w').close()        

# ----------------------------------------------------------------------------------------------------------------

# Simulates rolling dice with flexible input, number of dice, sides per die, and arithmetic modifiers 
# Die rolls are presented in two lists, one before modifiers and one after, and logged in a rolls.md file
def roll(numDice=1, numSides=20, mods=0):
    dieRolls = []
    modRolls = []

    # User feedback and 1d20 fallback for no-argument function call
    if numDice == 1 and numSides == 20:
        print('Rolling 1 D20')

    # Rolls all dice and stores rolls
    for die in range(int(numDice)):
        dieRoll = random.randint(1, int(numSides))
        dieRolls.append(dieRoll)

        # Parses arithmetic operations and modifier values using string evaluation
        # TODO Consider security concern of input string execution
        if mods:
            modRoll = eval(f'dieRoll {mods}')
            modRolls.append(modRoll)

    # Prints and logs all dice rolls and their total value
    with open('rolls.md', 'a') as rollsLog:
        logString = f'\n\nRolled {numDice} D{numSides}'

        # Prints all initial rolls and their total value 
        rollString = '{0}{1}{2}{3}'.format('\nRolls: ', ' '.join(map(str, dieRolls)), '\nTotal: ', sum(dieRolls))
        print(rollString)

        # Prints all modified rolls and their total value if a modifier was entered
        modRollString = ''
        if mods:
            modRollString = '{0}{1}{2}{3}'.format('\nModified Rolls: ', ' '.join(map(str, modRolls)), '\nTotal: ', sum(modRolls))
            logString = f'{logString} mod {mods}'
            print(modRollString)
            
        rollsLog.write(logString + rollString + modRollString)

# ----------------------------------------------------------------------------------------------------------------
