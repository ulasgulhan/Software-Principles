from abc import ABC, abstractmethod

# Interface definition for workable entities
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

# Interface definition for entities that can rest
class Restable(ABC):
    @abstractmethod
    def rest(self):
        pass

# Class using only the 'work' method
class WorkOnly(Workable):
    def work(self):
        # Implementation
        pass

# Class using both 'work' and 'rest' methods
class WorkAndRest(Workable, Restable):
    def work(self):
        # Work implementation
        pass

    def rest(self):
        # Rest implementation
        pass