names = input('이름 입력: ')
name = ""
for c in names:
    if(c == ","):
        reverse = name[::-1]
        if reverse != name:
            print(name, "is not palindrome")
        else:
            print(name, "is palindrome")
        name = ""
        continue
    name += c
reverse = name[::-1]
if reverse != name:
    print(name, "is not palindrome")
else:
    print(name, "is palindrome")
    
    
    
