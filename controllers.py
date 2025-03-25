import excel_data

class StudentController:
    @staticmethod
    def get_students():
        return excel_data.get_students()

    @staticmethod
    def add_student(full_name, student_id, grades):
        excel_data.add_student(full_name, student_id, grades)


    @staticmethod
    def save_students(students):
        excel_data.save_data(students)


class ProfessorController:
    @staticmethod
    def get_professors():
        return excel_data.get_professors()

    @staticmethod
    def add_professor(full_name, experience, subjects):
        excel_data.add_professor(full_name, experience, subjects)

    @staticmethod
    def save_professors(professors):
        # Передаем данные только преподавателей для сохранения в лист "Информация о сотрудниках"
        excel_data.save_data(professors=professors)


class SecretaryController:
    @staticmethod
    def authenticate(username, password):
        # Фиксированные данные для авторизации
        return username == "abc" and password == "cba"
