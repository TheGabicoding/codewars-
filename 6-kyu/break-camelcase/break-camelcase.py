def solution(s):
    camel = "" 
    for char in s:
        if char.isupper():
            camel +=" " + char
        else:
            camel += char
    return camel
            
            