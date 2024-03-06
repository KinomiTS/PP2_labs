def shizoid(h, bot, top):
    area=0.5*h*(bot + top)
    return area

height=int(input())
bot=int(input())
top=int(input())


area = shizoid(height, bot, top)
print("The area of a trapezoid: ", area)
