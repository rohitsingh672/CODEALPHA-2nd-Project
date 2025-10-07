import pandas as pd
import numpy as np

def clean_unemployment_data(df):
    """Clean and validate unemployment data"""
    print("Cleaning unemployment data...")
    
    # Make a copy to avoid modifying original
    df_clean = df.copy()
    
    # Check for missing values
    missing_values = df_clean.isnull().sum().sum()
    if missing_values > 0:
        print(f"Found {missing_values} missing values. Handling them...")
        df_clean = df_clean.dropna()
    
    # Check for duplicates
    duplicates = df_clean.duplicated().sum()
    if duplicates > 0:
        print(f"Found {duplicates} duplicate rows. Removing them...")
        df_clean = df_clean.drop_duplicates()
    
    # Validate data ranges
    min_rate = df_clean['unemployment_rate'].min()
    max_rate = df_clean['unemployment_rate'].max()
    
    if min_rate < 0 or max_rate > 50:
        print("Warning: Unemployment rates outside expected range (0-50%)")
    
    # Ensure date is datetime
    df_clean['date'] = pd.to_datetime(df_clean['date'])
    
    # Sort by date
    df_clean = df_clean.sort_values('date').reset_index(drop=True)
    
    print("Data cleaning completed successfully")
    return df_clean

def add_derived_features(df):
    """Add derived features for analysis"""
    df_enhanced = df.copy()
    
    # Year-over-year change
    df_enhanced['yoy_change'] = df_enhanced.groupby('month')['unemployment_rate'].shift(1) - df_enhanced['unemployment_rate']
    
    # Monthly change
    df_enhanced['monthly_change'] = df_enhanced['unemployment_rate'].diff()
    
    # Rolling averages
    df_enhanced['rolling_3mo'] = df_enhanced['unemployment_rate'].rolling(window=3).mean()
    df_enhanced['rolling_12mo'] = df_enhanced['unemployment_rate'].rolling(window=12).mean()
    
    return df_enhanced