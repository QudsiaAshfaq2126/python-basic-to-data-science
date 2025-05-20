for i in range(5):
    print(f"you run{i+1} miles")
    tired=input("Are you tired")
    if tired=="yes":
        break
    
if i==4:
    print("you won the race")
else:
    print("you lost the race")
