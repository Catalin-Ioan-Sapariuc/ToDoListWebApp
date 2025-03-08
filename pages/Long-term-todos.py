import streamlit as st 
import sys

def get_todos(filepath='long_term_todos.txt'):
    with open(filepath,'r') as file:
            todos_local = file.readlines()
    return todos_local

def write_todos(todos_list, filepath='long_term_todos.txt'):
    with open(filepath,'w') as file:
            file.writelines(todos_list)
    return 0

todos = get_todos()

def add_todo():
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    write_todos(todos)

#st.subheader("This should be a cool to do app!")

st.write("This page is for you to add your long terms todos!")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key =todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label = "" , placeholder="Add a new todo ...", 
              on_change = add_todo, key ='new_todo')


#print("Hello! ")

#st.session_state