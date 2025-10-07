import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

def analyze_seasonal_patterns(df):
    """Analyze seasonal patterns in unemployment data"""
    print("Analyzing seasonal patterns...")
    
    # Set date as index for time series analysis
    ts_data = df.set_index('date')['unemployment_rate']
    
    # Seasonal decomposition
    decomposition = seasonal_decompose(ts_data, model='additive', period=12)
    
    # Plot decomposition
    fig, axes = plt.subplots(4, 1, figsize=(15, 12))
    fig.suptitle('Time Series Decomposition - Unemployment Rate', fontsize=16, fontweight='bold')
    
    components = [
        (decomposition.observed, 'Original Series'),
        (decomposition.trend, 'Trend Component'),
        (decomposition.seasonal, 'Seasonal Component'),
        (decomposition.resid, 'Residual Component')
    ]
    
    for i, (component, title) in enumerate(components):
        axes[i].plot(component)
        axes[i].set_title(title)
        axes[i].set_ylabel('Unemployment Rate (%)')
        axes[i].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('output/seasonal_decomposition.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Monthly patterns
    monthly_stats = df.groupby('month').agg({
        'unemployment_rate': ['mean', 'std', 'min', 'max']
    }).round(3)
    
    # Create heatmap
    plt.figure(figsize=(12, 8))
    heatmap_data = df.pivot_table(index='year', columns='month', values='unemployment_rate')
    sns.heatmap(heatmap_data, cmap='YlOrRd', annot=False, cbar_kws={'label': 'Unemployment Rate (%)'})
    plt.title('Unemployment Rate Heatmap by Year and Month', fontsize=14, fontweight='bold')
    plt.xlabel('Month')
    plt.ylabel('Year')
    plt.tight_layout()
    plt.savefig('output/seasonal_heatmap.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Calculate seasonal strength
    seasonal_strength = decomposition.seasonal.std() / decomposition.observed.std()
    
    print("\n" + "="*50)
    print("SEASONAL ANALYSIS FINDINGS")
    print("="*50)
    print(f"Seasonal Strength: {seasonal_strength:.3f}")
    print("\nMonthly Averages:")
    for month in range(1, 13):
        month_data = df[df['month'] == month]['unemployment_rate']
        month_name = pd.to_datetime(f'2023-{month}-01').strftime('%B')
        print(f"  {month_name}: {month_data.mean():.2f}%")
    
    highest_month = monthly_stats[('unemployment_rate', 'mean')].idxmax()
    lowest_month = monthly_stats[('unemployment_rate', 'mean')].idxmin()
    
    print(f"\nHighest unemployment typically in: {pd.to_datetime(f'2023-{highest_month}-01').strftime('%B')}")
    print(f"Lowest unemployment typically in: {pd.to_datetime(f'2023-{lowest_month}-01').strftime('%B')}")
    
    return {
        'seasonal_strength': seasonal_strength,
        'monthly_stats': monthly_stats,
        'decomposition': decomposition
    }