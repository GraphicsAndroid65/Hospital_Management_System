import pandas as pd

def age_groups():
    df = pd.read_csv('hospital_data.csv')
    
    print("="*50)
    print("TASK 3: AGE GROUP CLASSIFICATION")
    print("="*50)
    
    def classify_age(age):
        if age < 18:
            return 'Child'
        elif age < 60:
            return 'Adult'
        else:
            return 'Senior'
    
    df['Age_Group'] = df['Age'].apply(classify_age)
    
    counts = df['Age_Group'].value_counts()
    
    print("\nAge Group Counts:")
    for group, count in counts.items():
        print(f"{group}: {count} patients")
    
    print("\nPatients by Group:")
    for group in ['Child', 'Adult', 'Senior']:
        if group in df['Age_Group'].values:
            print(f"\n{group}:")
            group_data = df[df['Age_Group'] == group]
            for row in group_data.itertuples():
                print(f"  {row.Name} ({row.Age} years)")
