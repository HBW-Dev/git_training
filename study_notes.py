# study_notes.py

# --- 1. List Slicing ---
# Define a list of 5 players
players = ['zhang san', 'li si', 'wang wu', 'zhao liq', 'zhou qi']
print(players[0:3])

players.append('xi ba') # Add
print(players)

del players[1]  # Delete (Remove by index)
print(players)

players.remove('wang wu') # Delete (Remove by value)
print(players)

players[0] = 'zhang ling' # Update
print(players[0])

# Search: Check if exists
player = "wang wu"
if player in players:
    print(player)
else:
    print("Not found")

# Search: Find position
location = players.index('zhang ling')
print(f"zhang ling is at index {location}")
# Task: Print the last 3 players using negative slicing
print(players[-3:])

# Copy
new_players = players[:]
print(new_players)

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

user['age'] = 26 # Add
print(user.get('age'))

del user['name'] # Delete
print(user.get('name'))

print(user.pop('id')) # Delete and return value
print(user.get('id'))

print(user.get('id', '01')) 

if '01' in user:
    print(f'{user.get('name')} has an ID')
else: 
    print(f'{user.get('name')} has no ID')
# --- 3. f-string Formatting ---
# Dfine a float variable pi = 3.1415926
pi = 3.1415926

# Task: Print it formatted to exactly 2 decimal places
print(f"Pi is approximately {pi:.2f}")