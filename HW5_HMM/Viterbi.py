import numpy as np

# Реализуйте алгоритмы Витерби (выводящий по последовательности открытых состояний наиболее вероятную последовательность скрытых)
# и FB (выводящий суммарные вероятности для состояний по позициям).

sequence = 'ОРОРОРООРРРРРРРРРРОООООООО'

sequence_back = [ [ 0 for col in range ( len ( sequence ) ) ] for row in range ( len ( sequence ) ) ]
delta = [ [ 0 for col in range ( 0 , 2 ) ] for row in range ( len ( sequence ) ) ]
d = [ [ 0 for col in range ( 0 , 4 ) ] for row in range ( len ( sequence ) ) ]

alpha = [ [ 0 for col in range ( 0 , 2 ) ] for row in range ( len ( sequence ) ) ]
beta = [ [ 0 for col in range ( 0 , 4 ) ] for row in range ( len ( sequence ) ) ]

pi = [ 0.5 , 0.5 ]
# a = np.array ( [ [ 0.8 , 0.2 ] ,
#                  [ 0.2 , 0.8 ] ] )
#
# b = np.array ( [ [ 0.5 , 0.5 ] ,
#                  [ 0.1 , 0.9 ] ] )

a = np.array ( [ [ 0.5 , 0.5 ] ,
                 [ 0.5 , 0.5 ] ] )

b = np.array ( [ [ 0.5 , 0.5 ] ,
                 [ 0.51 , 0.49 ] ] )

print ( 'a\n' , np.matrix ( a ) )
print ( 'b\n' , np.matrix ( b ) )


# print ( '\nP' , delta , 'b01' , b[ 0 ][ 1 ] , 'b11' , b[ 1 ][ 1 ] )
# print ( 'delta\n' , np.matrix ( delta ) )
def calculate_matrix(delta , a , b , d):
    if sequence[ 0 ] == 'О':
        delta[ 0 ][ 0 ] = pi[ 0 ] * b[ 0 ][ 0 ]
        delta[ 0 ][ 1 ] = pi[ 1 ] * b[ 1 ][ 0 ]
        # print ('\nO', delta, 'b00',b[ 0 ][ 0 ],'b10',b[ 1 ][ 0 ])
    else:
        delta[ 0 ][ 0 ] = pi[ 0 ] * b[ 0 ][ 1 ]
        delta[ 0 ][ 1 ] = pi[ 1 ] * b[ 1 ][ 1 ]
    for i in range ( 1 , len ( sequence ) ):
        if sequence[ i ] == 'О':
            d[ i ][ 0 ] = delta[ i - 1 ][ 0 ] * a[ 0 ][ 0 ] * b[ 0 ][ 0 ]
            d[ i ][ 1 ] = delta[ i - 1 ][ 1 ] * a[ 0 ][ 1 ] * b[ 0 ][ 0 ]
            d[ i ][ 2 ] = delta[ i - 1 ][ 0 ] * a[ 1 ][ 0 ] * b[ 1 ][ 0 ]
            d[ i ][ 3 ] = delta[ i - 1 ][ 1 ] * a[ 1 ][ 1 ] * b[ 1 ][ 0 ]

        else:
            d[ i ][ 0 ] = delta[ i - 1 ][ 0 ] * a[ 0 ][ 0 ] * b[ 0 ][ 1 ]
            d[ i ][ 1 ] = delta[ i - 1 ][ 1 ] * a[ 0 ][ 1 ] * b[ 0 ][ 1 ]
            d[ i ][ 2 ] = delta[ i - 1 ][ 0 ] * a[ 1 ][ 0 ] * b[ 1 ][ 1 ]
            d[ i ][ 3 ] = delta[ i - 1 ][ 1 ] * a[ 1 ][ 1 ] * b[ 1 ][ 1 ]

        delta[ i ][ 0 ] = max ( d[ i ][ 0 ] , d[ i ][ 1 ] )
        delta[ i ][ 1 ] = max ( d[ i ][ 2 ] , d[ i ][ 3 ] )
    # print ( 'd\n' , np.matrix ( d ))
    # print ('delta\n',np.matrix(delta))
    return (delta)


#
# print ( np.matrix ( calculate_Matrix ( delta , a , b , d ) ) )
calculate_matrix ( delta , a , b , d )


