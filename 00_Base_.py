import pandas


# Functions go here

# checks that input is either a float or an integer

def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


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
    print("Type in your budget and the item name,weight(grams) and cost and I will recommend the best item within "
          "your budget")

    return ""


# ****** Main  Routine Starts here *******

title = "***Welcome to the price comparison***"
print(title)
print()

used_before = yes_no("Have you used this programme before? ")

if used_before == "no":
    instructions()

print()

while True:
    budget = input("Enter your budget: ")
    try:
        budget = float(budget)
        if budget < 2:
            print("Invalid budget. Please enter a positive number that's above 2 .")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Your budget is: ${:.2f}".format(budget))
