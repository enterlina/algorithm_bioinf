import numpy as np

Genome_1 = [ 'A' , 'B' , 'C' , 'D' ]
Genome_2 = [ 'A' , 'B' , 'C' , 'D' ]

# Genome_1 = [ 'A' , 'B' , 'C' , 'D' , 'E' , 'F' ]
# Genome_2 = [ 'A' , 'B' , 'C' , 'D' , 'E' , 'F' ]

# Test1
D = np.array (
    [ [ 0.0 , 16.0 , 16.0 , 10.0 ] , [ 0 , 0 , 8.0 , 8.0 ] , [ 0 , 0 , 0 , 4.0 ] , [ 0 , 0 , 0 , 0 ] ] )
#
# Test2
# D = np.array (
#     [ [ 0.0 , 5.0 , 4.0 , 7.0 , 6.0 , 8.0 ] , [ 0.0 , 0.0 , 7.0 , 10.0 , 9.0 , 11.0 ] ,
#       [ 0.0 , 0.0 , 0.0 , 7.0 , 6.0 , 8.0 ] , [ 0.0 , 0.0 , 0.0 , 0.0 , 5.0 , 9.0 ] ,
#       [ 0 , 0 , 0 , 0 , 0 , 8.0 ] , [ 0 , 0 , 0 , 0 , 0 , 0 ] ] )

# Test3
# D = np.array (
#     [ [ 0.0 , 0.0 , 0.0 , 0.0 , 0.0 , 0.0 ] ,
#       [ 5.0 , 0.0 , 0.0 , 0.0 , 0.0 , 0.0 ] ,
#       [ 4.0 , 7.0 , 0.0 , 0.0 , 0.0 , 0.0 ] ,
#       [ 7.0 , 10.0 , 7.0 , 0.0 , 0.0 , 0.0 ] ,
#       [ 6.0 , 9.0 , 6.0 , 5.0 , 0.0 , 0.0 ] ,
#       [ 8.0 , 11.0 , 8.0 , 9.0 , 8.0 , 0.0 ] ] )


S_row_column = {'A': 0 , 'B': 0 , 'C': 0 , 'D': 0}
# S_row_column = {'A': 0 , 'B': 0 , 'C': 0 , 'D': 0 , 'E': 0 , 'F': 0}
M = [ [ 0 for col in range ( len ( D ) ) ] for row in range ( len ( D ) ) ]
S = [ 0 for col in range ( len ( M ) ) ]

node_1 = list ( )
node_2 = list ( )
# dictionary = {'A': 0 , 'B': 0 , 'C': 0 , 'D': 0 , 'E': 0 , 'F': 0}
dictionary = {'A': 0 , 'B': 0 , 'C': 0 , 'D': 0}
result = Genome_1.copy ( )

print ('\n Matrix\n',np.matrix(D))

def calculate_S(D , Genome_1):
    len_G = len ( Genome_1 ) - 2
    S = [ 0 for col in range ( len ( D ) ) ]
    if len_G <= 1:
        len_G = 1
    for k in range ( 0 , len ( D ) ):
        for i in range ( 0 , len ( D ) ):
            for j in range ( 0 , len ( D )):
                if (i == k) and (j > k):
                    S[ k ] += (D[ k ][ j ]) / len_G
                    # print ( 'SSS1    ' , "k" , k , '   i' , i , '  j' , j , '     D[ k j ]' , D[ k ][ j ] ,
                    #         ' D[ i k ]' ,
                    #         D[ i ][ k ] , "     S[k]" , S[ k ] , '    lenG' , len_G )
                if (i < k) and (j == k):
                    S[ k ] += (D[ i ][ k ]) / len_G
                    # print ( 'SSS2    ' , "k" , k , '   i' , i , '  j' , j , '     D[ k j ]' , D[ k ][ j ] ,
                    #         ' D[ i k ]' ,
                    #         D[ i ][ k ] ,
                    #         "     S[k]" , S[ k ] )
    return S


