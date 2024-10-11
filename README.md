# Text-to-Sql-Query-Using-LLM
This project leverages Google Gemini AI to convert English language questions into SQL queries. It uses Streamlit for the frontend and SQLite for the backend to retrieve and display data from a database of UPI transactions. The AI interprets user input and generates SQL queries to fetch relevant data from the database.

## Project Structure
app.py: The main Streamlit app file that contains the frontend logic and Google Gemini AI interaction.
sql.py: Script to create and populate the SQLite database from an Excel file.
.env: Stores environment variables, including the Google API key for Gemini.
requirements.txt: Lists all the dependencies for the project.
UPITransactions.xlsx: The source Excel file containing UPI transaction data (not included in the repo).
