import random

while True:
    mi, ma, trycount = 1, 100, 1

    n = random.randrange(ma) + 1

    print("수를 결정하였습니다. 맞추어 보세요", n)


    while True:
        print(mi, "-", ma)
        val = int(input(str(trycount) +">>"))

        if val > n:
            print("더 낮게")
            ma = val-1
        elif val < n :
            print("더 높게")
            mi = val+1
        else:
            print("맞았습니다.")
            break
        trycount += 1

    if 'y' != input('다시 하시겠습니까(y/n)>>').lower():
        break