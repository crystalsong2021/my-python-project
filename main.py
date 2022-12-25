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
    print(f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}")
    print(custom_msg)


# calc_units()
input_days = int(input("Enter the numbers of day\n"))
input_msg = input("Please enter your message\n")

days_to_units(input_days, input_msg)
# days_to_units(30, "Looks good!")

