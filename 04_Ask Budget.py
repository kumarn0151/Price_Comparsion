while True:
    budget = input("Enter your budget: ")
    try:
        budget = float(budget)
        if budget < 2.01:
            print("Invalid budget. Please enter a amount that's above $2 .")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Your budget is: ${:.2f}".format(budget))
