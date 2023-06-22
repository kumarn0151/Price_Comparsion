# checks for yes / no response
def yes_no(question):
    valid = False

    while not valid:

        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please answer yes/ no ")


# Show instructions
def instructions():
    print()
    print()
    print("Type in your budget and the item name,weight(grams) and cost and I will recommend the best item within "
          "your budget")

    return ""

