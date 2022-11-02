# import date time
import datetime

# defining the users dictionary
users = {}

# defining the function "reg_user" with parameters ()
def reg_user():
    # new_user variable is initialized to the input of user name entered by the user through the keyboard
    new_user = (input("Enter a new user name:\n"))
    # while loop; new_user in users dictionary
    while new_user in users:
        # print "username already exist"
        print("username already exists")
        # new_user is initialized to the input of "enter a username that doesn't exist"
        new_user = input("Enter a username that doesn't exist")

    # new_password is initialized to the input of new password entered by the user through the keyboard
    password = (input("Enter a new password:\n"))
    # confirm_password is initialized to the input of confirm password entered by the user through the keyboard
    con_password = (input( "Confirm password:\n" ))

    # open 'user.txt' append('a') as username
    while password != con_password:
        # print "password do not match"
        print("Password do not match")
        # con_password is initialized to the input of "Re enter your password"
        con_password = input("Re-enter your password")
        # username.write new line plus(+) new_user plus(+) comma and space(", ") plus(+) new_password.

    # open 'user.txt' append('a') as username
    with open('user.txt', 'a') as username:
        # username.write new line plus(+) new_user plus(+) comma and space(", ") plus(+) new_password.
        username.write("\n" + new_user + ", " + password)

# defining the function 'add_task' with the parameter ()
def add_task():
    # task is initialized to the username of the person the task is assigned to entered by the user and saved to
    # 'task.txt
    user_task = input("Enter the username of the person the task is assigned to:\n")

    # task_title is initialized to the title of the task entered by the user and saved to 'task.txt
    task_title = input("Enter the title of the task:\n")

    # task_description is initialized to the task description entered by the user and saved to 'task.txt
    task_description = input("Enter the task description:\n")

    # task_due is initialized to the due date of the task. (yyyy-mm-dd) entered by the user and saved to 'task.txt'
    task_due = input("input the due date of the task. (yyyy-mm-dd):\n")

    # date is initialized to datetime.date.today()
    date = datetime.date.today()

    # task_complete is initialize to 'No'
    task_completed = 'No'

    # open 'tasks.txt' append 'a', as task
    with open('tasks.txt', 'a') as tasks:
        # task.write new line plus(+) name plus(+) comma and empty space(", ") plus(+) task_description plus(+) comma
        # and empty space(", ") plus(+) str(date) plus(+) comma and empty space(", ") plus(+) task_due plus(+) comma
        # and empty space(", ") plus(+) task_completed.
        tasks.write("\n" + user_task + ", " + task_title + ", " + task_description + ", " + str(
            date) + ", " + task_due + ", " + task_completed)

# defining the function 'view_all' with the parameter ()
def view_all():
    # all_task is open 'tasks.txt read('r') to read
    all_tasks = open('tasks.txt', 'r')

    # for line in all_tasks
    for line in all_tasks:
        # task_list is initialized to line.split(", ") that is putting comma and space in task_list
        task_list = line.split(", ")

        # display task plus(+) task_list at index [1]
        print("Task:\t " + task_list[1])

        # display assigned to plus(+) task_list at index [0]
        print("Assigned to:\t" + task_list[0])

        # display Date assigned plus(+) task_list at index [3]
        print("Date assigned:\t" + task_list[3])

        # display Due date plus(+) task_list at index [4]
        print("Due date:\t" + task_list[4])

        # display task complete plus(+) task_list at index [5]
        print("Task Complete:\t" + task_list[5].strip('\n'))

        # display Task description plus(+) task_list at index [2]
        print("Task description:\n" + task_list[2])

        # print new line
        print("\n")

    # close all_tasks in the for loop
    all_tasks.close()


