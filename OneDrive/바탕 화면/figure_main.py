# %%

# [fill this line]

import figure


myline = figure.line(10)

square = myline.area_square(myline.get_length())
print(square)

myline.set_length(20)
regular_triangle = myline.area_regular_triangle(myline.get_length())
print(regular_triangle)

myline.set_length(30)
circle = myline.area_circle(myline.get_length())
print(circle)