# COVID-19 Dataset Documentation

## Dataset Source
The dataset used in this project is from Our World in Data (OWID), which compiles COVID-19 data from various official sources including the World Health Organization (WHO), Johns Hopkins University, and national health ministries.

- **Source URL**: https://covid.ourworldindata.org/data/owid-covid-data.csv
- **Format**: CSV (Comma Separated Values)

## Key Columns

The dataset contains numerous columns. Here are the most important ones used in our analysis:

### Identifiers
- `iso_code`: ISO 3166-1 alpha-3 country code
- `continent`: Continent of the geographical location
- `location`: Geographical location (typically a country)
- `date`: Date of observation (YYYY-MM-DD format)

### Case Data
- `total_cases`: Total confirmed cases of COVID-19
- `new_cases`: New confirmed cases of COVID-19
- `new_cases_smoothed`: New confirmed cases of COVID-19 (7-day smoothed)
- `total_cases_per_million`: Total confirmed cases per million people
- `new_cases_per_million`: New confirmed cases per million people
- `new_cases_smoothed_per_million`: New confirmed cases per million people (7-day smoothed)

### Death Data
- `total_deaths`: Total deaths attributed to COVID-19
- `new_deaths`: New deaths attributed to COVID-19
- `new_deaths_smoothed`: New deaths attributed to COVID-19 (7-day smoothed)
- `total_deaths_per_million`: Total deaths attributed to COVID-19 per million people
- `new_deaths_per_million`: New deaths attributed to COVID-19 per million people
- `new_deaths_smoothed_per_million`: New deaths attributed to COVID-19 per million people (7-day smoothed)

### Hospitalization Data
- `icu_patients`: Number of COVID-19 patients in intensive care units (ICUs)
- `icu_patients_per_million`: Number of COVID-19 patients in ICUs per million people
- `hosp_patients`: Number of COVID-19 patients in hospitals
- `hosp_patients_per_million`: Number of COVID-19 patients in hospitals per million people

### Testing Data
- `total_tests`: Total tests for COVID-19
- `new_tests`: New tests for COVID-19
- `total_tests_per_thousand`: Total tests per thousand people
- `new_tests_per_thousand`: New tests per thousand people
- `positive_rate`: Share of COVID-19 tests that are positive (rolling 7-day average)
- `tests_per_case`: Tests conducted per new confirmed case (rolling 7-day average)

### Vaccination Data
- `total_vaccinations`: Total number of COVID-19 vaccination doses administered
- `people_vaccinated`: Total number of people who received at least one vaccine dose
- `people_fully_vaccinated`: Total number of people who received all doses prescribed by the initial vaccination protocol
- `total_boosters`: Total number of COVID-19 vaccination booster doses administered
- `new_vaccinations`: New COVID-19 vaccination doses administered
- `total_vaccinations_per_hundred`: Total number of COVID-19 vaccination doses administered per 100 people
- `people_vaccinated_per_hundred`: Total number of people who received at least one vaccine dose per 100 people
- `people_fully_vaccinated_per_hundred`: Total number of people who received all doses prescribed by the initial vaccination protocol per 100 people
- `total_boosters_per_hundred`: Total number of COVID-19 vaccination booster doses administered per 100 people

### Demographic Data
- `population`: Population in 2020
- `population_density`: Number of people divided by land area, measured in square kilometers
- `median_age`: Median age of the population
- `aged_65_older`: Share of the population that is 65 years and older
- `aged_70_older`: Share of the population that is 70 years and older
- `gdp_per_capita`: Gross domestic product at purchasing power parity
- `life_expectancy`: Life expectancy at birth in 2019

## Derived Metrics

In our analysis, we also calculate some derived metrics:

- `death_rate`: Calculated as `total_deaths / total_cases`, representing the case fatality rate

## Data Limitations

When working with this dataset, it's important to be aware of the following limitations:

1. **Reporting Differences**: Countries have different testing, reporting, and classification systems, which can affect comparability.
2. **Data Gaps**: Some countries may have incomplete or delayed reporting for certain metrics.
3. **Definition Changes**: Definitions of cases, deaths, and other metrics may have changed over time in some countries.
4. **Population Effects**: Raw numbers should be interpreted in the context of population size.

## Using the Data

This dataset is suitable for:
- Tracking the spread of COVID-19 across countries and time
- Comparing metrics like case counts, death rates, and vaccination progress
- Analyzing the relationship between demographic factors and COVID-19 outcomes
- Visualizing global and regional trends
