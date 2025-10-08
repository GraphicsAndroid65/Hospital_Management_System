import pandas as pd

def expensive_treatments():
    df = pd.read_csv('hospital_data.csv')
    
    print("="*50)
    print("TASK 2: EXPENSIVE TREATMENTS")
    print("="*50)
    
    top_expensive = df.sort_values('Treatment_Cost', ascending=False).head(5)
    
    print("\nTop 5 Most Expensive:")
    for i, row in enumerate(top_expensive.itertuples(), 1):
        print(f"{i}. {row.Name} - {row.Disease}")
        print(f"   Cost: Rs. {row.Treatment_Cost:,}")
        print()
