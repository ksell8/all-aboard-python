from enum import Enum


class SimpleDude():
    """Simple, dude."""
    def __init__(self, name: str):
        self.quien = name

    def say_hello(self):
        print(f"Hello, {self.quien}")

class Gender(str, Enum):
    female = "female"
    male = "male"
    something_different = "something different"

    def call_them_what_it_is(self):
        if self == self.female:
            return "cabrona"
        return "cabrón"


class SpanishDude(SimpleDude):
    """Spanish, dude."""
    def __init__(self, name: str, genero: Gender):
        super().__init__(name)
        self.genero = genero

    def say_hello(self):
        print(f"Hola, {self.quien}")

    def say_hello_to_fucker(self):
        print(f"Hola, {self.genero.call_them_what_it_is()}")

if __name__ == "__main__":
    print("__main__")
    SimpleDude("Christian").say_hello()
    kurt = SpanishDude("Kurt", Gender.something_different)
    kurt.say_hello()
    kurt.say_hello_to_fucker()
    print("end __main__")
