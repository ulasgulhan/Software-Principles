class Bird:
    def fly(self):
        pass

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostrich can't fly!")

class Sparrow(Bird):
    def fly(self):
        # Sparrow's flying implementation
        pass