print("Enter Marks Obtained in 5 subjects: ")
M1=int(input())
M2=int(input())
M3=int(input())
M4=int(input())
M5=int(input())
total=M1+M2+M3+M4+M5
avg=total/5
if avg>=91 and avg<=100:
    print("Your Grade is A1")
elif avg>=91 and avg<=100:
    print("Your Grade is A2")
elif avg>=81 and avg<=91:
    print("Your Grade is A3")
elif avg>=71 and avg<=81:
    print("Your Grade is B1")
elif avg>=61 and avg<=71:
    print("Your Grade is B2")
elif avg>=51 and avg<=61:
    print("Your Grade is B3")
elif avg>=41 and avg<=51:
    print("Your Grade is C1")
elif avg>=31 and avg<=41:
    print("Your Grade is C2")
elif avg>=21 and avg<=31:
    print("Your Grade is C3")
elif avg>=11 and avg<=21:
    print("Your Grade is D")
elif avg>=0 and avg<=11:
    print("Your Grade is F")
else:
    print("Invalid Input!")