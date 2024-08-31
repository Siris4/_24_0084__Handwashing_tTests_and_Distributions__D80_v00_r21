import pandas as pd

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\monthly_deaths.csv"
df = pd.read_csv(file_path)

# Add a new column 'pct_deaths' to calculate the percentage of deaths per birth for each row
df['pct_deaths'] = (df['deaths'] / df['births']) * 100

# Display the first few rows to verify the new column
print(df.head())

# Save the updated DataFrame back to a CSV file if needed
output_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\monthly_deaths_with_pct.csv"
df.to_csv(output_path, index=False)

print(f"Updated DataFrame saved to {output_path}")
