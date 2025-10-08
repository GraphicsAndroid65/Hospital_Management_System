import pandas as pd

def disease_analysis():
    df = pd.read_csv('hospital_data.csv')
    
    print("="*50)
    print("TASK 1: DISEASE COST ANALYSIS")
    print("="*50)
    
    avg_cost = df.groupby('Disease')['Treatment_Cost'].mean()
    avg_cost = avg_cost.sort_values(ascending=False)
    
    print("\nAverage Cost by Disease:")
    for disease, cost in avg_cost.items():
        print(f"{disease}: Rs. {cost:,.0f}")
