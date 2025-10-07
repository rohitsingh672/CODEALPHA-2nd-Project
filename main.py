import os
import pandas as pd
from data_loader import generate_sample_data, load_real_data
from data_cleaner import clean_unemployment_data, add_derived_features
from exploratory_analysis import plot_overview, calculate_basic_statistics
from covid_impact import analyze_covid_impact
from seasonal_analysis import analyze_seasonal_patterns
from policy_insights import generate_policy_insights

def main():
    """Main function to run the complete unemployment analysis"""
    print("🚀 Starting Comprehensive Unemployment Analysis")
    print("="*60)
    
    # Create output directory
    os.makedirs('output', exist_ok=True)
    
    # Step 1: Load data
    print("\n📊 STEP 1: Loading Data")
    print("-" * 30)
    
    # Try to load real data, fall back to sample data
    df = load_real_data('data/unemployment_data.csv')  # Change path as needed
    if df is None:
        df = generate_sample_data()
    
    # Step 2: Clean and prepare data
    print("\n🧹 STEP 2: Cleaning Data")
    print("-" * 30)
    df_clean = clean_unemployment_data(df)
    df_enhanced = add_derived_features(df_clean)
    
    # Step 3: Exploratory Analysis
    print("\n🔍 STEP 3: Exploratory Analysis")
    print("-" * 30)
    basic_stats = calculate_basic_statistics(df_enhanced)
    overview_fig = plot_overview(df_enhanced)
    
    # Step 4: COVID-19 Impact Analysis
    print("\n🦠 STEP 4: COVID-19 Impact Analysis")
    print("-" * 30)
    covid_results = analyze_covid_impact(df_enhanced)
    
    # Step 5: Seasonal Analysis
    print("\n📅 STEP 5: Seasonal Pattern Analysis")
    print("-" * 30)
    seasonal_results = analyze_seasonal_patterns(df_enhanced)
    
    # Step 6: Policy Insights
    print("\n💡 STEP 6: Generating Policy Insights")
    print("-" * 30)
    policy_insights = generate_policy_insights(df_enhanced, covid_results, seasonal_results)
    
    # Final Summary
    print("\n" + "="*60)
    print("✅ ANALYSIS COMPLETED SUCCESSFULLY!")
    print("="*60)
    print("\n📁 Output files saved in '/output' directory:")
    print("   - overview_analysis.png")
    print("   - covid_impact.png")
    print("   - seasonal_decomposition.png")
    print("   - seasonal_heatmap.png")
    print("   - policy_insights.png")
    
    print("\n🎯 Key findings and policy recommendations have been generated.")
    print("   Use these insights to inform economic and social policies.")

if __name__ == "__main__":
    main()