'''
Career Crafter

- Background: you've been asked to build a program that validates the persnal data of a user's application
- Challenge: Allow a user to enter all their personal information for an application and validates the input according to a specific criteria
- Objective: use defensive programming to ensure the user input is valid:
    Use conditional statements for input validation
    Use try-ecept blocks to gracefully manage unexpected exceptions
    Recognize and address various error types

'''

# Validation of user email

user_email = input("Please enter your location: ")
if "@" in user_email and "." in user_email:
    print("The applicant has a valid email address.")
else:
    print("The applicant has an invalid email address.")