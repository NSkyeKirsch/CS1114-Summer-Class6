contacts = {"Lily": "212-111-2222", "Jenny": "212-867-5309", "Anthony": "212-333-4444"}
contacts['Heisenberg'] = '324-555-3369'
contacts['Lucy'] = '123-456-7890'

for key in contacts:
    print(key, '-', contacts[key])

print('-'*20)

for key in contacts.keys():
    print(key)

print('-'*20)

for values in contacts.values():
    print(values)

print('-'*20)

for key, value in contacts.items():  # look at the tuple!
    print(key, '-', value)

