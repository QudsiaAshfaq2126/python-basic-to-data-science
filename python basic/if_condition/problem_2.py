# problem number 2
india=["mumbai","banglore","chennai","dehli"]
pakistan=["lahore","karachi","islamabad"]
bangladash=["dhaka","khulna","rangpur"]
city=input("Enter your first city")
city2=input("Enter your second city")
if city in india and city2 in india:
    print("both cities are in india")
elif city in pakistan and city2 in pakistan:    
    print("both cities are in pakistan")
else:
    print("they dont belong to the same country")