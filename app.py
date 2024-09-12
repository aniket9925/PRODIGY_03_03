import re

def check_password_strength(password):
    # Criteria for password strength
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_numbers = bool(re.search(r'[0-9]', password))
    has_special_chars = bool(re.search(r'[!@#\$%\^\&*\)\(+=._-]', password))
    is_long_enough = len(password) >= 8

    # Assess strength
    strength = 0

    if is_long_enough:
        strength += 1
    if has_uppercase:
        strength += 1
    if has_lowercase:
        strength += 1
    if has_numbers:
        strength += 1
    if has_special_chars:
        strength += 1

    # Provide feedback based on strength
    if strength <= 2:
        feedback = 'Weak'
    elif 3 <= strength <= 4:
        feedback = 'Medium'
    else:
        feedback = 'Strong'

    return feedback


# Main function to prompt the user and display password strength
if __name__ == "__main__":
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")
