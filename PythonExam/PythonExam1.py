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

plist = original.splitlines()
#print(plist)
index = len(plist)

while index != 0:
    str = plist[len(plist)-index]
    str1 = ""

    if str.find('<') == -1:
        str1 = str
    else:
        str1 += str[:str.find('<')]
        str2 = str[str.find('>')+1:]
        str1 += str2[:str2.find('<')]
        str1 = str1.strip(" " "\t")

    if str1 != "":
        print(str1)

    index -= 1
