
def getCap(s):
    s = ' ' + s
    r = ''
    for i in range(1, len(s)):
        if s[i - 1] == ' ' and s[i] != ' ':
            r += s[i].upper()
        else:
            r += s[i]
    return r
    
s = input()
print(getCap(s))
