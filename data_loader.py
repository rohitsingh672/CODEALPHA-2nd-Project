import pandas as pd
import numpy as np
from datetime import datetime

def generate_sample_data():
    """Generate synthetic unemployment data with realistic patterns"""
    print("Generating sample unemployment data...")
    
    dates = pd.date_range('2010-01-01', '2024-12-01', freq='MS')
    n_periods = len(dates)
    
    # Base trend with seasonal patterns
    base_trend = np.linspace(8.5, 3.8, n_periods)
    
    # Seasonal component (higher in winter, lower in summer)
    seasonal = 0.5 * np.sin(2 * np.pi * np.arange(n_periods) / 12)
    
    # COVID-19 impact (sharp increase in 2020)
    covid_impact = np.zeros(n_periods)
    covid_start = 122  # March 2020
    covid_impact[covid_start:covid_start+6] = [8, 12, 10, 6, 4, 2]
    
    # Random noise
    noise = np.random.normal(0, 0.2, n_periods)
    
    # Combine components
    unemployment_rate = base_trend + seasonal + covid_impact + noise
    
    # Create DataFrame
    df = pd.DataFrame({
        'date': dates,
        'unemployment_rate': np.maximum(unemployment_rate, 0),
        'year': dates.year,
        'month': dates.month,
        'quarter': dates.quarter
    })
    
    # Add some categorical regions for analysis
    regions = ['Northeast', 'Midwest', 'South', 'West'] * (n_periods // 4 + 1)
    df['region'] = regions[:n_periods]
    
    print(f"Generated data with {len(df)} records")
    return df

def load_real_data(file_path):
    """Load real unemployment data from CSV file"""
    try:
        df = pd.read_csv(file_path)
        df['date'] = pd.to_datetime(df['date'])
        print(f"Loaded real data from {file_path}")
        return df
    except FileNotFoundError:
        print("Real data file not found. Using sample data.")
        return generate_sample_data()