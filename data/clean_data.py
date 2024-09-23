import pandas as pd

# This script cleans the data from the Excel file 'august.xlsx' and saves the cleaned data to a new Excel file.
# The data is expected to be in a specific format with columns: 'DATE', 'RECEIPT NO', 'SUPPLIER', 'DETAILS', 'CODE', 'AMT(KSH)'.
# The script performs the following steps:

# Step 1: Load the Excel file
file_path = 'august.xlsx'  # Update this path to your actual file location
xls = pd.ExcelFile(file_path)

# Step 2: Load the specific sheet containing the data
df = pd.read_excel(xls, sheet_name='Sheet1')

# Step 3: Clean the data
# The actual data starts from the 3rd row, so we'll adjust the DataFrame accordingly
df_cleaned = df.iloc[2:, :].copy()

# Rename columns to the appropriate headers
df_cleaned.columns = ['DATE', 'RECEIPT NO', 'SUPPLIER', 'DETAILS', 'CODE', 'AMT(KSH)']

# Remove rows where 'CODE' is missing (if there are any invalid rows)
df_cleaned.dropna(subset=['CODE'], inplace=True)

# Step 4: Reorganize the columns
df_cleaned = df_cleaned[['DATE', 'CODE', 'SUPPLIER', 'DETAILS', 'RECEIPT NO', 'AMT(KSH)']]

# Step 5: Sort the data by 'CODE'
df_cleaned_sorted = df_cleaned.sort_values(by='CODE').reset_index(drop=True)

# Step 6: Save the cleaned and sorted data back to a new Excel file
output_file_path = 'Cleaned_August_2024_Expenses.xlsx'
df_cleaned_sorted.to_excel(output_file_path, index=False)

# Success Alert: only true when conversion is done. 
print(f"Data cleaned and saved to {output_file_path}")
