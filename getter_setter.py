class Person():
    pass

person = Person()

first_key = 'first'
first_val = 'Jacob'

setattr(person, first_key, first_val)

first = getattr(person, first_key)

print(first)

# ********************************************
# Setting values while using a dictionary   **
# ********************************************

person_info = {'first': 'Jacob', 'last': 'Boyk'}

for key, value in person_info.items():
    setattr(person, key, value)

print(person.first, person.last)
print("\n*** Iterating through keys ***\n")

for key in person_info.keys():
    print(getattr(person, key))