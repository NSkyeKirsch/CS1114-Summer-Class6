import math


def main():
    user_value = int(input("Enter a number that is not 4!: "))

    try:
        if user_value == 4:
            raise ValueError("Dude, you entered a " + str(3 + 1))
        else:
            print("You entered:", user_value)
    except ValueError as val_error:
        print("The message was: ", val_error)

    #
    #
    #
    # ignore stuff below this
    #
    #
    #

    print()
    print("For homework:")
    the_list = []
    for i in range(-1, 2):
        try:
            the_list.append(i)
        except IndexError:  # Although there can be max 8 neighbors, some have less because of their location
            the_list.append('')
    print(the_list)


if __name__ == "__main__":
    main()

    # you could also wrap this part in the ty-except valueerror statement, then use if-else inside the function
