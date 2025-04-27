from sqlalchemy import create_engine
import pandas as pd

DB_USER = 'root'
DB_PASSWORD = 'Data7Dollar$'
DB_HOST = 'localhost'
DB_PORT = 3306
DB_NAME = 'mysql_python_learner'


engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
query = "SELECT * FROM cityofchicago LIMIT 5;"
df = pd.read_sql_query(query, engine)
print(df)