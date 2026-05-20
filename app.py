import streamlit as st
import sqlite3
import pandas as pd

from langchain_ollama import OllamaLLM

# Page title
st.title("SQL AI Assistant")

# Connect database
conn = sqlite3.connect("company.db")

# LLM
llm = OllamaLLM(model="llama3")

# User input
question = st.text_input(
    "Ask question about employee database"
)

if question:

    schema = """
    Table: employees

    Columns:
    id
    employee_name
    department
    salary
    experience
    """

    prompt = f"""
    You are an expert SQL generator.

    Database Schema:
    {schema}

    Rules:
    - Generate only SQLite SQL query
    - Do not explain anything
    - Only SELECT queries allowed

    User Question:
    {question}
    """

    # Generate SQL
    sql_query = llm.invoke(prompt)

    # Clean response
    sql_query = sql_query.replace("```sql", "")
    sql_query = sql_query.replace("```", "")
    sql_query = sql_query.strip()

    st.write("### Generated SQL")
    st.code(sql_query)

    try:

        # Execute SQL
        df = pd.read_sql_query(sql_query, conn)

        st.write("### Query Result")
        st.dataframe(df)

    except Exception as e:

        st.error(f"SQL Error: {e}")