import sqlite3
def main():
    # creating employees.db database
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    # Removing the Employee table if any exists already
    cur.execute('''DROP TABLE IF EXISTS Employee''')

    # Creating Employee table and EmployeeID (Primary Key)
    cur.execute('''CREATE TABLE Employee (EmployeeID INTEGER PRIMARY KEY NOT NULL,
                                          EmployeeName TEXT,
                                          DepartmentName TEXT,
                                          City TEXT)''')

    # Entering tha values in the Employee table
    cur.execute('''INSERT INTO Employee (EmployeeID , EmployeeName, DepartmentName, City)
                   VALUES (101, "Arlene Meyers", "Research and Development", "San Jose") ''')
    cur.execute('''INSERT INTO Employee (EmployeeID , EmployeeName, DepartmentName, City)
                   VALUES (102, "Janelle Grant", "Manufacturing", "Austin") ''')
    cur.execute('''INSERT INTO Employee (EmployeeID , EmployeeName, DepartmentName, City)
                   VALUES (103, "Jack Smith", "Marketing", "New York City") ''')
    cur.execute('''INSERT INTO Employee (EmployeeID , EmployeeName, DepartmentName, City)
                   VALUES (104, "Sonia Alvarado", "Accounting", "Boston") ''')
    cur.execute('''INSERT INTO Employee (EmployeeID , EmployeeName, DepartmentName, City)
                   VALUES (105, "Renee Kincaid ", "Marketing", "New York City") ''')
    cur.execute('''INSERT INTO Employee (EmployeeID , EmployeeName, DepartmentName, City)
                   VALUES (106, "Curt Green", "Manufacturing", "Austin") ''')
    cur.execute('''INSERT INTO Employee (EmployeeID , EmployeeName, DepartmentName, City)
                   VALUES (107, "Angela Taylor", "Research and Development", "San Jose") ''')
# Commit the changes in the database and table simultaneously
    conn.commit()
# closes the connection for all
    conn.close()
if _name_ == '_main_':
    main()
