import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

def init_db():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade TEXT NOT NULL
        )
        """
    )
    conn.commit()

init_db()

class Student:
    def __init__(self, name, age, grade, id=None):
        self.validate(name, age, grade)
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade

    def validate(self, name, age, grade):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Invalid age")
        if grade.upper() not in ["A", "A-", "B+", "B", "B-", "C+", "C", "C-"]:
            raise ValueError("Grade must be one of: A, A-, B+, B, B-, C+, C, C-")

    def save(self):
        cursor.execute(
            "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
            (self.name, self.age, self.grade)
        )
        conn.commit()
        self.id = cursor.lastrowid
        print("Student added")

    def update(self):
        if self.id is None:
            raise ValueError("Student must be saved before updating.")
        cursor.execute(
            "UPDATE students SET name = ?, age = ?, grade = ? WHERE id = ?",
            (self.name, self.age, self.grade, self.id)
        )
        conn.commit()
        print("Student updated")

    def delete(self):
        if self.id is None:
            raise ValueError("Student must be saved before deleting.")
        cursor.execute("DELETE FROM students WHERE id = ?", (self.id,))
        conn.commit()
        print("Student deleted")

    @staticmethod
    def search_by_name(name):
        cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
        rows = cursor.fetchall()
        students = [Student(id=row[0], name=row[1], age=row[2], grade=row[3]) for row in rows]
        
        print(f"Students named {name}:")
        for student in students:
            print(student) 

        return students 


    @staticmethod
    def all():
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()

        students = [Student(id=row[0], name=row[1], age=row[2], grade=row[3]) for row in rows]
        print("All Students in DB:")
        for student in students:
            print(student)  

        return students  

    def __repr__(self):
        return f"Student(id={self.id}, name='{self.name}', age={self.age}, grade='{self.grade}')"
