""" WAP to check if 3 points are co-linear or not [e.g., (1,4), (3,-2) & (4,-5) points are collinear] """

import math

point1_x, point1_y = input("Please enter x, y co-ordinate of point 1 : ").split()
pt1_x = int(point1_x)
pt1_y = int(point1_y)

point2_x, point2_y = input("Please enter x, y co-ordinate of point 2 : ").split()
pt2_x = int(point2_x)
pt2_y = int(point2_y)

point3_x, point3_y = input("Please enter x, y co-ordinate of point 3 : ").split()
pt3_x = int(point3_x)
pt3_y = int(point3_y)

dist12 = math.dist((pt1_x, pt1_y), (pt2_x, pt2_y))
dist23 = math.dist((pt2_x, pt2_y), (pt3_x, pt3_y))
dist31 = math.dist((pt3_x, pt3_y), (pt1_x, pt1_y))

if (dist12 + dist23 == dist31) or (dist23 + dist31 == dist12) or (dist31 + dist12 == dist23):
    print("The points are collinear")
else:
    print("The points are not collinear")