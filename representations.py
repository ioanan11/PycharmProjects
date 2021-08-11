class Cat:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"A {self.age} year old cat"

    def __format__(self, format_spec):
        if format_spec == "dog":
            return f"A {self.age * 7} dog years old cat"
        elif format_spec == "cat":
            return f"A {self.age * 5} cat years old cat"
        else:
            return self.__str__()

    whiskers = Cat(6)

    print(f"whiskers is {whiskers}")
    print(f"Whiskers is {whiskers:dog}")
    print(f"Whiskers is {whiskers: cat}")