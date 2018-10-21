import numpy as np

Genome_1 = "ATGAC-"
Genome_2 = "T-ATGA"
len_Genome1 = len ( Genome_1 )
len_Genome2 = len ( Genome_2 )

Ref_M = [
    [ 0, -1 , -1 , -1 , -1 ] ,
    [ -1 , 1 , -1 , -1 , 1] ,
    [ -1 , -1 , 1 , -1 , -1 ] ,
    [ -1 , -1 , -1 , 1 , -1 ] ,
    [ -1 , -1 , -1 , -1 ,0] ,
]

gap = '-'
Aligned_G1 = list ( )
Aligned_G2 = list ( )


Reference = {'A': 0 , 'G': 1 , 'C': 2 , 'T': 3 , '-': 4}

# print ( 'Original sequence:' )
print ( "Genome 1:" , Genome_1 )
print ( "Genome 2:" , Genome_2 )
# print ( Reference )
print ( 'Matrix' )
print ( np.matrix ( Ref_M ) )


def value(nucleo1 , nucle2 , Ref_M):
    return Ref_M[ Reference[ nucleo1 ] ][ Reference[ nucle2 ] ]


M = [ [ 0 for x in range ( len_Genome1 + 1 ) ] for y in range ( len_Genome2 + 1 ) ]
Path_M = [ [ '' for x in range ( len ( Genome_1 ) ) ] for y in range ( len ( Genome_2 ) ) ]

while len ( Genome_1 ) < len_Genome1:
    Genome_1 += gap
while len ( Genome_2 ) < len_Genome2:
    Genome_2 += gap

for j in range ( 1 , len_Genome1 + 1 ):
    M[ 0 ][ j ] = j * value ( Genome_1[ j - 1 ] , '-' , Ref_M )

for i in range ( 1 , len_Genome2 + 1 ):
    M[ i ][ 0 ] = i * value ( Genome_2[ i - 1 ] , '-' , Ref_M )

for i in range ( 1 , len ( Genome_1 ) + 1 ):
    for j in range ( 1 , len ( Genome_2 ) + 1 ):
        diag = M[ i - 1 ][ j - 1 ] + value ( Genome_2[ i - 1 ] , Genome_1[ j - 1 ] , Ref_M )
        top = M[ i - 1 ][ j ] + value ( Genome_2[ i - 1 ] , "-" , Ref_M )
        left = M[ i ][ j - 1 ] + value ( '-' , Genome_1[ j - 1 ] , Ref_M )

        choice = max ( diag , top , left )
        M[ i ][ j ] = choice

        if choice == diag:
            Path_M[ i - 1 ][ j - 1 ] = "diag"
        elif choice == top:
            Path_M[ i - 1 ][ j - 1 ] = "top"
        elif choice == left:
            Path_M[ i - 1 ][ j - 1 ] = "left"

print ( 'Aligned Matrix' )
print ( np.matrix ( M ) )
# print ( np.matrix ( Path_M ) )

# Restore Alignment
k = len ( Genome_1 ) - 1
m = len ( Genome_2 ) - 1

while (m >= 0) & (k >= 0):
    if Path_M[ m ][ k ] == 'diag':
        Aligned_G1.append ( Genome_1[ k ] )
        Aligned_G2.append ( Genome_2[ m ] )
        k -= 1
        m -= 1
    elif Path_M[ m ][ k ] == 'left':
        Aligned_G1.append ( Genome_1[ k ] )
        Aligned_G2.append ( gap )
        k -= 1
    elif Path_M[ m ][ k ] == 'top':
        Aligned_G1.append ( gap )
        Aligned_G2.append ( Genome_2[ m ] )
        m -= 1

    if m >= 0 and k <= 0:
        while m >= 0:
            Aligned_G1.append ( gap )
            Aligned_G2.append ( Genome_2[ m ] )
            m -= 1

    elif m <= 0 and k >= 0:
        while k >= 0:
            Aligned_G1.append ( Genome_1[ k ] )
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
