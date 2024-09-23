
# ----------------------------------------------------------------------------------------------------------------

# Provides user assistance with vttengine features
def vttHelp(dispatcher, dynamicArgs, feature='all'):

    # Prints all functions and defined dynamic arguments
    if feature == 'all': 
        print('Available functions: ')
        for key in dispatcher.keys():
            print(key)
        print('\nAvailable action synonyms as first or second word: ')
        for key, value in dynamicArgs.items():
            print(f'{key}: {value}')
        print('\nUse "help [function]" for more detailed information')

    # ---
    elif feature == 'roll':
        print('''Options: [see dice grammar]

Allows rolling a number of dice with a number of sides and optional modifiers.
Defaults to 1d20 if used with no inputs.

Stores dice rolls in a rolls.md file.

Example inputs: roll 5d8,   roll 6 d7 -1,   roll 50d10/2,   roll 2 d12''')
                
    # ---
    elif feature == 'rolls':
        print('''Actions: display / delete

Allows viewing or clearing past dice rolls stored in a rolls.md file.
Defaults to 'display' if used with no inputs.
''')

    # ---
    elif feature == 'hp':
        print('''Input: [playerName] ; [hpEffect]

Allows viewing or editing player hp values.
Defaults to displaying stats for all players if used with no inputs.

Accepts positive or negative hp changes, and respects min/max health.
For ease of input, names of existing players are not case-sensitive.

Example inputs: hp Playername 10,  hp Playername -10
''')

    # ---
    elif feature == 'stats':
        print('''Input: [none] / [see hp feature]

Allows viewing (or editing) all player hp values.
(Currently) a synonym for "hp", meant for showing all hp values.''')

    # ---
    elif feature == 'turn':
        print('''Input: [turnChange]

Allows incrementing (or altering) a global turn counter
Defaults to +1 if used with no inputs.

Example inputs: 1,   2,  -1,  -2''')

    # ---
    elif feature == 'clock':
        print('''Options: 
display / + / - / create / delete
[clockName]
[#] of stages / ["Stage 1" "Stage 2"...]


Allows viewing, incrementing, creating, and deleting "clock" constructs.
Clocks are stored as markdown lists in a clocks.md file.

Example inputs:
clock hackme
clock hackme +
create clock SneakingIn "Surveying area" "Moving close" "Picking lock"
clocks add BoomTimer 6
remove clock BoomTimer
''')

    # ---
    elif feature == 'clocks':
        print('''Options: [see clock feature]
         
(Currently) a synonym for "clock", and should be interchangeable. 
Also meant for showing all clocks with no input.''')

    # ---
    elif feature == 'help':
        print('''Options: [See dispatcher list]

Prints general or function-specific help info.''')

    # ---
    elif feature == 'end':
        print('Exits VTTEngine')    

    # ---
    else:
        print(f'Feature {feature} not found in help docs')

# ----------------------------------------------------------------------------------------------------------------
