import pandas as pd
from diseases import disease_analysis
from costs import expensive_treatments
from ages import age_groups

def show_data():
    df = pd.read_csv('hospital_data.csv')
    print("="*50)
    print("ALL PATIENT DATA")
    print("="*50)
    print(df.to_string(index=False))
    print(f"\nTotal Patients: {len(df)}")

def about_project():
    print("="*50)
    print("ABOUT PROJECT")
    print("="*50)
    print("Project: Hospital Patient Data Analysis")
    print("Purpose: Analyze patient treatment costs and demographics")
    print("Language: Python")
    print("Libraries: pandas, numpy")
    print("")
    print("DEVELOPMENT TEAM:")
    print("- Developer 1: [Mangesh Choudhary]")
    print("- Developer 2: [Riya Singh]") 
    print("- Developer 3: [Sean Ambrose]")
    print("- Developer 4: [Ayush Raybhar]")
    print("")
    print("Github - https://github.com/GraphicsAndroid65/Hospital_Management_System")

def menu():
    print("\n" + "="*50)
    print("HOSPITAL MANAGEMENT SYSTEM")
    print("="*50)
    print("1. View All Data")
    print("2. Disease Analysis")
    print("3. Expensive Treatments") 
    print("4. Age Groups")
    print("5. About Project")
    print("6. Exit")
    print("="*50)

def main():
    while True:
        menu()
        choice = input("\nEnter choice (1-6): ")
        
        if choice == '1':
            show_data()
        elif choice == '2':
            disease_analysis()
        elif choice == '3':
            expensive_treatments()
        elif choice == '4':
            age_groups()
        elif choice == '5':
            about_project()
        elif choice == '6':
            print("\nThank you!")
            break
        else:
            print("Invalid choice!")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
