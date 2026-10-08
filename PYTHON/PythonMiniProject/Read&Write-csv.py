import pandas as pd
print(pd.__version__)

# Read CSV file
df = pd.read_csv("data.csv")

print("CSV Data:")
print(df)

new_row = {"Name": "Riya", "Age": 22, "City": "Kolkata"}
# Append row
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# Save back to CSV
df.to_csv("data.csv", index=False)
print("\nAfter Adding Row:\n", df)

# csv_data.to_excel("data_output.xlsx", index=False)
# print("Data written to data_output.xlsx")


# excel_data = pd.read_excel("data_output.xlsx")
# print("Excel Data:")
# print(excel_data)
