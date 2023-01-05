
def days_to_units(num_of_days, conversion_unit):
    # use conditional statement (if/else)
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"


def validate_user_input(days_and_unit_dictionary):
    # if user_days.isdigit():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculate_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculate_value)
        elif user_input_number == 0:
            print("You enter a 0. Please enter positive value")
        else:
            print("You enter the negative number. Enter positive value")
    except ValueError:
        print("No a valid digit. Try it again")

