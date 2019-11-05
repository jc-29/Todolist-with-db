import todolist_with_data as tdd
import migrate


print('''=============================
What would you like to do?
=============================''')
print('''---------------------
1. Add new todo list
2. Add new todo task
3. Update todo task
4. Exit
---------------------''')
user_input = input('Enter action: ')

if user_input == '1':
    table_name = input('What would you like to name your table? ')
    tdd.Todo_list(name = table_name).save()

elif user_input == '2':
    print('''============
Your Tables
============''')
    for table in tdd.Todo_list.select():
        print(f'{table.id}. {table.name}')

    table_id = input('Which table id would you like to access? ')

    task = input('Enter your task: ')
    if task != "":
        tdd.Todo_task(task = task, todo_list = table_id).save()
    elif task == '':
        print('Invalid task...')

elif user_input == '3':
    print('''============
Your Tables
============''')

    for table in tdd.Todo_list.select():
        print(f'{table.id}. {table.name}')

    table_id = input('Choose a table to access: ')

    print('Here are your tasks: ')

    completion_symbol = "/"

    for task in tdd.Todo_task.select():
        if task.completed == False:
            completion_symbol = '|X|' 
        print(f'{task.id}. {completion_symbol} {task.task}')
    
    task_selection = input('Which task would you like to mark done? ')
    # todo_task_list = tdd.Todo_task.select()
    # print(todo_task_list)
    t = tdd.Todo_task.update(completed = True).where(tdd.Todo_task.id == task_selection)
    t.execute()
    # tdd.Todo_task.update(completed = True).where(id == int(task_selection))


    # tdd.Todo_task.select().where(id == int(task_selection)).get().update(completed=True)



# elif user_input == '4':
