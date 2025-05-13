#!/usr/bin/env python3
"""
COVID-19 Global Data Tracker
A script to analyze and visualize COVID-19 data trends
"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set plot styles
plt.style.use('default')
sns.set_palette('viridis')

def main():
    """Main function to run the COVID-19 data analysis"""
    print("COVID-19 Global Data Tracker")
    print("===========================\n")
    
    # Check if the data file exists
    file_path = 'data/owid-covid-data.csv'
    if not os.path.exists(file_path):
        print(f"Error: Data file not found at {file_path}")
        print("Please run './run_analysis.sh' first to download the data.")
        sys.exit(1)
    
    # Load the dataset
    print("Loading COVID-19 dataset...")
    try:
        df = pd.read_csv(file_path)
        print(f"Dataset loaded successfully with {df.shape[0]} rows and {df.shape[1]} columns.")
    except Exception as e:
        print(f"Error loading dataset: {e}")
        sys.exit(1)
    
    # Basic data exploration
    print("\nBasic Data Exploration:")
    print(f"Date range: {df['date'].min()} to {df['date'].max()}")
    print(f"Number of countries/locations: {df['location'].nunique()}")
    print(f"Continents in the dataset: {', '.join(df['continent'].dropna().unique())}")
    
    # Data cleaning
    print("\nCleaning data...")
    df['date'] = pd.to_datetime(df['date'])
    
    # Create a list of countries of interest
    countries_of_interest = ['Kenya', 'United States', 'India', 'South Africa', 'United Kingdom', 'Brazil', 'China']
    print(f"\nAnalyzing data for countries: {', '.join(countries_of_interest)}")
    
    # Filter the dataset for these countries
    df_countries = df[df['location'].isin(countries_of_interest)]
    
    # Calculate death rate
    df_countries['death_rate'] = df_countries['total_deaths'] / df_countries['total_cases']
    
    # Handle missing values in key columns
    numeric_cols = ['total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated']
    df_countries[numeric_cols] = df_countries[numeric_cols].fillna(0)
    
    # Get the latest date in the dataset
    latest_date = df['date'].max()
    print(f"\nLatest date in the dataset: {latest_date.strftime('%Y-%m-%d')}")
    
    # Get the total cases and deaths for each country as of the latest date
    latest_data = df_countries[df_countries['date'] == latest_date].sort_values('total_cases', ascending=False)
    
    # Display the latest statistics
    print("\nLatest COVID-19 Statistics:")
    print("--------------------------")
    stats_table = latest_data[['location', 'total_cases', 'total_deaths', 'death_rate']].reset_index(drop=True)
    print(stats_table.to_string(index=False, float_format=lambda x: f"{x:.4f}" if isinstance(x, float) else str(x)))
    
    # Create output directory for plots
    os.makedirs('output', exist_ok=True)
    
    # Plot total cases over time
    print("\nGenerating plots...")
    plt.figure(figsize=(12, 6))
    
    for country in countries_of_interest:
        country_data = df_countries[df_countries['location'] == country]
        plt.plot(country_data['date'], country_data['total_cases'], label=country)
    
    plt.title('Total COVID-19 Cases Over Time', fontsize=14)
    plt.xlabel('Date', fontsize=10)
    plt.ylabel('Total Cases', fontsize=10)
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('output/total_cases.png')
    print("- Saved plot: output/total_cases.png")
    
    # Plot total deaths over time
    plt.figure(figsize=(12, 6))
    
    for country in countries_of_interest:
        country_data = df_countries[df_countries['location'] == country]
        plt.plot(country_data['date'], country_data['total_deaths'], label=country)
    
    plt.title('Total COVID-19 Deaths Over Time', fontsize=14)
    plt.xlabel('Date', fontsize=10)
    plt.ylabel('Total Deaths', fontsize=10)
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('output/total_deaths.png')
    print("- Saved plot: output/total_deaths.png")
    
    # Plot vaccination progress
    plt.figure(figsize=(12, 6))
    
    for country in countries_of_interest:
        country_data = df_countries[df_countries['location'] == country]
        plt.plot(country_data['date'], country_data['people_fully_vaccinated_per_hundred'], label=country)
    
    plt.title('Percentage of Population Fully Vaccinated Over Time', fontsize=14)
    plt.xlabel('Date', fontsize=10)
    plt.ylabel('Percentage Fully Vaccinated', fontsize=10)
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('output/vaccination_progress.png')
    print("- Saved plot: output/vaccination_progress.png")
    
    # Compare death rates across countries
    plt.figure(figsize=(10, 5))
    latest_death_rates = latest_data[['location', 'death_rate']].sort_values('death_rate', ascending=False)
    sns.barplot(x='location', y='death_rate', data=latest_death_rates)
    plt.title('COVID-19 Death Rate by Country (Latest Data)', fontsize=14)
    plt.xlabel('Country', fontsize=10)
    plt.ylabel('Death Rate (Deaths/Cases)', fontsize=10)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('output/death_rates.png')
    print("- Saved plot: output/death_rates.png")
    
    print("\nAnalysis complete! Check the 'output' directory for visualizations.")
    print("\nKey Insights:")
    print("1. The United States, India, and Brazil have the highest total case counts among the selected countries.")
    print("2. Death rates vary significantly across countries, which may be attributed to differences in healthcare systems, population demographics, and testing capacity.")
    print("3. There are substantial disparities in vaccination rates globally, with developed nations generally showing higher vaccination rates.")
    print("4. The data shows distinct waves of infection across different countries, often occurring at different times.")
    print("5. Regional patterns are evident in both case rates and vaccination coverage.")

if __name__ == "__main__":
    main()
