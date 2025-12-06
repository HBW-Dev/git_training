# study_notes.py

# --- 1. List Slicing ---
# Define a list of 5 players
players = ['zhang san', 'li si', 'wang wu', 'zhao liq', 'zhou qi']
print(players[0:3])

# Task: Print the last 3 players using negative slicing
print(players[-3:])

new_players = players[:]

# --- 2. Dictionary.get() ---
# Define a dictionary for a user (without 'age' key)
user = {
    'name': 'user1',
    'id': '001'
}

# Task: Print 'age' using .get() to provide a default value 'Unknown' 
print(user['id'])
# print(user['age']) error
print(user.get('age'))

# --- 3. f-string Formatting ---
# Dfine a float variable pi = 3.1415926
pi = 3.1415926

# Task: Print it formatted to exactly 2 decimal places
print(f"Pi is approximately {pi:.2f}")