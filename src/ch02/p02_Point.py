# # Part 1
# # Methods
# class Point:
#     def reset(self):
#         'Move points to origin'
#         self.x = 0
#         self.y = 0

# p1 = Point()
# # calling method on object
# p1.reset()
# print(p1.x, p1.y)

# p2 = Point()
# # invoke function on class
# Point.reset(p2)
# print(p2.x,p2.y)

## ---------------------------------------------------------------------------------------------##
# # # Part 2 
# # More Arguments to methods

# import math
#
# class Point:
#     def move(self, x , y):
#         self.x = x
#         self.y = y
#
#     def reset(self):
#         self.move(0,0)
#
#     def calculate_distance(self, other_point):
#         return math.sqrt((self.x- other_point.x)**2 + (self.y - other_point.y)**2)
#
# # using above class
#
# point_a = Point()
# point_b = Point()
#
# point_a.reset()
# point_b.move(5,80)
#
# print(point_a.calculate_distance(point_b))
#
# assert (point_a.calculate_distance(point_b) == point_b.calculate_distance(point_a))
#
# point_a.move(5,25)
# print(point_a.calculate_distance(point_b))
# print(point_a.calculate_distance(point_a))
#
# print(Point.calculate_distance(point_a,point_b))

## ---------------------------------------------------------------------------------------------##
# # # Part 3a
# # Init method

# class Point:
#     def __init__(self,x,y):
#         self.move(x,y)

#     def move(self,x,y):
#         self.x = x
#         self.y = y

#     def reset(self):
#         self.move(0,0)

# # Constructing a Point
# point1 = Point(15,4)
# print(point1.x,point1.y)


## ---------------------------------------------------------------------------------------------##
# # # Part 3b
# # Init method with defaults

# class Point:
#     def __init__(self,x=0,y=0):
#         self.move(x,y)

#     def move(self,x,y):
#         self.x = x
#         self.y = y

#     def reset(self):
#         self.move(0,0)

# # Constructing a Point
# point2 = Point()
# print(point2.x,point2.y)


## ---------------------------------------------------------------------------------------------##
# # # Part 4
# # Class with docstrings
# import math
#
# class Point():
#     'Represents a point in two dimensional geometric coordinates'
#
#     def __init__(self, x=0, y=0):
#         ''' Initialize the position of a new point. The x and y coordinates can be specified.
#         If they are not, the point defaults to origin.
#         '''
#         self.move(x,y)
#
#     def move(self,x,y):
#         '''Move the point to a new location in 2D space
#         '''
#         self.x = x
#         self.y = y
#
#     def reset(self):
#         ''' Reset the point to the geometric origin: 0, 0
#         '''
#         self.move(0,0)
#
#     def calculate_distance(self, other_point):
#         ''' Calculate the euclidean distance between two points.
#         The distance is returned as a float
#         '''
#         return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
#
