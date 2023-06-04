# %%

# [fill this line]

import figure

myline = figure.line(10, 20)

width, height = myline.get_length()
try:
    rectangle = figure.line.area_rectangle(width, height)
    print(rectangle)

    ellipse = figure.line.area_ellipse(width, height)
    print(ellipse)

    regular_triangle = figure.line.area_right_triangle(width, height)
    print(regular_triangle)

except ValueError:
    print("please input positive number for width and height")