# defining the function 'view_mine' with the parameter ()
def view_mine():
    # filename is initialize to open ('tasks.txt , 'r') that is reading filename in tasks.txt
    filename = open('tasks.txt', 'r')
    # lines is initialized to filename.read().splitlines()
    lines = filename.read().splitlines()
    # display lines
    print(lines)

    # for lineNumber, line inenumerate(lines):
    for lineNumber, line in enumerate(lines):

        # task_list is initialize to line.split(', ") that is putting comma and space in task_list
        task_list = line.split(", ")
        # i += 1
        # if name is equal to task_list[0] that index [0]
        if name == task_list[0]:
            # display Task number plus str(lineNumber)
            print("Task Number: " + str(lineNumber))

            # display Task plus(=) task_list at index [0]
            print("Task:\t" + task_list[0])

            # display Assigned to plus(+) task_list at index [1]
            print("Assigned to:\t" + task_list[1])

            # display Date assigned plus(+) task_list at index [3]
            print("Date assigned:\t" + task_list[3])

            # display Due date plus(+) at index [4]
            print("Due date:\t" + task_list[4])

            # display Task complete plus(+) task_list at index [5]
            print("Task complete:\t" + task_list[5].strip('\n'))

            # display Task description plus(+) task_list at index [2]
            print("Task description:\n" + task_list[2])

            # print new line
            print("\n")
    # sets the file's current position at the offset
    filename.seek(0)

    # task_num is initialized the int(input("Please select Task Number you would like to edit: "))
    # asking user to select the task number they will like to edit
    task_num = int(input("Please select Task Number you would like to edit: "))

    # for lineNumber, line in enumerate(lines)
    for lineNumber, line in enumerate(lines):

        # task_list is initialize to line.split(', ") that is putting comma and space in task_list
        task_list = line.split(", ")

        # if name is equal to task_list[0] that index [0]
        if task_num == lineNumber:
            # edit_option is initialized to the input of the options to be edited
            edit_option = input('''Would you like to:
                                               e - edit task
                                               c - mark complete
                                                -1- return to main menu\n''')
            # if edit_option is equal to 'e'
            if edit_option == 'e':
                # This is how you would refer to the fields
                if task_list[5].strip('\n') == 'No':
                    # edit is initialized to the input of what would you like to edit:
                    edit = input('''What would you like to edit:
                                                     u - username
                                                     d - due date\n''')
                    # if edit is equal to 'u':
                    if edit == "u":

                        # updating a field
                        task_list = line.split(", ")

                        # newUserName is initialized to the input of please input user
                        newUserName = input("Please input new user: ")

                        # replacing task_list[0] with newUserName in the line
                        line = line.replace(task_list[0], newUserName)

                        # displaying the content of line
                        print(line)

                        # lines[lineNumber - 1] = line
                        lines[lineNumber - 1] = line

                        # displaying lines
                        print(lines)

                        # data_to_file  is initialized to '\n'.join(lines)
                        data_to_file = '\n'.join(lines)

                        # print "date_to_file"
                        print(data_to_file)

                        # open task.txt to write using the file handle of new_task_file
                        new_task_file = open('tasks.txt', 'w+')

                        # writing new content to taxt.txt
                        new_task_file.write(data_to_file)

                    # if edit is equal to 'd'
                    if edit == "d":
                        # updating a field
                        task_list = line.split(", ")
                        # due_date is initialized input("Please input new due date: ")
                        due_date = input("Please input new due date: ")
                        # line is initil
                        line = line.replace(task_list[4], due_date)
                        # printing the content of line
                        print(line)
                        # lines[lineNumber - 1] is initialized to line
                        lines[lineNumber - 1] = line
                        # displaying the content of lines
                        print(lines)
                        # initializing 'data_to_file' to '\n'.join(lines)
                        data_to_file = '\n'.join(lines)
                        # displaying the content of data_to_file
                        print(data_to_file)
                        # opening task.txt to write a new content
                        new_task_file = open('tasks.txt', 'w+')
                        # writing 'data_to_file' to 'new_task_file'
                        new_task_file.write(data_to_file)

            # elif edit_option equal to 'c':
            elif edit_option == 'c':
                # This is how you would refer to the fields
                if task_list[5].strip('\n') == 'No':
                    # task_complete is initialized to the input of 'enter yes or no'
                    task_complete = input('enter yes or no: ')
                    # if task_complete is equal to 'Yes' or 'No'
                    if task_complete == "Yes" or "No":
                        # updating a field
                        task_list = line.split(", ")
                        # yes is initialized to the input of enter 'yes' or n'o'
                        yes = input("enter yes or no: ")
                        # replacing 'task_list' with yes
                        line = line.replace(task_list[-1], yes)
                        # printing the content of line
                        print(line)
                        # lines[lineNumber - 1] is initial line
                        lines[lineNumber - 1] = line
                        # display lines
                        print(lines)
                        # joining lines by initializing  data_to_file to "'\n'.join(lines)"
                        data_to_file = '\n'.join(lines)
                        # displaying (data_to_file)
                        print(data_to_file)
                        # opening tasks.txt using the handle new_task_file to write new content
                        new_task_file = open('tasks.txt', 'w+')
                        # wrinting the content of 'data_to_file' to 'new_task_file'
                        new_task_file.write(data_to_file)
                        # displaying 'successfully updated the file'
                        print('successfully updated the file')

