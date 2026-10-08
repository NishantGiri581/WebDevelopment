# import mysql.connector as conn
# import mysql.connector

# # 1. Connect to the database
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="Saless"
# )

# cursor = conn.cursor()

# # 2. Define the SQL Query
# sql_query = "INSERT INTO Sales_data (product, quantity, price) VALUES (%s, %s, %s)"

# # 3. Define the data as a LIST of tuples
# # (Note: I wrapped your tuples in a list [] to make it clear it's a collection of rows)
# val = [
#     ("Laptop", 5, 50000),
#     ("Mouse", 15, 500),
#     ("Keyboard", 10, 1500)
# ]

# # 4. Execute and Commit
# try:
#     # CHANGE HERE: Use executemany() for multiple rows
#     cursor.executemany(sql_query, val)
    
#     conn.commit() 
#     print(f"{cursor.rowcount} records inserted successfully.")

#     # Optional: Check the data immediately to verify
#     cursor.execute("SELECT * FROM Sales_data")
#     result = cursor.fetchall()
#     print("\n--- Current Table Data ---")
#     for x in result:
#         print(x)

# except Exception as e:
#     print(f"Error: {e}")
#     conn.rollback()

# finally:
#     cursor.close()
#     conn.close()
#     print("Connection closed.")


#------------------------------------------------------------


# import mysql.connector

# try:
#     # 1. Connect
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="@Giri581.",
#         database="Saless"
#     )
#     cursor = conn.cursor()

#     # 2. Define Query (No WHERE clause means delete EVERYTHING)
#     sql_query = "DELETE FROM Sales_data"

#     # 3. Execute
#     cursor.execute(sql_query)

#     # 4. Commit
#     conn.commit()

#     print(f"Success! {cursor.rowcount} records were deleted.")

#     # 5. Verify (Should be empty)
#     cursor.execute("SELECT * FROM Sales_data")
#     result = cursor.fetchall()
    
#     if not result:
#         print("The table is now empty.")
#     else:
#         print("Data still remains.")

# except mysql.connector.Error as e:
#     print(f"Error: {e}")
#     conn.rollback()

# finally:
#     if conn.is_connected():
#         cursor.close()
#         conn.close()
#         print("Connection closed.")

#------------------------------------------
# import mysql.connector
# import requests

# # --- 1. Fetch Data from API ---
# api_url = "https://jsonplaceholder.typicode.com/users"
# response = requests.get(api_url)

# if response.status_code == 200:
#     users_json = response.json() # Convert response to Python list/dict
#     print(f"Successfully fetched {len(users_json)} records from API.")
# else:
#     print("Failed to fetch data")
#     exit()

# # --- 2. Connect to Database ---
# try:
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="@Giri581.",
#         database="Saless"
#     )
#     cursor = conn.cursor()

#     # (Optional) Create a table to store this specific API data
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS Api_Users (
#             id INT PRIMARY KEY,
#             name VARCHAR(255),
#             email VARCHAR(255),
#             city VARCHAR(255)
#         )
#     """)

#     # --- 3. Prepare Data for Insertion ---
#     # We need to extract specific fields from the JSON object and make a list of tuples
#     data_to_insert = []
    
#     for user in users_json:
#         # Extracting specific fields from the complex JSON object
#         u_id = user['id']
#         name = user['name']
#         email = user['email']
#         city = user['address']['city'] # Example of accessing nested data
        
#         data_to_insert.append((u_id, name, email, city))

#     # --- 4. Insert Data (Bulk Insert) ---
#     sql_query = "INSERT INTO Api_Users (id, name, email, city) VALUES (%s, %s, %s, %s)"
    
#     # Use executemany for fast bulk insertion
#     # We use 'INSERT IGNORE' here just in case you run the script twice (to avoid duplicate ID errors)
#     sql_query = "INSERT IGNORE INTO Api_Users (id, name, email, city) VALUES (%s, %s, %s, %s)"
    
#     cursor.executemany(sql_query, data_to_insert)
#     conn.commit()
    
#     print(f"{cursor.rowcount} records inserted into 'Api_Users' table.")

# except mysql.connector.Error as err:
#     print(f"Error: {err}")

# finally:
#     if conn.is_connected():
#         cursor.close()
#         conn.close()
#         print("MySQL connection is closed.")

#------------------------------------------------------------

import mysql.connector as conn

connection = conn.connect(
    host = "localhost",
    user = "root",
    password = '@Giri581.',
    database = "Saless"
)
print("Database connected..")

cursor = connection.cursor()

query = '''create table Sales_data(
           product varchar(40),
           quantity int,
           price decimal(10,2)
);
        '''

query1 = '''insert into Sales_data values("Laptop", 5, 50000),("phone",19,5600);'''


query2 = "desc Sales_data;"
cursor.execute(query1)
cursor.execute(query2)
rows = cursor.fetchall()
for i in rows:
    print(i)
   
connection.commit()

#query = """Delete from Sales_data where product = 'Laptop' """
#cursor.execute(query1)
#connection.commit()
connection.rollback()