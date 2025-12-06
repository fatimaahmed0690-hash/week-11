import streamlit as st
from database_manager import DatabaseManager
from classes import User

db = DatabaseManager()

def main():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = User(username, password)
        if user.authenticate(db):
            st.success("Login successful")
        else:
            st.error("Invalid credentials")

    if st.button("Register"):
        user = User(username, password)
        if user.register(db):
            st.success("Registered successfully")
        else:
            st.warning("User already exists")
