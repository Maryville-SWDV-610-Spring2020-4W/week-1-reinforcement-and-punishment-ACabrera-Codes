#Write a funtion, is_multiple(n, m), that takes two integer values
#and returns True is n is a multiple of m, that is, n = mi for some integer i, and False otherwise.

def is_multiple(n, m):
    # the below will divide n by m 
    if n % m == 0:
        print("True")
    else:
    #if there is a remainder the statment is false.
        print("False")

is_multiple(20, 3)

