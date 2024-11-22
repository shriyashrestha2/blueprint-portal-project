import sqlite3
import socket

# Connect to the SQLite database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT,
                   password TEXT)''')

# Insert data into the table
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("MariamKhan", "supersecret1"))
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("DannyWatson", "supersecret2"))
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("josephuang45", "supersecret3"))
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("ShriyaShrestha", "supersecret4"))
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("JohnCena", "supersecret5"))
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("JustinSmith", "supersecret6"))
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("DwayneTheRock", "supersecret7"))

# Commit the changes and close the connection
conn.commit()
conn.close()

# Retrieve data from table
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute(f"""SELECT * 
FROM users""")
rows = cursor.fetchall()

# Display the retrieved data
for row in rows:
    print(f"ID: {row[0]}, Username: {row[1]}, Password: {row[2]}")

# Close the connection
conn.close()
