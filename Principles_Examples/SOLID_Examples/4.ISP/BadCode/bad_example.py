from abc import ABC, abstractmethod

# Poorly designed interface containing both methods
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def rest(self):
        pass

# Class using only the 'work' method
class WorkOnly(Worker):
    def work(self):
        # Implementation
        pass

    def rest(self):
        # This method is unnecessary here
        pass