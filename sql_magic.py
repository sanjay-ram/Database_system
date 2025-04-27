from datetime import date, datetime, timedelta, time
from typing import Tuple, Set, Dict

import mysql.connector
from _decimal import Decimal
from prettytable import PrettyTable
"""
database = myslq_python_learner
"""

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='Data7Dollar$',
    database='mysql_python_learner'
)
cursor_obj = conn.cursor()

statement = "select * from INTERNATIONAL_STUDENT_TEST_SCORES where country = %s"
country = ("Canada",)
cursor_obj.execute(statement, country)
output = cursor_obj.fetchall()
table = PrettyTable()
table.field_names = [desc[0] for desc in cursor_obj.description]


for row in output:
    table.add_row(row)

print("All the data:")
print(table)
cursor_obj.close()
conn.close()


