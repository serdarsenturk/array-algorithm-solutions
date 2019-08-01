name = "Serdar Senturk"

name = name.lower()
name = name.replace(" ", "")
name = ''.join(sorted(name))

dic = set(name)

if len(dic) < len(name):
    print("False")
else:
    print("True")