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
    
    print("\nAge Group Classification:")
    counts = df['Age_Group'].value_counts()
    for group, count in counts.items():
        print(f"{group}: {count} patients")
    
    print("\nPatients by Group:")
    for group in ['Child', 'Adult', 'Senior']:
        group_patients = df[df['Age_Group'] == group]
        if len(group_patients) > 0:
            print(f"\n{group}:")
            for _, row in group_patients.iterrows():
                print(f"  {row['Name']} ({row['Age']} years)")
