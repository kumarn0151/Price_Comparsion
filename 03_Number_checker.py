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


my_num = num_check("Enter a number", "Enter an integer more than 0", int)
print("you chose", my_num)

my_other_num = num_check("Enter a number", "Enter an float more than 0", float)
print("you chose", my_other_num)
