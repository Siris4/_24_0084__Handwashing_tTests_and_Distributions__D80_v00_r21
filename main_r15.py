import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\annual_deaths_by_clinic.csv"
df = pd.read_csv(file_path)

# Filter data for clinic 1 and clinic 2
clinic1 = df[df['clinic'] == 'clinic 1']
clinic2 = df[df['clinic'] == 'clinic 2']

# Plot the number of deaths per year for both clinics
plt.figure(figsize=(10, 6))

plt.plot(clinic1['year'], clinic1['deaths'], label='Clinic 1', marker='o', color='skyblue', linewidth=2)
plt.plot(clinic2['year'], clinic2['deaths'], label='Clinic 2', marker='o', color='crimson', linewidth=2)

# Add labels, title, and legend
plt.xlabel('Year')
plt.ylabel('Number of Deaths')
plt.title('Number of Deaths per Year for Clinic 1 and Clinic 2')
plt.legend()

# Add gridlines
plt.grid(True, which='both', linestyle='--', color='gray', alpha=0.7)

# Save the plot to a file
output_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\deaths_per_year_clinics.png"
plt.savefig(output_path)

print(f"Plot saved to {output_path}")
