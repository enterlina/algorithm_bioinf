import numpy as np

# Genome_1 = "AAACAUGAGGAUUACCCAUGU"
# Genome_2 = "AAACAUGAGGAUUACCCAUGU"

Genome_1 = "GCACGACG"
Genome_2 = "GCACGACG"

# Genome_1 = "GGACC"
# Genome_2 = "GGACC"

complement = {'A': 'U' , 'U': 'A' , 'C': 'G' , 'G': 'C'}

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
    for k in range ( index1 + 1 , index2 ):
        s = M[ index1 ][ k ] + M[ k + 1 ][ index2 ]
        if s > max_local:
            max_local = s
    return max_local


for i in range ( 0 , max_length + 1 ):
    M[ i ][ i ] = 0

for i in range ( 0 , max_length + 1 ):
    for j in range ( i + 1 , max_length + 1 ):
        diag = 0

        if complementary ( Genome_1[ i - 1 ] , Genome_2[ j - 1 ] ) == 'true':
            diag = M[ i + 1 ][ j - 1 ] + 1

        max_k = max_row_column ( i , j , M )

        top = M[ i + 1 ][ j ]

        left = M[ i ][ j - 1 ]

        M[ i ][ j ] = max ( top , left , diag , max_k )

        print ( "ij" , i , j , "Mij" , M[ i ][ j ] , "M[i+1][j]" , M[ i + 1 ][ j ] , i + 1 , j , "top" , top , "left" ,
                left ,
                "diag" , diag , "M[ i + 1 ][ j - 1 ]" , M[ i + 1 ][ j - 1 ] , "Gen_1" ,
                Genome_1[ i - 1 ] , "i-1" , i - 1 , "Gen_2" , Genome_2[ j - 1 ] , "j-1" , j - 1 , "max_pok" ,
                max_row_column ( i , j , M ) )

print ( '\nMatrix M \n' , np.matrix ( M ) )

# def traceback(M , i , j , pairs):
#     if j <= i:
#         return
#     if M[ i ][ j ] == M[ i + 1 ][ j ]:
#         traceback ( M , i + 1 , j , pairs )
#     elif M[ i ][ j ] == M[ i ][ j - 1 ]:
#         traceback ( M , i , j - 1 , pairs )
#     elif complementary ( Genome_1[ i ] , Genome_2[ j ] ) and (M[ i ][ j ] == M[ i + 1 ][ j - 1 ] + 1):
#         pairs.append ( (i , j) )
#         print ( Genome_1[ i ] , Genome_2[ j ] )
#         traceback ( M , i + 1 , j - 1 , pairs )
#     else:
#         for k in range ( i + 1 , j ):
#             if M[ i ][ j ] == M[ i ][ k ] + M[ k + 1 ][ j ]:
#                 traceback ( M , k + 1 , j , pairs )
#                 traceback ( M , i , k , pairs )
#                 break


# pairs = list ( )
# traceback ( M , 0 , max_length - 1 , pairs )

# print ( "pairs2" , pairs )
