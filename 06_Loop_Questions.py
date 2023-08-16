import pandas


# checks user response is not blank
def not_blank(question):
    while True:
        response = input(question)
        if response != "":
            return response
        else:
            print("This can't be blank, please enter a response")
            print()


# checks users enter an integer
def num_check(question):
    while True:
        try:
            response = float(input(question))
            return response
        except ValueError:
            print("Please enter an integer.")


def get_budget():
    while True:
        budget_input = input("Enter your budget: ")
        try:
            budget = float(budget_input)
            if budget < 2.99:
                print("Invalid budget. Please enter an amount that's above $2.")
            else:
                return budget
        except ValueError:
            print("Invalid input")


def calc_cost_per_kg(var_weight, var_cost):
    cost_per_kg = (var_cost / var_weight) * 1000
    return round(cost_per_kg, 2)


yes_no_list = ["yes", "no"]
item_list = []
weight_list = []
cost_list = []
cost_per_kg_list = []

budget_value = get_budget()

# loop to enter items
while True:
    item_name = not_blank("Enter the item name or 'xxx' to quit: ")

    if item_name == 'xxx' and len(item_list) > 0:
        break
    elif item_name == 'xxx':
        print("You must enter at least one item before exiting")
        continue

    item_cost = num_check("Cost: $")
    if item_cost > budget_value:
        print("The cost is over the budget of ${:.2f}.".format(budget_value))
        print()
        continue

    weight = num_check("Weight (in grams): ")

    # check user entered weight is a positive number
    if weight > 0:
        pass
    else:
        print("Weight must be above 0")
        continue

    print("Item: {}".format(item_name))
    print("Weight: {} grams".format(weight))
    print("Cost: ${:.2f}".format(item_cost))

    # Calculate the cost per kilogram for this item and append to the list
    cost_per_kg = calc_cost_per_kg(weight, item_cost)
    cost_per_kg_list.append(cost_per_kg)

    item_list.append(item_name)
    weight_list.append(weight)
    cost_list.append(item_cost)
print()
print("Selected items: ", item_list)

# Create a pandas DataFrame with the item list
data = {
    "Item Name": item_list,
    "Weight (grams)": weight_list,
    "Cost": cost_list,
    "Cost per kg": cost_per_kg_list
}
DataFrame = pandas.DataFrame(data)

# Print the DataFrame with price per kilogram
print()
print("---- Cost per kg ----")
print("\nCost per kilogram:")
print(DataFrame)
