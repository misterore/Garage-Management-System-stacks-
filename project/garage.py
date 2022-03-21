import re


garage = [None] * 11
temp = []
temp2 = []


def push(car):
    j = 0
    while j < len(garage):
        if garage[j] == None:
            garage[j] = car
            break
        j += 1


def pop():
    j = 0
    while j < len(garage):
        if garage[j] == None:
            i = garage[j-1]
            del garage[j-1]
            break
        elif j == 9:
            i = garage[j]
            del garage[j]
            break
        j += 1
    return i


def empty():
    for cars in garage:
        if not None:
            print("Garage not empty")
            break
    else:
        print("Garage empty")
    pass


def top():
    # mark the top of the stack
    j = 0
    while j < len(garage):
        if garage[j] == None:
            top = garage[j-1]
            break
        elif j == 9:
            top = garage[j]
        j += 1
    print(top)
    return top


def garage_checker(license):
    j = 0
    while j < len(garage):
        if license == garage[j]:
            return True
        j += 1


def parking(license):
    matched = re.match(
        "[A-Z][A-Z][A-Z][A-Z][-][0-9][0-9][-][0-9][0-9][0-9]", license)
    is_match = bool(matched)
    if len(license) != 12:
        is_match = False

    if is_match is True:
        garage_check = garage_checker(license)
        print("\nLicense plate number correct.\n")
        if garage_check == True:
            print("Car already in the garage.")
        else:
            print("Parking...\n")
            push(license)
            print("Completed! See you soon.")
    if is_match is False:
        print("\nLicense Incorrect.\n")
        license = str(input(
            "Please re-enter your license plate number in ABCD-12-3456 format: "))
        parking(license)


def retrieving(license, stats):
    matched = re.match(
        "[A-Z][A-Z][A-Z][A-Z][-][0-9][0-9][-][0-9][0-9][0-9]", license)
    is_match = bool(matched)
    if len(license) != 12:
        is_match = False

    if is_match is True:
        print("\nLicense plate number correct.\n")
        if stats == 0:
            print("Garage empty!")
        elif stats <= 10 and license in garage:
            print("Retrieving...\n")
            while license in garage:
                temp1 = pop()
                temp.append(temp1)
            temp.reverse()
            temp.pop(0)
            garage.extend(temp)
            print("Completed! Good Bye!")
        else:
            print("Car not in garage!")
    if is_match is False:
        print("\nLicense Incorrect.\n")
        license = str(input(
            "Please re-enter your license plate number in ABCD-12-3456 format: "))
        retrieving(license, stats)


def garage_stats():
    stats = 0
    i = 0
    while i < len(garage):
        if garage[i] != None:
            stats += 1
        i += 1
    print("Cars parked:", stats)
    return stats


def cars():
    i = 0
    cars_list = ''
    print("\nCars in garage:")
    while i < len(garage):
        if garage[i] != None:
            cars_list += garage[i] + ('\n')
        i += 1
    print(cars_list)


def main():

    while 1:
        print("\n")
        print("Welcome to Oreoluwa's Garage!\n")
        stats = garage_stats()
        print("\n(1) Parking")
        print("(2) Retrieving")
        print("(3) Exit\n")
        user_option = str(input("Option: "))

        if stats < 10 and user_option == "1":
            print("\nStanding By...\n")
            license = str(
                input("Enter your license plate number: ").strip())
            parking(license)
            cars()
        elif stats == 10 and user_option == "1":
            print("\nGarage Full. Please come back later.")
        elif user_option == "2":
            if stats == 0:
                print("No car in garage...")
            elif stats <= 10:
                print("\nStanding By...\n")
                license = str(
                    input("Enter your license plate number: ").strip())
                retrieving(license, stats)
                cars()
        elif user_option == "3":
            print("Good bye.\n")
            break
        elif user_option != "1" or user_option != "2" or user_option != "3":
            print("Incorrect option. Try again.")


main()
