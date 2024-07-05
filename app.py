import streamlit as st
import pandas as pd
import google.generativeai as genai
import sqlite3

# Configure Google Generative AI
GOOGLE_API_KEY = "ADD YOUR GEMINI API KEY"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def clean_sql_query(sql_query):
    sql_query = sql_query.strip().strip('sql').strip().strip()
    return sql_query

def main():
    st.set_page_config(page_title="SQL QUERY GEN", page_icon=":robot:")
    st.markdown(
        """
        <div style="text-align: center;">
        <h1>🌐 SQL QUERY GENERATOR</h1>
        <h3>SQL QUERIES IN A FLASH⚡</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("CSV File Data:")
        st.write(df)

        text_input = st.text_input("Enter your Query:")
        submit = st.button("GENERATE SQL Query")

        if submit:
            with st.spinner("GENERATING SQL QUERY"):
                template = """
                Based on the table columns {columns}, create a SQL query snippet using the below text:
                ...
                {text_input}
                ...
                I just want the SQL query and remove the backtick and sql
                """
                columns = ', '.join(df.columns)
                formatted_template = template.format(columns=columns, text_input=text_input)
                
                response = model.generate_content(formatted_template)
                sql_query = clean_sql_query(response.text)
                sql_query = sql_query.replace("table_name", "data")
                
                st.write("Generated SQL Query:")
                st.code(sql_query, language="sql")


if __name__ == "__main__":
    main()
