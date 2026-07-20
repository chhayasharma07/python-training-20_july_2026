import math

def square(side):
    square_area=side*side
    square_perimeter=4*side

    print(f"Area of square is {square_area}")
    print(f"Perimeter of square is {square_perimeter}")
    
def circle(radius):
    circle_area=math.pi*radius*radius
    circle_perimeter=2*math.pi*radius

    print(f"Area of circle is {circle_area}")
    print(f"Circumference of circle is {circle_perimeter}")
    
def triangle(base,height,side1,side2,side3):
    triangle_area=0.5*base*height
    triangle_perimeter=side1+side2+side3

    print(f"Area of triangle is {triangle_area}")
    print(f"Perimeter of triangle is {triangle_perimeter}")


side=float(input("Enter the side of the square : "))
square(side)

# Circle
radius=float(input("Enter the radius of the circle : "))
circle(radius)

# Triangle
base=float(input("Enter the base of the triangle : "))
height=float(input("Enter the height of the triangle : "))
side1=float(input("Enter the first side : "))
side2=float(input("Enter the second side : "))
side3=float(input("Enter the third side : "))

triangle(base,height,side1,side2,side3)

