def format_name(f_name, l_name):
    """This is function to take a first and last name and
    return the name combined in title case"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)



