def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"

name = format_name(input("What is your first name?"), input("What is your last name?"))
print(name)