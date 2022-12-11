import tkinter as tk
from tkinter import ttk
import psycopg2
from tkinter import *
import db
from datetime import datetime
import hashlib
from config import host, user, password, db_name

connection = psycopg2.connect(host=host, user=user, password=password, database=db_name)
cursor = connection.cursor()
connection.autocommit = True


class Registration:
    def __init__(self):
        super().__init__()
        self.signup = None
        self.firstname_signup_label = None
        self.firstname_signup_entry = None
        self.lastname_signup_label = None
        self.lastname_signup_entry = None
        self.phone_signup_label = None
        self.phone_signup_entry = None
        self.email_signup_label = None
        self.email_signup_entry = None
        self.login_signup_label = None
        self.login_signup_entry = None
        self.password_signup_label = None
        self.password_signup_entry = None
        self.position_signup_label = None
        self.position_signup_entry = None
        self.register_button = None
        self.sign_up()

    def sign_up(self):
        self.signup = Toplevel()
        self.signup.geometry('250x220')
        self.signup.title('Registration')

        self.position_signup_label = tk.Label(self.signup, text='Position', font=('Times New Roman', 12))
        self.position_signup_label.grid(column=0, row=0)

        self.position_signup_entry = tk.Entry(self.signup)
        self.position_signup_entry.grid(column=1, row=0)

        self.firstname_signup_label = tk.Label(self.signup, text='Name', font=('Times New Roman', 12))
        self.firstname_signup_label.grid(column=0, row=1)

        self.firstname_signup_entry = tk.Entry(self.signup)
        self.firstname_signup_entry.grid(column=1, row=1)

        self.lastname_signup_label = tk.Label(self.signup, text='Surname', font=('Times New Roman', 12))
        self.lastname_signup_label.grid(column=0, row=2)

        self.lastname_signup_entry = tk.Entry(self.signup)
        self.lastname_signup_entry.grid(column=1, row=2)

        self.login_signup_label = tk.Label(self.signup, text='Login', font=('Times New Roman', 12))
        self.login_signup_label.grid(column=0, row=3)

        self.login_signup_entry = tk.Entry(self.signup)
        self.login_signup_entry.grid(column=1, row=3)

        self.phone_signup_label = tk.Label(self.signup, text='Phone number', font=('Times New Roman', 12))
        self.phone_signup_label.grid(column=0, row=4)

        self.phone_signup_entry = tk.Entry(self.signup)
        self.phone_signup_entry.grid(column=1, row=4)

        self.email_signup_label = tk.Label(self.signup, text='Email', font=('Times New Roman', 12))
        self.email_signup_label.grid(column=0, row=5)

        self.email_signup_entry = tk.Entry(self.signup)
        self.email_signup_entry.grid(column=1, row=5)

        self.password_signup_label = tk.Label(self.signup, text='Password', font=('Times New Roman', 12))
        self.password_signup_label.grid(column=0, row=6)

        self.password_signup_entry = tk.Entry(self.signup)
        self.password_signup_entry.grid(column=1, row=6)

        self.register_button = tk.Button(self.signup, text='Registry', command=self.create_user,
                                         font=('Times New Roman', 12))
        self.register_button.grid(row=7, columnspan=2)

    def create_user(self):
        global cursor

        select_query = "SELECT employee_id FROM employee;"
        cursor.execute(select_query)
        employee_id_worker = cursor.fetchall()

        for row in employee_id_worker:
            employee_id_worker = row[0]

        employee_id_worker_create = employee_id_worker + 1
        employee_id_worker_insert = employee_id_worker + 1

        query = f"INSERT INTO employees_passwords (employee_id, user_password) VALUES" \
                f" ({int(employee_id_worker_insert)}, '{str(self.password_signup_entry.get())}')"
        cursor.execute(query)

        db.create_new_user(employee_id_worker_create, self.position_signup_entry.get(),
                           self.firstname_signup_entry.get(), self.lastname_signup_entry.get(),
                           self.login_signup_entry.get(), self.phone_signup_entry.get(), self.email_signup_entry.get(),
                           self.password_signup_entry.get())

    def quit(self):
        self.signup.destroy()


