import streamlit as st
import functions


todos = functions.get_todos()

st.title('My Todo App')
st.subheader('This is my todo app')
st.write('this app is to increase productivity')


for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter todo:",placeholder='Add new todo...')