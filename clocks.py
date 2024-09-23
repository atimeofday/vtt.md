
import re

# ----------------------------------------------------------------------------------------------------------------

# Manages markdown-checklist clocks
def clock(action='display', clockName='all', *args):
    # Copies contents of clocks file and creates backup of initial data
    with open('clocks.md') as clocks:
        data = clocks.read()
        newData = data

    # Catches partial input cases, prints all clocks if no arguments are entered
    if (clockName == 'all') and (action == 'display'):
        print(data)
        return
    # Provides user feedback if user attempts to create a clock without a name
    elif (clockName == 'all') and (action == 'create'):
        print('Clock must be named')
        return

    # Searches for a matching clock entry by name with regex
    pattern = rf'(Clock )({clockName})\n(.([x ]). (.*)\n?)+'
    match = re.search(pattern, data)
    if match:
        clock = match.group(0)
        # Displays named clock  
        if action == 'display':
            print(clock)
            return
        # Provides user feedback if a matching clock is found while trying to create one
        elif action == 'create':
            print(f'Clock {clockName} already exists')
            print(clock)
        # Deletes a named clock
        elif action == 'delete':
            # Allows user to clear/delete a clock after confirmation prompt
            print(f'Confirm deletion of clock: {clockName}: ')
            inputString = input()
            if inputString in ('y', 'yes', 'confirm'):
                newData = data.replace(clock, '')
        # Increments a named clock
        elif action == '+':
            updatedClock = clock.replace('[ ]', '[x]', 1)
            newData = data.replace(clock, updatedClock)
        # Decrements a named clock
        elif action == '-':
            updatedClock = clock[::-1].replace(']x[', '] [', 1)[::-1]
            newData = data.replace(clock, updatedClock)
        # END IF/ELIF
        
        # WRITES UPDATED FILE CONTENTS AFTER MATCHING CLOCK IS UPDATED --------------------------------------#
        with open('clocks.md', 'w') as clocks:
            newData = newData.rstrip() + '\n'
            clocks.write(newData)
            print(f'Clocks updated\n{newData}')
        # WRITES UPDATED FILE CONTENTS AFTER MATCHING CLOCK IS UPDATED --------------------------------------#


    # Creates a user-defined clock in clocks.md
    elif action == 'create':
        # Handles missing input cases
        if clockName == 'all':
            print('Clock must be named')
            return
        elif not args:
            print('A number of stages or set of quoted stages must be entered')
            return
        # Defines clock parameters from input
        else:
            numStages = args[0]
            inputString = args[-1]
            stagesList = inputString[0].split('"')[1::2]
            newClock = ''

        # Builds a new clock from an input number of generic stages 
        if numStages.isdigit():
            stageRange = range(1, int(numStages) + 1)
            newClock = 'Clock ' + clockName + ''.join([f'\n[ ] Stage {stage}' for stage in stageRange])
        # Builds a new clock from an input set of "quoted" stages
        elif stagesList:
            newClock = 'Clock ' + clockName + ''.join([f'\n[ ] {stage}' for stage in stagesList])
        # Provides user feedback if there is an input handling issue
        else:
            print('Could not parse number of stages or quoted stages\n')

        # Appends new clock to clocks file ff a new clock has been properly defined
        # Prints newly created clock as user feedback
        if newClock:
            with open('clocks.md', 'a') as clocks:
                clocks.write('\n\n' + newClock + '\n')
                print(newClock)
            
    # Provides user feedback if no clock with the input name is found
    else:
        print(f'Clock {clockName} not found')

# (Clock )(\w+)\n                       # regex for clock first line
# (.([x ]). (.*)\n?)                    # regex for each subsequent clock line
# (Clock )(\w+)\n(.([x ]). (.*)\n?)+    # regex for one full clock

# ----------------------------------------------------------------------------------------------------------------
