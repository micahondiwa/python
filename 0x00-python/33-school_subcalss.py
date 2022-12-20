'''
Implements the concept of inheritance; base/supper class and derived/sub-class
The SchoolMember class in this situation is known as the base class or the superclass.
he Teacher and Student classes are called the derived classes or subclasses
'''
class SchoolMember:
    '''Represents any member of school'''

    def __init__(self, name, age):
        self.name = name
        self.age = age

        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''Tell my details.'''

        print('Name: "{}" Age: "{}"'.format(self.name, self.age), end = " " )

class Teacher(SchoolMember):
    '''Represents a teacher'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)

        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    '''Represents a student'''

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mr. Tilex', 28, 3000000)
s = Student('Sibuor', 25, 75)

# prints a blank line
print()

memmbers = [t, s]
for member in memmbers:
    # Works for both Teachers and Students
    member.tell()

