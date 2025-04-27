import pandas as pd
import mysql.connector

# Connect to MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Data7Dollar$",
        database="company"
    )
    cursor_obj = conn.cursor()
    print("Successfully connected to the database.")

    # Load CSV file and manually assign column names
    column_names = ['loct_id', 'dept_id_loc']
    df = pd.read_csv(r'C:\projects\Databasesystem\Locations (1).csv', header=None, names=column_names)

    # Debugging: Print CSV content
    print("CSV Content Before Insertion:")
    print(df)

    # Check if DataFrame is empty
    if df.empty:
        print("CSV file is empty or not loaded correctly!")
    else:
        # Insert data into the 'locations' table
        query = 'INSERT INTO locations (`loct_id`, `dept_id_loc`) VALUES (%s, %s)'

        # Loop through and insert rows
        for _, row in df.iterrows():
            loct_id = str(row["loct_id"]).zfill(9)  # Ensure it's a 9-character string
            dept_id_loc = str(row["dept_id_loc"]).zfill(9)

            try:
                cursor_obj.execute(query, (loct_id, dept_id_loc))
            except mysql.connector.Error as e:
                print(f"Error inserting row {row}: {e}")
                continue

        # Commit changes
        conn.commit()
        print("CSV data inserted successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if conn.is_connected():
        cursor_obj.close()
        conn.close()
        print("Connection closed.")