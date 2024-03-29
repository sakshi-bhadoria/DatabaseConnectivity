import sqlite3
def main():
    # Menu Choice
    choice = 0

    # creating employees.db database
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()

    # Get the users menu choice
    while choice != 4:
        choice = get_menu_choice()
        execute_choice(choice, cur)
    # Close the connections
    conn.close()

# The display_menu function displays a menu
def display_menu():
    print('                   MENU')
    print('------------------------------------------')
    print('1 - Display the list of employees sorted by EmployeeName in ascending Order')
    print('2 - Display the list of employees sorted by DepartmentName in descending Order')
    print('3 - Display the list of employees sorted by City')
    print('4 - EXIT ')

# The get_menu_choice function displays the menu and gets the users choice
def get_menu_choice():
    display_menu()
    choice = int(input('Enter your choice: '))
    # validate the choice
    while choice < 1 or choice > 4:
        choice = int(input('Enter a valid choice :'))
    return choice

# Perform the action that the user selected
def execute_choice(choice, cur):
    if choice == 1:
        employees_sorted_by_EmployeeName_ascending(cur)
    if choice == 2:
        employees_sorted_by_DepartmentName_descending(cur)
    if choice == 3:
        employees_sorted_by_City(cur)

# Display the Employees , sorted by EmployeeName, in ascending order.
def employees_sorted_by_EmployeeName_ascending(cur):
    # Execute the SELECT statement on the database
    cur.execute('''SELECT * FROM Employee ORDER BY EmployeeName ASC''')

    # Fetch the results
    results = cur.fetchall()

    # Display the results
    print('\n Employees sorted by EmployeeName in ascending order')
    print('------------------------------------------------------')
    display_results(results)

# Display the Employees , Sorted by DepartmentName , in descending order.
def employees_sorted_by_DepartmentName_descending(cur):
    # Execute the SELECT statement on the database
    cur.execute('''SELECT * FROM Employee ORDER BY DepartmentName DESC''')

    # Fetch the results
    results = cur.fetchall()

    # Display the results
    print('\n Employees sorted by DepartmentName in descending order')
    print('------------------------------------------------------')
    display_results(results)

# Display the Employees , Sorted by City.
def employees_sorted_by_City(cur):
    # Execute the SELECT statement on the database
    cur.execute('''SELECT * FROM Employee ORDER BY City''')

    # Fetch the results
    results = cur.fetchall()

    # Display the results
    print('\n Employees sorted by City')
    print('------------------------------------------------------')
    display_results(results)


# The display_results function displays the values in the
# results of the SELECT statement. It is assumed that the results
# contain the employees list in that order
def display_results(results):
    for row in results:
        print(f'{row[0]:5} | {row[1]:25} | {row[2]:25} | {row[3]:25} | ')
    print()


if __name__ == '__main__':
    main()