def traceback(delta , a , b , d):
    result_str = " "
    k = 2
    for i in range ( len ( sequence ) - 1 , 0 , -1 ):
        if max ( d[ i ][ k ] , d[ i ][ k + 1 ] ) == d[ i ][ k ]:
            result_str = 'T' + result_str
            # print ( ' T result_str' , result_str , 'max' , max ( d[ i ][ k ] , d[ i ][ k ] ) , 'di0' , d[ i ][ k ] ,
            #         'i' , i , 'k' , k )
            k = 0
        else:
            result_str = 'F' + result_str
            k = 2
            # print ( ' F result_str' , result_str , 'max' , max ( d[ i ][ k ] , d[ i ][ k ] ) , 'di0' , d[ i ][ k ] ,
            #         'i' , i , 'k' , k )

    return (result_str)

print ( '\nResult\n' , " ".join ( traceback ( delta , a , b , d ) ) )

def calculate_matrix_fb(delta , a , b , d):
    if sequence[ 0 ] == 'О':
        delta[ 0 ][ 0 ] = pi[ 0 ] * b[ 0 ][ 0 ]
        delta[ 0 ][ 1 ] = pi[ 1 ] * b[ 1 ][ 0 ]
        # print ('\nO', delta, 'b00',b[ 0 ][ 0 ],'b10',b[ 1 ][ 0 ])
    else:
        delta[ 0 ][ 0 ] = pi[ 0 ] * b[ 0 ][ 1 ]
        delta[ 0 ][ 1 ] = pi[ 1 ] * b[ 1 ][ 1 ]
    for i in range ( 1 , len ( sequence ) ):
        if sequence[ i ] == 'О':
            d[ i ][ 0 ] = delta[ i - 1 ][ 0 ] * a[ 0 ][ 0 ] * b[ 0 ][ 0 ]
            d[ i ][ 1 ] = delta[ i - 1 ][ 1 ] * a[ 0 ][ 1 ] * b[ 0 ][ 0 ]
            d[ i ][ 2 ] = delta[ i - 1 ][ 0 ] * a[ 1 ][ 0 ] * b[ 1 ][ 0 ]
            d[ i ][ 3 ] = delta[ i - 1 ][ 1 ] * a[ 1 ][ 1 ] * b[ 1 ][ 0 ]

        else:
            d[ i ][ 0 ] = delta[ i - 1 ][ 0 ] * a[ 0 ][ 0 ] * b[ 0 ][ 1 ]
            d[ i ][ 1 ] = delta[ i - 1 ][ 1 ] * a[ 0 ][ 1 ] * b[ 0 ][ 1 ]
            d[ i ][ 2 ] = delta[ i - 1 ][ 0 ] * a[ 1 ][ 0 ] * b[ 1 ][ 1 ]
            d[ i ][ 3 ] = delta[ i - 1 ][ 1 ] * a[ 1 ][ 1 ] * b[ 1 ][ 1 ]

        delta[ i ][ 0 ] = d[ i ][ 0 ] + d[ i ][ 1 ]
        delta[ i ][ 1 ] = d[ i ][ 2 ] + d[ i ][ 3 ]

    # print ( 'd\n' , np.matrix ( d ))
    # print ('delta\n',np.matrix(alpha))
    return (delta)


print ( '\n',np.matrix(calculate_matrix_fb ( delta , a , b , d )) )


def forwardback(delta , a , b , d):
    result_str = " "
    k = 2
    for i in range ( len ( sequence ) - 1 , 0 , -1 ):
        if max ( d[ i ][ k ] , d[ i ][ k + 1 ] ) == d[ i ][ k ]:
            result_str = 'T' + result_str
            # print ( ' T result_str' , result_str , 'max' , max ( d[ i ][ k ] , d[ i ][ k ] ) , 'di0' , d[ i ][ k ] ,
            #         'i' , i , 'k' , k )
            k = 0
        else:
            result_str = 'F' + result_str
            k = 2
            # print ( ' F result_str' , result_str , 'max' , max ( d[ i ][ k ] , d[ i ][ k ] ) , 'di0' , d[ i ][ k ] ,
            #         'i' , i , 'k' , k )

    return (result_str)


# traceback ( delta , a , b , d )
