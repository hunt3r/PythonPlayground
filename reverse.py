def reverse(string):
    i = len(string)-1
    reversed_string = ''
    
    while i >= 0:
        reversed_string += string[i]
        i-=1
    
    return reversed_string

print reverse('food')
print reverse('foodus')

def reverse2(string):
    txet = ''
    for l in string:
        txet = l + txet
    return txet 

print reverse2('foods')

def palindrome(string):
    print "is %s a palindrome?" % string
    b = len(string)-1
    f = 0
    
    while b >= 0:
        if string[f] != string[b]:
            return False
        b-=1
        f+=1

    return True

print palindrome("racecar")
print palindrome("mom")
print palindrome("foo")
