# --------------------------------#
# Title: "Todo"
# Dev: mseeley3
# Date: 4/27/19
# Changelog: (Who, When, What)
# mseeley3,4/27/19, Created Script
# --------------------------------#

# -------------Data------------- #
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.
objFile = open("Todo.txt", "r")

# read each line of the text file and turn in into a list
strData = objFile.readlines()

# create an empty table
lstTable = []

# read the "strData" list
# use the for loop to add each line to the table lstTable as a dictionary
for st in strData:

    # create a temporary list from the splitting the first element of lines
    # the readlines() function leaves a "\n" at the end, so we will scrub that with strip()
    # separate the task from the priority by "," using split()
    templine = st.strip("\n").split(",")

    # the first object in our templine is the task, store as "task"
    task = templine[0]

    # second object in our templine is the priority, store as "priority"
    priority = templine[1]

    # create a dictionary using task and priority
    dicRow = {"Task":task, "Priority":priority}

    #add dicRow to the empty table
    lstTable.append(dicRow)

# -------------Input/Output------------- #
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

# create a function to print out the user's options
def strMenue():
    print("""What would you like to do? Enter the number to the left of the action you would like to take.
    1: Show current data
    2: Add a new task
    3: Remove an existing task
    4: Save Data to File
    5: Exit Program""")

# create a function to print out lstTable
def printtable ():
    print("**************************************************")

    for lst in lstTable:
        print(lst["Task"] + ": " + lst["Priority"])

    print("**************************************************")

# -------------Processing------------- #
# create a while loop so that as long as the script is running
# this way the program will stay in this loop until the user is done
while (True):

    # Step 2
    # Display a menu of choices to the user
    strMenue()

    # Display all todo items to user
    printtable()

    # if the user puts in something other than an integer number, we use this try-except construct to trap the error
    try:
        strChoice = int(input())

        # Step 3
        # Display all todo items to user
        # if the user enters a "1", simply print out the currently existing data in lstTable
        if (strChoice == 1):
            printtable()

        # Step 4
        # Add a new item to the list/Table
        # if the user enters a "2", store their inputs into a temporary dictionary row
        # then add that row to the lstTable
        elif (strChoice == 2):
            task = input("Enter a new task: ")
            priority = input("What is the priority level of this task?: ")

            tempdicRow = {"Task": task, "Priority": priority}

            lstTable.append(tempdicRow)

        # Step 5
        # Remove a new item to the list/Table
        # create a loop that searches the table for the task that the user wants to delete
        elif (strChoice == 3):

            # create a counter that starts as the first row of the table
            x = 0
            # create a value that matches how many row are in the table minus 2
            y = len(lstTable) - 2

            # get the task the user wants to delete
            search = input("Enter the task you want to delete (case sensitive): ")

            # this for loop will go through the lstTable row by row
            # it looks up the string under the key "Task" and try to match it to the input
            for task in lstTable:

                # if there is a match, the entire row will be removed from the table
                if (task["Task"] == search):

                    # because the value of x matches which row the for loop is looking at
                    # we can remove the whole row using .pop(x)
                    lstTable.pop(x)

                    # print out the table again so that the user can see their update
                    print("'" + search + "'" + " has been removed.")

                # if the user enters a term that is not in the table
                # eventually the for lop will run more times than there are rows in the table
                # this will make x (the number of times the loop was run) greater than:
                # y (the number of rows in the table minus 2)
                # (it's a minus 2 instead of minus one, becaase python marks the 1st row as 0)
                # at that point we can tell the user their term was not found
                else:
                    if (x > y):
                        print("That task was not found.")

                # for each run of the for loop, increase the counter by 1
                x = x + 1

        # Step 6
        # Save tasks to the ToDo.txt file
        # if the user enters a 4, the data currently existing in the lstTable should be saved
        elif (strChoice == 4):

            # open the file
            Todo = open("C:\\_PythonClass\\Assignment05\\Todo.txt", "w")

            # go down the tuple and store each row into the text file
            for lst in lstTable:

                #store the strings under each dictioary key as it's own object
                task = lst["Task"]
                priority = lst["Priority"]

                # store the data as "task" , "priority"
                Todo.write(str(task) + "," + str(priority) + "\n")

            # close connection to text file
            Todo.close

        # Step 7
        # Exit program
        # if the user enters a 5, they are done with the program, so break the script
        elif (strChoice == 5):
            break  # and exit the program

        # if the user inputs a number greater than 5
        elif (strChoice > 5):
            print("Wrong number.")

        # if the user inputs a number lower than 1
        elif (strChoice < 1):
            print("Wrong number.")

    # print message telling the user that they can only put in a number 1-5
    except:
        print("Please enter a number that is from 1-5.")