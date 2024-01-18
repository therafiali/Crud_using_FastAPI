# Import necessary libraries
from streamlit_js_eval import streamlit_js_eval
import streamlit as st
import requests
import json

# Define the base URL for the API
BASE_URL = "http://127.0.0.1:8000"

# Set the title of the Streamlit app
st.title("Todo App")

# Function to create a new todo


def createtodo():
    st.markdown("### ___________________________________________________")
    st.markdown("### Create Todo")  # Set the title of the section
    # Create a markdown box with a specific background color
    st.markdown("<div style='background-color: #097969; padding: 10px; border-radius: 10px;'>",
                unsafe_allow_html=True)
    
    title = st.text_input(
        "Enter New Todo", placeholder="Read Book before Sleep")  # Get input from user
    convert_str = str(title)  # Convert input to string
    if st.button("Add Todo"):  # If the "Add Todo" button is clicked
        if title:  # If the title is not empty
            # Send POST request to API to create new todo
            response = requests.post(
                f"{BASE_URL}/addTodo", json={"message": convert_str, "status": False})

            # res_json = response.json()  # Convert response to JSON
            # res_str = json.dumps(res_json)  # Convert JSON to string
            # Reload the page
            streamlit_js_eval(js_expressions="parent.window.location.reload()")
            st.success("Added Todo Successfully")  # Display success message




def delete_todo():
    st.markdown("### ___________________________________________________")
    st.markdown("### Delete Todo")
    # Create a markdown box with a specific background color
    st.markdown("<div style='background-color: #C41E3A; padding: 10px; border-radius: 10px;'>",
                unsafe_allow_html=True)
    todo_id = st.number_input(
        "Enter Todo ID to delete", step=1)  # Get input from user
    todo_id = int(todo_id)  # Convert input to integer
    if st.button("Delete Todo"):  # If the "Delete Todo" button is clicked
        # Send DELETE request to API to delete todo
        response = requests.delete(f"{BASE_URL}/delete_todo/{todo_id}")
        st.warning("Deleted Todo Succesfully!")
        if response:  # If the request was successful
            # Reload the page
            streamlit_js_eval(js_expressions="parent.window.location.reload()")





# Function to update a todo


def update_todo():
    """Edit todo"""
    # Create a markdown box with a specific background color
    st.markdown("### Edit Todo")  # Set the title of the section
    st.markdown("<div style='background-color: #ffc299; padding: 10px; border-radius: 10px;'>",
                unsafe_allow_html=True)
    todo_id = st.number_input("Enter Todo ID to Edit",
                              step=1)  # Get input from user
    # Get input from user
    message = st.text_input("Enter Todo", placeholder="Buy Milk")
    status = st.radio("Enter Status", ('False', 'True'))  # Get input from user
    status = True if status == 'True' else False  # Convert input to boolean

    data = {
        "id": todo_id,
        "message": message,
        "status": status
    }  # Create data for the PUT request

    if st.button("Edit Todo"):  # If the "Edit Todo" button is clicked
        # Create URL for the PUT request
        url = f"http://127.0.0.1:8000/update_todo/{todo_id}"
        response = requests.put(url, json=data)  # Send PUT request to API

        if response:  # If the request was successful
            # Reload the page
            streamlit_js_eval(js_expressions="parent.window.location.reload()")
            st.success("Todo Updated Successfully")  # Display success message
        else:  # If the request failed
            st.error(
                f"PUT request failed with status code: {response.status_code}")  # Display error message
            # Print the response content for debugging purposes
            print(response.text)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("### ___________________________________________________")

# Function to display all todos


def show_todo():
    # Create a markdown box with a specific background color
    st.markdown("<div style='background-color: #0096FF	; padding: 10px; border-radius: 10px;'>",
                unsafe_allow_html=True)
    # Set the title of the section
    st.markdown("## _______Here is yours Todos List________")
    table_content = ""  # Initialize the table content
    response = requests.get(f"{BASE_URL}/")
    app = response.json()
    for i, item in enumerate(app):  # For each todo in the list
        # Add a row to the table content
        table_content += f"<tr><td style='border:1px solid black; padding:10px;'>{item['id']}</td><td style='border:1px solid black; padding:10px;'>{item['message']}</td><td style='border:1px solid black; padding:10px;'>{item['status']}</td></tr>"

    # Display the table
    st.markdown(
        f"<table style='background-color:#D4F1F4; border:1px solid black; border-collapse: collapse; width:100%;'><tr><th>ID</th><th>Todo Message</th><th>Status</th></tr>{table_content}</table>", unsafe_allow_html=True)


# Run the Streamlit app
if __name__ == "__main__":
    createtodo()
    delete_todo()
    update_todo()
    show_todo()
