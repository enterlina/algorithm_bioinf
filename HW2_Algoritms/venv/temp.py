import numpy as np

# Genome_1 = "GCACGACG"
# Genome_2 = "GCACGACG"

Genome_1 = "GGACC"
Genome_2 = "GGACC"

match = 1

complement = {'A': 'T' , 'C': 'G' , 'G': 'C' , 'T': 'A'}

Aligned_G1 = list ( )
Aligned_G2 = list ( )

max_length = max ( len ( Genome_1 ) , len ( Genome_2 ) )

M = [ [ 0 for x in range ( max_length + 1 ) ] for y in range ( max_length + 1 ) ]


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

    return max_local


# print (max_row_column ( 3 , 3 , M ))


for i in range ( 0 , max_length + 1 ):
    for j in range ( 0 , max_length + 1 ):
        if (i == j):
            M[ i ][ j ] = 0
        if (i == j - 1):
            M[ i ][ j ] = 0

for i in range ( 0 , max_length + 1 ):
    for j in range ( i , max_length + 1 ):
        # if (i < max_length):
        #     top = M[ i + 1 ][ j ]
        #     left = M[ i ][ j - 1 ]
        if complementary ( Genome_1[ i - 1 ] , Genome_2[ i - 1 ] ) == 'true':
            diag = M[ i + 1 ][ j - 1 ] + match
        else:
            diag = M[ i + 1 ][ j - 1 ]

        # M[ i ][ j ] = max ( top , left , diag , max_row_column ( 3 , 3 , M ) )

print (np.matrix ( M ))
