
import os
import re

from dice import roll, rolls
from clocks import clock
from gamestate import turn
from stats import hp
from helpvtt import vttHelp

# ----------------------------------------------------------------------------------------------------------------

# Primary VTT interface/logic loop using a dictionary of functions callable by user input
def interact():
    dispatcher = {
        'roll':     roll, 
        'rolls':    rolls, 
        'hp':       hp, 
        'stats':    hp, 
        'turn':     turn, 
        'clock':    clock, 
        'clocks':   clock, 
        'help':     vttHelp,
        'end':      exit
    }
    # Handles synonyms or alternative orders of input arguments
    dynamicArgs = {
        'delete':   'delete',
        'remove':   'delete',
        'clear':    'delete',
        'del':      'delete', 
        'create':   'create', 
        'make':     'create',
        'add':      'create',
        'new':      'create'
    }

    # Input variable and main loop
    action = 'init'
    while action != 'end':

        # Prompts user for input and splits input string into arguments for processing
        print('\nInput action: ')
        inputString = input()
        action = inputString.split()
        # Clears screen to maintain readability and consistent user experience
        os.system('cls||clear')
        print(f'Input: {inputString}\n')

        # Switches the order of certain arguments for grammatically comfortable input
        if (len(action) > 1) and (action[0] in dynamicArgs):
            switchTemp = dynamicArgs[action[0]]
            action[0] = action[1]
            action[1] = switchTemp
        # Replaces certain arguments with synonyms
        elif (len(action) > 1) and (action[1] in dynamicArgs):
            action[1] = dynamicArgs[action[1]]

        # Calls functions with dispatcher
        # Handles special input cases first, does nothing but print feedback if input is unusable
        if action[0] not in dispatcher:
            print('Function not found in dispatcher\n')
            
        # Provides user assistance with vttengine features
        elif action[0] == 'help':
            dispatcher[action[0]](dispatcher, dynamicArgs, *action[1:])

        # Calls dispatcher without attempting to pass arguments if none are provided 
        elif len(action)==1:
            dispatcher[action[0]]()
            
        # Restructures input arguments if the user is attempting to roll dice
        # Uses regex to parse a flexible pattern of potential dice roll inputs
        # Example inputs: 6d6, 5 d4 +1, 3d20/2, 1d8**2, 5 2, 100 d4-1
        elif action[0] == 'roll':
            diceArgs = re.split(rf'(\d+)[ ]?[d]?(\d+)[ ]?(\S+\d+)?', inputString.split(' ', 1)[1])
            dispatcher[action[0]](*diceArgs[1:-1])

        # Handles special input cases for the clock function
        elif action[0] == 'clock':
            dispatcher[action[0]](*action[1:], inputString)

        # Calls a function with the first input word and the rest of the input as arguments
        else:
            dispatcher[action[0]](*action[1:])

# ----------------------------------------------------------------------------------------------------------------

# VTT initialization and isolated top-level for extensibility
def main():
    os.system('cls||clear')
    print('Initiating VTTEngine')
    interact()
main()

# ----------------------------------------------------------------------------------------------------------------
