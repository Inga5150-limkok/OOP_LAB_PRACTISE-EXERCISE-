class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def greet_user(self, user):
        # Matches the format: - Greet message to {user.username}:
        print(f"- Greet message to {user.username}:")
        # Matches the format: - Hi {user.username}, It's me, {self.username}
        print(f"- Hi {user.username}, It's me, {self.username}")

    def login(self, user):
        # Checks if email equals amkam@lenosol.com and password equals 1234
        # (Handles both string and integer formats for the password)
        if user.email == "amkam@lenosol.com" and str(user.password) == "1234":
            print(f"Hello {user.username}, you're logged in")
        else:
            print("Access denied.")


# --- Example Verification ---
if __name__ == "__main__":
    # Creating instances to test
    me = User("Bai Inga", "alice@example.com", "password123")
    other_user = User("amkam", "amkam@lenosol.com", 1234)

    # 1. Test greet_user
    me.greet_user(other_user)
    
    print() # Newline for readability

    # 2. Test login (Success case)
    me.login(other_user)

    # 3. Test login (Failure case)
    me.login(me)
