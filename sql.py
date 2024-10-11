import sqlite3
import pandas as pd # type: ignore
## Read Excel file into pandas dataframe
excel_file = 'UPITransactions.xlsx'
df = pd.read_excel(excel_file)

## Connect to SQLite
connection = sqlite3.connect("transaction.db")

# create a cursor object to insert record, create table
cursor = connection.cursor()

# Step 2: Convert TransactionDate column to string format to match SQLite format
df['TransactionDate'] = df['TransactionDate'].astype(str)
df['TransactionTime'] = df['TransactionTime'].astype(str)  # Convert time to string as well


# create the table
table_info = """
CREATE TABLE IF NOT EXISTS TRANSACTIONS (
    TransactionID TEXT,
    TransactionDate TEXT,  -- SQLite does not have a dedicated datetime type, store as TEXT
    Amount REAL,
    BankNameSent TEXT,
    BankNameReceived TEXT,
    RemainingBalance REAL,
    City TEXT,
    Gender TEXT,
    TransactionType TEXT,
    Status TEXT,
    TransactionTime TEXT,  -- Store as TEXT since it's a time
    DeviceType TEXT,
    PaymentMethod TEXT,
    MerchantName TEXT,
    Purpose TEXT,
    CustomerAge INTEGER,
    PaymentMode TEXT,
    Currency TEXT,
    CustomerAccountNumber INTEGER,
    MerchantAccountNumber INTEGER
);
"""
cursor.execute(table_info)

# Insert records from the DataFrame into the SQLite table
df.to_sql('TRANSACTIONS', connection, if_exists='append', index=False)

# Display the inserted records
print("The inserted records are:")
data = cursor.execute('SELECT * FROM TRANSACTIONS LIMIT 10')
for row in data:
    print(row)

# Commit the changes and close the connection
connection.commit()
connection.close()
print("Data successfully added to the SQLite database!")
