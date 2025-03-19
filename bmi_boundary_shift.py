def calculate_bmi(feet: int, inches: int, weight: float) -> tuple:
    # Convert height to inches and calculate BMI
    total_inches = (feet * 12) + inches
    height_m = total_inches * 0.0254
    weight_lbs = weight * 0.453592
    bmi = (weight_lbs) / (height_m ** 2)
    bmi = round(bmi, 1)

    # Shift the lower boundary for "Normal weight" by 0.1 (boundary shift)
    if bmi < 18.4: # Shifted lower boundary by 0.1
        category = "Underweight"
    elif 18.4 <= bmi < 25.0:   # Normal weight range shifted down by 0.1
        category = "Normal weight"
    elif 25.0 <= bmi < 30.0:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category


