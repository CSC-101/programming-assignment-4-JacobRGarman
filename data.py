class CountyDemographics:
    # Initialize a new CountyDemographics object.
    # input: the county's age demographics data as a dictionary
    # input: the county's name as a string
    # input: the county's education demographics data as a dictionary
    # input: the county's ethnicities demographics data as a dictionary
    # input: the county's income demographics data as a dictionary
    # input: the county's population demographics data as a dictionary
    # input: the county's state as a string
    def __init__(self,
                  age: dict[str,float],
                  county: str,
                  education: dict[str,float],
                  ethnicities: dict[str,float],
                  income: dict[str,float],
                  population: dict[str,float],
                  state: str):
        self.age = age
        self.county = county
        self.education = education
        self.ethnicities = ethnicities
        self.income = income
        self.population = population
        self.state = state


    # Provide a developer-friendly string representation of the object.
    # input: CountyDemographics for which a string representation is desired.
    # output: string representation
    def __repr__(self):
        return 'CountyDemographics({}, {}, {}, {}, {}, {}, {})'.format(
                self.age,
                self.county,
                self.education,
                self.ethnicities,
                self.income,
                self.population,
                self.state
            )