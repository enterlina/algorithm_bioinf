n , k = map ( int , input ( ).split ( ) )
# n= 3
# k=2
def factorial(n):
    res = 1
    for i in range ( 1 , n + 1 , 1 ):
        res *= i
    return res


C = factorial ( n ) / (factorial ( n - k ) * factorial ( k ))

print ( int (C ))
