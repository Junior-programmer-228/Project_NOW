import unittest
from controllers import StudentController, ProfessorController
from unittest.mock import patch

class TestStudentController(unittest.TestCase):
    @patch('excel_data.get_students')
    def test_get_students(self, mock_get_students):
        # Задаём тестовые данные
        mock_get_students.return_value = [{'full_name': 'John Doe', 'student_id': '12345', 'grades': 'A'}]

        students = StudentController.get_students()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]['full_name'], 'John Doe')
        self.assertEqual(students[0]['student_id'], '12345')

    @patch('excel_data.save_data')
    def test_save_students(self, mock_save_data):
        # Пример того, как тестировать сохранение
        test_students = [{'full_name': 'Jane Smith', 'student_id': '67890', 'grades': 'B'}]

        StudentController.save_students(test_students)
        mock_save_data.assert_called_once_with(test_students)


class TestProfessorController(unittest.TestCase):
    @patch('excel_data.get_professors')
    def test_get_professors(self, mock_get_professors):
        # Задаём тестовые данные
        mock_get_professors.return_value = [{'full_name': 'Dr. Smith', 'experience': 10, 'subjects': 'Math'}]

        professors = ProfessorController.get_professors()
        self.assertEqual(len(professors), 1)
        self.assertEqual(professors[0]['full_name'], 'Dr. Smith')
        self.assertEqual(professors[0]['experience'], 10)

    @patch('excel_data.save_data')
    def test_save_professors(self, mock_save_data):
        # Пример того, как тестировать сохранение
        test_professors = [{'full_name': 'Dr. Brown', 'experience': 5, 'subjects': 'Physics'}]

        ProfessorController.save_professors(test_professors)
        mock_save_data.assert_called_once_with(professors=test_professors)


if __name__ == '__main__':
    unittest.main()