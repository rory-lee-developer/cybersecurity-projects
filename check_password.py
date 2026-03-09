#------------------------------
#Password Checker Application
#------------------------------

#------------------------------
#Variable initialisation
#------------------------------

special_characters = ["!", "@", "#", "$", "%", "^", "&", "(", ")", "-", "_", "+", "="]
password_viability = 0

#------------------------------
#Subprograms
#------------------------------
def is_upper_and_lower(password):
    return any(char.isupper() for char in password) and any(char.islower() for char in password)

def is_number(password):
    return any(char.isdigit() for char in password)

def is_special_character(password):
    return any(char in special_characters for char in password)

def is_length(password):
    return len(password) >= 8

def determine_strength(password_viability):
    if password_viability <= 2:
        return "poor"
    elif password_viability <= 3:
        return "fair"
    elif password_viability == 4:
        return "strong - don't forget to change it regularly!"
#------------------------------
#Main Program
#------------------------------
print("Welcome to the password authenticator program.")
user_password = input("Please enter your password: ")

if is_upper_and_lower(user_password):
    password_viability += 1
if is_number(user_password):
    password_viability += 1
if is_special_character(user_password):
    password_viability += 1
if is_length(user_password):
    password_viability += 1
    
if not all([is_upper_and_lower(user_password), is_number(user_password), 
            is_special_character(user_password), is_length(user_password)]):
    print("\n-----------------------------------------------------------------")

if not is_upper_and_lower(user_password):
    print("\nYour password must include both upper and lowercase characters.")
if not is_number(user_password):
    print("\nYour password must include at least one digit.")
if not is_special_character(user_password):
    print("\nYour password must include at least one special character.")
if not is_length(user_password):
    print("\nYour password must be at least 8 characters (12+ recommended).")
    
    
print(f"\nYour password score is: {password_viability}/4")
print(f"Your password strength score is: {determine_strength(password_viability)}")
