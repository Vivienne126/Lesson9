medical_cause=input("Enter the medical condition y or n")
attendence=int(input("Enter your attendence"))

if medical_cause=="Yes":
    print("Allowd")
else:
    if attendence >= 75:
        print("Allowd")
    else:
        print("not allowd")