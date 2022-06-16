def main():
    contacts = {"Lily": "212-111-2222", "Jenny": "212-867-5309", "Anthony": "212-333-4444"}

    # Access one contact, via the key using index operator [] (do NOT use numbers, use keys)

    print(contacts["Jenny"])

    other_person = "Anthony"
    print(contacts[other_person])

    print("before change:", contacts)

    contacts['Anthony'] = '609-333-3344'
    print("after change: ", contacts)

    try:
        print(contacts['Lucy'])
    except KeyError:
        print("Lucy has no phone.")

    # Add a key-value pair, via assignment statement
    # if the key does not exist, it is created with specified value
    # otherwise, key's value is updated

    contacts['Heisenberg'] = '324-555-3369'

    print('updated contacts:', contacts)

    pete_in_dictionary = "Pete" in contacts  # checks to see if the key is in the dictionary
    print(pete_in_dictionary)
    lily_in_dictionary = "Lily" in contacts
    print(lily_in_dictionary)

    this_number = "609-333-3344"
    print(this_number in contacts)  # the value is not a key, therefore False











if __name__ == "__main__":
    main()


