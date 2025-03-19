def calculate_bmi(feet: int, inches: int, weight: float) -> tuple:
    # Convert height to inches and calculate BMI
    total_inches = (feet * 12) + inches
    height_m = total_inches * 0.0254
    weight_lbs = weight * 0.453592
    bmi = (weight_lbs) / (height_m ** 2)
    bmi = round(bmi, 1)

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25.0:
        category = "Normal weight"
    elif 25.0 <= bmi < 30.0:
        category = "Overweight"
    else:
        category = "Obese"

    ##bmi = round(bmi, 1)
    return bmi, category


