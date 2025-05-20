# iF condition solution
# problem number 1
india=["mumbai","banglore","chennai","dehli"]
pakistan=["lahore","karachi","islamabad"]
bangladash=["dhaka","khulna","rangpur"]
city=input("enter your city name:")
if city in india:
    print(f"{city} is in india")
elif city in pakistan:
    print(f"{city} is in pakistan")
elif city in bangladash:
    print(f"{city} is in bangladesh")
else:
    print(f"{city} is not found in these countries")