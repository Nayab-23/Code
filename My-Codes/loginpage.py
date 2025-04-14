def validate_user_id(user_id):
    # Check if user_id ends with @ and a valid domain
    if "@" in user_id and (user_id.endswith(".com") or user_id.endswith(".org")
                           or user_id.endswith(".net")):
        return True
    else:
        return False


def validate_password(password):
    # Check if password is at least 8 characters long
    if len(password) < 8:
        return "Password has not been accepted!!! It's a weak password."

    # Initialize variables to check for password strength
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    # Check each character in the password
    for char in password:
        if 'A' <= char <= 'Z':
            has_upper = True
        elif 'a' <= char <= 'z':
            has_lower = True
        elif '0' <= char <= '9':
            has_digit = True
        else:
            has_symbol = True

    # Determine the strength of the password
    if has_upper and has_lower and has_digit and has_symbol:
        return "Password has been accepted!!! It's a strong password."
    elif (has_upper or has_lower) and has_digit and has_symbol:
        return "Password has been accepted!!! It's a medium password."
    else:
        return "Password has not been accepted!!! It's a weak password."


# Example usage:
user_id = input("Enter User ID: ")
password = input("Enter Password: ")

if validate_user_id(user_id):
    print("User ID is valid.")
    print(validate_password(password))
else:
    print("User ID is invalid.")
