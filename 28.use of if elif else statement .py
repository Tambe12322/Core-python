per=float(input("Enter percentage:"))
if per>=75:
    print("First class with distinction")
elif per>=60 and per<=75:
    print("First class")
elif per>=35 and per<=50:
    print("Third Class")
else:
    print("Fail")