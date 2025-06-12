def format_name(f_name, l_name):
    if f_name == "" and l_name == "":
        return "You have entered invalid values"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
format_condition = True
while format_condition:
    print(format_name(input("What is your first name? "), input("What is your last name? ")))
    ask = input("Do you want to continue? Type 'yes' or 'no'.\n").lower()
    if ask == "yes":
        format_condition = True
        print("lets continue".title())
    else:
        format_condition = False
        print("Thank you for using our service")
