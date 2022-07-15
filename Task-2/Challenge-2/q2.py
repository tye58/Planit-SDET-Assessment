ASCII_SIZE = 256
 
def getMaxOccurringChar(str):
    j = [0] * ASCII_SIZE
    s=str.lower()
    max = -1
    c = ''
 
    for i in s:
        j[ord(i)]+=1;
 
    for i in s:
        if max < j[ord(i)]:
            max = j[ord(i)]
            c = i
 
    return c
    
st = input("Please input string: ")
print(getMaxOccurringChar(st))