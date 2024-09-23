
import re

# ----------------------------------------------------------------------------------------------------------------

# Manages turn-based game state advancement
def turn(turnChange=1):
    with open('gamestate.md') as gamestate:
        data = gamestate.read()

    # Locates turn data in gamestate.md
    pattern = rf'(Turn\n)(\d*)'
    match = re.search(pattern, data)
    if match:
        # Advances recorded game state by one turn or advances/reverses by the input number of turns
        newTurn = int(match.group(2)) + int(turnChange)
        print(f'Turn {match.group(2)} -> {newTurn}.\n')
        newData = re.sub(pattern, f'{match.group(1)}{newTurn}', data)
        # Writes the edited file contents to gamestate.md 
        with open('gamestate.md', 'w') as gamestate:
            gamestate.write(newData)

    # Provides user feedback if turn data cannot be found in the gamestate.md file    
    else:
        print(f'Turn data not found')
        gamestate.write(data)

# ----------------------------------------------------------------------------------------------------------------
