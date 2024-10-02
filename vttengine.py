
import os
import re
# from collections import defaultdict
# from functools import partial

from dice import roll, rolls
from clocks import clock
from gamestate import turn
from stats import hp
from helpvtt import vttHelp

# ----------------------------------------------------------------------------------------------------------------

# Primary VTT interface/logic loop using a dictionary of functions callable by user input
def interact():

    # Handles synonyms of functions and most function calling
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
    options = {
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
        inputString = input('\nInput action: ')
        action = inputString.split()
        function = 'help'
        option = 'all'
        
        # Clears screen to maintain readability and consistent user experience
        os.system('cls||clear')
        print(f'Input: {inputString}\n')

        # Assigns variables by permutations of input argument order for grammatically comfortable input
        match action:
            case ['end']: break
            case []: pass
            case ['help' as function]: pass 
            case ['help' as function, option] | [option, 'help' as function]: pass
            case [function, option, *args] if function in dispatcher: pass
            case [option, function, *args] if function in dispatcher: pass
            # Calls functions with no arguments if none are given
            case [function] if function in dispatcher:
                dispatcher[function]()
                continue
            # Provides user feedback if no function-call matches are found for a given input
            case _: 
                print('Function not found in dispatcher\n')

        # Calls functions with dispatcher and handles special argument cases
        match function:
            # Uses regex to parse a flexible pattern of potential dice roll inputs
            # Example inputs: 6d6, 5 d4 +1, 3d20/2, 1d8**2, 5 2, 100 d4-1
            case 'roll':
                diceArgs = re.split(rf'(\d+)[ ]?[d]?(\d+)[ ]?(\S+\d+)?', inputString.split(' ', 1)[1])[1:-1]
                dispatcher[function](*diceArgs)
            # Handles extended arguments and stage definition strings for the clock function
            case 'clock':
                dispatcher[function](options[option], *args, inputString)
            # Passes additional meta-programming information to the help function
            case 'help':
                dispatcher[function](dispatcher, options, option)
            # Calls all other functions with optionally aliased arguments
            case _:
                dispatcher[function](options.get(option, option), *args)

# ----------------------------------------------------------------------------------------------------------------

# VTT initialization and isolated top-level for extensibility
def main():
    os.system('cls||clear')
    print('Initiating VTTEngine')
    interact()
main()

# ----------------------------------------------------------------------------------------------------------------
