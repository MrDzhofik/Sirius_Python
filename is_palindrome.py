def IsPalindrome(S):
    S = S.upper()
    if S == S[::-1]:
        return True
    else:
	    return False

S = input()
if IsPalindrome(S):
    print('YES')
else:
    print('NO')