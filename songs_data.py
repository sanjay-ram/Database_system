import mysql.connector
import csv
# data science from sanjay
conn = mysql.connector.connect(
    host="localhost",
    port = 3306,
    user="root",
    password="Data7Dollar$",
    database="songs"
)
cursor_con = conn.cursor()

cursor_con.execute("""
CREATE TABLE IF NOT EXISTS songs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    artist VARCHAR(255),
    album VARCHAR(255),
    year INT,
    genre VARCHAR(100),
    duration INT,
    youtube_link VARCHAR(255)
)
""")

# CSV einlesen und Daten einfügen
with open("songs.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor_con.execute("""
            INSERT INTO songs (title, artist, album, year, genre,duration,youtube_link )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (row["Titel"], row["Künstler"], row["Album"], row["Jahr"], row["Genre"], row["Dauer"], row["YouTube_Link"]))

conn.commit()
cursor_con.close()
conn.close()

print("✅ Songs wurden erfolgreich in die Datenbank hochgeladen.")