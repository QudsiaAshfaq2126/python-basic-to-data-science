length=float(input("Enter your length:"))
width=float(input("Enter your width:"))
shape=input("Enter your shape:")
def area(length,width,shape):
    if shape=="triangle":
        area=(1/2)*length*width
    elif shape=="rectangle":
        area=length*width
    else:
        area=(1/2)*length*width
    print(area)
 
area(length,width,shape)



