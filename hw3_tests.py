import data
import build_data
import unittest

from hw3 import (population_total, filter_by_state, population_by_education,
                 population_by_ethnicity, population_below_poverty_level, percent_by_education,
                 percent_by_ethnicity,percent_below_poverty_level, education_greater_than,
                 education_less_than, ethnicity_less_than, ethnicity_greater_than,
                 below_poverty_level_greater_than, below_poverty_level_less_than)

# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]

class TestCases(unittest.TestCase):
    pass

    # Part 1
    def test_population_total_standard(self):
        result = population_total(reduced_data)
        self.assertEqual(result, 655813)

    def test_population_total_some_counties(self):
        counties = [
            reduced_data[0],
            reduced_data[2],
            reduced_data[4]
        ]
        result = population_total(counties)
        self.assertEqual(result, 337100)

    # Part 2
    def test_filter_by_state_standard(self):
        ca_counties = filter_by_state(reduced_data, "CA")
        self.assertEqual(len(ca_counties), 2)
        county_names = {county.county for county in ca_counties}
        expected = {"San Luis Obispo County", "Yolo County"}
        self.assertEqual(county_names, expected)

    def test_filter_by_state_empty(self):
        result = filter_by_state(reduced_data, "XX")
        self.assertEqual(result, [])

    # Part 3
    def test_population_by_education_standard(self):
        result = population_by_education([reduced_data[0], reduced_data[1], reduced_data[2], reduced_data[3],
                                          reduced_data[4], reduced_data[5], reduced_data[6]],
                                         "Bachelor's Degree or Higher")
        expected = (
            float(55395 * 0.209) + # Autauga County
            float(61697 * 0.143) + # Crawford County
            float(279083 * 0.315) + # San Luis Obispo County
            float(207590 * 0.379) + # Yolo county
            float(2622 * 0.179) + # Butte County
            float(42225 * 0.152) + # Pettis County
            float(7201 * 0.172) # Weston County
        )
        self.assertAlmostEqual(result, expected, places=5)

    def test_population_by_education_some_counties(self):
        result = population_by_education([reduced_data[0], reduced_data[1]], "High School or Higher")
        expected = (
            float(55395 * 0.856) + # Autauga County
            float(61697 * 0.822) # Crawford County
        )
        self.assertAlmostEqual(result, expected, places=5)

    def test_population_by_ethnicity(self):
        result = population_by_ethnicity(reduced_data, "Asian Alone")
        expected = (
            float(55395 * 0.011) +  # Autauga County
            float(61697 * 0.016) +  # Crawford County
            float(279083 * 0.038) +  # San Luis Obispo County
            float(207590 * 0.138) +  # Yolo County
            float(2622 * 0.003) +  # Butte County
            float(42225 * 0.007) +  # Pettis County
            float(7201 * 0.004)  # Weston County
        )
        self.assertAlmostEqual(result, expected, places=5)

    def test_population_by_ethnicity_some_counties(self):
        result = population_by_ethnicity([reduced_data[2], reduced_data[3]], "Black Alone")
        expected = (
            float(279083 * 0.022) +  # San Luis Obispo County
            float(207590 * 0.03)  # Yolo County
        )
        self.assertAlmostEqual(result, expected, places=5)

    def test_population_below_poverty_level_standard(self):
        result = population_below_poverty_level(reduced_data)
        expected = (
            float(55395 * 0.121) +  # Autauga County
            float(61697 * 0.202) +  # Crawford County
            float(279083 * 0.143) +  # San Luis Obispo County
            float(207590 * 0.191) +  # Yolo County
            float(2622 * 0.157) +  # Butte County
            float(42225 * 0.184) +  # Pettis County
            float(7201 * 0.112)  # Weston County
        )
        self.assertAlmostEqual(result, expected, places=5)

    def test_population_below_poverty_level_some_counties(self):
        result = population_below_poverty_level([reduced_data[4], reduced_data[5], reduced_data[6]])
        expected = (
            float(2622 * 0.157) +  # Butte County
            float(42225 * 0.184) +  # Pettis County
            float(7201 * 0.112)  # Weston County
        )
        self.assertAlmostEqual(result, expected, places=5)

    # Part 4
    def test_percent_by_education_standard(self):
        counties = reduced_data
        education_key = "Bachelor's Degree or Higher"
        result = percent_by_education(counties, education_key)
        expected_total_population = 55395 + 61697 + 279083 + 207590 + 2622 + 42225 + 7201
        expected_total_educated = (
            float(55395 * 0.209) + # Autauga County
            float(61697 * 0.143) + # Crawford County
            float(279083 * 0.315) + # San Luis Obispo County
            float(207590 * 0.379) + # Yolo County
            float(2622 * 0.179) + # Butte County
            float(42225 * 0.152) + # Pettis County
            float(7201 * 0.172) # Weston County
        )
        expected = expected_total_educated / expected_total_population * 100
        self.assertAlmostEqual(result, expected, places=5)

    def test_percent_by_education_some_counties(self):
        counties = [reduced_data[0], reduced_data[2], reduced_data[4]]
        education_key = "Bachelor's Degree or Higher"
        result = percent_by_education(counties, education_key)
        expected_total_population = 55395 + 279083 + 2622
        expected_total_educated = (
            float(55395 * 0.209) + # Autauga County
            float(279083 * 0.315) + # San Luis Obispo County
            float(2622 * 0.179) # Butte County
        )
        expected = expected_total_educated / expected_total_population * 100
        self.assertAlmostEqual(result, expected, places=5)

    def test_percent_by_ethnicities_standard(self):
        counties = reduced_data
        education_key = "Asian Alone"
        result = percent_by_ethnicity(counties, education_key)
        expected_total_population = 55395 + 61697 + 279083 + 207590 + 2622 + 42225 + 7201
        expected_total_educated = (
            float(55395 * 0.011) +  # Autauga County
            float(61697 * 0.016) +  # Crawford County
            float(279083 * 0.038) +  # San Luis Obispo County
            float(207590 * 0.138) +  # Yolo County
            float(2622 * 0.003) +  # Butte County
            float(42225 * 0.007) +  # Pettis County
            float(7201 * 0.004)  # Weston County
        )
        expected = expected_total_educated / expected_total_population * 100
        self.assertAlmostEqual(result, expected, places=5)

    def test_percent_below_poverty_level_standard(self):
        counties = reduced_data
        result = percent_below_poverty_level(counties)
        expected_total_population = 55395 + 61697 + 279083 + 207590 + 2622 + 42225 + 7201
        expected_total_impoverished = (
                float(55395 * 0.121) +  # Autauga County
                float(61697 * 0.202) +  # Crawford County
                float(279083 * 0.143) +  # San Luis Obispo County
                float(207590 * 0.191) +  # Yolo County
                float(2622 * 0.157) +  # Butte County
                float(42225 * 0.184) +  # Pettis County
                float(7201 * 0.112)  # Weston County
        )
        expected = expected_total_impoverished / expected_total_population * 100
        self.assertAlmostEqual(result, expected, places=5)

    # Part 5
    def test_education_greater_than_standard(self):
        counties = reduced_data
        result = education_greater_than(counties, "Bachelor's Degree or Higher", 30.0)
        expected = [reduced_data[2], reduced_data[3]]
        self.assertEqual(result, expected)

    def test_education_less_than_standard(self):
        counties = reduced_data
        result = education_less_than(counties, "Bachelor's Degree or Higher", 15.0)
        expected = [reduced_data[1]]
        self.assertEqual(result, expected)

    def test_ethnicity_greater_than_standard(self):
        counties = reduced_data
        result = ethnicity_greater_than(counties, "Asian Alone", 10.0)
        expected = [reduced_data[3]]
        self.assertEqual(result, expected)

    def test_ethnicity_less_than_standard(self):
        counties = reduced_data
        result = ethnicity_less_than(counties, "Asian Alone", 1.0)
        expected = [reduced_data[4], reduced_data[5], reduced_data[6]]
        self.assertEqual(result, expected)

    def test_percent_below_poverty_level_greater_than_standard(self):
        counties = reduced_data
        result = below_poverty_level_greater_than(counties, 20.0)
        expected = [reduced_data[1]]
        self.assertEqual(result, expected)

    def test_percent_below_poverty_level_less_than_standard(self):
        counties = reduced_data
        result = below_poverty_level_less_than(counties, 15.0)
        expected = [reduced_data[0], reduced_data[2], reduced_data[6]]
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()
