import todolist_with_data as tdd
while True:
    current_user_id = 0
    print('''=========================
Welcome to My To-Do-List
=========================''')
    print('''Please choose an action: 
1. Login
2. Signup
    ''')
    login_or_signup = input('Enter action: ')
    if login_or_signup == '2':
        print('Create a username:')
        username_create = input()
        print('Create a password: ')
        password_create = input()
        print('Confirm password: ')
        confirm_password = input()
        if password_create == confirm_password:
            tdd.User_xyz(username = username_create, password = password_create).save()
        else: 
            print('Passwords do not match!')

    elif login_or_signup == '1':
        print('Enter username:')
        username_login = input()
        username_check = tdd.User_xyz.get_or_none(tdd.User_xyz.username == username_login)
        if username_check is not None:
            print('Enter password:')
            password_login = input()
            
            user_password = tdd.User_xyz.get(tdd.User_xyz.username == username_login)
            print(user_password)
            current_user_id = user_password.id


            while True:
                if password_login == user_password.password:
                    print('''=============================
What would you like to do?
=============================''')
                    print('''--------------------
1. Add new todo list
2. Add new todo task
3. Update todo task
4. Delete task
5. Delete list
6. Exit
--------------------''')
                    user_input = input('Enter action: ')

                    if user_input == '1':
                        print('These are your current table(s): ')
                        for table in tdd.Todo_list.select().where(tdd.Todo_list.user == current_user_id):
                            print(f'{table.id}. {table.name}')

                        table_name = input('''
What would you like to name your table? ''')
                        tdd.Todo_list(name = table_name).save()
                        print('New table added! Time to get down and dirty!')

                    elif user_input == '2':
                        print('''============
Your Tables
============''')
                        for table in tdd.Todo_list.select().where(tdd.Todo_list.user == current_user_id):
                            print(f'{table.id}. {table.name}')

                        table_id = input('Which table id would you like to access? ')

                        task = input('Enter your task: ')
                        if task != "":
                            tdd.Todo_task(task = task, todo_list = table_id).save()
                            print('New todo added! Time to get to work!')
                        elif task == '':
                            print('Invalid task...')
                        

                    elif user_input == '3':
                        print('''============
Your Tables
============''')

                        for table in tdd.Todo_list.select().where(tdd.Todo_list.user == current_user_id):
                            print(f'{table.id}. {table.name}')

                        table_id = input('Choose a table to access: ')

                        print('Here are your tasks: ')

                        completion_symbol = "|/|"

                        for task in tdd.Todo_task.select():
                            if task.completed == False:
                                completion_symbol = '|X|' 
                            print(f'{task.id}. {completion_symbol} {task.task}')
                        
                        task_selection = input('Which task would you like to mark done? ')
                        t = tdd.Todo_task.update(completed = True).where(tdd.Todo_task.id == task_selection)
                        t.execute()
                        print('Congratualations on being productive!')

                    elif user_input == '4':
                        for table in tdd.Todo_list.select().where(tdd.Todo_list.user == current_user_id):
                            print(f'{table.id}. {table.name}')

                        print('Which table would you like to access?')
                        table_choice = input()

                        lists_of_tasks = tdd.Todo_task.select().where(tdd.Todo_task.todo_list == int(table_choice))

                        for x in lists_of_tasks:
                            print(f"{x.id}. {x.task}")
                            which_to_delete = input('Which task would you like to delete?: ')
                            tdd.Todo_task.delete().where(tdd.Todo_task.id == int(which_to_delete)).execute()

                    elif user_input == '5':
                        for table in tdd.Todo_list.select().where(tdd.Todo_list.user == current_user_id):
                            print(f'{table.id}. {table.name}')

                        print('Which table would you like to delete?')
                        table_choice = input()
                        tdd.Todo_list.delete().where(tdd.Todo_list.id == int(table_choice)).execute()

                    elif user_input == '6':
                        break

        else:
            print('Username not found!')
        
            

