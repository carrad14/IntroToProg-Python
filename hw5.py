"""
Title: Assignment 5
Dev: Diego J. Carrasquillo

In this activity you will learn to work with for Lists and Dictionaries.
Now that you have reviewed the websites and videos, you will create a new script that manages a "To Do List."
This project is like to the last one, but this time The To Do file will contain two columns of data (Task, Priority)
which you store in a Python dictionary. Each Dictionary will represent one row of data and these rows of data are added
to a Python List to create a table of data.

1. Create a text file called text file (get name from class website) using the following data:
2. When the program starts, load each row of data from the text file into a Python dictionary. (The data will
   be stored like a row in a table.)
   Tip: You can use a for loop to read a single line of text from the file and then place the data into a new dictionary
   object.
3. After you get the data in a Python dictionary, Add the new dictionary “row” into a Python list object (now the data
   will be managed as a table).
4. Display the contents of the List to the user.
5. Allow the user to Add or Remove tasks from the list using numbered choices. Something like this would work:

    Menu of Options:

    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program

6. Save the data from the table into the text file when the program exits.
"""

"""
The first part of this code will read the default text file. It will read the information, store as a dictionary, and 
store those dictionaries as rows of a table. Using objFile1 for the first section of this code.
"""

objFile1 = open('/Users/carrad/intro_to_python/HW5/ToDo.txt', 'r')  # opens txt file, assigns result to objFile1

todo_dict_master = {}  # Creating empty dictionary to be updated
Table_master = []  # Creating Table to store dictionary entries as rows

todo_dict = {}  # Creating empty dictionary to be updated
Table = []  # Creating Table to store dictionary entries as rows

for line in objFile1:  # For loop wll split string, store in dictionary, and put as row in table
    values = line.split()
    task = values[0]
    priority = values[1]
    todo_dict_1 = {task: priority}
    todo_dict_master.update(todo_dict_1)
    Table_master.append(todo_dict_1)
#  end loop

objFile1.close()  # closes text file and seals it off from further reading or writing

"""
The second part of the code will display a menu for user interface (please look at general instructions at top to see
menu options).
"""

objFile2 = open('/Users/carrad/intro_to_python/HW5/ToDo.txt', 'w')  # opens txt file, assigns result to objFile2

while True:

    # Display a menu of choices to the user
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)

    strInput = str(input("Which option would you like to perform? (Select 1 - 5): "))

    # Display all list/Table items to user
    if strInput == "1":
        print("Current Data")
        print()
        for lines in Table_master:
            print(lines)
        continue

    # Add a new item to the list/Table
    elif strInput == "2":  # For loop wll split string, store in dictionary, and put as row in table
        task = str(input("What is the task you want to add? "))  # Input task of choice
        priority = str(input("What is the priority level? "))  # Input matching value
        todo_dict_2 = {task: priority}
        todo_dict.update(todo_dict_2)
        Table.append(todo_dict_2)
        todo_dict_master.update(todo_dict_2)
        Table_master.append(todo_dict_2)
        continue

    # Remove a new item to the list/Table
    #  Will check for input in master and section 2 dictionary. Will delete accordingly, and recreate rows
    #  (dictionaries) in Tables
    elif strInput == "3":
        print(Table_master)  # Illustrates task/priority options
        delInput = (input("What task would you like to delete? (Please delete a task from above)"))
        if delInput in todo_dict:  # checking for value in dictionary
            del todo_dict[delInput]  # deletes value in both dictionaries
            del todo_dict_master[delInput]
            Table = []  # resets values in Tables
            Table_master = []
            for item in todo_dict_master:  # loop that will reset value of tables after deleting task
                temp_dict = {item: todo_dict_master[item]}
                Table_master.append(temp_dict)
            for item in todo_dict:    # deletes value in both dictionaries
                temp_dict = {item: todo_dict[item]}
                Table.append(temp_dict)
        elif delInput in todo_dict_master:  # checking for value in dictionary
            del todo_dict_master[delInput]  # deletes value in master dictionary
            Table = []  # resets values in Tables
            Table_master = []
            for item in todo_dict_master:  # deletes value in both dictionaries
                temp_dict = {item: todo_dict_master[item]}
                Table_master.append(temp_dict)
            for item in todo_dict:  # deletes value in both dictionaries
                temp_dict = {item: todo_dict[item]}
                Table.append(temp_dict)
        else:
            print("Task was not found.")  # If task not saved, cannot delete and will bring back to menu
        continue

    # Save tasks to the text file
    elif strInput == "4":
        for item in Table_master:
            key = list(item.keys())  # takes task (priority) and stores
            value = list(item.values())  # takes priority (value) and stores
            objFile2.write(key[0])  # join command turns tuple into string
            objFile2.write(", ")
            objFile2.write(value[0])
            objFile2.write('\r')
        continue

    # Exit program
    elif strInput == "5":
        break  # get ous of Menu loop
    else:       # If input is not 1-5, user will be asked for input again
        print("Try again")
        print("Which option would you like to perform? (Select between 1 & 5)")
        continue

objFile2.close()  # closes file and seals it off from further reading or writing until opened again
