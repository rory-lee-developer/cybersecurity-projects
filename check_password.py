#------------------------------
#Password Checker Application
#------------------------------


#------------------------------
#Variables
#------------------------------


#------------------------------
#Subprograms
#------------------------------
def is_upper_and_lower(password):
  if (any(char.isupper() for char in password)):
    return True


#------------------------------
#Main Program
#------------------------------
print("Welcome to the password authenticator program.")
user_password = input("Please enter your password: ")

