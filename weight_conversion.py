weight = float (input("enter your weight : "))
unit = (input"In kilograms or In pounds? (K or L): ")

if unit == "K" :
    weight = weight * 2.205
    unit = "Lbs."
    print(f"your weight is {round(weight, 1)}{unit} ")

elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"your weight is {round(weight, 1)}{unit} ")


else:
    print(f"Invalid {unit}. Please enter either kilograms or pounds.")

    