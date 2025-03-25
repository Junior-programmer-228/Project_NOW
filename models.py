class Student:
    def __init__(self, id, full_name, student_id, grades):
        self.id = id
        self.full_name = full_name
        self.student_id = student_id
        self.grades = grades

    def __str__(self):
        return f"Student(id={self.id}, full_name='{self.full_name}', student_id='{self.student_id}', grades='{self.grades}')"


class Professor:
    def __init__(self, id, full_name, experience, subjects):
        self.id = id
        self.full_name = full_name
        self.experience = experience
        self.subjects = subjects

    def __str__(self):
        return f"Professor(id={self.id}, full_name='{self.full_name}', experience={self.experience}, subjects='{self.subjects}')"


class Secretary:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return f"Secretary(id={self.id}, username='{self.username}', password='*****')"
