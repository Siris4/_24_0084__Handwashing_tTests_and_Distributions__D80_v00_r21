import pandas as pd

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\annual_deaths_by_clinic.csv"
df = pd.read_csv(file_path)

# Filter data for the year 1842
data_1842 = df[df['year'] == 1842]

# Calculate the death percentage for Clinic 1 and Clinic 2
clinic1_data = data_1842[data_1842['clinic'] == 'clinic 1']
clinic2_data = data_1842[data_1842['clinic'] == 'clinic 2']

# Calculate death percentage for Clinic 1
clinic1_deaths = clinic1_data['deaths'].values[0]
clinic1_births = clinic1_data['births'].values[0]
clinic1_death_percentage = (clinic1_deaths / clinic1_births) * 100

# Calculate death percentage for Clinic 2
clinic2_deaths = clinic2_data['deaths'].values[0]
clinic2_births = clinic2_data['births'].values[0]
clinic2_death_percentage = (clinic2_deaths / clinic2_births) * 100

# Print the results
print(f"Clinic 1 - 1842 Death Percentage: {clinic1_death_percentage:.2f}%")
print(f"Clinic 2 - 1842 Death Percentage: {clinic2_death_percentage:.2f}%")
