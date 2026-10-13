# CLASS EXERCISE - 1

class User:
    # 1. Constructor initializing the specific fields
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    # 2. Greet user method based on internal instance data
    def greet_user(self, other_user):
        print(f"Greet message to {other_user.username}:")
        print(f"Hi {other_user.username}, It's me, {self.username}")

    # 3. Login method checking against the hardcoded credentials automatically
    def login(self):
        # Automatically checks the object's own variables against the requirement
        if self.email == "amkam@lenosol.com" and str(self.password) == "1234":
            print(f"Hello {self.username}, you're logged in")
        else:
            print("Access denied.")


# --- AUTOMATIC EXECUTION (No User Input Required) ---

# Declaring the users directly in the program script
user_success = User("Amkam", "amkam@lenosol.com", "1234")
user_failure = User("John", "john@example.com", "password123")

print("--- Testing Greeting System ---")
user_success.greet_user(user_failure)

print("\n--- Testing Automatic Login (Valid Account details) ---")
# This will automatically read the declared attributes and grant access
user_success.login()

print("\n--- Testing Automatic Login (Invalid Account details) ---")
# This will automatically read the declared attributes and deny access
user_failure.login()
