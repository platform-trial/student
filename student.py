class Student():
    """Represents a student.

    Provides attributes and methods for representing a student.

    Attributes:
        name: A string with the student's name.
        age: An integer with the students age. This may be None.
    """
    
    def __init__(self, name, age=None):
        """Initializes a new Student.

        Sets initial values for the attributes of a new Student instance.

        Args:
            name: A string with the student's name.
            age: An integer with the student's age. Default value is None.

        Returns:
            None
        """
        
        self.name = name
        self.age = age

    def intro(self):
        """Introduces a Student.

        Provides an introduction for a Student instance. If the student's
        age is set, the intro includes a reference to that.

        Args:
            None

        Returns:
            A string identifying the student by name and (possibly) age.
        """
        
        text = f"I'm {self.name}!"
        if self.age:
            text += f" I'm {self.age}!"
        return text

    def celebrate_birthday(self, phrase):
        """Celebrates a Student's birthday.

        Prints a phrase from the student whose celebrating. If the student's
        age is set, this method increments it by 1.

        Args:
            phrase: The phrase to print.

        Returns:
            None
        """
        print(phrase)
        if self.age:
            self.age += 1
        return
    

chee = Student("Chee",11)
print(chee.name)
chee.celebrate_birthday("Great!")

john = Student("John", 13)
print(f"John's age: {john.age}")

print(john.name)
print(john.age)

print(chee.intro())

suav = Student("Suav")
print(suav.name)
