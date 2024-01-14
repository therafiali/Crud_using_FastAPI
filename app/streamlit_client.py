from email import message
from logging import PlaceHolder
from altair import Literal
from numpy import place
from streamlit_js_eval import streamlit_js_eval
from ast import Pass
from operator import ge
from httpx import get
import streamlit as st
import requests
import json

BASE_URL = "http://127.0.0.1:8000"


def get_all_todos():
    """Get List of all Todos"""
    response = requests.get('http://127.0.0.1:8000/')
    res_json = response.json()
    res_str = json.dumps(res_json)
    return res_str


st.title("Todo App")

def createtodo():
    """create todo"""
    st.markdown("### Create Todo")
    title = st.text_input("Enter New Todo",placeholder="Read Book before Sleep")
    convert_str = str(title)
    # print("title_____________________________________",title,"_______________________",convert_str)
    if title:  # This will be True when the user enters some text
        response = requests.post(
            f"{BASE_URL}/addTodo", json={"id": new_id, "message": convert_str, "status": False})
        res_json = response.json()
        res_str = json.dumps(res_json)
        return "Todos Added Succesfully"
    if st.button("Add Todo"):
        streamlit_js_eval(js_expressions="parent.window.location.reload()")


app_string = get_all_todos()
app = json.loads(app_string)
max_id = app[0]['id']
for item in app:
    current_id = item['id']
    if current_id > max_id:
        max_id = current_id

new_id = max_id + 1

# new = createtodo()
new = createtodo()
if new:
    st.write(new)
    

def delete_todo():
    todo_id = st.number_input("Enter Todo ID to delete",step=1)
    todo_id = int(todo_id)  # Convert to integer to remove decimal point
    if st.button("Delete Todo"):
        response = requests.delete(f"{BASE_URL}/delete_todo/{todo_id}")
        if response.status_code == 200:
            streamlit_js_eval(js_expressions="parent.window.location.reload()")
            
st.markdown("### ___________________________________________________")

st.markdown("### Delete Todo")

def update_todo():
    st.markdown("### Edit Todo")
    todo_id = st.number_input("Enter Todo ID to Edit",step=1)
    message = st.text_input("Enter Todo",placeholder="Buy Milk")
    status = st.text_input("Enter Status",placeholder="True/False")
    # Example URL

    # Example data to be sent in the request body
    data = {
        "id": todo_id,
        "message": message,
        "status": status
    }
    if st.button("Edit Todo"):
        url = f"http://127.0.0.1:8000/update_todo/{todo_id}"
        streamlit_js_eval(js_expressions="parent.window.location.reload()")
    # Send PUT request
        response = requests.put(url, json=data)

        # Check the response
        if response.status_code == 200:
                streamlit_js_eval(js_expressions="parent.window.location.reload()")
        else:
            print(f"PUT request failed with status code: {response.status_code}")
            print(response.text)  # Print the response content for debugging purposes



# def edit_todo():
#     todo_id = st.number_input("Enter Todo ID to Edit",step=1)
#     todo_text = st.text_input("Enter Todo")
#     todo_status = st.text_input("Enter Status")
    
#     todo_id = int(todo_id)  # Convert to integer to remove decimal point
#     if st.button("Edit Todo"):
#         response = requests.put(
#             f"{BASE_URL}/update_todo/", json={"id": new_id, "message": todo_text, "status": todo_text})
#         if response.status_code == 200:
#             streamlit_js_eval(js_expressions="parent.window.location.reload()")



def show_todo():
    table_content = ""
    for i, item in enumerate(app):
        table_content += f"<tr><td style='border:1px solid black; padding:10px;'>{item['id']}</td><td style='border:1px solid black; padding:10px;'>{item['message']}</td><td style='border:1px solid black; padding:10px;'>{item['status']}</td></tr>"

    st.markdown(
        f"<table style='background-color:#D4F1F4; border:1px solid black; border-collapse: collapse; width:100%;'><tr><th>ID</th><th>Todo Message</th><th>Status</th></tr>{table_content}</table>", unsafe_allow_html=True)

# Run the Streamlit app
if __name__ == "__main__":
    delete_todo()
    update_todo()
    show_todo()
