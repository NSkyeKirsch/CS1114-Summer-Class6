def main():
    stuff = {}

    stuff[1] = "One"
    stuff[12.3] = 12.3

    stuff[0] = (1, 2)
    stuff[(1, 0)] = [1, 3, 6, 9]

    stuff["data"] = {1: 2, 3: 4, 5: [5, 67]}

    return stuff  # keys and values can be a lot of different things


my_data = main()
print(my_data)
print(my_data["data"][5][1])

print()

print(len(my_data))
print(my_data.get((1, 0)))  # similar to my_data[(1, 0)], but you can set a default value
my_data.pop('data')  # can remove a key-value pair from the dictionary

print(my_data)