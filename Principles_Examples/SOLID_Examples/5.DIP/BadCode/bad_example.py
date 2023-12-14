class UserManager:
    def __init__(self):
        self.logger = ConsoleLogger()

    def add_user(self, username):
        # User addition operation
        self.logger.log(f"User added: {username}")

class ConsoleLogger:
    def log(self, message):
        print(f"Console Log: {message}")

# Usage example
user_manager = UserManager()
user_manager.add_user("John Doe")