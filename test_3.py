import unittest
from unittest.mock import patch
import excel_data

class TestExcelData(unittest.TestCase):
    @patch('excel_data.load_excel_data')
    def test_get_students(self, mock_load_excel_data):
        # Подставляем замещающие данные
        mock_load_excel_data.return_value = {
            "Успеваемость студентов": [{
                "ФИО студента": "John Doe",
                "student_id": "12345",
                "grades": "A"
            }]
        }

        students = excel_data.get_students()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]['ФИО студента'], "John Doe")

    @patch('excel_data.save_data')
    def test_save_data(self, mock_save_data):
        students = [{"ФИО студента": "Jane Smith", "student_id": "67890", "grades": "B"}]
        excel_data.save_data(students=students)
        mock_save_data.assert_called_once_with(students=students)

if __name__ == '__main__':
    unittest.main()