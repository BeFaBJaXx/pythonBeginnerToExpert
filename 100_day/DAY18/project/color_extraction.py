import colorgram as c

colors_list = c.extract('D:/saaap/100_day/DAY18/project/image.jpg',10)
rgb_list = []

for color in colors_list:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_list.append((r,g,b))
 