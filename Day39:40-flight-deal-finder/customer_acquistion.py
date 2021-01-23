from data_manager import DataManager

data_manager = DataManager()

print("Welcome to Lui's Flight Club.\nWe're dedicated to finding the best flight deals for you and will notify you "
      "through email.")
continue_verification = True
first_name = input("What is your first name?\n").capitalize()
last_name = input("What is your last name?\n").capitalize()
user_email = input("What is your email?\n")
while continue_verification:
    email_confirmation = input("Type your email again, please.\n")
    if email_confirmation == user_email:
        print("Alright! You're in the club.")
        data_manager.add_new_user(
            first_name,
            last_name,
            user_email)
        continue_verification = False
    else:
        print("Emails don't match.")
        continue
