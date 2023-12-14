from abc import ABC, abstractmethod

# Abstract class (abstraction)
class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

# Low-level module (concrete implementation)
class ConsoleLogger(Logger):
    def log(self, message):
        print(f"Console Log: {message}")

# High-level module
class UserManager:
    def __init__(self, logger: Logger):
        self.logger = logger

    def add_user(self, username):
        # User addition operation
        self.logger.log(f"User added: {username}")

# Usage example
console_logger = ConsoleLogger()
user_manager = UserManager(console_logger)
user_manager.add_user("John Doe")