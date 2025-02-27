from data import CountyDemographics
from build_data import get_data

# Part 1
# Input: one parameter type `list[CountyDemographics]`
# Output: return total `2014 Population` across the set of counties
def population_total(counties: list[CountyDemographics]) -> int:
    total_population = 0
    for county in counties:
        total_population += county.population["2014 Population"]
    return total_population

# Part 2
# Input: two parameters type `list[CountyDemographics]` and a two-letter state abbreviation `states`
# Output: return corresponding county demographics
def filter_by_state(counties: list[CountyDemographics], states: str) -> list[CountyDemographics]:
    county_matches = []
    for county in counties:
        if county.state == states:
            county_matches.append(county)
    return county_matches

# Part 3
# Input: two parameters type `list[CountyDemographics]` and an `education_key` of interest
# Output: return the total population with corresponding education type `float`
def population_by_education(counties: list[CountyDemographics], education_key: str) -> float:
    total_population_by_education = 0
    for county in counties:
        education_population = county.population["2014 Population"] * (county.education.get(education_key, 0) / 100)
        total_population_by_education += education_population
    return total_population_by_education

# Input: two parameters type `list[CountyDemographics]` and an `ethnicity_key` of interest
# Output: return the total population with corresponding ethnicity type `float`
def population_by_ethnicity(counties: list[CountyDemographics], ethnicity_key: str) -> float:
    total_population_by_ethnicity = 0
    for county in counties:
        ethnicity_population = county.population["2014 Population"] * (county.ethnicities.get(ethnicity_key, 0) / 100)
        total_population_by_ethnicity += ethnicity_population
    return total_population_by_ethnicity

# Input: one parameter type `list[CountyDemographics]`
# Output: return the total population which are below the poverty level
def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total_population_below_poverty = 0
    for county in counties:
        below_poverty_population = county.population["2014 Population"] * (county.income.get("Persons Below Poverty Level", 0) / 100)
        total_population_below_poverty += below_poverty_population
    return total_population_below_poverty

# Part 4
# Input: two parameters type `list[CountyDemographics]` and an `education_key` of interest
# Output: return the percent of total population of corresponding education type `float`
def percent_by_education(counties: list[CountyDemographics], education_key: str) -> float:
    total_population = population_total(counties)
    total_educated = population_by_education(counties, education_key)
    return (total_educated / total_population) * 100 if total_population > 0 else 0

# Input: two parameters type `list[CountyDemographics]` and an `ethnicity_key` of interest
# Output: return the percent of total population with corresponding ethnicity type `float`
def percent_by_ethnicity(counties: list[CountyDemographics], ethnicity_key: str) -> float:
    total_population = population_total(counties)
    total_ethnicity = population_by_ethnicity(counties, ethnicity_key)
    return (total_ethnicity / total_population) * 100 if total_population > 0 else 0

# Input: one parameter type `list[CountyDemographics]`
# Output: return the percent of total population which are below the poverty level
def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total_population = population_total(counties)
    total_poverty = population_below_poverty_level(counties)
    return (total_poverty / total_population) * 100 if total_population > 0 else 0

# Part 5
# Input: three parameters type `list[CountyDemographics]`, an `education_key` of interest, and a threshold type `float`
# Output: return the county demographics of counties that are greater than the threshold of corresponding education
def education_greater_than(counties: list[CountyDemographics], education_key: str, threshold: float) -> list[CountyDemographics]:
    counties_greater_than = []
    for county in counties:
        if county.education.get(education_key) > threshold:
            counties_greater_than.append(county)
    return counties_greater_than

# Input: three parameters type `list[CountyDemographics]`, an `education_key` of interest, and a threshold type `float`
# Output: return the county demographics of counties that are less than the threshold of corresponding education
def education_less_than(counties: list[CountyDemographics], education_key: str, threshold: float) -> list[CountyDemographics]:
    counties_less_than = []
    for county in counties:
        if county.education.get(education_key) < threshold:
            counties_less_than.append(county)
    return counties_less_than

# Input: three parameters type `list[CountyDemographics]`, an `ethnicity_key` of interest, and a threshold type `float`
# Output: return the county demographics of counties that are greater than the threshold of corresponding ethnicity
def ethnicity_greater_than(counties: list[CountyDemographics], ethnicity_key: str, threshold: float) -> list[CountyDemographics]:
    counties_greater_than = []
    for county in counties:
        if county.ethnicities.get(ethnicity_key) > threshold:
            counties_greater_than.append(county)
    return counties_greater_than

# Input: three parameters type `list[CountyDemographics]`, an `ethnicity_key` of interest, and a threshold type `float`
# Output: return the county demographics of counties that are less than the threshold of corresponding ethnicity
def ethnicity_less_than(counties: list[CountyDemographics], ethnicity_key: str, threshold: float) -> list[CountyDemographics]:
    counties_less_than = []
    for county in counties:
        if county.ethnicities.get(ethnicity_key) < threshold:
            counties_less_than.append(county)
    return counties_less_than

# Input: two parameters type `list[CountyDemographics]` and a threshold type `float`
# Output: return the county demographics of counties that are greater than the threshold which are below poverty lvl
def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    counties_greater_than = []
    for county in counties:
        if county.income.get("Persons Below Poverty Level", 0) > threshold:
            counties_greater_than.append(county)
    return counties_greater_than

# Input: two parameters type `list[CountyDemographics]` and a threshold type `float`
# Output: return the county demographics of counties that are less than the threshold which are below poverty lvl
def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    counties_less_than = []
    for county in counties:
        if county.income.get("Persons Below Poverty Level", 0) < threshold:
            counties_less_than.append(county)
    return counties_less_than