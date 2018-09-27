original = 	'''<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
            To connect to the most powerful tolls int the world.
        </p>
    </body>
</html>
'''

plist = original.splitlines()           # html 문자열을 '\n'를 기준으로 라인을 나눠 list로 만든다.

for str in plist:

    if str.find('<') == -1:             # '<' 이 없는 문자열은 그대로 출력
        str2 = str
    else:
        str1 = str[str.find('>')+1:]    # '>'문자룰 찾고 그 이후의 문자열을 str1에 저장
        str2 = str1[:str1.find('<')]    # str1에서 '<'문자열 이후로 전부 버림

    if str2 != "":
        print(str2)


#print(plist)                           # list가 잘 생겼는지 확인

# index = len(plist)                      #while 문의 반복횟수
# while index != 0:
#     str = plist[len(plist)-index]
#
#     if str.find('<') == -1:             # '<' 이 없는 문자열은 그대로 출력
#         str2 = str
#     else:
#         str1 = str[str.find('>')+1:]    # '>'문자룰 찾고 그 이후의 문자열을 str1에 저장
#         str2 = str1[:str1.find('<')]    # str1에서 '<'문자열 이후로 전부 버림
#
#     if str2 != "":
#         print(str2)
#
#     index -= 1
