import numpy as np

Genome_1 = "GGACT"
Genome_2 = "TAGAC"
match = 1
penalty = -1
gapcost = -1
gap = '-'

Aligned_G1 = list ( )
Aligned_G2 = list ( )

max_length = max ( len ( Genome_1 ) , len ( Genome_2 ) )

M = [ [ 0 for x in range ( max_length + 1 ) ] for y in range ( max_length + 1 ) ]

while len ( Genome_1 ) < max_length:
    Genome_1 +='-'
while len ( Genome_2 ) < max_length:
    Genome_2 +='-'

print ( 'Original sequence:' )
print ( Genome_2 )
print ( Genome_1 )

for i in range ( 1 , max_length + 1 ):
    M[ i ][ 0 ] = M[ i - 1 ][ 0 ] + penalty

for j in range ( 1 , max_length + 1 ):
    M[ 0 ][ j ] = M[ 0 ][ j - 1 ] + penalty

for i in range ( 1 , len ( Genome_1 ) + 1 ):
    for j in range ( 1 , len ( Genome_2 ) + 1 ):
        if Genome_2[ i - 1 ] == Genome_1[ j - 1 ]:
            M[ i ][ j ] = max ( M[ i ][ j - 1 ] + gapcost , M[ i - 1 ][ j ] + gapcost ,
                                M[ i - 1 ][ j - 1 ] + match )
        else:
            M[ i ][ j ] = max ( M[ i ][ j - 1 ] + gapcost , M[ i - 1 ][ j ] + gapcost ,
                                M[ i - 1 ][ j - 1 ] + penalty )

print ( 'Alignment Matrix:' )

np.set_printoptions ( suppress=True )
print ( np.matrix ( M ) )

k = len ( Genome_1 )
m = len ( Genome_2 )

while (m > 0) & (k > 0):
    if Genome_1[ k - 1 ] == Genome_2[ m - 1 ]:
        temp = match
    else:
        temp = penalty

    if (M[ m ][ k ] == M[ m - 1 ][ k - 1 ] + temp):
        Aligned_G1.append ( Genome_1[ k - 1 ] )
        Aligned_G2.append ( Genome_2[ m - 1 ] )
        k -= 1
        m -= 1

    elif M[ m ][ k ] == M[ m ][ k - 1 ] + gapcost:
        Aligned_G1.append ( Genome_1[ k - 1 ] )
        Aligned_G2.append ( gap )
        k -= 1
    elif M[ m ][ k ] == M[ m - 1 ][ k ] + gapcost:
        Aligned_G1.append ( gap )
        Aligned_G2.append ( Genome_2[ m - 1 ] )
        m -= 1

    if (k == 0):
        while m > 0:
            Aligned_G1.append ( gap )
            Aligned_G2.append ( Genome_2[ m - 1 ] )
            m -= 1

    if (m == 0):
        while k > 0:
            Aligned_G1.append ( Genome_1[ k - 1 ] )
            Aligned_G2.append ( gap )
            k -= 1

    for i in range ( 0 , len ( Aligned_G1 ) - 1 ):
        if (Aligned_G1[ i ] == gap) and (Aligned_G2[ i ] == gap):
            del Aligned_G1[ i ]
            del Aligned_G2[ i ]
        elif (Aligned_G1[ i ] == " ") and (Aligned_G2[ i ] == gap):
            del Aligned_G1[ i ]
            del Aligned_G2[ i ]
        elif (Aligned_G1[ i ] == gap) and (Aligned_G2[ i ] == " "):
            del Aligned_G1[ i ]
            del Aligned_G2[ i ]
print ( 'Aligned Genome1' , list ( reversed ( Aligned_G1 ) ) )
print ( 'Aligned Genome2' , list ( reversed ( Aligned_G2 ) ) )