class manager_menu():
    def __init__(self):
        super().__init__()
        self.contract_id_entry = None
        self.contract_id_label = None
        self.success_employee_json_label = None
        self.success_task_json_label = None
        self.employee_to_json_button = None
        self.task_to_json_button = None
        self.show_tasks = None
        self.show_employees = None
        self.employees_report_button = None
        self.task_report_button = None
        self.show_employees_button = None
        self.show_task_button = None
        self.confirm_button = None
        self.create_task = None
        self.executor_entry = None
        self.executor_label = None
        self.deadline_date_entry = None
        self.deadline_date_label = None
        self.creation_date_entry = None
        self.creation_date_label = None
        self.priority_entry = None
        self.priority_label = None
        self.description_entry = None
        self.description_label = None
        self.signin_manager = None
        self.create_task_button = None
        self.manager_menu()

    def manager_menu(self):
        self.signin_manager = Toplevel()
        self.signin_manager.geometry('250x200')
        self.signin_manager.title('Manager')

        self.create_task_button = tk.Button(self.signin_manager, text='Create task', command=self.create_task_menu,
                                            width=15, font=('Times New Roman', 12))
        self.create_task_button.grid(column=0, row=0)

        self.show_task_button = tk.Button(self.signin_manager, text='Show task', command=self.show_task, width=15,
                                          font=('Times New Roman', 12))
        self.show_task_button.grid(column=0, row=1)

        self.show_employees_button = tk.Button(self.signin_manager, text='Show employees', command=self.show_employee,
                                               width=15, font=('Times New Roman', 12))
        self.show_employees_button.grid(column=0, row=2)

        self.task_report_button = tk.Button(self.signin_manager, text='Task report', command=self.task_to_json,
                                            width=15, font=('Times New Roman', 12))
        self.task_report_button.grid(column=0, row=3)

        self.employees_report_button = tk.Button(self.signin_manager, text='Employees report',
                                                 command=self.employee_to_json, width=15, font=('Times New Roman', 12))
        self.employees_report_button.grid(column=0, row=4)

    def create_task_menu(self):
        self.create_task = Toplevel()
        self.create_task.geometry('250x175')
        self.create_task.title('Creation')

        self.description_label = tk.Label(self.create_task, text='Description', font=('Times New Roman', 12))
        self.description_label.grid(column=0, row=0)

        self.description_entry = tk.Entry(self.create_task)
        self.description_entry.grid(column=1, row=0)

        self.priority_label = tk.Label(self.create_task, text='Priority', font=('Times New Roman', 12))
        self.priority_label.grid(column=0, row=1)

        self.priority_entry = tk.Entry(self.create_task)
        self.priority_entry.grid(column=1, row=1)

        self.deadline_date_label = tk.Label(self.create_task, text='Deadline date', font=('Times New Roman', 12))
        self.deadline_date_label.grid(column=0, row=2)

        self.deadline_date_entry = tk.Entry(self.create_task)
        self.deadline_date_entry.grid(column=1, row=2)

        self.contract_id_label = tk.Label(self.create_task, text='Contract ID', font=('Times New Roman', 12))
        self.contract_id_label.grid(column=0, row=3)

        self.contract_id_entry = tk.Entry(self.create_task)
        self.contract_id_entry.grid(column=1, row=3)

        self.executor_label = tk.Label(self.create_task, text='Executor ID', font=('Times New Roman', 12))
        self.executor_label.grid(column=0, row=4)

        self.executor_entry = tk.Entry(self.create_task)
        self.executor_entry.grid(column=1, row=4)

        self.confirm_button = tk.Button(self.create_task, text='Confirm', command=self.create_task_confirm,
                                        font=('Times New Roman', 12), width=10)
        self.confirm_button.grid(row=5, columnspan=2)

    def create_task_confirm(self):
        global cursor

        select_query = "SELECT task_id FROM task;"
        cursor.execute(select_query)
        task_id = cursor.fetchall()

        for row in task_id:
            task_id = row[0]

        task_id = task_id + 1

        datetime_now = datetime.now()
        current_datetime = datetime_now.replace(microsecond=0)
        status = 'active'

        select_query = f"SELECT employee_id FROM employee WHERE login = '{str(login)}';"
        cursor.execute(select_query)
        employee_id = cursor.fetchall()

        for row in employee_id:
            employee_id = row[0]

        db.create_new_task(task_id, self.description_entry.get(), self.priority_entry.get(), current_datetime,
                           self.deadline_date_entry.get(), status, self.contract_id_entry.get(), employee_id,
                           self.executor_entry.get())

    def show_employee(self):
        self.show_employees = Toplevel()
        self.show_employees.title('Show employees')
        self.show_employees.state('zoomed')

        global cursor
        cursor.execute("select count(*) from employee")
        rows = cursor.fetchall
        cursor.execute("select * from employee;")
        employees = cursor.fetchall()

        columns = ('employee_id', 'post', 'firstname', 'lastname', 'login', 'phone_number', 'email', 'user_password')

        table = ttk.Treeview(self.show_employees, columns=columns, show='headings', height=400)
        table.grid(row=0, column=0, sticky="nsew")
        table.heading('employee_id', text='Employee ID')
        table.heading('post', text='Post')
        table.heading('firstname', text='Firstname')
        table.heading('lastname', text='Lastname')
        table.heading('login', text='Login')
        table.heading('phone_number', text='Phone number')
        table.heading('email', text='email')
        table.heading('user_password', text='Password')

        for employee in employees:
            table.insert("", 'end', values=employee)

        scrollbar = ttk.Scrollbar(self.show_employees, orient='vertical', command=table.yview)
        table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

    def show_task(self):
        self.show_tasks = Toplevel()
        self.show_tasks.title('Show tasks')
        self.show_tasks.state('zoomed')

        global cursor
        cursor.execute("select count(*) from task")
        rows = cursor.fetchall
        cursor.execute("select * from task;")
        tasks = cursor.fetchall()

        columns = ('task_id', 'description', 'priority', 'creation_date', 'deadline_date', 'status', 'contract_id',
                   'author_employee_id', 'executor_employee_id')

        table = ttk.Treeview(self.show_tasks, columns=columns, show='headings', height=400)
        table.grid(row=0, column=0, sticky="nsew")
        table.heading('task_id', text='Task ID')
        table.heading('description', text='Description')
        table.heading('priority', text='Priority')
        table.heading('creation_date', text='Creation date')
        table.heading('deadline_date', text='Deadline date')
        table.heading('status', text='Status')
        table.heading('contract_id', text='Contract ID')
        table.heading('author_employee_id', text='Author ID')
        table.heading('executor_employee_id', text='Executor ID')

        for task in tasks:
            table.insert("", 'end', values=task)

        scrollbar = ttk.Scrollbar(self.show_tasks, orient='vertical', command=table.yview)
        table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

        scrollbar2 = ttk.Scrollbar(self.show_tasks, orient='horizontal', command=table.xview)
        scrollbar2.grid(row=1, column=0, sticky='we')
        table.configure(xscrollcommand=scrollbar2.set)

    def task_to_json(self):
        db.create_json_task('F:\db\json_task.json')

        self.task_to_json_button = Toplevel()
        self.task_to_json_button.geometry('225x75')
        self.task_to_json_button.title('Success')

        self.success_task_json_label = tk.Label(self.task_to_json_button, text='Файл сохранен успешно!',
                                                font=('Times New Roman', 12))
        self.success_task_json_label.pack(expand=True)

    def employee_to_json(self):
        db.create_json_employee('F:\db\json_employee.json')

        self.employee_to_json_button = Toplevel()
        self.employee_to_json_button.geometry('225x75')
        self.employee_to_json_button.title('Success')

        self.success_employee_json_label = tk.Label(self.employee_to_json_button, text='Файл сохранен успешно!',
                                                    font=('Times New Roman', 12))
        self.success_employee_json_label.pack(expand=True)


