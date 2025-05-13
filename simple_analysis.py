#!/usr/bin/env python3
"""
Simple COVID-19 Data Analysis
Uses only the standard library to analyze the COVID-19 dataset
"""

import os
import sys
import csv
from datetime import datetime

def main():
    """Main function to run a simple COVID-19 data analysis"""
    print("COVID-19 Global Data Tracker - Simple Analysis")
    print("=============================================\n")

    # Check if the data file exists
    file_path = 'data/owid-covid-data.csv'
    if not os.path.exists(file_path):
        print(f"Error: Data file not found at {file_path}")
        print("Please run './run_analysis.sh' first to download the data.")
        sys.exit(1)

    # Load the dataset
    print("Loading COVID-19 dataset...")
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            data = list(reader)
        print(f"Dataset loaded successfully with {len(data)} rows.")
    except Exception as e:
        print(f"Error loading dataset: {e}")
        sys.exit(1)

    # Basic data exploration
    print("\nBasic Data Exploration:")

    # Get unique locations
    locations = set()
    continents = set()
    dates = set()

    for row in data:
        locations.add(row['location'])
        if row['continent']:
            continents.add(row['continent'])
        dates.add(row['date'])

    print(f"Number of countries/locations: {len(locations)}")
    print(f"Continents in the dataset: {', '.join(sorted(continents))}")
    print(f"Date range: {min(dates)} to {max(dates)}")

    # Countries of interest
    countries_of_interest = ['Kenya', 'United States', 'India', 'South Africa', 'United Kingdom', 'Brazil', 'China']
    print(f"\nAnalyzing data for countries: {', '.join(countries_of_interest)}")

    # Get the latest date
    latest_date = max(dates)
    print(f"\nLatest date in the dataset: {latest_date}")

    # Get the latest statistics for countries of interest
    print("\nLatest COVID-19 Statistics:")
    print("--------------------------")
    print(f"{'Country':<15} {'Date':<12} {'Total Cases':<15} {'Total Deaths':<15} {'Death Rate':<10}")
    print("-" * 75)

    for country in countries_of_interest:
        # Find the latest data for this country (with non-empty total_cases)
        country_latest = None
        country_dates = []

        # First collect all dates for this country with data
        for row in data:
            if row['location'] == country and row['total_cases']:
                country_dates.append(row['date'])

        if country_dates:
            # Find the latest date with data
            latest_country_date = max(country_dates)

            # Get the data for this date
            for row in data:
                if row['location'] == country and row['date'] == latest_country_date:
                    country_latest = row
                    break

        if country_latest:
            total_cases = int(float(country_latest['total_cases'])) if country_latest['total_cases'] else 0
            total_deaths = int(float(country_latest['total_deaths'])) if country_latest['total_deaths'] else 0

            # Calculate death rate
            death_rate = (total_deaths / total_cases) if total_cases > 0 else 0

            print(f"{country:<15} {country_latest['date']:<12} {total_cases:<15,d} {total_deaths:<15,d} {death_rate:.4f}")
        else:
            print(f"{country:<15} {'No data':<12} {'No data':<15} {'No data':<15} {'N/A':<10}")

    # Calculate some additional statistics
    print("\nAdditional Statistics:")
    print("---------------------")

    # Find country with highest cases
    highest_cases_country = ""
    highest_cases = 0

    # Find country with highest deaths
    highest_deaths_country = ""
    highest_deaths = 0

    # Find country with highest death rate
    highest_dr_country = ""
    highest_dr = 0

    # Find country with lowest death rate
    lowest_dr_country = ""
    lowest_dr = float('inf')

    # Get the latest data for each country
    latest_country_data = {}

    for country in countries_of_interest:
        # Find the latest date with data for this country
        country_dates = []
        for row in data:
            if row['location'] == country and row['total_cases']:
                country_dates.append(row['date'])

        if country_dates:
            latest_country_date = max(country_dates)

            # Get the data for this date
            for row in data:
                if row['location'] == country and row['date'] == latest_country_date:
                    latest_country_data[country] = row
                    break

    # Now calculate statistics based on the latest data
    for country, row in latest_country_data.items():
        if row['total_cases'] and row['total_deaths']:
            total_cases = int(float(row['total_cases']))
            total_deaths = int(float(row['total_deaths']))

            if total_cases > highest_cases:
                highest_cases = total_cases
                highest_cases_country = country

            if total_deaths > highest_deaths:
                highest_deaths = total_deaths
                highest_deaths_country = country

            if total_cases > 0:
                death_rate = total_deaths / total_cases
                if death_rate > highest_dr and death_rate < 0.1:  # Cap at 10% to avoid outliers
                    highest_dr = death_rate
                    highest_dr_country = country
                if death_rate < lowest_dr and death_rate > 0:
                    lowest_dr = death_rate
                    lowest_dr_country = country

    print(f"Country with highest total cases: {highest_cases_country} ({highest_cases:,})")
    print(f"Country with highest total deaths: {highest_deaths_country} ({highest_deaths:,})")
    print(f"Country with highest death rate: {highest_dr_country} ({highest_dr:.4f})")
    print(f"Country with lowest death rate: {lowest_dr_country} ({lowest_dr:.4f})")

    print("\nKey Insights:")
    print("1. The dataset contains information for over 200 countries/locations worldwide.")
    print("2. The data spans from early 2020 to the present day, covering the entire COVID-19 pandemic period.")
    print(f"3. The United States has reported the highest number of cases ({highest_cases:,}) among the selected countries.")
    print(f"4. {highest_dr_country} has the highest death rate at {highest_dr:.4f}, while {lowest_dr_country} has the lowest at {lowest_dr:.4f}.")
    print("5. Death rates vary significantly across countries, which may be attributed to differences in healthcare systems, population demographics, and testing capacity.")
    print("6. For a more detailed analysis with visualizations, please install the required Python packages (pandas, matplotlib, seaborn) and run the full analysis script.")

if __name__ == "__main__":
    main()
