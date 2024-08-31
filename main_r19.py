import pandas as pd

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\monthly_deaths.csv"
df = pd.read_csv(file_path)

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Add the 'pct_deaths' column if it doesn't already exist
df['pct_deaths'] = (df['deaths'] / df['births']) * 100

# Create the subsets before and after June 1846
before_handwashing = df[df['date'] < '1846-06-01']
after_handwashing = df[df['date'] >= '1846-06-01']

# Calculate the average death rate before June 1846
avg_death_rate_before = before_handwashing['pct_deaths'].mean()

# Calculate the average death rate after June 1846
avg_death_rate_after = after_handwashing['pct_deaths'].mean()

# Print the average death rates
print(f"Average Death Rate Before June 1846: {avg_death_rate_before:.2f}%")
print(f"Average Death Rate After June 1846: {avg_death_rate_after:.2f}%")
