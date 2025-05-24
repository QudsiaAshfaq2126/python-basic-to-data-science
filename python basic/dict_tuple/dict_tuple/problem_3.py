import math
def circle_calc(radius):
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    diameter=radius**2
    return area, circumference, diameter
def main():
    radius = float(input("Enter the radius of the circle: "))
    a,c,d=circle_calc(radius)
    print("Area is",a)
    print("circumference is",c)
    print("Diameter is",d)

main()
# import math
# def circle_cal(radius):
#     area=math.pi*(radius**2)
#     diameter=radius*2
#     circumference=2*math.pi*radius
#     return area,circumference,diameter

# def main():
#     radius=float(input("Enter the radius of the circle : "))
#     area,circumference,diameter=circle_cal(radius)
#     print("The area of circle is ",area)
#     print("Circumference of the circle is ",circumference)
#     print("Diameter of the circle is ",diameter)

# main()