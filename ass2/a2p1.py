def generate_full_name(first_input, last_input):

    return f"{first_input} {last_input}"

def get_alternative_string(full_input):

    return full_input[::2]

user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
user_full_name = generate_full_name(user_first_name, user_last_name)
user_alternative_string = get_alternative_string(user_full_name)

print(f"Alternative string: {user_alternative_string}")