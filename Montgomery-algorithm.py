import math

def get_gcd(a,b):
    if a%b == 0:
        return b
    else :
        return get_gcd(b,a%b)

def get_(a, b):
    if b == 0:
        return 1, 0
    else:
        k = a // b
        remainder = a % b
        x1, y1 = get_(b, remainder)
        x, y = y1, x1 - k * y1
    return x, y

def Multiplicative_inverse_modulo( a , b ):
    if b < 0:
        m = abs(b)
    else:
        m = b
    flag = get_gcd(a, b)

    if flag == 1:
        x, y = get_(a, b)
        x0 = x % m
        return x0
    else:
        print("Error!")
        exit()


print('To calculate a * b ( mod N ),')
a , b , N = eval(input('Please input a , b , N (Like 68,57,109)：'))

R = 2**(int(math.log2(N)+1))

N1 = Multiplicative_inverse_modulo( N , R )
N2 = R-N1

a_ =( a * R ) % N
b_ =( b * R ) % N
c_ =((( a_ * b_ ) + ((( a_ * b_ ) * N2 ) % R ) * N )/ R ) % N

c = int(((c_ + ( c_* N2 ) % R * N ))/R)

print( str(a) + ' * ' + str(b) + ' ( mod ' + str(N) +' ) = ' + str(c))
