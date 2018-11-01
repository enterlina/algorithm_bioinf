Genome_1 = "AAACAUGAGGAUUACCCAUGU"
Genome_2 = "AAACAUGAGGAUUACCCAUGU"

max_length = max ( len ( Genome_1 ) , len ( Genome_2 ) )

M =[[0 0 0 0 1]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]]


def traceback(M , i , j , pairs):
    if j <= i:
        return
    if M[ i ][ j ] == M[ i + 1 ][ j ]:
        traceback ( M , i + 1 , j , pairs )
        print ( '1' )
    elif M[ i ][ j ] == M[ i ][ j - 1 ]:
        traceback ( M , i , j - 1 , pairs )
        print ( '2' )
    elif complementary ( Genome_1[ i - 1 ] , Genome_2[ j - 1 ] ) and (M[ i ][ j ] == M[ i + 1 ][ j - 1 ] + 1):
        pairs.append ( (i , j) )
        print ( "pairs" , pairs )
        traceback ( M , i + 1 , j - 1 , pairs )
        print ( '3' )
    else:
        for k in range ( i + 1 , j ):
            if M[ i ][ j ] == M[ i ][ k ] + M[ k + 1 ][ j ]:
                traceback ( M , k + 1 , j , pairs )
                traceback ( M , i , k , pairs )
                break


pairs = list ( )
traceback ( M , 0 , max_length , pairs )
print ( pairs )
