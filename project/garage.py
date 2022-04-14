import re


max_length = 10
garage = [None] * 11
second_garage = [None] * 11


def push(array, car, top):
    # print(top)
    # if top is provided
    if (top + 1) < max_length:
        top = top + 1
        if array[top] == None:
            array[top] = car
    return top


def pop(garage, top):
    item = None
    if garage[top] != None:
        item = garage[top]
        garage[top] = None
        top = top - 1
        return item, top


def garage_checker(license):
    # print(license)
    checker = False
    j = 0
    while j < len(garage):
        if license == garage[j]:
            checker = True
            return checker
        j += 1


def check_license(license):
    matched = re.match(
        "[A-Z][A-Z][A-Z][A-Z][-][0-9][0-9][-][0-9][0-9][0-9]", license)
    is_match = bool(matched)
    if len(license) != 12:
        is_match = False
    return is_match


def empty(garage):
    for car in garage:
        if not None:
            car = None


def parking(license, top):
    # print(top)
    parking_top = top
    print("\nLicense plate number correct.\n")

    # check if the car is already registered in the garage
    garage_check = garage_checker(license)
    # print(garage)
    # print(garage_check)

    # if the car is already in the car
    if garage_check == True:
        print("Car already in the garage.")
        return parking_top

    # if the car is not in the garage
    else:
        print("Parking...\n")

        # call the push function to add the car to the garage
        top_from_push = push(garage, license, parking_top)
        print("Completed! See you soon.")
        return top_from_push


def retrieving(license, top):
    second_top = -1

    # check if the car is already registered in the garage
    garage_check = garage_checker(license)
    retrieving_top = top

    print("\nLicense plate number correct.\n")

    # if license is in garage
    if garage_check == True:
        print("Retrieving...\n")
        # print(retrieving_top)

        # while car is in the garage
        while license in garage:
            # pop car at the top
            item, pop_top = pop(garage, retrieving_top)
            # print(item)
            # print(pop_top)

            # change top value
            retrieving_top = pop_top
            # print(second_garage)
            # print(second_top)
            # add car at the top to a new array
            top_from_push = push(second_garage, item, second_top)
            second_top = top_from_push
            # print(second_top)
            # print(second_garage)

            # print(retrieving_top)
            # reverse the array
        x, n = pop(second_garage, second_top)
        second_top = n
        for item in second_garage:
            if item is not None:
                item, pop_top = pop(second_garage, second_top)
                second_top = pop_top
                # print(item)
                top_from_push = push(garage, item, retrieving_top)
                retrieving_top = top_from_push
                # print(retrieving_top)

        # clear the new array
        empty(second_garage)
        print("Completed! Good Bye!")
        return retrieving_top
    else:
        print("Car not in garage!")


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
    # variable for stack
    top = -1

    # inifinity loop
    while 1:
        # print initial options
        print("\n")
        print("Welcome to Oreoluwa's Garage!\n")

        # check how many cars are in garage
        stats = garage_stats()

        print("\n(1) Parking")
        print("(2) Retrieving")
        print("(3) Exit\n")

        # take user input
        user_option = str(input("Option: "))

        # if user wants to park
        if user_option == "1":

            # if there is space in the garage
            if stats < 10:
                print("\nStanding By...\n")

                # take in the license as input
                license = str(
                    input("Enter your license plate number: ").strip())

                # check license
                checked_license = check_license(license)

                # call the parking function with the license an top variable as input
                if checked_license is False:
                    while checked_license is False:
                        print("\nLicense Incorrect.\n")
                        license = str(input(
                            "Please re-enter your license plate number in ABCD-12-3456 format: "))
                        checked_license = check_license(license)
                        # print(checked_license)

                if checked_license is True:
                    top_from_parking = parking(license, top)

                    # change top to the new top from parking
                    top = top_from_parking
                    # print(garage)
                    # call the cars function to print out the cars in the garage
                    cars()

            # if the user wants to park but the garage is full
            elif stats == 10:
                print("\nGarage Full. Please come back later.")

        # if the user wants to retrieve a car
        elif user_option == "2":

            # if there are no cars in the garage
            if stats == 0:
                print("Garage empty.")

            # if there is space in the garage
            elif stats <= 10:
                print("\nStanding By...\n")

                # take license as input
                license = str(
                    input("Enter your license plate number: ").strip())

                # check license
                checked_license = check_license(license)

                if checked_license is False:
                    while checked_license is False:
                        print("\nLicense Incorrect.\n")
                        license = str(input(
                            "Please re-enter your license plate number in ABCD-12-3456 format: "))
                        checked_license = check_license(license)
                        # print(checked_license)

                if checked_license is True:
                    # call the retrieving function with license, stats and top as inputs
                    top_from_retrieving = retrieving(license, top)

                    # change top to the new top from parking
                    top = top_from_retrieving
                    # print(garage)

                    # call the cars function to print out the cars in the garage
                    cars()
        # if user wants to quit the program
        elif user_option == "3":
            print("Good bye.\n")
            break

        # if the user does not input the right option
        elif user_option != "1" or user_option != "2" or user_option != "3":
            print("Incorrect option. Try again.")


main()
