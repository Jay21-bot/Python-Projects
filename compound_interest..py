
print("COMPOUND INTEREST CALCULATOR :-> ")
print("                          ")

principle = 0

rate = 0

time = 0

while True:
    principle = float(input("Please enter a princple Amount: "))

    if principle < 0:
        print("Principal amount should not be in negative.")

    else :
        break 

while True:
    rate = float(input("Please enter a rate of interest per annum: "))
    if rate < 0:
        print("Rate of interest should not be less than zero.")
    
    else :
        break 

while True:
    time = float(input("Please enter the time period in years: "))
    if time < 0:
        print("Time period should not be in negative.")
    
    else :
        break 

total = principle * pow((1 + rate / 100), time)
print(f"balance after{time} years the amount to pay is {total:.2f}")