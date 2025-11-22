def get_valid_number(prompt, min_val, max_val, is_float=False):
    """Repeatedly asks user for input until valid number is received."""
    while True:
        try:
            user_input = input(prompt)
            if is_float:
                value = float(user_input)
            else:
                value = int(user_input)
            
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Error: Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

def get_non_empty_string(prompt):
    """Ensures user doesn't leave a field blank."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: This field cannot be empty.")