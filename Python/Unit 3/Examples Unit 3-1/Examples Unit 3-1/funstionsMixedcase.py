import math
def mixedcase(s):
    new = ' '
    i = 0
    for i in range(0, len(s)):
        if i % 2 == 0:
            new += s[i].lower()
        else:
            new += s[i].upper()
    return new

text = input("Enter some text")
text = mixedcase(text)
print("Mixed Case", text)
