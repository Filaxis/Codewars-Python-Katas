# Calculate the area of a regular n sides polygon inside a circle of radius r

# Write the following function:

# def area_of_inscribed_polygon(circle_radius, number_of_sides):
# It should calculate the area of a regular polygon of numberOfSides, number-of-sides, or number_of_sides sides inside a circle of radius circleRadius, circle-radius, or circle_radius which passes through all the vertices of the polygon (such circle is called circumscribed circle or circumcircle).

# Input :: Output Examples

# area_of_inscribed_polygon(3, 3) # returns 11.691342951089922

# area_of_inscribed_polygon(5.8, 7) # returns 92.05283874578583

# area_of_inscribed_polygon(4, 5) # returns 38.04226065180614
# Note: if you need to use Pi in your code, use the native value of your language unless stated otherwise.

def area_of_inscribed_polygon(circle_radius, number_of_sides):
    import math
    polygonArea = int(number_of_sides)*float(circle_radius)*float(circle_radius)*math.sin(2*math.pi/int(number_of_sides))/2
    print(str(polygonArea))
    return polygonArea

area_of_inscribed_polygon(3, 3)
area_of_inscribed_polygon(5.8, 7)
area_of_inscribed_polygon(4, 5)