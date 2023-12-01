radius = float(input("Enter radius: "))
height = float(input("Enter height: "))
PI = 3.1415926
volume = PI * radius ** 2 * height
area = (2 * PI * radius * height) + (2 * PI * radius ** 2)
print("Volume =", volume)
print("Area =", area)