def find_min_M(D , S):
    M = [ [ 0 for col in range ( len ( D ) ) ] for row in range ( len ( D ) ) ]
    for i in range ( 0 , len ( D ) ):
        for j in range ( 0 , len ( D ) ):
            if (i < j):
                M[ i ][ j ] = D[ i ][ j ] - S[ i ] - S[ j ]
                # print ( '   i' , i , '  j' , j , '     D[ i j ]' , D[ i ][ j ] ,'   Si' , S[ i ],'   Sj' , S[ j ], '   Mij',  M[i][j] )

    Min_M = np.min ( M )
    position = np.where ( M == Min_M )
    # print('Matrix_M\n',np.matrix(M))
    return position


def newick(D , S , index1 , index2):
    global dictionary
    global result
    global Genome_1
    global Genome_2
    global node_1
    global node_2
    node_1 = Genome_1[ index1 ]
    node_2 = Genome_2[ index2 ]
    new_node = node_1 + node_2

    if (len ( new_node ) == 2):
        distance_1 = D[ index1 ][ index2 ] / 2 + (S[ index1 ] - S[ index2 ]) / 2
        distance_2 = D[ index1 ][ index2 ] / 2 + (S[ index2 ] - S[ index1 ]) / 2
        # print ( 'Di1i2' , D[ index1 ][ index2 ] , 'Si1' , S[ index1 ] , 'Si2' , S[ index2 ] , 'i1' , index1 , 'i2' ,
        #         index2 )
        Genome_1[ index1 ] = new_node
        Genome_2[ index1 ] = new_node
        result[ index1 ] = '(' + node_1 + ':' + str ( distance_1 ) + ', ' + node_2 + ':' + str ( distance_2 ) + ')'
        dictionary[ new_node ] = [ distance_1 , distance_2 ]
        # print ( '1' , result[ index1 ] , 'dictionary' , dictionary , '     dictionary_node12    ' ,
        #         dictionary[ new_node ][ 0 ] , dictionary[ new_node ][ 1 ] )
    else:
        distance_1 = D[ index1 ][ index2 ] / 2 + (S[ index1 ] - S[ index2 ]) / 2
        distance_2 = D[ index1 ][ index2 ] / 2 + (S[ index2 ] - S[ index1 ]) / 2
        # print ( '\nstep2\n' , 'Di1i2' , D[ index1 ][ index2 ] , 'Si1' , S[ index1 ] , 'Si2' , S[ index2 ] , 'i1' ,
        #         index1 , 'i2' ,
        #         index2 )
        # distance_new_1 = distance_1
        # distance_new_2 = distance_2
        Genome_1[ index1 ] = new_node
        Genome_2[ index2] = new_node

        # distance = 1` / 2 * (D[ index2 ][ index0 ] + D[ index1 ][ index0 ] - D[ index1 ][ index2 ]))

        result[ index1 ] = '(' + result[ index1 ] + ':' + str ( round ( distance_1 , 2 ) ) + ', ' + result[
            index2 ] + ':' + str ( round ( distance_2 , 2 ) ) + ')'
        dictionary[ new_node ] = [ distance_1 , distance_2 ]
        # print ( '2' , 'new node' , new_node , 'Genome_1i1' , Genome_1[ index1 ] , 'Genome_2_i1' , Genome_2[ index1 ] ,
        #         'resulti1' , result[ index1 ] , 'resulti2' , result[ index2 ] , 'dictionary' , dictionary )

    Genome_1 = Genome_1[ :index2 ] + Genome_1[ index2 + 1: ]
    Genome_2 = Genome_2[ :index2 ] + Genome_2[ index2 + 1: ]
    result = result[ :index2 ] + result[ index2 + 1: ]

    return result


