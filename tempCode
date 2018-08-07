# Python3 program to find GCD of 
# two numbers such that the second
# number can be very large.


# Function to find gcd
# of two integer numbers
def gcd(a, b) :
    
    if (a == 0) :
        return b
        
    return gcd(b % a, a)

# Here 'a' is integer and 'b' is string.
# The idea is to make the second number
# (represented as b) less than and equal
# to first number by calculating its mod
# with first integer number using basic
# mathematics
def reduceB(a, b) :
    
    # Initialize result
    mod = 0

    # Calculating mod of b with a 
    # to make b like 0 <= b < a
    for i in range(0, len(b)) :
        
        mod = (mod * 10 + ord(b[i])) % a

    return mod      # return modulo


# This function returns GCD of
# 'a' and 'b' where b can be
# very large and is represented
# as a character array or string
def gcdLarge(a, b) :
    
    # Reduce 'b' (second number)
    # after modulo with a
    num = reduceB(a, b)

    # gcd of two numbers
    return gcd(a, num)


# Driver program

# First number which is integer
a = 1221

# Second number is represented
# as string because it can not
# be handled by integer data type
b = "1234567891011121314151617181920212223242526272829"

print(gcdLarge(a, b))


# This code is contributed by Nikita Tiwari.
