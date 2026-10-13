# CLASS EXERCISE - 1

# Define a User class with the following data, username, email, password
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    # Create two class methods, greet_user and login.
    # Note: In standard Python, these act as instance methods because they 
    # require access to individual user data.
    
    # The greet_user method greets the user as in the example format
    def greet_user(self, other_user):
        print(f"Greet message to {other_user.username}:")
        print(f"Hi {other_user.username}, It's me, {self.username}")

    # The login method should take a user object, and checks if
    # their email equals amkam@lenosol.com and password equals 1234
    def login(self, user_to_check):
        if user_to_check.email == "amkam@lenosol.com" and user_to_check.password == "1234":
            # If the email and password is correct, print to the screen
            print(f"Hello {user_to_check.username}, you're logged in")
        else:
            # Else if any is wrong, print "Access denied."
            print("Access denied.")


# --- Example Usage ---

# Creating two user instances
user1 = User("Alice", "amkam@lenosol.com", "1234")
user2 = User("Bai Inga", "bob@example.com", "password567")

# Testing the greet_user method (Alice greets Bob)
user1.greet_user(user2)

print("\n--- Testing Login ---")
# Testing login with correct credentials (user1)
user1.login(user1)

# Testing login with incorrect credentials (user2)
user1.login(user2)
