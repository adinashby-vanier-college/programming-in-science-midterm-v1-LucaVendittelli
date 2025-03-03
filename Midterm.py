import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    return round(math.pi * radius ** 2, 2)

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    # if n >= 4:
    #     result = ""
    #     row = 1
    #     while row == 1:
    #         result += "*" + "\n"
    #     while row < n or row > 1:
    #         result += "*" + " " * (row - 2) + "*" + "\n"
    #     while row == n:
    #         result += "*" * n + "\n"
    #         row += 1
    #     return result.strip()
    # else: 
        return "The triangle height should be at least 4."
        
# Q3: Inverted Pyramid
def inverted_pyramid(n):
    # if n >= 3:
    #     result = ""
    #     row = 1
    #     while row <= n:
    #         spaces = row - 1
    #         stars = ...
    #         line = spaces + stars
    #         result += line
    #         if row != n:
    #             result += "\n"
    #         row += 1
    #         return result
    # else:
        return "The pyramid height should be at least 3."

# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()