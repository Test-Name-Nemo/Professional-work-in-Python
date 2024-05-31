from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

dt = datetime.today().strftime("%d-%m-%Y")

if __name__ == '__main__':
    print(f'Дата вызова функции: {dt}')
    get_employees()
    calculate_salary()
