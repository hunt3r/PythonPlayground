def is_prime(number):
    print "is %s prime?" % number
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
            
    return True

print is_prime(0)
print is_prime(1)
print is_prime(2)
print is_prime(3)
print is_prime(5)
print is_prime(9)
print is_prime(19)
print is_prime(29)
print is_prime(33)