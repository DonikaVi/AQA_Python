"""
Hometask 07 if_elif_else.

# given values w,x,y,z
# write if-elif-else statement that will search
minimum value and print smth aka "'y' is minimum value'
# where 'y' is variable name (not value)
# advice use python debugger and different values to check your algorithm
# optionally you can check your algorithm somehow with assert statements

"""

w, x, y, z = 100, 200, 40, 300

if w > x:
    wx = x
else:
    wx = w
if y > z:
    yz = z
else:
    yz = y
if (wx == yz) or (w == x) or (y == z):
    print('we have more than one min value')
elif wx < yz:
    if (x < yz) and (x < w):
        print('x is minimum value')
    if (w < yz) and (w < x):
        print('w is minimum value')
elif yz < wx:
    if (y < wx) and (y < z):
        print('y is minimum value')
    if (z < wx) and (z < y):
        print('z is minimum value')
