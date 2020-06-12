'''
You are given two classes, Person and Student, where Person is the base class and Student is 
the derived class. Completed code for Person and a declaration for Student are provided for 
you in the editor. Observe that Student inherits all the properties of Person.

Link: https://www.hackerrank.com/challenges/30-inheritance/problem
'''

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    def calculate(self):
        avarage = sum(scores)/len(scores)

        if (90 <= avarage) and (avarage <= 100):
            return 'O'
        elif (80 <= avarage) and (avarage < 90):
            return 'E'
        elif (70 <= avarage) and (avarage < 80):
            return 'A'
        elif (55 <= avarage) and (avarage < 70):
            return 'P'
        elif (40 <= avarage) and (avarage < 55):
            return 'D'
        else:
            return 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())