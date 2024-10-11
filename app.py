from dotenv import load_dotenv # type: ignore
load_dotenv() ## load all the environemnt variables

import streamlit as st # type: ignore
import os
import sqlite3

import google.generativeai as genai # type: ignore
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide sql queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the sql database

def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        rows = []
    finally:
        conn.commit()
        conn.close()
    return rows


## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name TRANSACTIONS and has the following columns - TRANSACTIONID, TRANSACTIONDATE, AMOUNT, BANKNAMESENT, BANKNAMERECEIVED, REMAININGBALANCE, CITY, GENDER,TRANSACTIONTYPE, STATUS, TRANSACTIONTIME, DEVICETYPE,PAYMENTMETHOD, MERCHANTNAME, PURPOSE, CUSTOMERAGE, PAYMENTMODE, CURRENCY, CUSTOMERACCOUNTNUMBER,MERCHANTACCOUNTNUMBER \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM UPI_TRANSACTIONS;
    \nExample 2 - Tell me how many transactions got successful?, 
    the SQL command will be something like this SELECT COUNT(*) FROM UPI_TRANSACTIONS  WHERE Status = "Success"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"transaction.db")
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)