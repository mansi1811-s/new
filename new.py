import sqlite3
"""
gyji
"""

def get_user_data(username):
    """
    gyji
    """
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    #Correct code without vulnerability
    # query = "SELECT * FROM users WHERE username = ?"

    #Directly concatenating user input into SQL query -CVE-2018-6829
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)

    user_data = cursor.fetchall()
    conn.close()
    return user_data

username = input("Enter a username: ") # pylint: disable=redefined-outer-name
user_data = get_user_data(username) # pylint: disable=redefined-outer-name
print(user_data)
