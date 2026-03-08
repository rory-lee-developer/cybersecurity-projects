#------------------------------
#Password Checker Application
#------------------------------

"""
TODO: 8 character threshold
"""

#------------------------------
#Variables
#------------------------------
user_password_score = 0


#------------------------------
#Subprograms
#------------------------------
def above_character_threshold(password):
  pass
def has_lowercase_and_uppercase(password):
  pass
def has_digits(password):
  pass
def has_special_characters(password):
  pass


#------------------------------
#Main Program
#------------------------------
print("Welcome to my password checker program!")
user_password = input("Please enter the password that you would like to check: ")

if above_character_threshold(user_password) == True:
  user_password_score += 1
  threshold_check = True
if has_lowercase_and_uppercase(user_password) == True:
  user_password_score += 1
  lowercase_uppercase_check = True
if has_digits(user_password) == True:
  user_password_score += 1
  digits_check = True
if has_special_characters(user_password) == True:
  user_password_score += 1
  special_characters_check = True
