import mysql.connector

"""
basic database
"""
conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='Data7Dollar$',
    database='mysql_learner'
)
cursor_obj = conn.cursor()
statement = """select * from INSTRUCTOR"""
cursor_obj.execute(statement)
print("all the data")
output = cursor_obj.fetchall()
for row in output:
    print(row)

cursor_obj.close()
conn.close()