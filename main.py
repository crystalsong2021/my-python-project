#
# practice string concatenate (f stand for format)
# Triple code to comment out
"""
calculation_to_hours = 24
name_of_unit = "hours"

days = [20, 30, 25, 50, 110]


def calc_units():
    for i in days:
        print(f"There are {i * 24 * 60} minutes in {i} days")
    print("All Good")


def days_to_units(num_of_days, custom_msg):
    print(f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}")
    print(custom_msg)


# calc_units()
days_to_units(20, "Awesome!")
days_to_units(30, "Looks good!")
"""
real_age = int(input("Type your real age: "))

if real_age >= 18:
    print("You are an adult")
else:
    print("you are not an adult")
