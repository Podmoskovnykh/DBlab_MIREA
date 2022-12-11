import psycopg2
import hashlib
from config import host, user, password, db_name

connection = psycopg2.connect(host=host, user=user, password=password, database=db_name)
cursor = connection.cursor()
connection.autocommit = True


def create_new_user(employee_id: int, post: str, firstname: str, lastname: str, login: str, phone_number: str,
                    email: str, password: str):
    global cursor

    hash = hashlib.md5(password.encode())
    hash_password = hash.hexdigest()

    cursor.execute(
        f"INSERT INTO employee(employee_id, post, firstname, lastname, login, phone_number, email, user_password) "
        f"VALUES"
        f"({int(employee_id)}, '{str(post)}', '{str(firstname)}', '{str(lastname)}', '{str(login)}', "
        f"'{str(phone_number)}', '{str(email)}', '{str(hash_password)}')")


def create_new_task(task_id: int, description: str, priority: int, creation_date, deadline_date,
                    status: str, contract_id: int, author_employee_id: int, executor_employee_id: int):
    global cursor
    cursor.execute(f"INSERT INTO task(task_id, description, priority, creation_date, deadline_date, status, "
                   f"contract_id, author_employee_id, executor_employee_id) VALUES ({int(task_id)}, "
                   f"'{str(description)}', {int(priority)}, '{creation_date}', "
                   f"'{deadline_date}', '{str(status)}', {int(contract_id)}, {int(author_employee_id)}, "
                   f"{int(executor_employee_id)})")


def create_json_task(directory: str):
    global cursor
    cursor.execute(f"CALL create_json('{str(directory)}');")


def create_json_employee(directory: str):
    global cursor
    cursor.execute(f"CALL create_json_employee('{str(directory)}');")