#
# S = calculate_S ( D , Genome_1 )
# position = find_min_M ( D , S )
#
# index1 = position[ 0 ][ 1 ]
# index2 = position[ 1 ][ 1 ]
# print ( position , index1 , index2 , Genome_1[ index1 ] , Genome_2[ index2 ] )


def recalculate_matrix(D , S , index1 , index2):
    row = [ 0 for x in range ( 0 , len ( D ) ) ]
    column = [ 0 for x in range ( 0 , len ( D ) ) ]

    distance_1 = D[ index1 ][ index2 ] / 2 + (S[ index1 ] - S[ index2 ]) / 2
    distance_2 = D[ index1 ][ index2 ] / 2 + (S[ index2 ] - S[ index1 ]) / 2

    # print ( distance_1 , distance_2 , 'Di2i1' , D[ index1 ][ index2 ] , 'Si1' , S[ index1 ] , 'Si2' , S[ index2 ] )

    for i in range ( 0 , len ( D ) ):
        if (i < index1) and (i < index2):
            column[ i ] = D[ i ][ index1 ] - distance_1
            # print ( 'column' , column , ' i' , i , '      D[ ii1 ]' , D[ i ][ index1 ] , '     D[ ii2]' ,
            #         D[ i ][ index2 ] , '      D[i1i2]' , D[ index2 ][ index1 ] )
        elif (i > index1) and (i < index2):
            row[ i ] = (D[ index1 ][ i ] - distance_1)
            # print ( 'row1' , row , ' i' , i , '      D[ i1i ]' , D[ index1 ][ i ] , '     D[ i2i]' ,
            #         D[ index2 ][ i ] , '      D[i1i2]' , D[ index2 ][ index1 ] )
        elif (i > index1) and (i > index2):
            row[ i ] = (D[ index1 ][ i ] - distance_1)
            # print ( 'row2' , row , ' i' , i , '      D[ i1i ]' , D[ index1 ][ i ] , '     D[ i2i]' ,
            #     D[ index2 ][ i ] , '      D[i1i2]' , D[ index2 ][ index1 ] )

    # print ( 'row\n' , row , '  i2' , index2 , '  i1' , index1 , '\ncolumn\n' , column )
    del row[ index2 ]
    del row[ index1 ]
    del column[ index1 ]
    # print ( '\nD before delete\n' , np.matrix ( D ) )
    D = np.delete ( D , index1 , axis=0 )
    D = np.delete ( D , index2 - 1 , axis=0 )
    D = np.delete ( D , index1 , axis=1 )
    D = np.delete ( D , index2 - 1 , axis=1 )
    # print ( 'D before insertion\n' , np.matrix ( D ) )
    D = np.insert ( D , index1 , row , axis=0 )
    D = np.insert ( D , index1 , column , axis=1 )
    # print ( '\nD after insertion\n' , np.matrix ( D ) )

    return D


# print ('\newick1\n',newick(D , S , index1 , index2))
# print ( recalculate_matrix ( D , S , index1 , index2 ) )
# S = calculate_S ( D , Genome_1 )
# position = find_min_M ( D , S )
# # index1 = position[ 1 ][ 1 ]
# # index2 = position[ 0 ][ 1 ]
# print (position)
# print ('\nnewick2\n',newick(D , S , index1 , index2))


def neighborhood(D):
    k = 1
    while (len ( D ) > 1):

        S = calculate_S ( D , Genome_1 )
        position = find_min_M ( D , S )

        if k == 1:
            index1 = position[ 0 ][ 1 ]
            index2 = position[ 1 ][ 1 ]
            k += 1
            # print ( index1 , index2 )
        else:
            index1 = position[ 0 ][ 0 ]
            index2 = position[ 1 ][ 0 ]

        # print ( "S" , S , 'position' , position, index1, index2 )
        newick ( D , S , index1 , index2 )

        D = recalculate_matrix ( D , S , index1 , index2 )
    else:
        return result[ 0 ]


print ( neighborhood ( D ) )
