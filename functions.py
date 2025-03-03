def get_todos(filepath='todos.txt'):
    with open(filepath,'r') as file:
            todos_local = file.readlines()
    return todos_local

def write_todos(todos_list, filepath='todos.txt'):
    with open(filepath,'w') as file:
            file.writelines(todos_list)
    return 0