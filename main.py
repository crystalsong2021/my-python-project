#
# practice string concatenate (f stand for format)
# Triple code to comment out

calculation_to_hours = 24
name_of_unit = "hours"

days = [20, 30, 25, 50, 110]


def calc_units():
    for i in days:
        print(f"There are {i * 24 * 60} minutes in {i} days")
    print("All Good")


def days_to_units(num_of_days):
    # use conditional statement (if/else)
    return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"


def validate_user_input(user_days):
    # if user_days.isdigit():
    try:
        user_days = int(user_days)
        if user_days > 0:
            result = days_to_units(user_days)
            print(result)
        elif user_days == 0:
            print("You enter a 0. Please enter positive value")
        else:
            print("You enter the negative number. Enter positive value")
    except ValueError:
        print("No a valid digit")


# calc_units()
input_days = ""
while True:
    input_days = input("Enter the numbers of day\n")
    if input_days == "exit":
        break
    else:
        validate_user_input(input_days)

# always encapsulate the logic in the function definition