# defining the function 'task_overview' with the parameter()
def task_overview():
    # if menu is equal to gr:
    if menu == 'gr':
        # opening 'task_overview.txt' as task, to read
        with open('task_overview.txt', 'r', encoding='utf-8') as task:
            # displaying '\nTASK OVERVIEW STATS:\n'
            print('\nTASK OVERVIEW STATS:\n')
            # for line in task
            for line in task:
                # display line.strip()
                print(line.strip())

        task_count = 0
        task_complete = 0
        uncompleted_tasks = 0
        overdue_tasks = 0

        # open and read the content of tasks.txt as task
        with open('tasks.txt', 'r+', encoding='utf-8') as task:
            # for line in task: task_list is initialize to line.split(', ')
            for line in task:
                # splitting the line of task and initialize it to task_list
                task_list = line.split(", ")

                datetime_object = datetime.datetime.strptime(task_list[4], '%Y-%m-%d')
                # task_count plus(+) equal to 1
                task_count += 1

                # if task_list at index position -1 strip new line character is equal to 'Yes'
                if task_list[-1].strip("\n") == 'Yes':
                    # task_complete is initialize to plus(+) equal 1
                    task_complete += 1

                # elif task_list at index position -1 strip new line character is equal to 'No'
                elif task_list[-1].strip("\n") == 'No':
                    # uncompleted_task is set to plus(+) equal 1
                    uncompleted_tasks += 1

                # if datetime_object is less than datetime.datetime.today and task_list at index position 5 strip new
                # line character is equal to 'No'
                if datetime_object < datetime.datetime.today() and task_list[5].strip("\n") == 'No':
                    # overdue_task is set to plus(+) equal 1
                    overdue_tasks += 1

            #  printing all the content of counter set above
            print(f"The number of tasks is: {task_count}")
            print(f"The number of complete tasks is: {task_complete}")
            print(f"The number of incomplete tasks is: {uncompleted_tasks}")
            print(f"The number of overdue tasks is: {overdue_tasks}")

            #  performing the calculation of the content
            percentage_incomplete = (uncompleted_tasks * 100) / task_count
            percentage_overdue = (overdue_tasks * 100) / task_count

            # Print / write everything to the file.
            task = open('tasks_overview.txt', 'w', encoding='utf-8')
            task.write(f"\nTotal number of tasks generated using Task Manager: {task_count}\n")
            task.write(f"Number of completed tasks: {task_complete}\n")
            task.write(f"Number of uncompleted tasks: {uncompleted_tasks}\n")
            task.write(f"Number of uncompleted tasks that are overdue: {overdue_tasks:.0f}\n")
            task.write(f"Percentage of uncompleted tasks: {percentage_incomplete:.0f}%\n")
            task.write(f"Percentage of uncompleted overdue tasks: {percentage_overdue:.0f}%\n")

            # print new line
            print('\n')


#  defining the function user_overview
def user_overview():
    # opening and reading to user_overview as user
    with open('user_overview.txt', 'r') as user:
        # print the content of user overview state
        print('\nUSER OVERVIEW STATS:\n')
        # for line in user
        for line in user:
            # print line.strip
            print(line.strip())

    # Print / write everything to the file.
    user_over = open('user_overview.txt', 'w', encoding='utf-8')

    # open and reading from users.txt as username
    with open('user.txt', 'r+', encoding='utf-8') as user:
        # for line in task: task_list is initialize to line.split(', ')
        for line in user:

            # setting all the content counter to zero(0)
            task_count = 0
            task_complete = 0
            uncompleted_user = 0
            overdue_user = 0
            # splitting the line of user and initialize it to user_list
            user_list = line.split(", ")
            # open and read the content of tasks.txt
            with open('tasks.txt', 'r') as task:
                # line in username
                for line in task:
                    # splitting the line of task and initialize it to task_list
                    task_list = line.split(", ")
                    # if user_list at position 0 is equal to task_list position 0
                    if user_list[0] == task_list[0]:
                        # task_list is plus(+) equal to 0
                        task_count += 1

                        # getting the datetime object
                        datetime_object = datetime.datetime.strptime(task_list[4], '%Y-%m-%d')

                        # if task_list at index position -1 strip new line character is equal to 'Yes'
                        if task_list[-1].strip("\n") == 'Yes':
                            # task_complete is initialize to plus(+) equal 1
                            task_complete += 1

                        # elif task_list at index position -1 strip new line character is equal to 'No'
                        elif task_list[-1].strip("\n") == 'No':
                            # uncompleted_task is set to plus(+) equal 1
                            uncompleted_user += 1

                            # if datetime_object is less than datetime.datetime.today and task_list at index position
                            # 5 strip new line character is equal to 'No'
                            if datetime_object < datetime.datetime.today() and task_list[5].strip("\n") == 'No':
                                # overdue_task is set to plus(+) equal 1
                                overdue_user += 1

                    print(f'A task assigned to {user_list[0]} is: {task_list[2]}')
            print('\n')
            print(f'The user {user_list[0]} has {task_count} tasks')
            print(f"This is how the datetime returns the date object {datetime.datetime.today()}")

            # any user with zero(0) task assign to will be display without any error message
            if task_count != 0:

                # performing the calculation of the content
                percentage_incomplete = (uncompleted_user / task_count) * 100
                percentage_overdue = (overdue_user / task_count) * 100
                percentage_of_tasks = (task_count / task_count) * 100
                percentage_completed = (task_complete / task_count) * 100

            # Print / write everything to the file.
            user_over.write(f"\nThe total number of tasks that have been generated and tracked using the "
                            f"task_manager.py are: {task_count}\n")
            user_over.write(f"The total number of tasks assigned to the user: {task_complete}\n")
            user_over.write(f"The percentage of the total number of tasks that have been assigned to the user: "
                            f"{percentage_of_tasks}%\n")
            user_over.write(f"The percentage of the tasks that have assigned to the user that have been completed: "
                            f"{percentage_completed:.0f}%\n")
            user_over.write(f"The percentage of the tasks assigned to the user that must still be completed: "
                            f"{percentage_incomplete:.0f}%\n")
            user_over.write(f"The percentage of the tasks assigned to the user that have not been completed and are "
                            f"overdue: {percentage_overdue:.0f}%\n")
    # closing user_over
    user_over.close()


