import pandas as pd

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\monthly_deaths.csv"
df = pd.read_csv(file_path)

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Add the 'pct_deaths' column if it doesn't already exist
df['pct_deaths'] = (df['deaths'] / df['births']) * 100

# Create the subset before June 1846
before_handwashing = df[df['date'] < '1846-06-01']

# Set the 'date' column as the index
before_handwashing.set_index('date', inplace=True)

# Calculate the 6-month rolling average for 'pct_deaths'
before_handwashing['6_month_rolling_avg'] = before_handwashing['pct_deaths'].rolling(window=6).mean()

# Display the resulting DataFrame
print(before_handwashing[['pct_deaths', '6_month_rolling_avg']].head(15))
