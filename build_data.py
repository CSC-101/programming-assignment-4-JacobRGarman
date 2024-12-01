import county_demographics

from data import CountyDemographics


# Given county demographics in dictionary form, convert to an object.
# input: county demographics information as an inconsistently typed dictionary
# output: the county demographics information as a CountyDemographics object
#
# Note that this function assumes the dictionary is properly structured.
def convert_county(county) -> CountyDemographics:
    if 'Median Houseold Income' in county['Income']:
        county['Income']['Median Household Income'] =\
                county['Income']['Median Houseold Income']
        del county['Income']['Median Houseold Income']
    return CountyDemographics(
            county['Age'],
            county['County'],
            county['Education'],
            county['Ethnicities'],
            county['Income'],
            county['Population'],
            county['State']
        )


# To avoid reprocessing the full data set on multiple calls of get_data.
_converted = None


# This function retrieves the full demographics data set and converts
# it to store each entry as a CountyDemographics object.
# input: no input
# output: county information as a list of CountyDemographics objects
def get_data() -> list[CountyDemographics]:
    global _converted
    if not _converted:
       report = county_demographics.get_report()
       _converted = [convert_county(county) for county in report]
    return _converted