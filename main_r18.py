import pandas as pd

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\monthly_deaths.csv"
df = pd.read_csv(file_path)

# Convert the 'date' column to datetime format if not already done
df['date'] = pd.to_datetime(df['date'])

# Create the subset before June 1846
before_handwashing = df[df['date'] < '1846-06-01']

# Create the subset after (including) June 1846
after_handwashing = df[df['date'] >= '1846-06-01']

# Display the first few rows of each subset to verify
print("Before handwashing:")
print(before_handwashing.head())

print("\nAfter handwashing:")
print(after_handwashing.head())
