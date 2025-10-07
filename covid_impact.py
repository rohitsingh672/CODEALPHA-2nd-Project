import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def analyze_covid_impact(df):
    """Analyze the impact of COVID-19 on unemployment"""
    print("Analyzing COVID-19 impact...")
    
    # Define periods
    pre_covid = df[df['date'] < '2020-03-01']
    covid_period = df[(df['date'] >= '2020-03-01') & (df['date'] <= '2021-12-01')]
    post_covid = df[df['date'] > '2021-12-01']
    
    # Calculate metrics
    max_covid_rate = covid_period['unemployment_rate'].max()
    pre_covid_avg = pre_covid[pre_covid['date'] >= '2019-01-01']['unemployment_rate'].mean()
    covid_increase = ((max_covid_rate - pre_covid_avg) / pre_covid_avg) * 100
    
    # Create visualization
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    fig.suptitle('COVID-19 Impact on Unemployment', fontsize=16, fontweight='bold')
    
    # Period comparison
    periods = ['Pre-COVID', 'COVID Period', 'Post-COVID']
    averages = [
        pre_covid['unemployment_rate'].mean(),
        covid_period['unemployment_rate'].mean(),
        post_covid['unemployment_rate'].mean()
    ]
    
    bars = axes[0].bar(periods, averages, color=['blue', 'red', 'green'], alpha=0.7)
    axes[0].set_title('Average Unemployment Rate by Period')
    axes[0].set_ylabel('Unemployment Rate (%)')
    
    # Add value labels on bars
    for bar, value in zip(bars, averages):
        axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                    f'{value:.2f}%', ha='center', va='bottom')
    
    # Detailed COVID timeline
    covid_extended = df[(df['date'] >= '2019-01-01') & (df['date'] <= '2022-12-01')]
    axes[1].plot(covid_extended['date'], covid_extended['unemployment_rate'], 
                linewidth=2, color='crimson')
    axes[1].fill_between(covid_extended['date'], covid_extended['unemployment_rate'],
                        alpha=0.3, color='red')
    axes[1].set_title('COVID-19 Impact Timeline (2019-2022)')
    axes[1].set_xlabel('Date')
    axes[1].set_ylabel('Unemployment Rate (%)')
    axes[1].tick_params(axis='x', rotation=45)
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('output/covid_impact.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Print findings
    print("\n" + "="*50)
    print("COVID-19 IMPACT FINDINGS")
    print("="*50)
    print(f"Pre-COVID Average (2019-2020): {pre_covid_avg:.2f}%")
    print(f"Peak COVID Rate: {max_covid_rate:.2f}%")
    print(f"Maximum Increase: {covid_increase:.1f}%")
    print(f"COVID Period Average: {covid_period['unemployment_rate'].mean():.2f}%")
    print(f"Post-COVID Average: {post_covid['unemployment_rate'].mean():.2f}%")
    
    return {
        'pre_covid_avg': pre_covid_avg,
        'peak_covid_rate': max_covid_rate,
        'covid_increase_pct': covid_increase,
        'covid_period_avg': covid_period['unemployment_rate'].mean(),
        'post_covid_avg': post_covid['unemployment_rate'].mean()
    }