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


def days_to_units(num_of_days, custom_msg):
    # use conditional statement (if/else)
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"
    elif num_of_days == 0:
        return "you are entering zero. no conversion"
    else:
        return "Please enter positive value"


# calc_units()
input_days = input("Enter the numbers of day\n")

if input_days.isdigit():
    input_days = int(input_days)
    result = days_to_units(input_days)
    print(result)
else:
    print("No a digit")

# days_to_units(30, "Looks good!")
