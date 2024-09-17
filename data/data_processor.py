import pandas as pd
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('shipping_data.db')
cursor = conn.cursor()

# Load spreadsheet 0 and insert data
spreadsheet_0 = pd.read_excel('spreadsheet_0.xlsx')
spreadsheet_0.to_sql('shipping_data', conn, if_exists='append', index=False)

# Load spreadsheet 1 and 2
spreadsheet_1 = pd.read_excel('spreadsheet_1.xlsx')
spreadsheet_2 = pd.read_excel('spreadsheet_2.xlsx')

# Merge spreadsheet 1 and 2 based on the shipping identifier
merged_data = pd.merge(spreadsheet_1, spreadsheet_2, on='shipping_identifier')

# Process and insert data row by row
for index, row in merged_data.iterrows():
    # Extract the relevant data (e.g., product, quantity, origin, destination)
    product = row['product']
    quantity = row['quantity']
    origin = row['origin']
    destination = row['destination']

    # Insert the data into the database
    cursor.execute('''INSERT INTO shipping_data (product, quantity, origin, destination)
                      VALUES (?, ?, ?, ?)''', (product, quantity, origin, destination))

# Commit and close the database connection
conn.commit()
conn.close()
