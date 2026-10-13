# CLASS EXERCISE - 1

class User:
    # 1. Constructor initializing the declared fields
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    # 2. Method to verify prompt inputs against the declared attributes
    def check_credentials(self, input_email, input_password):
        # Checks if the user's typed input matches the declared email and password
        if input_email == self.email and str(input_password) == str(self.password):
            print(f"\nHello {self.username}, you're logged in successfully!")
        else:
            print("\nAccess denied. Username or password does not match.")


# --- PROGRAM EXECUTION ---

# 1. Pre-declaring the correct user data directly in the script
# (This acts as "database" record)
registered_user_1 = User("amkam", "amkam@lenosol.com", "1234")
registered_user_2 = User("inga", "inga@5150.sl", "1234")


print("=== LOGIN SYSTEM ===")

# 2. Prompts requesting the user to type their credentials
typed_email = input("Enter your Email: ")
typed_password = input("Enter your password: ")


# 3. Automatically matches the input against the declared data
for registered_user in (registered_user_1, registered_user_2):
    if (typed_email == registered_user.email
            and typed_password == str(registered_user.password)):
        registered_user.check_credentials(typed_email, typed_password)
        break
else:
    print("\nAccess denied. Username or password does not match.")
