import threading # two things happening at once
import sqlite3
# import hashlib
import socket # used to establish the connection between client and server

try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # internet socket, connection oriented protocol (TCP)
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ("localhost", 9999)
ss.bind(server_binding)
ss.listen()

# Function to verify login credentials
def check_credentials(username, password):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    # Check if the username and password inputted is present in the table 'users'
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password)) 
    # Once SQL query is run, fetch the username and password set in the first row. 'user' will be None if there is no match.
    user = cursor.fetchone() 
    conn.close()
    return user is not None # If a user is present, this returns True, if not then False


def start_connection(c): # taking client as parameter
    # receive and process username
    username = c.recv(1024).decode()
    print("[S]: Received username: " + username)    

    # receive and process password
    password = c.recv(1024).decode()
    print("[S]: Received password: " + password)    

    if check_credentials(username, password):
        c.send("Authorized user. Access granted.".encode())
        print("[S]: Authorized user has logged in.")
    else:
        c.send("Unauthorized user. Access denied.".encode())
        print("[S]: Unauthorized login attempt.")
    
    # close client connection
    c.close()

while True:
    client, addr = ss.accept()
    t2 = threading.Thread(target=start_connection, args=(client,))
    t2.start()

    # Close the server socket
    ss.close()
    exit()