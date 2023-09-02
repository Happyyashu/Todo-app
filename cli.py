import functions
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")
while True:
    user_action = input("Type add,show,edit,complete or exit: ")
    user_action = user_action.strip()

    # match user_action:
    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + '\n')

        # writing to files
        functions.write_todos(todos,'todos.txt')

    # case 'show' | 'display':
    elif user_action.startswith('show'):
        todos = functions.get_todos()

        if len(todos) == 0:
            print('No task in todo(please first add task in todos):')
        else:
            new_todos = [item.strip('\n') for item in todos]
            [print(i+1,"->",text.title()) for i,text in enumerate(new_todos)]
    # case 'edit':
    elif user_action.startswith('edit'):
        try:
            todos = functions.get_todos()
            item = int(user_action[5:])
            print(f"You selected item: {todos[item-1]} to change")
            print("Now enter the new item:")

            todos = functions.get_todos()
            todos[item-1] = input() + '\n'

            functions.write_todos(todos,'todos.txt')
            print('Success')
        except ValueError:
            print("Your command is not valid")
            continue

    # case 'complete':
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            todo_to_remove = todos[number-1].strip('\n')

            todos.pop(number-1)

            functions.write_todos(todos,'todos.txt')

            print(f"{todo_to_remove} is removed from the list")

        except IndexError:
            print(f"There is no item with that {number}")
            continue
    # case 'exit':
    elif user_action.startswith('exit'):
        break
    else:
        print("wrong input: please type 'add','show','edit' or 'exit':  ")



print('Bye')