class worker_menu():
    def __init__(self):
        super().__init__()
        self.worker_tasks = None
        self.worker_tasks_button = None
        self.signin_worker = None
        self.worker_menu()

    def worker_menu(self):
        self.signin_worker = Toplevel()
        self.signin_worker.geometry('250x200')
        self.signin_worker.title('Worker')

        self.worker_tasks_button = tk.Button(self.signin_worker, text='Show tasks', command=self.show_worker_tasks,
                                             font=('Times New Roman', 12))
        self.worker_tasks_button.grid(row=0)

    def show_worker_tasks(self):
        self.worker_tasks = Toplevel()
        self.worker_tasks.title('Tasks')
        self.worker_tasks.geometry('800x200')

        global cursor
        select_query1 = "select employee_id from employee where post = 'worker' AND employee_id = 4;"
        select_query2 = "select employee_id from employee where post = 'worker' AND employee_id = 5;"
        select_query3 = "select employee_id from employee where post = 'worker' AND employee_id = 6;"
        cursor.execute(select_query1)
        employee_id_worker1 = cursor.fetchall()

        for row in employee_id_worker1:
            employee_id_worker1 = row[0]

        cursor.execute(select_query2)
        employee_id_worker2 = cursor.fetchall()

        for row in employee_id_worker2:
            employee_id_worker2 = row[0]

        cursor.execute(select_query3)
        employee_id_worker3 = cursor.fetchall()

        for row in employee_id_worker3:
            employee_id_worker3 = row[0]
        cursor.execute(
            f"SELECT description, creation_date, priority, deadline_date FROM task WHERE executor_employee_id = "
            f"{int(employee_id_worker1)} OR executor_employee_id = {int(employee_id_worker2)} "
            f"OR executor_employee_id = {int(employee_id_worker3)}")
        employees = cursor.fetchall()

        columns = ('description', 'creation_date', 'priority', 'deadline_date')

        table = ttk.Treeview(self.worker_tasks, columns=columns, show='headings', height=400)
        table.grid(row=0, column=0, sticky="nsew")
        table.heading('description', text='Description')
        table.heading('creation_date', text='Creation date')
        table.heading('priority', text='Priority')
        table.heading('deadline_date', text='Deadline date')

        for employee in employees:
            table.insert("", 'end', values=employee)

        scrollbar = ttk.Scrollbar(self.worker_tasks, orient='vertical', command=table.yview)
        table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")


