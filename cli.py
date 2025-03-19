from bmi_calculator import calculate_bmi

def main():
    print("BMI Calculator CLI")
    feet = int(input("Enter height (feet): "))
    inches = int(input("Enter height (inches): "))
    weight = float(input("Enter weight (pounds): "))

    bmi, category = calculate_bmi(feet, inches, weight)
    print(f"\nYour BMI is: {bmi:.1f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()