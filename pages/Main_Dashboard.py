import streamlit as st
from database_manager import DatabaseManager
from classes import SecurityIncident, Dataset
import pandas as pd

db = DatabaseManager()

def main():
    st.title("Main Dashboard")
    incidents = SecurityIncident.fetch_all(db)

    if incidents:
        ds = Dataset(incidents)
        st.dataframe(ds.data)
    else:
        st.warning("No incident records found")