class MainWindow:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.win = tk.Tk()
        self.win.title('Main')
        self.win.geometry(f"200x175")

        self.signin_label = tk.Label(self.win, text='Authorization', font=('Times New Roman', 16))
        self.signin_label.grid(column=0, row=0, columnspan=2)

        self.login_label = tk.Label(self.win, text='Login', font=('Times New Roman', 12), anchor='w')
        self.login_label.grid(column=0, row=1)

        self.login_entry = tk.Entry(self.win, font=('Times New Roman', 12), width=15)
        self.login_entry.grid(column=1, row=1)

        self.password_label = tk.Label(self.win, text='Password', font=('Times New Roman', 12), anchor='w')
        self.password_label.grid(column=0, row=2)

        self.password_entry = tk.Entry(self.win, font=('Times New Roman', 12), width=15, show='*')
        self.password_entry.grid(column=1, row=2)

        self.signin_button = tk.Button(self.win, text='Sign In', width=6, command=self.sign_in,
                                       font=('Times New Roman', 12))
        self.signin_button.grid(column=0, row=4, columnspan=2)

        self.signup_button = tk.Button(self.win, text='Sign Up', width=6, command=self.sign_up_press,
                                       font=('Times New Roman', 12))
        self.signup_button.grid(column=0, row=5, columnspan=2)

    def sign_up_press(self):
        Registration()

    def sign_in(self):
        global cursor
        cursor.execute(f"SELECT login FROM employee WHERE login = '{str(self.login_entry.get())}'")
        global login
        login = cursor.fetchall()
        for row in login:
            login = row[0]

        cursor.execute(f"SELECT user_password FROM employees_passwords WHERE user_password ="
                       f" '{str(self.password_entry.get())}';")
        user_password = cursor.fetchall()
        for row in user_password:
            user_password = row[0]

        cursor.execute(f"SELECT post FROM employee WHERE login = '{str(self.login_entry.get())}';")
        user_post = cursor.fetchall()
        for row in user_post:
            user_post = row[0]

        if login == self.login_entry.get() and user_password == self.password_entry.get() and user_post == 'manager':
            manager_menu()
        elif login == self.login_entry.get() and user_password == self.password_entry.get() and user_post == 'worker':
            worker_menu()
        else:
            self.message_label = tk.Label(self.win, text='Incorrect login or password', font=('Times New Roman', 12))
            self.message_label.grid(column=0, row=3, columnspan=2)


MainWindow().win.mainloop()