# defining the function 'display_statistics'
def display_statistics():
    # if menu equal
    if menu == 'ds':
        # open task_overview.txt and read the content then initialize it to task_list
        task_list = open('tasks_overview.txt', 'r', encoding='utf-8')

        # task_list is initialize to task_list.read which is reading the content of task_list
        task_list = task_list.read()

        # displaying the content of task_list
        print(task_list)

        # open user_overview.txt and read the content then initialize it to user_list
        user_list = open('user_overview.txt', 'r', encoding='utf-8')

        # user_list is initialize to user_list.read which is reading the content of user_list
        user_list = user_list.read()

        # displaying the content of task_list
        print(user_list, "\n")


# open and reading from users.txt as username
with open('user.txt', 'r') as username:
    # line in username
    for line in username:
        # username , password is initialize to line.split(", ") which is putting new line character in all the comma
        # and space (,) in username and password.
        username, password = line.split(",")

        # strip removes leading/trailing whitespaces
        users[username.strip()] = password.strip()

# getting the username from the user through the keyboard
name = input("Enter your username:\n")

# while name not in users
while not name in users:
    # display username incorrect.
    print("Username incorrect.")

    # getting the username valid from the user through the keyboard
    name = input("Enter a valid username:\n")

# if name in users:
if name in users:
    # display username correct.
    print("Username correct")

# open and reading from users.txt as password
with open('user.txt', 'r') as password:
    # for line in password:
    for line in password:
        # username , password is initialize to line.split(", ") which is putting new line character in all the comma
        # and space (,) in username and password
        username, password = line.split(",")

        # strip removes leading/trailing whitespaces
        users[password.strip()] = username.strip()

# getting the password from the user through the keyboard
password = input("Enter your password:\n")

# while password not in users:
while not password in users[name]:
    # display your username is correct but your password is incorrect.
    print("Your username is correct but your password is incorrect.")

    # getting the valid password from the user through the keyboard
    password = input("Enter a valid password:\n")

# initializing menu to None
menu = None
while 1:
    # if name is equal to 'admin':
    if name == 'admin':

        # menu is initialize to all the string in task task.txt
        menu = (input(
            "\nSelect one of the following options:\nr - register user\na - add task\nva - view all tasks\nvm - "
            "view my tasks\ngr - generate report\nds - statistics\ne - exit\n"))

    # elif menu is not equal to 'admin':
    elif menu != 'admin':
        # menu is initialized to all the string in the task text
        menu = (input(
            "\nSelect one of the following options:\nr - register user\na - add task\nva - view all tasks\nvm - "
            "view my tasks\ne - exit\n"))

    # if menu is equal to 'r' or menu  is equal 'R'
    if menu == "r" or menu == "R":
        # calling the function reg_user
        reg_user()
    # elif menu is equal to 'a' or menu is equal to 'A'
    elif menu == "a" or menu == "A":
        # calling the function add_task
        add_task()
    # elif menu is equal to 'va' or menu is equal to 'VA'
    elif menu == "va" or menu == "VA":
        # calling the function view_all
        view_all()
    # elif menu is equal to 'vm' or menu is equal to 'VM'
    elif menu == "vm" or menu == "VM":
        # calling the function view_mine
        view_mine()
    # elif menu is equal 'gr'
    if menu == 'gr':
        # calling the function task_overview
        task_overview()
    # elif menu is equal to 'gr'
    if menu == 'gr':
        # calling the function user_overview
        user_overview()
    # elif menu is equal to 'ds'
    if menu == 'ds':
        # calling the function display_statistics
        display_statistics()
    # elif menu is equal to 'e'
    if menu == 'e':
        # exit menu
        exit()
