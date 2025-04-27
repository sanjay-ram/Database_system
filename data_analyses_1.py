from sqlalchemy import create_engine
import pandas as pd
# data science from sanjay
from analyzing_data import DB_USER, DB_HOST, DB_PASSWORD, DB_PORT, DB_NAME

DB_USER = DB_USER
DB_HOST = DB_HOST
DB_PASSWORD = DB_PASSWORD
DB_PORT = DB_PORT
DB_NAME = DB_NAME

csv_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_Coursera_V5/data/ChicagoCrimeData.csv"
engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
df = pd.read_csv(csv_url)
df.to_sql('chicago_socioeconomic_data', con = engine, if_exists = 'replace', index = False, method = 'multi')

print("Data sucessfully created")