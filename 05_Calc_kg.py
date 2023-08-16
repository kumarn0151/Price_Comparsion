def calc_cost_per_kg(var_weight, var_cost):
    cost_per_kg = (var_cost / var_weight) * 1000
    return round(cost_per_kg, 2)

while True:
    weight = float(input("Weight? "))
    cost = float(input("Price? "))
    unit_cost = calc_cost_per_kg(weight, cost)

    print(unit_cost)