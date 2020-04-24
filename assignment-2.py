age = input ("Are you cigarette addict older than 75 years old? : (Yes/No)").title().strip() == "Yes"
chronic = input ("Do you have a severe chronic disease? : (Yes/No)").title().strip() == "Yes"

immune = input("Is your immune system too weak? : (Yes/No)").title().strip() == "Yes"

print("age answer = ", age, "\nchronic answer = ", chronic, "\nimmune answer = ", immune)

if age or chronic or immune :
    print("You are in the risky group")
else :
    print("You are not in the risky group")
