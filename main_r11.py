import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load the CSV files
annual_deaths_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\annual_deaths_by_clinic.csv"
monthly_deaths_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\monthly_deaths.csv"

# Load the data into DataFrames
df_annual = pd.read_csv(annual_deaths_path)
df_monthly = pd.read_csv(monthly_deaths_path)

# Convert the 'date' column in the monthly data to datetime format
df_monthly['date'] = pd.to_datetime(df_monthly['date'])
df_monthly['year'] = df_monthly['date'].dt.year

# Filter the data for the years 1841 to 1849
annual_1840s = df_annual[(df_annual['year'] >= 1841) & (df_annual['year'] <= 1849)]
monthly_1840s = df_monthly[(df_monthly['year'] >= 1841) & (df_monthly['year'] <= 1849)]

# Group the monthly data by year and sum only the 'births' and 'deaths' columns
monthly_1840s_grouped = monthly_1840s.groupby('year')[['births', 'deaths']].sum()

# Prepare data for plotting
years = pd.date_range(start='1841-01-01', end='1849-12-31', freq='Y')
births = monthly_1840s_grouped['births'].tolist()
deaths = monthly_1840s_grouped['deaths'].tolist()

# Create a figure and a set of twin axes
fig, ax1 = plt.subplots()

# Plot the total number of births on the primary y-axis
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Births', color='tab:blue')
ax1.plot(years, births, color='tab:blue', marker='o', label='Births')
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.set_ylim(0, 4000)  # Scale the y-axis for births appropriately

# Format the x-axis with major year locators and minor month locators
ax1.xaxis.set_major_locator(mdates.YearLocator())
ax1.xaxis.set_minor_locator(mdates.MonthLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

# Customize tick parameters for major and minor ticks
ax1.tick_params(axis='x', which='major', length=10, width=2, labelsize=12)
ax1.tick_params(axis='x', which='minor', length=4, width=1, labelbottom=False)

# Create a secondary y-axis to plot the number of deaths
ax2 = ax1.twinx()
ax2.set_ylabel('Number of Deaths', color='tab:red')
ax2.plot(years, deaths, color='tab:red', marker='o', label='Deaths')
ax2.tick_params(axis='y', labelcolor='tab:red')
ax2.set_ylim(0, 600)  # Scale the y-axis for deaths appropriately

# Add title to the plot
plt.title('Total Births and Deaths during Childbirth in the 1840s')

# Save the plot to a file
output_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\births_deaths_1840s.png"
plt.savefig(output_path)

print(f"Plot saved to {output_path}")
