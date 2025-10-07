import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def generate_policy_insights(df, covid_analysis, seasonal_analysis):
    """Generate policy insights and recommendations"""
    print("Generating policy insights...")
    
    try:
        # Data validation
        if df.empty:
            raise ValueError("DataFrame is empty")
        
        if 'unemployment_rate' not in df.columns:
            raise ValueError("'unemployment_rate' column not found in DataFrame")
        
        # Calculate key metrics with error handling
        try:
            overall_trend = df[df['year'] == 2024]['unemployment_rate'].mean() - df[df['year'] == 2010]['unemployment_rate'].mean()
        except:
            overall_trend = 0  # Default value if calculation fails
        
        volatility = df['unemployment_rate'].std()
        
        # Calculate recovery speed safely
        if 'pre_covid_avg' in covid_analysis:
            recovery_speed = len(df[(df['date'] >= '2020-03-01') & (df['unemployment_rate'] > covid_analysis['pre_covid_avg'])])
        else:
            recovery_speed = 0
        
        # Create summary report
        insights = {
            'trend_analysis': {
                'long_term_change': overall_trend,
                'volatility': volatility,
                'pre_covid_stability': df[df['date'] < '2020-01-01']['unemployment_rate'].std() if len(df[df['date'] < '2020-01-01']) > 0 else 0
            },
            'covid_impact': covid_analysis,
            'seasonal_patterns': seasonal_analysis
        }
        
        # Generate visualization
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Policy-Ready Insights Dashboard', fontsize=16, fontweight='bold')
        
        # 1. Crisis impact comparison
        crisis_data = [
            covid_analysis.get('peak_covid_rate', 0),
            df['unemployment_rate'].max(),
            df['unemployment_rate'].quantile(0.95)
        ]
        crisis_labels = ['COVID-19 Peak', 'Historical Max', '95th Percentile']
        bars1 = axes[0, 0].bar(crisis_labels, crisis_data, color=['red', 'darkred', 'orange'])
        axes[0, 0].set_title('Crisis Impact Comparison')
        axes[0, 0].set_ylabel('Unemployment Rate (%)')
        
        # Add value labels on bars
        for bar, value in zip(bars1, crisis_data):
            axes[0, 0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                           f'{value:.1f}%', ha='center', va='bottom')
        
        # 2. Recovery analysis
        recovery_metrics = [
            recovery_speed,  # Months to recover
            covid_analysis.get('covid_increase_pct', 0),  # Percentage increase
            covid_analysis.get('post_covid_avg', 0) - covid_analysis.get('pre_covid_avg', 0)  # Net change
        ]
        recovery_labels = ['Recovery\nMonths', 'Peak\nIncrease %', 'Net Change']
        bars2 = axes[0, 1].bar(recovery_labels, recovery_metrics, color=['green', 'red', 'blue'])
        axes[0, 1].set_title('Recovery Metrics')
        
        # Add value labels on bars
        for bar, value in zip(bars2, recovery_metrics):
            axes[0, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                           f'{value:.1f}', ha='center', va='bottom')
        
        # 3. Seasonal vulnerability
        monthly_avg = df.groupby('month')['unemployment_rate'].mean()
        axes[1, 0].plot(monthly_avg.index, monthly_avg.values, marker='o', linewidth=2, color='purple')
        axes[1, 0].set_title('Seasonal Vulnerability Pattern')
        axes[1, 0].set_xlabel('Month')
        axes[1, 0].set_ylabel('Unemployment Rate (%)')
        axes[1, 0].grid(True, alpha=0.3)
        axes[1, 0].set_xticks(range(1, 13))
        
        # 4. Regional disparities
        if 'region' in df.columns:
            regional_volatility = df.groupby('region')['unemployment_rate'].std().sort_values()
            bars4 = axes[1, 1].barh(regional_volatility.index, regional_volatility.values, alpha=0.7)
            axes[1, 1].set_title('Regional Volatility (Standard Deviation)')
            axes[1, 1].set_xlabel('Standard Deviation')
        else:
            axes[1, 1].text(0.5, 0.5, 'Regional data\nnot available', 
                           ha='center', va='center', transform=axes[1, 1].transAxes)
            axes[1, 1].set_title('Regional Volatility')
        
        plt.tight_layout()
        plt.savefig('output/policy_insights.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Print policy recommendations
        print_policy_recommendations(insights)
        
        return insights
        
    except Exception as e:
        print(f"Error in generate_policy_insights: {e}")
        return None

def print_policy_recommendations(insights):
    """Print formatted policy recommendations"""
    print("\n" + "="*60)
    print("ECONOMIC AND SOCIAL POLICY RECOMMENDATIONS")
    print("="*60)
    
    print("\n🚨 CRISIS PREPAREDNESS AND RESPONSE:")
    print("   • Establish automatic unemployment benefit triggers during economic shocks")
    print("   • Develop rapid-response job retraining programs")
    print("   • Create digital infrastructure for remote job matching")
    print("   • Build emergency employment programs for future crises")
    
    print("\n📊 SEASONAL EMPLOYMENT STRATEGIES:")
    print("   • Implement counter-cyclical public sector hiring")
    print("   • Develop seasonal worker transition programs")
    print("   • Offer tax incentives for off-season employment")
    print("   • Create weather-adaptive employment policies")
    
    print("\n🎯 REGIONAL ECONOMIC DEVELOPMENT:")
    print("   • Target economic development in high-unemployment regions")
    print("   • Create region-specific job training programs")
    print("   • Develop infrastructure projects in vulnerable areas")
    print("   • Promote regional industry diversification")
    
    print("\n📈 LONG-TERM WORKFORCE DEVELOPMENT:")
    print("   • Invest in future-oriented education and training")
    print("   • Promote entrepreneurship and small business development")
    print("   • Strengthen apprenticeship and vocational programs")
    print("   • Develop lifelong learning initiatives")
    
    print("\n🔍 MONITORING AND EVALUATION:")
    print("   • Implement real-time labor market monitoring")
    print("   • Regular policy impact assessments")
    print("   • Data-driven workforce development planning")
    print("   • Stakeholder engagement in policy design")