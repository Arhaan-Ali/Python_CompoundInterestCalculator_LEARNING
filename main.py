# Compound Interest Calculator.
print("Please tell the following info to calculate compound interest ")
principal = float(input("please tell the principal amount (initial investment): ₹"))
while principal <=0 :
    print("the principal amount cannot be 0.")
    principal = float(input("please tell the principal amount (initial investment): ₹"))
Rate_Of_Interest = float(input("select the rate of interest in percent. : "))
while 0 <= Rate_Of_Interest > 50 :
    print("Rate Of Interest cannot be equal or less than 0 and cannot be more than 50 percent.")
    Rate_Of_Interest = float(input("select the rate of interest."))
Time_Period = float(input("Select the Time Period Of Investment in Years "))
while Time_Period < 1 :
    print("Rate of Interest cannot be negative or less than 1")
    Time_Period = float(input("Select the Time Period Of Investment "))
print("types of Compounding Frequency from which you can choose: "
      "\n1) Annually (Once a Year)"
      "\n2) Semi-Annually (Twice a Year)"
      "\n3) Quarterly (Four Times a Year)")
Compounding_frequency = (input("please select the compounding frequency"
                                    "\n A for Annually "
                                    "\n S for Semi-Annually"
                                    "\n Q for Quarterly : "
                               "\n "))
Response = int
if Compounding_frequency == "A" :
    Response = 1
elif Compounding_frequency == "S" :
    Response = 2
elif Compounding_frequency == "Q" :
    Response = 4
else:
    print(f"choose from the above given choice {Compounding_frequency} is not valid")
R = Rate_Of_Interest / 100
Time_years = Time_Period * Response
Answer = round(principal * pow((1 + (R / Response)), Time_Period * Response), 2)
print(f"Total Amount after Compounding is : ₹{Answer}")
