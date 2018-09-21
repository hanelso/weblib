
def PrintCost(menu):
    str = input("메뉴: ")
    if str == '오뎅': #오뎅 가격이 반값이라...
        return int(menu[str]/2)
    return menu[str]

menu = {"오뎅":600,"순대":800,"만두":600}
# print(menu)
print("가격: " + str(PrintCost(menu)))