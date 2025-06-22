import pandas as pd

# Step 1: Read the messy CSV
df = pd.read_csv('netflix1.csv')

# Step 2: Check the first few rows
print("Original Data:")
print(df.head())

# Step 3: Remove duplicates
df = df.drop_duplicates()

# Step 4: Handle missing values
df = df.fillna('Unknown')   # You can use dropna() if you prefer dropping

# Step 5: Fix column names
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

# Step 6: Save the cleaned file
df.to_csv('cleaned_data.csv', index=False)

print("✅ Data cleaned and saved as 'cleaned_data.csv'")
