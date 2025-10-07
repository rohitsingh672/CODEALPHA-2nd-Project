import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_overview(df):
    """Create overview visualizations"""
    print("Creating overview visualizations...")
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Unemployment Rate Analysis - Overview', fontsize=16, fontweight='bold')
    
    # Overall trend
    axes[0, 0].plot(df['date'], df['unemployment_rate'], linewidth=2, color='navy')
    axes[0, 0].set_title('Overall Trend (2010-2024)')
    axes[0, 0].set_xlabel('Year')
    axes[0, 0].set_ylabel('Unemployment Rate (%)')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Distribution
    axes[0, 1].hist(df['unemployment_rate'], bins=30, alpha=0.7, color='skyblue', edgecolor='black')
    axes[0, 1].axvline(df['unemployment_rate'].mean(), color='red', linestyle='--', 
                      label=f'Mean: {df["unemployment_rate"].mean():.2f}%')
    axes[0, 1].set_title('Distribution of Unemployment Rates')
    axes[0, 1].set_xlabel('Unemployment Rate (%)')
    axes[0, 1].legend()
    
    # Yearly averages
    yearly_avg = df.groupby('year')['unemployment_rate'].mean()
    axes[1, 0].plot(yearly_avg.index, yearly_avg.values, marker='o', linewidth=2)
    axes[1, 0].set_title('Yearly Average Unemployment Rate')
    axes[1, 0].set_xlabel('Year')
    axes[1, 0].set_ylabel('Average Unemployment Rate (%)')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Regional comparison
    regional_avg = df.groupby('region')['unemployment_rate'].mean().sort_values()
    axes[1, 1].barh(regional_avg.index, regional_avg.values, alpha=0.7)
    axes[1, 1].set_title('Average Unemployment Rate by Region')
    axes[1, 1].set_xlabel('Average Unemployment Rate (%)')
    
    plt.tight_layout()
    plt.savefig('output/overview_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return fig

def calculate_basic_statistics(df):
    """Calculate and display basic statistics"""
    print("\n" + "="*50)
    print("BASIC STATISTICS")
    print("="*50)
    
    stats = {
        'Total Period': f"{df['date'].min().strftime('%Y-%m')} to {df['date'].max().strftime('%Y-%m')}",
        'Mean Unemployment Rate': f"{df['unemployment_rate'].mean():.2f}%",
        'Median Unemployment Rate': f"{df['unemployment_rate'].median():.2f}%",
        'Standard Deviation': f"{df['unemployment_rate'].std():.2f}%",
        'Minimum Rate': f"{df['unemployment_rate'].min():.2f}%",
        'Maximum Rate': f"{df['unemployment_rate'].max():.2f}%",
        '25th Percentile': f"{df['unemployment_rate'].quantile(0.25):.2f}%",
        '75th Percentile': f"{df['unemployment_rate'].quantile(0.75):.2f}%"
    }
    
    for key, value in stats.items():
        print(f"{key}: {value}")
    
    return stats