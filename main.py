from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

if __name__ == '__main__':
  calculate_salary()
  d = datetime.now()
  get_employees()
  print(d)