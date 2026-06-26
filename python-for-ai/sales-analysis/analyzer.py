import os

# Check if we are in the right folder
print("Current directory: ", os.getcwd())

# Check if our data file exists
data_path = "data/sales.csv"

if os.path.exists(data_path):
    print(f"File found! ✅ {data_path}")
else:
    print(f"File not found! ❌ {data_path}")
    print("Make sure you are running from the sales-analysis folder!")