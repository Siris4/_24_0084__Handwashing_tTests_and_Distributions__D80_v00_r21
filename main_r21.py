import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\monthly_deaths.csv"
df = pd.read_csv(file_path)

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Add the 'pct_deaths' column to calculate the percentage of deaths per birth
df['pct_deaths'] = (df['deaths'] / df['births']) * 100

# Create the subsets before and after June 1846
before_handwashing = df[df['date'] < '1847-06-01'].copy()
after_handwashing = df[df['date'] >= '1847-06-01'].copy()

# Set the 'date' column as the index for the before_handwashing subset
before_handwashing.set_index('date', inplace=True)

# Calculate the 6-month rolling average for 'pct_deaths'
before_handwashing['6_month_rolling_avg'] = before_handwashing['pct_deaths'].rolling(window=6).mean()

# Plot the data
plt.figure(figsize=(12, 6))

# Plot the actual death rates before and after handwashing
plt.plot(before_handwashing.index, before_handwashing['pct_deaths'], color='black', linestyle='--', label='Before Handwashing')
plt.plot(after_handwashing['date'], after_handwashing['pct_deaths'], color='skyblue', linestyle='-', label='After Handwashing')

# Plot the 6-month rolling average death rate
plt.plot(before_handwashing.index, before_handwashing['6_month_rolling_avg'], color='crimson', linestyle='-', linewidth=2, label='6m Moving Average')

# Add labels, title, and legend
plt.xlabel('Year')
plt.ylabel('Percentage of Deaths', color='tab:red')
plt.title('Monthly Death Rate Before and After Handwashing')
plt.legend()

# Add gridlines
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Save the plot to a file
output_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\death_rate_chart.png"
plt.savefig(output_path)

print(f"Plot saved to {output_path}")

# Display the plot
plt.show()
