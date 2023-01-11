names = ['Jebediah', 'David', 'Cory', 'Travis']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

# Code to refactor
index = 0
for name in names:
    print(index, name)
    index += 1

print("\n *** New loop *** \n")

# Refactored Code
for index, name in enumerate(names):
    print(index, name)

print("\n *** New loop *** \n")

# Enumerate for two lists example:

# Code to refactor
for index, name in enumerate(names):
    hero = heroes[index]
    print(f'{name} is actually {hero}')

print("\n *** New loop *** \n")

# Refactor code
for name, hero in zip(names, heroes):
    print(f'{name} is actually {hero}')

print("\n *** New loop *** \n")

# Refactor code with universes
for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')