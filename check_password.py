#------------------------------
#Password Checker Application
#------------------------------
"""

TODO: Add feedback, Add strength level, remove unnecessary brackets, show precise python confidence:(

def is_length(password):
        return len(password) >= 8

)

"""

#------------------------------
#Variable initialisation
#------------------------------
special_characters = ["!", "@", "#", "$", "%", "^", "&", "(", ")", "-", "_", "+", "="]
password_viability = 0
#------------------------------
#Subprograms
#------------------------------
def is_upper_and_lower(password):
  if (any(char.isupper() for char in password) and any(char.islower() for char in password)):
    return (True)

def is_number(password):
  if (any(char.isdigit() for char in password)):
    return (True)

def is_special_character(password):
  if (any(char in special_characters for char in password)):
    return (True)

def is_length(password):
  if (len(password) >= 8):
    return (True)


#------------------------------
#Main Program
#------------------------------
print("Welcome to the password authenticator program.")
user_password = input("Please enter your password: ")

if (is_upper_and_lower(user_password)):
  password_viability += 1
if (is_number(user_password)):
  password_viability += 1
if (is_special_character(user_password)):
  password_viability += 1
if (is_length(user_password)):
  password_viability += 1

print(f"your password score is: {password_viability}")
