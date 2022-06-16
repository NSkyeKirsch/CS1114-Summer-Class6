def main():
    filename = input("What is the name of the file you want to open? ")

    try:
        in_file = open(filename, 'r')

    except FileNotFoundError as error_obj:
        print("Unable to open the file:", error_obj.filename)
        print("\t Error number:", error_obj.errno)
        print("\t String error:", error_obj.strerror)
        print()
        print("Error object:", error_obj)

    else:  # Runs only if try is successful and nothing is "raised"
        counter = 0
        for line in in_file:
            counter += 1
        in_file.close()
        print("There were", counter, "lines in the file.")

    finally:  # Runs after both the except or the successful run (else)
        print("Goodbye.")


if __name__ == "__main__":
    main()
