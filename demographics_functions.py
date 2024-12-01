class CountyDemographics:
    def __init__(self, county, age, population, education, ethnicities, income, state):
        self.county = county
        self.age = age
        self.population = population
        self.education = education
        self.ethnicities = ethnicities
        self.income = income
        self.state = state

# Function to filter counties with poverty level greater than a given threshold
def below_poverty_level_greater_than(data, threshold):
    return [entry for entry in data if entry.income.get('Persons Below Poverty Level', 0) > threshold]

# Function to filter counties with poverty level less than a given threshold
def below_poverty_level_less_than(data, threshold):
    return [entry for entry in data if entry.income.get('Persons Below Poverty Level', 0) < threshold]

# Function to filter counties with percentage of people with a Bachelor's degree or higher greater than a given threshold
def education_greater_than(data, threshold):
    return [entry for entry in data if entry.education.get("Bachelor's Degree or Higher", 0) > threshold]

# Function to filter counties with percentage of people with a Bachelor's degree or higher less than a given threshold
def education_less_than(data, threshold):
    return [entry for entry in data if entry.education.get("Bachelor's Degree or Higher", 0) < threshold]

# Function to filter counties with a certain ethnicity percentage greater than a given threshold
def ethnicity_greater_than(data, ethnicity, threshold):
    return [entry for entry in data if entry.ethnicities.get(ethnicity, 0) > threshold]

# Function to filter counties with a certain ethnicity percentage less than a given threshold
def ethnicity_less_than(data, ethnicity, threshold):
    return [entry for entry in data if entry.ethnicities.get(ethnicity, 0) < threshold]

# Function to calculate the total population based on the percentage of people with a Bachelor's Degree or Higher
def population_by_education(data):
    return sum(
        (entry.education.get("Bachelor's Degree or Higher", 0) / 100) * entry.population.get('2014 Population', 0)
        for entry in data
    )

# Function to calculate the total population for a specific ethnicity
def population_by_ethnicity(data, ethnicity):
    return sum(
        (entry.ethnicities.get(ethnicity, 0) / 100) * entry.population.get('2014 Population', 0)
        for entry in data
    )

# Function to calculate the total population of all counties
def population_total(data):
    return sum(entry.population.get('2014 Population', 0) for entry in data)