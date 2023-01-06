#
# practice string concatenate (f stand for format)
# Triple code to comment out


# days = [20, 30, 25, 50, 110]
#
#
# def calc_units():
#     for i in days:
#         print(f"There are {i * 24 * 60} minutes in {i} days")
#     print("All Good")


from days_to_units import helper

# Another way to reference the function is:
# <<from helper import validate_and_execute>> to import only one function
# or <<from helper import *>> to import everything

# calc_units()
input_days = ""
while True:
    input_days = input("Enter the numbers of days and unit conversion.\n example: 20: hour \n")
    if input_days == "exit":
        break
    else:
        input_day = input_days.split(":")[0]
        unit = input_days.split(":")[1]
        days_and_unit_dictionary = {"days": input_day, "unit": unit}
        helper.validate_user_input(days_and_unit_dictionary)

# always encapsulate the logic in the function definition
