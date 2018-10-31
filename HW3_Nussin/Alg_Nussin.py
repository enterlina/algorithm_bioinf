import numpy as np

# Genome_1 ="AAACAUGAGGAUUACCCAUGU"
# Genome_2 ="AAACAUGAGGAUUACCCAUGU"

# Genome_1 = "GCACGACG"
# Genome_2 = "GCACGACG"

Genome_1 = "GGACC"
Genome_2 = "GCACC"


Genome_1 = "GUACC"
Genome_2 = "GAACC"

complement = {'A': 'U' , 'C': 'G' , 'G': 'C' , 'U': 'A'}
match = 1

max_length = max ( len ( Genome_1 ) , len ( Genome_2 ) )

M = [ [ 0 for x in range ( max_length + 1 ) ] for y in range ( max_length + 1 ) ]

Max_M = [ [ 0 for x in range ( max_length + 1 ) ] for y in range ( max_length + 1 ) ]


# M = [
#     [ 0 , 1 , 1 , 1 , 1 , 1 ] ,
#     [ 0 , 0 , 1 , 1 , 1 , 1 ] ,
#     [ 0 , 0 , 0 , 1 , 1 , 1 ] ,
#     [ 0 , 0 , 0 , 0 , 1 , 1 ] ,
#     [ 0 , 0 , 0 , 0 , 0 , 1 ] ,
#     [ 0 , 0 , 0 , 0 , 0 , 0 ] ,
# ]


def complementary(nucleo1 , nucleo2):
    if complement[ nucleo1 ] == nucleo2:
        value = 'true'
    else:
        value = 'false'
    return value


def max_row_column(index1 , index2 , M):
    max_local = 0
    for i in range ( 0 , index1 + 1 ):
        for j in range ( 0 , index2 + 1 ):
            s = [ ]
            for k in range ( i , j ):
                s.append ( M[ i ][ k ] + M[ k + 1 ][ j ] )
                if max ( s ) > max_local:
                    max_local = max ( s )
                # print ( "ik" , i , k , "Mik" , M[ i ][ k ] , "k+1,j" , k + 1 , j , "Mk+1j" , M[ k + 1 ][ j ] , "s" , s ,
                #         "max" , max ( s ) , "mlocal" , max_local)

    return max_local


for i in range ( 0 , max_length + 1 ):
    for j in range ( 0 , max_length + 1 ):
        if (i == j):
            M[ i ][ j ] = 0
        if (i == j - 1):
            M[ i ][ j ] = 0

for i in range ( 0 , max_length + 1 ):
    for j in range ( i , max_length + 1 ):
        if (i < max_length):
            top = M[ i + 1 ][ j ]
            left = M[ i ][ j - 1 ]
            if complementary ( Genome_1[ i - 1 ] , Genome_2[ j - 1 ] ) == 'true':
                diag = M[ i + 1 ][ j - 1 ] + match
            else:
                diag = M[ i + 1 ][ j - 1 ]
        print ( M[ i ][ j ] , "top" , top , "left" , left , "diag" , diag , "max_h_w" , max_row_column ( i , j , M ) )
        M[ i ][ j ] = max ( top , left , diag , max_row_column ( i , j , M ) )

print ( '\nMatrix M \n' , np.matrix ( M ) )


def traceback(M , i , j , pairs):
    if j <= i:
        return
    if M[ i ][ j ] == M[ i + 1 ][ j ]:
        traceback ( M , i + 1 , j , pairs )
    elif M[ i ][ j ] == M[ i ][ j - 1 ]:
        traceback ( M , i , j - 1 , pairs )
    elif complementary ( Genome_1[ i ] , Genome_2[ j ] ) and M[ i ][ j ] == M[ i + 1 ][ j - 1 ] + 1:
        pairs.append ( (i , j) )
        print ( "pairs" , pairs )
        traceback ( M , i + 1 , j - 1 , pairs )
    else:
        for k in range ( i + 1 , j ):
            if M[ i ][ j ] == M[ i ][ k ] + M[ k + 1 ][ j ]:
                traceback ( M , k + 1 , j , pairs )
                traceback ( M , i , k , pairs )
                break


pairs = list()
traceback ( M , 0 , max_length, pairs )

print ( "pairs2" , pairs )
