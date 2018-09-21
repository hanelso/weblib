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

list = original.splitlines()
print(list)
index = len(list)
while index != 0:
    str = list[len(list)-index]
    str1 =""
    if str.find('<') == -1:
        str1 = str
    else:
        str1 += str[:str.find('<')]
        str2 = str[str.find('>')+1:]
        str1 += str2[:str2.find('<')]
    print(str1)
    index-=1