import math
def circumference(radius):
    return 2 * math.pi * radius
    
# circumference and area functions defined with radius as the parameter
def area(radius):
    return math.pi * (radius ** 2)

def main():
    radius = int (input ("Give the radius of a circle: "))
    circumference_circle = circumference(radius)
    area_circle = area(radius)

    print(f"Circumference: {circumference_circle:.3f}",end='')
    print(f", Area: {area_circle:.3f}")
if __name__ == "__main__":
    main()