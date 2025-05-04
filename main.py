import stuent_db as db
from stuent_db import Student



s1 = Student("Sami", 18, "A")
s1.save()
s2 = Student("Sami", 28, "C")
s2.save()

s1.age = 19
s1.grade = "B+"
s1.update()

Student.search_by_name("Sami")




Student.all()


s1.delete()
s2.delete()
Student.all()