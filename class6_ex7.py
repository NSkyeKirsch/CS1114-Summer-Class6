contacts = {"Lily": "212-111-2222", "Jenny": "212-867-5309", "Anthony": "212-333-4444",
            'Heisenberg': '324-555-3369', 'Lucy': '123-456-7890'}

keys_list = []
for key in contacts:
    keys_list.append(key)

keys_list.sort()

for sorted_key in keys_list:
    print(sorted_key, ':', contacts[sorted_key])  # We did all of this to have a sorted output, since dicts are not
