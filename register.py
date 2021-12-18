def CaseChange(c):
    if c.isupper():
        c = chr(ord(c) + 32)
    elif c.islower():
    	c = chr(ord(c) - 32)
    return c

a = input()
ans =  CaseChange(a)
print (ans)