# COVID-19 Global Data Tracker
    
A data analysis project that tracks global COVID-19 trends, including cases, deaths,recoveries, and vaccinations across countries and time.

## Project Overview 
 
This project analyzes real-world COVID-19 data to:
- Track the spread of COVID-19 across different countries
- Compare metrics like case counts, death rates, and vaccination progress
- Visualize trends using various charts and maps
- Generate insights about the global pandemic response

## Data Source

The project uses the Our World in Data COVID-19 dataset, which provides comprehensive data on COVID-19 cases, deaths, testing, hospitalizations, and vaccinations for countries worldwide.

- Dataset: [Our World in Data COVID-19 Dataset](https://covid.ourworldindata.org/data/owid-covid-data.csv)

### Key Columns

The dataset contains numerous columns including:

- `date`: Date of observation
- `location`: Country or region
- `total_cases`: Total confirmed cases of COVID-19
- `total_deaths`: Total deaths attributed to COVID-19
- `new_cases`: New confirmed cases of COVID-19
- `new_deaths`: New deaths attributed to COVID-19
- `total_vaccinations`: Total number of COVID-19 vaccination doses administered
- `people_vaccinated`: Total number of people who received at least one vaccine dose
- `people_fully_vaccinated`: Total number of people who received all doses prescribed

For a complete documentation of all columns, see `data/DATASET_DOCUMENTATION.md`.

## Tools and Libraries Used

This project utilizes the following tools and libraries:

- **Python**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib & Seaborn**: Data visualization
- **Plotly**: Interactive visualizations and choropleth maps
- **Jupyter Notebook**: Interactive computing environment
- **GeoPandas**: Geospatial data handling (for advanced mapping)

## Project Structure

```
COVID-19 Global Data Tracker/
├── data/
│   ├── owid-covid-data.csv       # COVID-19 dataset from Our World in Data
│   └── DATASET_DOCUMENTATION.md  # Detailed documentation of dataset columns
├── notebooks/
│   └── COVID19_Global_Data_Analysis.ipynb  # Main analysis notebook
├── analyze_covid_data.py         # Python script for comprehensive analysis
├── simple_analysis.py            # Simple analysis script (no dependencies)
├── run_analysis.sh               # Shell script to run the analysis
└── requirements.txt              # Required Python packages
```

## Key Features

1. **Data Loading & Exploration**
   - Load and explore the COVID-19 dataset
   - Examine data structure, missing values, and basic statistics

2. **Data Cleaning**
   - Convert date column to datetime
   - Handle missing values
   - Filter countries of interest
   - Create derived metrics (e.g., death rate)

3. **Exploratory Data Analysis (EDA)**
   - Analyze time trends for cases and deaths
   - Compare metrics across countries
   - Visualize daily new cases and cumulative totals

4. **Vaccination Analysis**
   - Track vaccination progress over time
   - Compare vaccination rates across countries
   - Analyze the relationship between vaccination and case/death rates

5. **Choropleth Map Visualization**
   - Create world maps showing COVID-19 metrics by country
   - Visualize case density and vaccination rates globally

6. **Insights & Reporting**
   - Document key findings and insights
   - Provide a comprehensive analysis with visualizations and narrative

## Requirements

The project requires the following Python packages:
- pandas
- numpy
- matplotlib
- seaborn
- plotly
- jupyter
- geopandas

You can install all required packages using:
```
pip install -r requirements.txt
```

## How to Run

### Option 1: Using the Run Script (Recommended)

The easiest way to run the analysis is using the provided shell script:

```bash
chmod +x run_analysis.sh  # Make the script executable (if needed)
./run_analysis.sh
```

This script will:
- Check if the required dependencies are installed
- Download the COVID-19 dataset if it's not already present
- Launch the Jupyter Notebook for analysis

### Option 2: Running the Jupyter Notebook Manually

If you prefer to run the notebook manually:

1. Clone this repository
2. Install the required packages: `pip install -r requirements.txt`
3. Navigate to the notebooks directory
4. Open and run the Jupyter Notebook: `jupyter notebook COVID19_Global_Data_Analysis.ipynb`

### Option 3: Using the Python Scripts

For environments without Jupyter or the required dependencies, you can use the Python scripts:

```bash
# For a simple analysis with no dependencies:
python3 simple_analysis.py

# For a more comprehensive analysis (requires pandas, matplotlib, etc.):
python3 analyze_covid_data.py
```

The simple analysis script works with just the Python standard library and provides basic statistics and insights.

## Key Insights and Reflections

### Major Findings

Our analysis of global COVID-19 data revealed several important insights:

1. **Global Spread Patterns**: The pandemic spread in distinct waves across different regions, often with asynchronous timing. Countries experienced peaks at different times, reflecting the complex nature of viral transmission and the impact of local policies.

2. **Case Distribution**: The United States, India, and Brazil consistently showed the highest total case counts among our selected countries. This reflects both population size and varying effectiveness of containment measures.

3. **Death Rate Variations**: Death rates varied significantly across countries. South Africa showed the highest death rate among our selected countries at approximately 2.52%, while China reported the lowest at 0.12%. These variations likely reflect differences in healthcare systems, population demographics, testing capacity, and reporting methodologies.

4. **Vaccination Disparities**: There are substantial disparities in vaccination rates globally. Developed nations generally showed higher vaccination rates compared to developing countries, highlighting issues of vaccine equity and distribution.

5. **Regional Patterns**: The choropleth maps revealed regional patterns in both case rates and vaccination coverage, with notable variations between continents and economic regions.

### Reflections on the Analysis Process

Working on this COVID-19 data analysis project provided valuable insights into handling real-world data:

- **Data Quality Challenges**: The dataset contained numerous missing values and required careful cleaning. Different countries had varying levels of reporting consistency, highlighting the challenges of working with global datasets.

- **Visualization Power**: Visualizations proved essential for understanding complex trends that weren't immediately apparent in the raw data. The combination of time series plots and geographic visualizations helped reveal both temporal and spatial patterns.

- **Contextual Interpretation**: Numbers alone don't tell the full story. Interpreting COVID-19 statistics required considering contextual factors like testing capacity, healthcare infrastructure, and policy responses.

- **Technical Learnings**: The project demonstrated the power of Python's data science ecosystem for analyzing large datasets and creating insightful visualizations. The combination of pandas for data manipulation and various visualization libraries enabled comprehensive analysis.

This project serves as a foundation for understanding global pandemic trends and could be extended with more sophisticated analyses as new data becomes available.

## Future Enhancements

Potential future improvements include:
- Adding more sophisticated statistical analysis
- Incorporating policy data to correlate with case trends
- Creating an interactive dashboard for real-time monitoring
- Analyzing the impact of variants on case trends
