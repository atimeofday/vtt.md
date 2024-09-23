
import re

# ----------------------------------------------------------------------------------------------------------------

# Modifies a given player's health in players.md by a given positive or negative amount
# Example input: hp PlayerName -10
def hp(player='all', hpEffect='0'):
    hpEffect = int(hpEffect)

    # Stores backup of initial players.md file contents
    with open('players.md') as players:
        data = players.read() 
    if player == 'all':
        print(data)
        return

    # Extracts, searches, and conditionally modifies players.md file contents
    # Searches for a matching player name and health entry with regex
    # Regex format example: PlayerName\nHP 40/50
    pattern = rf'(({player})\nHP )+(\w+)\/+(\w+)'
    match = re.search(pattern, data, re.IGNORECASE)
    if match:
        # If a matching entry in players.md is found for the input name, their health is calculated
        # The new health value is clamped within min and max health bounds
        maxHP = int(match.group(4))
        HP = int(match.group(3))
        newHP = max(min(maxHP, HP + hpEffect), 0)
        hpDiff = newHP - HP

        # Prints the actual amount of health gained or lost by the player
        # Uses the same regex search pattern to replace health values in players.md
        print(f'{match.group(2)} {'gained' if hpDiff >= 0 else 'lost'} {abs(hpDiff)} health.\n')
        newData = re.sub(pattern, f'{match.group(1)}{newHP}/{match.group(4)}', data, flags=re.IGNORECASE)
        # Writes the edited file contents to players.md
        with open('players.md', 'w') as players:
            players.write(newData)

    # If no matching entry is found, the user is informed and the file is unchanged
    else:
        print(f'Player "{player}" not found.\n')

    # Prints the new contents of the players.md file
    with open('players.md') as players:
        print(players.read())

# ----------------------------------------------------------------------------------------------------------------
