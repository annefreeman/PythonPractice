#***********           BACKGROUND           ***********
#
# Karatsub Multiplication is a divide and conquer algorithm and is helpful in showing the power of recursion in everyday problems
# Karatsuba figured out that multiplication could be broken down into recursive calls
# considering that x is an n-digit number where the first n/2 digits = a and the last n/2 digits = b
# and that y is an n-digit numbers where the first n/2 digits = c and the last n/2 digits = d
# multiplication could be written so that:
#                         x*y = (10^n)ac + (10^n/2)(ad+bc) + bd
# could compute multiplication in recursive format by only computing the products ac, bd, ad, bc
# 
# Gauss: had an observation that it might be possible to simplify this even more (from 4 recursive calls to 3 recursive calls)
#        Instead of calculating ac, ad, bc, and bd we can calculate the product (a+b)*(c+d) = ac+ad+bc+bd. Then subtract ac and bd to get the sum(ad+bc)



#***********           Algorithm Details           ***********
# input: X, Y (two equal length n-digit integers)
# output: the product P=XY
# additional assumptions: we assume n is a power of two
# The classroom method of multiplying numers is O(N^2)
# This algorithm is O(N^log3)

import math

def karatsubMultiplication(x, y):
    if(len(str(x))==1):
        return x*y
    else:
        #split up the larger numbers in half
        splitValue = int((len(str(x))/2))
        firstX_A = int(str(x)[:splitValue])
        lastX_B = int(str(x)[splitValue:])
        firstY_C = int(str(y)[:splitValue])
        lastY_D = int(str(y)[splitValue:])

        # compute the product of A and C
        AC = karatsubMultiplication(firstX_A, firstY_C) 
        
        #compute the product of B and D
        BD = karatsubMultiplication(lastX_B, lastY_D)

        # compute the (A-B)*(C-D)
        W = karatsubMultiplication(firstX_A + lastX_B, firstY_C + lastY_D)
        
        # W = (A + B)(C + D)  = AC + AD + BC + BD
        # Therefore: W - BD- AC =  AC+AD+BC+BD - AC - BD = AD + BC
        #Sumproducts = AD + BC
        SumProducts = W - BD - AC

        #get the digits so that the powers are set right
        digits = int(len(str(x)))
        return math.pow(10,digits)*AC + (math.pow(10,(digits/2)))*(SumProducts) + BD


#test out function with a couple calls
print(karatsubMultiplication(20,30))
print(karatsubMultiplication(1000,3330))
print(karatsubMultiplication(1000,3330))