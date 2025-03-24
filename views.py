import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from controllers import SecretaryController, StudentController, ProfessorController

class LoginView:
    """Класс представления окна входа"""
    def __init__(self, root):
        self.root = root
        self.root.title("Вход в систему")

        # Метка и поле ввода имени пользователя
        self.username_label = tk.Label(root, text="Имя пользователя:")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        # Метка и поле ввода пароля
        self.password_label = tk.Label(root, text="Пароль:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=5)

        # Кнопка входа
        self.login_button = tk.Button(root, text="Войти", command=self.login)
        self.login_button.pack(pady=10)

    def login(self):
        """Метод обработки входа пользователя"""
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Проверка учетных данных через контроллер секретаря
        if SecretaryController.authenticate(username, password):
            messagebox.showinfo("Вход выполнен", "Добро пожаловать!")
            self.root.destroy() # Закрываем окно входа
            show_main_view() # Открываем главное меню
        else:
            messagebox.showerror("Ошибка", "Неверные учетные данные!")

class MainView:
    """Класс представления главного меню"""
    def __init__(self, root):
        self.root = root
        self.root.title("Главное меню")

        # Кнопка перехода к списку студентов
        self.student_button = tk.Button(root, text="Студенты", command=self.show_students)
        self.student_button.pack(pady=10)

        # Кнопка перехода к списку преподавателей
        self.professor_button = tk.Button(root, text="Преподаватели", command=self.show_professors)
        self.professor_button.pack(pady=10)

    def show_students(self):
        """Открывает окно со списком студентов"""
        StudentListView(self.root)

    def show_professors(self):
        """Открывает окно со списком преподавателей"""
        ProfessorListView(self.root)


class StudentListView:
    """Класс представления списка студентов"""
    def __init__(self, root):
        self.window = tk.Toplevel(root)  # Открытие нового окна
        self.window.title("Список студентов")
        self.window.geometry("800x400")

        # Таблица с данными студентов
        self.tree = ttk.Treeview(self.window)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Обработчики событий
        self.tree.bind("<Button-1>", self.clear_selection)  # Снятие выделения
        self.tree.bind("<Double-1>", self.edit_student)  # Редактирование при двойном клике

        # Кнопка добавления студента
        tk.Button(self.window, text="Добавить студента", command=self.add_student).pack(pady=10)

        self.load_students()  # Загрузка данных

    def clear_selection(self, event):
        """Убирает выделение строки при клике вне элемента"""
        if not self.tree.identify_row(event.y):
            self.tree.selection_remove(self.tree.selection())

    def load_students(self):
        """Загружает и отображает данные студентов"""
        self.students = StudentController.get_students()
        if not self.students:
            messagebox.showinfo("Информация", "Нет данных для отображения.")
            return

        # Настройка столбцов
        self.tree["columns"] = list(self.students[0].keys())
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Очистка и заполнение таблицы
        self.tree.delete(*self.tree.get_children())
        for student in self.students:
            self.tree.insert("", tk.END, values=tuple(student.values()))

    def edit_student(self, event):
        """Редактирование данных студента"""
        selected_item = self.tree.selection()
        if not selected_item:
            return

        selected_item = selected_item[0]
        student = self.students[self.tree.index(selected_item)]
        updated_student = {}

        # Запрос новых значений
        for key, value in student.items():
            new_value = simpledialog.askstring(f"Редактировать {key}", f"{key}:", initialvalue=value)
            if new_value is None:
                return
            updated_student[key] = new_value

        # Сохранение обновленных данных
        self.students[self.tree.index(selected_item)] = updated_student
        StudentController.save_students(self.students)
        self.load_students()

    def add_student(self):
        """Добавление нового студента"""
        new_student = {}
        keys = self.students[0].keys() if self.students else ["ФИО студента"]

        for key in keys:
            value = simpledialog.askstring("Добавить студента", f"{key}:")
            if value is None:
                return
            new_student[key] = value

        self.students.append(new_student)
        StudentController.save_students(self.students)
        self.load_students()

class ProfessorListView:
    """Класс представления списка преподавателей"""
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Список преподавателей")
        self.window.geometry("800x400")

        # Таблица с данными преподавателей
        self.tree = ttk.Treeview(self.window)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Обработчики событий
        self.tree.bind("<Button-1>", self.clear_selection)  # Снятие выделения
        self.tree.bind("<Double-1>", self.edit_professor)  # Редактирование при двойном клике

        # Кнопка добавления преподавателя
        tk.Button(self.window, text="Добавить преподавателя", command=self.add_professor).pack(pady=10)

        self.load_professors()  # Загрузка данных

    def clear_selection(self, event):
        """Убирает выделение строки при клике вне элемента"""
        if not self.tree.identify_row(event.y):
            self.tree.selection_remove(self.tree.selection())

    def load_professors(self):
        """Загружает и отображает данные преподавателей"""
        self.professors = ProfessorController.get_professors()
        if not self.professors:
            messagebox.showinfo("Информация", "Нет данных для отображения.")
            return

        # Настройка столбцов
        self.tree["columns"] = list(self.professors[0].keys())
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Очистка и заполнение таблицы
        self.tree.delete(*self.tree.get_children())
        for professor in self.professors:
            self.tree.insert("", tk.END, values=tuple(professor.values()))

    def edit_professor(self, event):
        """Редактирование данных преподавателя"""
        selected_item = self.tree.selection()
        if not selected_item:
            return

        selected_item = selected_item[0]
        professor = self.professors[self.tree.index(selected_item)]
        updated_professor = {}

        for key, value in professor.items():
            new_value = simpledialog.askstring(f"Редактировать {key}", f"{key}:", initialvalue=value)
            if new_value is None:
                return
            updated_professor[key] = new_value

        self.professors[self.tree.index(selected_item)] = updated_professor
        ProfessorController.save_professors(self.professors)
        self.load_professors()

    def add_professor(self):
        """Добавление нового преподавателя"""
        new_professor = {}
        keys = self.professors[0].keys() if self.professors else ["ФИО преподавателя"]

        for key in keys:
            value = simpledialog.askstring("Добавить преподавателя", f"{key}:")
            if value is None:
                return
            new_professor[key] = value

        self.professors.append(new_professor)
        ProfessorController.save_professors(self.professors)
        self.load_professors()

def show_main_view():
    """Запуск главного окна"""
    root = tk.Tk()
    MainView(root)
    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    LoginView(root)
    root.mainloop()