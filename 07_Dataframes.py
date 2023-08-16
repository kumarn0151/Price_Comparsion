import pandas


# Calculate the cost per kilogram based on weight and cost
def calc_cost_per_kg(var_weight, var_cost):
    cost_per_kg = (var_cost / var_weight) * 1000
    return round(cost_per_kg, 2)

    # Calculate the cost per kilogram for this item and append to the list
    cost_per_kg = calc_cost_per_kg(weight, item_cost)
    cost_per_kg_list.append(cost_per_kg)

    item_list.append(item_name)
    weight_list.append(weight)
    cost_list.append(item_cost)


# Lists to hold item details
item_list = []
weight_list = []
cost_list = []
cost_per_kg_list = []

variable_dict = {
    "item"
    "weight"
    "cost"
}

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

# Finds the cheapest item per kilogram
cheapest_item = DataFrame.loc[DataFrame["Cost per kg"].idxmin()]
print("\n====== Cheapest item  ======")
print("\nCheapest item per kilogram:")
print(cheapest_item)
